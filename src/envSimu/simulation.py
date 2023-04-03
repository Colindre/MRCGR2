from module.robot import Robot
from module.environnement import Obstacle, Environnement
from module.simulationtkinter import Simulationtkinter
from time import sleep
import threading
from module.proxy import proxy_virtuel
from module.ia import *


# A SAVOIR: dans l'interface graphique 2D tourner gauche et tourner droite sont inversé.

def simulation(simulation, affichage):

    t1 = threading.Thread(target=simulation.run)
    t2 = threading.Thread(target=simulation.ia.run)
    
    t2.start()
    t1.start()
    affichage.loop()

#ROBOT
rbt = Robot(250,250,180,50,100)
rbt.dessine(True)

#OBSTACLE
obs1 = Obstacle(50,50,20,'#FFA500')
obs2 = Obstacle(400,400,20,'#FFA500')
obs3 = Obstacle(50,400,20,'#FFA500')
obs4 = Obstacle(400,50,20,'#FFA500')

#ENVIRONNEMENT
env= Environnement(500, 500)
env.addObstacle(obs1)
env.addObstacle(obs2)
env.addObstacle(obs3)
env.addObstacle(obs4)
env.add(rbt)

#PROXY
rbt_simu = proxy_virtuel(env)

#ACTION
dist50 = ParcourirDistance(rbt_simu,50,50)
stop = Arrete(rbt_simu)
demitourD = TournerDroiteAngle(rbt_simu,180,50)
tourneG90 = TournerGaucheAngle(rbt_simu,90,50)
tourneD90 = TournerDroiteAngle(rbt_simu,90,50)

carre = IAseq(rbt_simu, [dist50,tourneD90,dist50,stop]*4)

iaseq = IAseq(rbt_simu, [dist50,demitourD,dist50,stop])

ialoop = IAloop(rbt_simu, dist50)

iaifte = IAifte(rbt_simu, ialoop, IAloop(rbt_simu, tourneG90), obstacle_proche)

#IA
rr = IA(rbt_simu,carre)
env.addIA(rr)


affi=Simulationtkinter(env)
simulation(env, affi)


