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

env= Environnement(400, 400)
rbt = Robot(150,350,0,30,5,40,0)
obs1 = Obstacle(300,230,20,20,50,'black')
obs2 = Obstacle(320,70,20,20,50,'yellow')
env.addObstacle(obs1)
env.addObstacle(obs2)
env.add(rbt)
affi=Simulationtkinter(env)
#app.mainloop()
simu(env, affi, None)
