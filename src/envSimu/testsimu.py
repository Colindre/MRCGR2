from robot import Robot
from environnement import Obstacle, Environnement
from time import sleep


def simu(simulation, affichage, ia):

    while True:
        simulation.update()
        #affichage.step()
        #ia.update()
        sleep(1)

env= Environnement(400, 400)
rbt = Robot(280,280,45,10,20,100,100)
obs1 = Obstacle(320,320,20,20,50,'black')
obs2 = Obstacle(320,70,20,20,50,'yellow')
env.addObstacle(obs1)
env.addObstacle(obs2)
env.add(rbt)
simu(env, None, None)