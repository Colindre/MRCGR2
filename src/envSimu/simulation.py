from module.robot import Robot
from module.environnement import Obstacle, Environnement
from simulationtkinter import Simulationtkinter
from time import sleep
import threading


def simulation(simulation, affichage, ia):

    t1 = threading.Thread(target=simulation.run)
    t1.start()
    affichage.loop()


env= Environnement(700, 500)
rbt = Robot(250,250,90,50,3)
rbt.dpsD = 180
obs1 = Obstacle(30,230,50,'black')
obs2 = Obstacle(320,70,30,'yellow')

env.addObstacle(obs1)
env.addObstacle(obs2)
env.add(rbt)
affi=Simulationtkinter(env)
#a.mainloop()
simulation(env, affi, None)


