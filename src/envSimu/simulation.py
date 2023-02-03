from robot import Robot, angleVecteur
from environnement import Obstacle, Environnement
from time import sleep
import math
import random



def simulation(environnement, robot, temps):
    dirrRad    = math.radians(robot.getDirr())
    vecteur    = math.cos(dirrRad), math.sin(dirrRad)       #vecteur du deplacement de depart 
    depX, depY = vecteur

    for i in range(temps):
        if (robot.collision(environnement.ensPointsObstacle) or robot.collision(environnement.getBordures())):      #si collision avec obstacle ou bordures
            print("collision en: ", robot.getPos())

            environnement.deplacement(robot, (-depX, -depY))        #robot recule
            print("le robot a reculer en: ", robot.getPos())
            vecteur = random.randrange(-9, 10), random.randrange(-9, 10)        #vecteur avec valeures (min -9 et max 9)
        environnement.deplacement(robot, vecteur)       #deplace le robot (possibilite que le robot traverse un obstacle)
        print("le robot s'est deplacé en: ", robot.getPos())
        sleep(1)





