import tkinter as tk
import math
import random
import threading
from module.robot import Robot, angleVecteur
from module.environnement import Obstacle, Environnement

class Simulationtkinter(tk.Tk):
    def __init__(self,environnement):
        tk.Tk.__init__(self)
#OBJETS
        self.environnement = environnement
        self.bool = False
        self.robot = self.environnement.robot
#CANVAS TKINTER
        self.canvas = tk.Canvas(self, bg='white', width=700, height=500)

        self.robot_coord = (0,0,0,0)
        self.coordrobot()
        self.robot_canv = self.canvas.create_oval(self.robot_coord, fill='red')

        self.line_coord = (0,0,0,0)
        self.coordline()
        self.line = self.canvas.create_line(self.line_coord, arrow="last")

        self.label = tk.Label( text="Vitesse gauche:         Vitesse droite:0\nAngle: 0\nPosition: (0, 0)")
        self.label.pack()
        for i in self.environnement.ensObstacle:
            obstacle_canv=self.canvas.create_oval(i.posx-i.rayon,i.posy-i.rayon,i.posx+i.rayon,i.posy+i.rayon, fill=i.color)
        self.canvas.pack()

#BOUTTONS TKINTER
        self.PlusVg = tk.Button(self, text='+ Vd', command=self.robot.augDPSd)
        self.PlusVg.pack(side='right')
        self.DimVg = tk.Button(self, text='- Vd', command=self.robot.dimDPSd)
        self.DimVg.pack(side='right')
        self.PlusVd = tk.Button(self, text='+ Vg', command=self.robot.augDPSg)
        self.PlusVd.pack(side='left')
        self.DimVd = tk.Button(self, text='- Vg', command=self.robot.dimDPSg)
        self.DimVd.pack(side='left')
        self.quit_button = tk.Button(self, text="Quitter Simulation", command=self.destroy)
        self.quit_button.pack()

#FONCTION LANCER SIMULATION 

    def coordrobot(self):
        x = self.robot.posx
        y = self.robot.posy
        r = self.robot.rayon
        self.robot_coord = (x-r, y-r, x+r, y+r)

    def coordline(self):
        x = self.robot.posx
        y = self.robot.posy
        r = self.robot.rayon
        w = math.cos(math.radians(self.robot.dirr))
        z = math.sin(math.radians(self.robot.dirr))
        self.line_coord = (x, y, x+w*r, y+z*r)

    def update_robot(self):
        self.environnement.update()
        self.coordrobot()
        self.coordline()
        self.canvas.coords(self.robot_canv,self.robot_coord)
        self.canvas.coords(self.line,self.line_coord)
        self.label.config(text=f"Vitesse gauche: {self.robot.dpsG}          Vitesse droite: {self.robot.dpsD} \nAngle: {self.robot.dirr}\nPosition: {self.robot.getPos()}")
        self.canvas.after(20, self.update_robot)

    def loop(self):
        self.update_robot()   
        self.mainloop()
