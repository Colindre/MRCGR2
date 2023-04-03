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
rbt = Robot(250,250,270,50,100)
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
env.addEmetteur(0,0)

#PROXY
rbt_simu = proxy_virtuel(env)

#ACTION
dist100 = ParcourirDistance(rbt_simu,100,50)
dist50 = ParcourirDistance(rbt_simu,50,50)
dist25 = ParcourirDistance(rbt_simu,25,50)
stop = Arrete(rbt_simu)
demitourD = TournerDroiteAngle(rbt_simu,180,50)
tourneG90 = TournerGaucheAngle(rbt_simu,90,50)
tourneG60 = TournerGaucheAngle(rbt_simu,60,50)
tourneD90 = TournerDroiteAngle(rbt_simu,90,50)

carre = IAseq(rbt_simu, [dist50,tourneD90,dist50,stop]*4)

iaseq = IAseq(rbt_simu, [dist50,demitourD,dist50,stop])

ialoop = IAloop(rbt_simu, dist50)

iaifte = IAifte(rbt_simu, ialoop, IAloop(rbt_simu, tourneG90), obstacle_proche)

hexagone = IAseq(rbt_simu, [dist50,tourneG60,stop]*6)

dessine1 = IAseq(rbt_simu, [dist50,demitourD, dist50, demitourD, stop])

dessine0 = IAseq(rbt_simu, [tourneG90, dist25,tourneD90,dist50,tourneD90,dist25,tourneD90,dist50, demitourD, stop])

dessine0_1 = IAseq(rbt_simu, [dessine0, tourneG90, dist100, tourneD90, dessine1])

dessine0_1inf = IAifte(rbt_simu, IAloop(rbt_simu, IAseq(rbt_simu,[dessine0_1,tourneG90, dist100, tourneD90])), stop, obstacle_proche)

#IA
rr = IA(rbt_simu,dessine0_1inf)
env.addIA(rr)


affi=Simulationtkinter(env)
#simulation(env, affi)

print("distance signal: ",rbt.getSignal(env.emetteur))


