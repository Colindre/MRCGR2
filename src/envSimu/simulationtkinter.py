import tkinter as tk
import math
import random
from robot import Robot, angleVecteur
from environnement import Obstacle, Environnement

class Simulationtkinter(tk.Tk):
    def __init__(self, robot,environnement):
        tk.Tk.__init__(self)
#OBJETS
        self.robot = robot
        self.environnement = environnement
        self.temps=50
        self.bool = False

#CANVAS TKINTER
        self.canvas = tk.Canvas(self, bg='white', width=400, height=400)
        self.canvas.pack()
        self.robot_canv = self.canvas.create_oval(robot.posx,robot.posy, robot.posx+robot.rayon, robot.posy+robot.rayon, fill='red')
        for i in self.environnement.ensObstacle:
            obstacle_canv=self.canvas.create_oval(i.posx,i.posy,i.posx+i.rayon,i.posy+i.rayon, fill=i.color)

#BOUTTONS TKINTER
        self.start_button = tk.Button(self, text='Lance Simulation', command=self.start)
        self.start_button.pack()
        self.stop_button = tk.Button(self, text='Stop Simulation', command=self.stop, state='disabled')
        self.stop_button.pack()
        self.PlusVg = tk.Button(self, text='+ Vg', command=self.environnement.augVg)
        self.PlusVg.pack(side='right')
        self.DimVg = tk.Button(self, text='- Vg', command=self.environnement.dimVg)
        self.DimVg.pack(side='right')
        self.PlusVd = tk.Button(self, text='+ Vd', command=self.environnement.augVd)
        self.PlusVd.pack(side='left')
        self.DimVd = tk.Button(self, text='- Vd', command=self.environnement.dimVd)
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
            self.environnement.update(self.robot,self.environnement.vitesseg,self.environnement.vitessed)
            self.update_robot()
            self.after(20, self.step)

    def update_robot(self):
        x1, y1, x2, y2 = self.canvas.coords(self.robot_canv)
        self.canvas.coords(self.robot_canv, self.robot.posx, self.robot.posy, self.robot.posx+self.robot.rayon, self.robot.posy+self.robot.rayon)


env= Environnement(400, 400,40)
rbt = Robot(120,120,45,50,20)
obs1 = Obstacle(320,320,20,20,50,'black')
obs2 = Obstacle(320,70,20,20,50,'yellow')
#obs3 = Obstacle(random.uniform(50,350),random.uniform(50,350),20,20,random.uniform(20,50))
#obs4 = Obstacle(random.uniform(50,350),random.uniform(50,350),20,20,random.uniform(20,50))

env.addObstacle(obs1)
env.addObstacle(obs2)
#env.addObstacle(obs3)
#env.addObstacle(obs4)
env.add(rbt)
app =Simulationtkinter(rbt,env)
app.mainloop()

