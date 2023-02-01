from robot import Robot, angleVecteur
from environnement import Environnement, Obstacle


#CREATION OBJET OBSTACLE ENVIRONNEMENT (100,100) ET ROBOT (position 0,0 et regarde vers le haut)
print("\n------------CREATION OBJETS------------")
robot1 = Robot(0,0,1)
robot2 = Robot(96,13,1)
o = Obstacle(3,4,2,1)
monde = Environnement(100,100)  
print("\n")
monde.afficherEnv()
print("\n")
print("Robot1 initialisé dans la case",robot1.getPos(),"\n")
print("Robot2 initialisé dans la case",robot1.getPos(),"\n")
print("Obstacle occupe ces cases :",o.listePoints(),"\n")


#Test Methodes ENV
print("------------Add Robot & Update du monde------------\n")
monde.add(robot2)
print("\n")
print("le robot se trouve en ",robot2.getPos()," et est dirigé vers ",robot2.getDirr())
for i in range(0,3):
    robot2.avancer()
    monde.update(robot2)
print("\nLe Robot tourne vers la droite\n")
robot2.tourner('d')
monde.update(robot2)

for i in range(0,5):
    robot2.avancer()
    monde.update(robot2)

#DETECTER


#OBSTACLE
print("------------LISTE DE POINTS DU ROBOT------------\n")
o = Obstacle(0,0,2,4)
print(o.ensPointsObstacle())

#ROTATION
print("------------ROTATION DU ROBOT------------\n")
robotTest = Robot(2,2,90)
print("direction robot: ",robotTest.getDirr())
print("position robot: ",robotTest.getPos())
robotTest.rotation(-45)
print("direction robot: ",robotTest.getDirr())

#ANGLE VECTEUR
print("------------ANGLE DU VECTEUR------------\n")
print("angle du vecteur (1,1): ",angleVecteur((1,1)))

#DEPLACEMENT ROBOT
print("------------DEPLACEMENT------------\n")
print("direction robot: ",robotTest.getDirr())
print("position robot: ",robotTest.getPos())
robotTest.deplacement((1,-1))
print("angle du vecteur: ",angleVecteur((1,-1)))
print("apres deplacement:")
print("dir: ",robotTest.getDirr())
print("pos: ",robotTest.getPos())
