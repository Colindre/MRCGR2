from robot import Robot
from obstacle import Obstacle
from environnement import Environnement


#CREATION OBJET OBSTACLE ENVIRONNEMENT (100,100) ET ROBOT (position 0,0 et regarde vers le haut)
print("\n------------CREATION OBJETS------------")
robot1 = Robot("1",0,0,1)
robot2 = Robot("2",96,13,1)
o = Obstacle(0,0,2,1)
monde = Environnement(100,100)  
print("\n")
print("Robot1 initialisé dans la case",robot1.getPos(),"\n")
print("Robot2 initialisé dans la case",robot1.getPos(),"\n")
print("Obstacle occupe ces cases :",o.ensPoints(),"\n")


#Test Methodes ENV
print("------------Add Robot & Update du monde------------\n")
monde.add(robot2)
monde.addObstacle(o)
print("\n")
print("le robot se trouve en ",robot2.getPos()," et est dirigé vers ",robot2.getDirr())
for i in range(0,3):
    robot2.detecter(o.ensPoints())
    robot2.avancer()
    monde.update(robot2)
print("\nLe Robot tourne vers la droite\n")
robot2.tourner('d')
monde.update(robot2)

for i in range(0,5):
    robot2.detecter(o.ensPoints())
    robot2.avancer()
    monde.update(robot2)

    
#AVANCER
print("\n------------Debut test AVANCER------------")
print("position avant" ,robot1.getPos())
print("direction: " ,robot1.getDirr())
for i in range(0,10):
    robot1.detecter(o.ensPoints())
    robot1.avancer()
    print("position apres" ,i,robot1.getPos())   

#TOURNER
print("\n------------Debut test TOURNER------------")
print("direction de base: ",robot1.getDirr())
robot1.tourner("d")
print("apres tourner a doite: ",robot1.getDirr())
robot1.tourner("g")
print("apres tourner a gauche: ",robot1.getDirr())
robot1.tourner("mauvais_argument")
robot1.tourner(5)


#RECULER
print("\n------------Debut test RECULER------------")
print("direction: ",robot1.getDirr())
print("position avant" ,robot1.getPos())
for i in range(0,10):
    robot1.reculer()
    print("position apres" ,i,robot1.getPos())
 

#DETECTER
print("\n------------Debut test DETECTER------------")
print("Premier test:")
print("position robot1:" ,robot1.getPos())
print("Obstacle occupe ces cases :",o.ensPoints())
robot1.detecter(o.ensPoints())
print("\nDeuxieme test:")
for i in range(5):
    if (not robot1.detecter(o.ensPoints())):

        print(robot1.getPos())
        robot1.avancer()

    if (not robot1.detecter(o.ensPoints())):
        print(robot1.getPos())
        robot1.tourner("d")
        robot1.avancer()

    if (not robot1.detecter(o.ensPoints())):
        print(robot1.getPos())
        robot1.tourner("g")

robot1.avancer()
robot1.detecter(o.ensPoints())
print("position du robot: ",robot1.getPos())

#TEST LA METHODE addObstacles AVEC PLUSIEURS OBSTACLES