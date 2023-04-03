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
rbt = Robot(350,350,180,50,100)
rbt.dessine(True)

#OBSTACLE
obs1 = Obstacle(650,100,30,'#FFA500')
obs2 = Obstacle(100,650,30,'#FFA500')
obs3 = Obstacle(650,650,30,'#FFA500')
obs4 = Obstacle(100,100,30,'#FFA500')


#ENVIRONNEMENT
env= Environnement(700, 500)
env.addObstacle(obs1)
env.addObstacle(obs2)
env.addObstacle(obs3)
env.addObstacle(obs4)
env.add(rbt)

#PROXY
rbt_simu = proxy_virtuel(env)

#ACTION
dist50 = ParcourirDistance(rbt_simu,50,50)
dist100 = ParcourirDistance(rbt_simu,100,100)
stop = Arrete(rbt_simu)
demitourD = TournerDroiteAngle(rbt_simu,180,50)
tourneG90 = TournerGaucheAngle(rbt_simu,90,50)
tourneD90 = TournerDroiteAngle(rbt_simu,90,50)

tourneD60 = TournerDroiteAngle(rbt_simu,60,50)

carre = IAseq(rbt_simu, [dist50,tourneD90,dist50,stop]*4)

iaseq = IAseq(rbt_simu, [dist50,demitourD,dist50,stop])

ialoop = IAloop(rbt_simu, dist100)

iaifte = IAifte(rbt_simu, ialoop, IAloop(rbt_simu, tourneG90), obstacle_proche)

hexagone = IAseq(rbt_simu,[dist50,tourneD60,stop]*6)

dessine_0 = IAseq(rbt_simu,[dist50,tourneD90,stop,dist100,tourneD90,stop]*2)
dessine_1 = IAseq(rbt_simu,[tourneD90,dist100,stop])
#IA
rr = IA(rbt_simu,dessine_1)
env.addIA(rr)


affi=Simulationtkinter(env)
simulation(env, affi)

