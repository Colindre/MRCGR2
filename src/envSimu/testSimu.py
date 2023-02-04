from robot import Robot, angleVecteur
from environnement import Obstacle, Environnement
from time import sleep
from simulation import *
import math
import random

#CREATION OBJET OBSTACLE ENVIRONNEMENT (100,100) ET ROBOT (position 0,0 et regarde vers le haut)
print("\n------------CREATION OBJETS------------")
robot1 = Robot(1,1,1,20, False, False)
robot2 = Robot(96,13,1,20, False, False)
o = Obstacle(20,20,2,1)
monde = Environnement(100,100)  
temps = 10
print("\n")
print("\n")
print("Robot1 initialisé dans la case",robot1.getPos(),"\n")
print("Robot2 initialisé dans la case",robot1.getPos(),"\n")
print("Obstacle occupe ces cases :",o.ensPoints(),"\n")

monde.add(robot1)
monde.addObstacle(o)


simulation(monde,robot1,temps)
