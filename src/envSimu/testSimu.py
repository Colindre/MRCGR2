from robot import Robot, angleVecteur
from environnement import Obstacle, Environnement
from time import sleep
from simulation import *
import math
import random


global num_points
num_points =100

#CREATION OBJET OBSTACLE ENVIRONNEMENT (100,100) ET ROBOT (position 0,0 et regarde vers le haut)
print("\n------------CREATION OBJETS------------")
robot1 = Robot(12,12,45,2, False, False)
o = Obstacle(20,20,20,20,2)
obs2 = Obstacle(0,0,20,20,2)
monde = Environnement(400,200)  
temps = 20
print("\n")
print("\n")
print("Robot1 initialisé dans la case",robot1.getPos(),"\n")
print("Obstacle occupe ces cases :",o.ensPoints(),"\n")

monde.add(robot1)
monde.addObstacle(o)
monde.addObstacle(obs2)

simulation(monde,robot1,temps,o,obs2)
