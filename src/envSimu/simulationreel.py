from module.robot import Robot
from module.robot2IN013 import Robot2IN013
from module.environnement import Obstacle, Environnement
from time import sleep
import threading
from module.proxy import proxy_virtuel, proxy_physique
from module.ia import *


def simulationtest(simulation, affichage):

    t1 = threading.Thread(target=simulation.run)
    t2 = threading.Thread(target=simulation.ia.run)
    
    t2.start()
    t1.start()
    #affichage.loop()

#ROBOT
rbt = Robot(250,250,180,50,100)
rbtreel = Robot2IN013()

#ENVIRONNEMENT
env= Environnement(700, 500)
env.add(rbt)

#PROXY
rbt_reel = proxy_physique(rbtreel)


#ACTION REEL
testcercle = TestCercle(rbt_reel,1200, 200, 100)

dist50reel = ParcourirDistance(rbt_reel,200,200)
tourneD90reel = TournerDroiteAngle(rbt_reel,90+10,100)
stopreel = Arrete(rbt_reel)
carrereel = IAseq(rbt_reel, [dist50reel,stopreel,testcercle,stopreel])
tournereel = IAseq(rbt_reel, [tourneD90reel,stopreel])
avancereel = IAseq(rbt_reel, [dist50reel,stopreel])
testcercleseq = IAseq(rbt_reel, [testcercle,stopreel])


#IA
rr = IA(rbt_reel,avancereel)
env.addIA(rr)


simulationtest(env, None)

