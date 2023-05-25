from module.robot import Robot
#from module.robot2IN013 import Robot2IN013
from module.environnement import Obstacle, Environnement
from module.simulationtkinter import Simulationtkinter
from time import sleep
import threading
from module.proxy import proxy_virtuel, proxy_physique
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
#rbtreel = Robot2IN013()

#OBSTACLE
obs1 = Obstacle(30,230,50,'black')
obs2 = Obstacle(320,70,30,'yellow')

#ENVIRONNEMENT
env= Environnement(700, 500)
env.addObstacle(obs1)
env.addObstacle(obs2)
env.add(rbt)

#PROXY
rbt_simu = proxy_virtuel(env)

#ACTION VIRTUELLE
dist50 = ParcourirDistance(rbt_simu,50,50)
stop = Arrete(rbt_simu)
demitourD = TournerDroiteAngle(rbt_simu,180,50)
tourneG90 = TournerGaucheAngle(rbt_simu,90,50)
tourneD90 = TournerDroiteAngle(rbt_simu,90,50)
testcercle = TestCercle(rbt_simu,360, 100, 10)
testcercle2 = IAseq(rbt_simu, [TestCercle(rbt_simu,100, 100, 10),TestCercle(rbt_simu,360, 10, 100),TestCercle(rbt_simu,180, 100, 10),stop])

carre = IAseq(rbt_simu, [dist50,tourneD90,dist50,stop]*4)

iaseq = IAseq(rbt_simu, [dist50,demitourD,dist50,stop])

ialoop = IAloop(rbt_simu, dist50)

iaifte = IAifte(rbt_simu, ialoop, IAloop(rbt_simu, tourneG90), obstacle_proche)

#PROXY
#rbt_reel = proxy_physique(rbtreel)


#ACTION REEL
#dist50reel = ParcourirDistance(rbt_reel,50,50)
#tourneD90reel = TournerDroiteAngle(rbt_reel,50,50)
#stopreel = Arrete(rbt_reel)
#carrereel = IAseq(rbt_reel, [dist50reel,tourneD90reel,dist50reel,stopreel]*4)

#IA
rr = IA(rbt_simu,testcercle2)
env.addIA(rr)


affi=Simulationtkinter(env)
simulation(env, affi)
