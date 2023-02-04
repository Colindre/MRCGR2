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
        print("le robot s'est deplace en: ", robot.getPos())
        sleep(1)

def carre(environnement, robot):
    environnement.deplacement(robot, (1,0))         #se deplace a droite
    #sleep(1)
    environnement.deplacement(robot, (0,0))         #stop
    print("le robot s'est deplace en: ", robot.getPos())
    environnement.deplacement(robot, (0,1))         #se deplace tout droit
    #sleep(1)
    environnement.deplacement(robot, (0,0))         #stop
    print("le robot s'est deplace en: ", robot.getPos())
    environnement.deplacement(robot, (-1,0))        #se deplace a gauche
    #sleep(1)
    environnement.deplacement(robot, (0,0))         #stop  
    print("le robot s'est deplace en: ", robot.getPos())
    environnement.deplacement(robot, (0,-1))        #se deplace 
    #sleep(1)
    environnement.deplacement(robot, (0,0))         #stop
    print("le robot s'est deplace en: ", robot.getPos()," carre fini.")




