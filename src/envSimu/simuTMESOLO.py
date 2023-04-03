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
env = Environnement(500,500)
env.add(rbt)
env.addObstacle(obs1)
env.addObstacle(obs2)
env.addObstacle(obs3)
env.addObstacle(obs4)



#Hexagone (1.4)
rbt.dessine(True)
rbt_simu = proxy_virtuel(rbt)

avancer = ParcourirDistance(rbt_simu,20,50)
tourner_droite = TournerDroiteAngle(rbt_simu,70,50)
arret = Arrete(rbt_simu)
L = [tourner_droite,avancer]*6
L2 = L.append(arret)

hexagone = IAseq(rbt_simu,L2)

ia = IA(rbt_simu,hexagone)
env.addIA(ia)

#aff = Simulationtkinter(env)
#simulation(env,aff)

#dessin 0 ou 1 (q2.1 et 2.2)
dessiner1 = IAseq(rbt_simu,[avancer,arret])

avancer40 = ParcourirDistance(rbt_simu,40,50)
angle_droitG = TournerGaucheAngle(rbt_simu,90,50)
angle_droitD = TournerGaucheAngle(rbt_simu,90,50)
dessiner0 = IAseq(rbt_simu,[avancer40,angle_droitD,avancer,angle_droitG,avancer40,angle_droitG,avancer,arret])

ia2 = IA(rbt_simu,dessiner0)
env.add(ia2)

aff2 = Simulationtkinter(env)
simulation(env,aff2)

#dessiner 0 et 1
ia0 = IA(rbt_simu,dessiner0)
env.add(ia2)

aff0 = Simulationtkinter(env)
simulation(env,aff0)

self.crayon = False

bouger = IAseq(rbt_simu,[avancer40,avancer40])

self.crayon = True

ia1 = IA(rbt_simu,dessiner1)
env.add(ia1)

aff1 = Simulationtkinter(env)
simulation(env,aff1)