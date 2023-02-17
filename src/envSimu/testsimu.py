from robot import Robot
from environnement import Obstacle, Environnement
from simulationtkinter import Simulationtkinter
from time import sleep


def simu(simulation, affichage, ia):

    while True:
        simulation.update()
        if affichage != None:
            affi.mainloop()
        if ia != None:
            ia.update()
        sleep(1)

env= Environnement(1500, 800)
rbt = Robot(350,300,270,50,3,0,0)
"""obs1 = Obstacle(30,230,20,20,50,'black')
obs2 = Obstacle(320,70,20,20,50,'yellow')
env.addObstacle(obs1)
env.addObstacle(obs2)"""
env.add(rbt)
affi=Simulationtkinter(env)
#a.mainloop()
simu(env, affi, None)
