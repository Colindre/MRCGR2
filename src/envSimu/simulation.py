from robot import Robot
from environnement import Obstacle, Environnement
from simulationtkinter import Simulationtkinter
from time import sleep


def simulation(simulation, affichage, ia):

    while True:
        simulation.update()
        if affichage != None:
            affi.loop()
        if ia != None:
            ia.update()
        sleep(0.5)

env= Environnement(700, 500)
rbt = Robot(250,250,90,50,3)
#rbt.dpsD = 180
obs1 = Obstacle(30,230,50,'black')
obs2 = Obstacle(320,70,30,'yellow')

env.addObstacle(obs1)
env.addObstacle(obs2)
env.add(rbt)
affi=Simulationtkinter(env)
#a.mainloop()
simulation(env, affi, None)


