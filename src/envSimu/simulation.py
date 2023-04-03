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

#OBSTACLE
obs1 = Obstacle(25,475,20,'black')
obs2 = Obstacle(475,475,20,'yellow')


#PROXY
rbt_simu = proxy_virtuel(rbt)

#ACTION
act1 = ParcourirDistance(rbt_simu,10,20)
act2 = Arrete(rbt_simu)

act3 = ParcourirDistance(rbt_simu,30,40)
act4 = Arrete(rbt_simu)

act5 = TournerDroiteAngle(rbt_simu,90,50)
act6 = Arrete(rbt_simu)

act7 = TournerDroiteAngle(rbt_simu,180,50)

act8 = Arrete(rbt_simu)

act9 = TournerDroiteAngle(rbt_simu,270,50)

carre = Carre(rbt_simu)
carre2 = Carre2(rbt_simu, 100, 50)

iaseq = IAseq(rbt_simu, [act5])


#IA
rr = IA(rbt_simu,carre2)
env.addIA(rr)

#ENVIRONNEMENT
env= Environnement(500, 500)
env.addObstacle(obs1)
env.addObstacle(obs2)
env.add(rbt)


affi=Simulationtkinter(env)
simulation(env, affi)


