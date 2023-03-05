from module.robot import Robot
from module.environnement import Obstacle, Environnement
from simulationtkinter import Simulationtkinter
from time import sleep
import threading
from module.TMPproxy import proxy_virtuel
from module.TMPia import *

def simulation(simulation, affichage):

    t1 = threading.Thread(target=simulation.run)
    t2 = threading.Thread(target=simulation.ia.run)
    
    t2.start()
    t1.start()
    affichage.loop()

#ROBOT
rbt = Robot(250,250,90,50,100)

#OBSTACLE
obs1 = Obstacle(30,230,50,'black')
obs2 = Obstacle(320,70,30,'yellow')

#PROXY
rbt_simu = proxy_virtuel(rbt)

#ACTION
act = ParcourirDistance(rbt_simu,30,10)

#IA
rr = IA(rbt_simu,act)

#ENVIRONNEMENT
env= Environnement(700, 500,rr)
env.addObstacle(obs1)
env.addObstacle(obs2)
env.add(rbt)


affi=Simulationtkinter(env)
simulation(env, affi)


