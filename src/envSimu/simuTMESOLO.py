from module.robot import Robot
from module.environnement import Obstacle, Environnement
from module.simulationtkinter import Simulationtkinter
from time import sleep
import threading
from module.proxy import proxy_virtuel
from module.ia import *

def simulation(simulation, affichage):

    t1 = threading.Thread(target=simulation.run)
    t2 = threading.Thread(target=simulation.ia.run)
    
    t2.start()
    t1.start()
    affichage.loop()

#ROBOT
rbt = Robot(250,250,90,50,100)
rbt.dessine(True)

#OBSTACLE
obs1 = Obstacle(25,475,20,'#FFA500')
obs2 = Obstacle(475,475,20,'#FFA500')
obs3 = Obstacle(25,25,20,'#FFA500')
obs4 = Obstacle(475,25,20,'#FFA500')

#Environnement
env = Environnement(500,500,None)
env.add(rbt)
env.addObstacle(obs1)
env.addObstacle(obs2)
env.addObstacle(obs3)
env.addObstacle(obs4)

#Hexagone (1.4)
