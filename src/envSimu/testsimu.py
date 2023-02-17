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

env= Environnement(500, 500)
rbt = Robot(250,250,90,50,3)
obs1 = Obstacle(30,230,50,'black')
obs2 = Obstacle(320,70,30,'yellow')
env.addObstacle(obs1)
env.addObstacle(obs2)
env.add(rbt)
affi=Simulationtkinter(env)
#app.mainloop()
simu(env, affi, None)
