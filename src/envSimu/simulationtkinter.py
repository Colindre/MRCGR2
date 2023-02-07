import tkinter as tk
import math
import random
from simulation import simulation, carre
from robot import Robot, angleVecteur
from environnement import Obstacle, Environnement

global depX,depY
global dirrRad
global vecteur

class Simulationtkinter(tk.Tk):
    def __init__(self, robot, obstacle,obstacle2,environnement):
        tk.Tk.__init__(self)
#OBJETS
        self.robot = robot
        self.obstacle = obstacle
        self.obstacle2=obstacle2
        self.environnement = environnement

        self.temps=5
        self.running = False

#CANVAS TKINTER
        self.canvas = tk.Canvas(self, bg='white', width=400, height=400)
        self.canvas.pack()
        self.robot_canv = self.canvas.create_oval(robot.posx,robot.posy, robot.posx+robot.rayon, robot.posy+robot.rayon, fill='red')
        self.obstacle_canv=self.canvas.create_oval(obstacle.posx,obstacle.posy,obstacle.posx+obstacle.rayon,obstacle.posy+obstacle.rayon, fill='blue')
        self.obstacle2_canv=self.canvas.create_oval(obstacle2.posx,obstacle2.posy,obstacle2.posx+obstacle2.rayon,obstacle2.posy+obstacle.rayon, fill='blue')

#BOUTTONS TKINTER
        self.start_button = tk.Button(self, text='Lance Simulation', command=self.start)
        self.start_button.pack()
        self.stop_button = tk.Button(self, text='Stop Simulation', command=self.stop, state='disabled')
        self.stop_button.pack()
        self.quit_button = tk.Button(self, text='Quitte Simulation', command=self.quit)
        self.quit_button.pack()

#FONCTION LANCER SIMULATION
    def start(self):
        self.running = True
        self.start_button['state'] = 'disabled'
        self.stop_button['state'] = 'normal'
        self.step()

#FONCTION ARRETER SIMULATION
    def stop(self):
        self.running = False
        self.start_button['state'] = 'normal'
        self.stop_button['state'] = 'disabled'

#FONCTION QUI AGIT SUR SIMULATION
    def step(self):
        if self.running:
            simulation(self.environnement,self.robot,self.temps,self.obstacle,self.obstacle2)
            self.update_robot()
            self.after(20, self.step)

#FONCTION QUI MET A JOUR LA SIMULATION
    def update_robot(self):
        x1, y1, x2, y2 = self.canvas.coords(self.robot_canv)
        self.canvas.coords(self.robot_canv, self.robot.posx, self.robot.posy, self.robot.posx+self.robot.rayon, self.robot.posy+self.robot.rayon)


env= Environnement(400, 400)
rbt = Robot(120,120,45,50, False, False)
obs = Obstacle(200,200,20,20,50)
obs2 = Obstacle(0,0,20,20,50)
env.addObstacle(obs)
env.addObstacle(obs2)
env.add(rbt)
app = Simulationtkinter(rbt,obs,obs2,env)
app.mainloop()


