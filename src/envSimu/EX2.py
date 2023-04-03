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
rbt = Robot(250,250,90,50,100)

#ENVIRONNEMENT
env= Environnement(700, 500)

env.add(rbt)
env.robot.dessine(True)
#PROXY
rbt_simu = proxy_virtuel(env)


#ACTION
dist50 = ParcourirDistance(rbt_simu,50,50)
dist15 = ParcourirDistance(rbt_simu,15,50)
stop = Arrete(rbt_simu)
demitourD = TournerDroiteAngle(rbt_simu,180,50)
tourneG90 = TournerGaucheAngle(rbt_simu,90,50)
tourneD90 = TournerDroiteAngle(rbt_simu,90,50)
tourneD45 = TournerDroiteAngle(rbt_simu,45,50)

#QUESTION1
strategie1 = IAseq(rbt_simu,[dist50,stop])
#QUESTION2
strategie0 = IAseq(rbt_simu,[dist50,tourneD90,dist15,tourneD90,dist50,tourneD90,dist15,stop])
#QUESTION3
strategie01= IAseq(rbt_simu,[strategie0,demitourD,dist50,tourneG90,strategie1,demitourD,dist50,tourneG90,dist50,tourneG90])
#QUESTION4
strategieloop = IAloop(rbt_simu,strategie01)
#IA
rr = IA(rbt_simu,strategieloop)
env.addIA(rr)


affi=Simulationtkinter(env)
simulation(env, affi)


