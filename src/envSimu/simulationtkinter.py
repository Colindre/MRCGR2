import tkinter as tk
import math
import random
from robot import Robot, angleVecteur
from environnement import Obstacle, Environnement

class Simulationtkinter(tk.Tk):
    def __init__(self,environnement):
        tk.Tk.__init__(self)
#OBJETS
        self.environnement = environnement
        self.temps=50
        self.bool = False
        self.robot = self.environnement.robot
#CANVAS TKINTER
        self.canvas = tk.Canvas(self, bg='white', width=400, height=400)
        self.canvas.pack()
        self.robot_canv = self.canvas.create_oval(self.robot.posx-self.robot.rayon,self.robot.posy-self.robot.rayon, self.robot.posx+self.robot.rayon, self.robot.posy+self.robot.rayon, fill='red')
        self.line = self.canvas.create_line(self.robot.posx,self.robot.posy,self.robot.posx+math.cos(math.radians(self.robot.dirr))*self.robot.rayon,self.robot.posx+math.sin(math.radians(self.robot.dirr))*self.robot.rayon, arrow="last")
        for i in self.environnement.ensObstacle:
            obstacle_canv=self.canvas.create_oval(i.posx-i.rayon,i.posy-i.rayon,i.posx+i.rayon,i.posy+i.rayon, fill=i.color)

#BOUTTONS TKINTER
        self.start_button = tk.Button(self, text='Lance Simulation', command=self.start)
        self.start_button.pack()
        self.stop_button = tk.Button(self, text='Stop Simulation', command=self.stop, state='disabled')
        self.stop_button.pack()
        self.PlusVg = tk.Button(self, text='+ Vg', command=self.robot.augDPSg)
        self.PlusVg.pack(side='right')
        self.DimVg = tk.Button(self, text='- Vg', command=self.robot.dimDPSg)
        self.DimVg.pack(side='right')
        self.PlusVd = tk.Button(self, text='+ Vd', command=self.robot.augDPSd)
        self.PlusVd.pack(side='left')
        self.DimVd = tk.Button(self, text='- Vd', command=self.robot.dimDPSd)
        self.DimVd.pack(side='left')
        self.quit_button = tk.Button(self, text='Quitte Simulation', command=self.quit)
        self.quit_button.pack()

#FONCTION LANCER SIMULATION
    def start(self):
        self.bool = True
        self.start_button['state'] = 'disabled'
        self.stop_button['state'] = 'normal'
        self.step()


    def stop(self):
        self.bool = False
        self.start_button['state'] = 'normal'
        self.stop_button['state'] = 'disabled'


    def step(self):
        if self.bool:
            self.environnement.update()
            self.update_robot()
            print("direction",self.robot.dirr)
            self.after(20, self.step)

    def update_robot(self):
        x1, y1, x2, y2 = self.canvas.coords(self.robot_canv)
        self.canvas.coords(self.robot_canv,self.robot.posx-self.robot.rayon,self.robot.posy-self.robot.rayon,self.robot.posx+self.robot.rayon, self.robot.posy+self.robot.rayon)
        self.canvas.coords(self.line,self.robot.posx,self.robot.posy,self.robot.posx+math.cos(math.radians(self.robot.dirr))*self.robot.rayon,self.robot.posy+math.sin(math.radians(self.robot.dirr))*self.robot.rayon)

