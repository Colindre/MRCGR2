import tkinter as tk
import math
import random
from simulation import simulation, carre
from robot import Robot, angleVecteur
from environnement import Obstacle, Environnement

class Simulationtkinter(tk.Tk):
    def __init__(self, robot,environnement):
        tk.Tk.__init__(self)
#OBJETS
        self.robot = robot
        self.environnement = environnement
        self.temps=5
        self.bool = False

#CANVAS TKINTER
        self.canvas = tk.Canvas(self, bg='white', width=400, height=400)
        self.canvas.pack()
        self.robot_canv = self.canvas.create_oval(robot.posx,robot.posy, robot.posx+robot.rayon, robot.posy+robot.rayon, fill='red')
        for i in self.environnement.ensPointsObstacle:
            obstacle_canv=self.canvas.create_oval(i.posx,i.posy,i.posx+i.rayon,i.posy+i.rayon, fill=i.color)

#BOUTTONS TKINTER
        self.start_button = tk.Button(self, text='Lance Simulation', command=self.start)
        self.start_button.pack()
        self.stop_button = tk.Button(self, text='Stop Simulation', command=self.stop, state='disabled')
        self.stop_button.pack()
        self.quit_button = tk.Button(self, text='Quitte Simulation', command=self.quit)
        self.quit_button.pack()

#FONCTION LANCER SIMULATION
    def start(self):
        self.bool = True
        self.start_button['state'] = 'disabled'
        self.stop_button['state'] = 'normal'
        self.step()

#FONCTION ARRETER SIMULATION
    def stop(self):
        self.bool = False
        self.start_button['state'] = 'normal'
        self.stop_button['state'] = 'disabled'

#FONCTION QUI AGIT SUR SIMULATION
    def step(self):
        if self.bool:
            self.environnement.update(self.robot,self.temps)
            self.update_robot()
            self.after(20, self.step)

#FONCTION QUI MET A JOUR LA SIMULATION
    def update_robot(self):
        x1, y1, x2, y2 = self.canvas.coords(self.robot_canv)
        self.canvas.coords(self.robot_canv, self.robot.posx, self.robot.posy, self.robot.posx+self.robot.rayon, self.robot.posy+self.robot.rayon)


env= Environnement(400, 400)
rbt = Robot(120,120,45,50,20)
obs1 = Obstacle(random.uniform(50,350),random.uniform(50,350),20,20,random.uniform(20,50),'black')
obs2 = Obstacle(random.uniform(50,350),random.uniform(50,350),20,20,random.uniform(20,50),'yellow')
#obs3 = Obstacle(random.uniform(50,350),random.uniform(50,350),20,20,random.uniform(20,50))
#obs4 = Obstacle(random.uniform(50,350),random.uniform(50,350),20,20,random.uniform(20,50))

env.addObstacle(obs1)
env.addObstacle(obs2)
#env.addObstacle(obs3)
#env.addObstacle(obs4)
env.add(rbt)
app =Simulationtkinter(rbt,env)
app.mainloop()


