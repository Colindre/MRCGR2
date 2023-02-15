from robot import Robot, angleVecteur
import random
import math
import numpy as np
from time import sleep
class Environnement:
        """ 
        initialisation de notre environnement avec ses differents parametres
        
        :param max_x: max de l'environnement en x
        :param max_y: max de l'environnement en y
        :param dirr: direction du robot, angle en degre
        :param ensPointsObstacle: ensemble des points ou se trouve un obstacle
        """
        def __init__(self,max_x,max_y,temps):
            self.max_x= max_x 
            self.max_y=max_y
            self.vitesseg = 0
            self.vitessed = 0
            self.temps = temps
            self.ensPointsObstacle = set()

        def getPos(self):
            """retourne les données x,y de l'environnement
            :retour: (max_x,max,y)
            """
            return (self.max_x, self.max_y)

        def getBordures(self):
            """retourne les bordure de l'environement (arene)
            :retour: ensemble des points de la bordure
            """
            ens=set()
            for x in range(self.max_x+1):
                ens.add((x,0))
                ens.add((x,self.max_y))
            for y in range(self.max_y+1):
                ens.add((0,y))
                ens.add((self.max_x,y))
            return ens

        def deplacement(self, robot, vG, vD, dT):       #dT en sec   
            if vD == 0 and vG == 0:
                return
            if vD == vG:
                robot.posx+= vD*dT              # /!\ PROBLEME A CORRIGER ICI!!!!!!!
                robot.posy+= vD*dT
                return

            w = (vD - vG) / robot.distR         #angle de rotation
            r = (robot.distR / 2) * ((vD + vG) / (vD - vG))         #distance entre ICC et milieu des deux roues
            x, y = robot.getPos()
            dirr = robot.dirr
            icc = ((x - r * math.sin(dirr)), y + r * math.cos(dirr))          #point de rotation du robot   /!\robot.dirr en radians 
            iccX, iccY = icc
            cos = math.cos(w*dT)
            sin = math.sin(w*dT)
            robot.posx = (cos * (x - iccX) - sin * (y - iccY)) + iccX
            robot.posy = (sin * (x - iccX) + cos * (y - iccY)) + iccY
            robot.dirr = dirr + w*dT

        def collision(self,robot,obstacle):	
        	"""détermine si le robot entre en collision avec un obstacle: si l'ensemble des points ou se trouve le robot rencontre l'ensemble des points ou se trouve un obstacle
        	:param ensPointsObstacle:ensemble des points ou se trouve un obstacle
        	:retour: True si collision, False sinon et affichage si collision ou non
        	"""
        	# Calculer la distance entre le centre du robot et celui de l'obstacle
        	distance = math.sqrt((robot.posx - obstacle.posx)**2 + (robot.posy - obstacle.posy)**2)
        	
        	# Si la distance est inférieure à la somme des rayons, il y a collision
        	if(distance <obstacle.rayon):
        		return True

        	#gère les bordures
        	if(robot.posx-robot.rayon <=-robot.rayon  or robot.posx + robot.rayon >= self.max_x):
        		return True
        	if (robot.posy-robot.rayon <=-robot.rayon or robot.posy + robot.rayon >= self.max_y):

        		return True
        	return False


            
        def add(self,robot):
            """ajout d'un robot dans le monde
            :retour:rien, ajoute le robot dans ses position x,y et affiche message d'erreur si robot sort du monde
            """
            rx , ry = robot.getPos()
            if((rx < 0) or (rx > self.max_x) or (ry < 0) or (ry > self.max_y)): #comparaison de la position du robot avec les limites du mondes
                print("Erreur : Les positions du robots sont en dehors du monde. Il n'a pas pu etre place")
                return
                
                
            print("Le robot a ete place dans le monde en ",robot.getPos()," et est dirige vers ",robot.getDirr())

        def addObstacle(self,obstacle):
            """ajout d'un obstacle dans le monde
            :retour:rien, ajoute l'obstacle dans ses position x,y et affiche message d'erreur si obstacle sort du monde
            """
            self.ensPointsObstacle.add(obstacle)

        def update(self,robot,vitesseg,vitessed):
            for i in range(self.temps):
                for obstacle in self.ensPointsObstacle:
                    if self.collision(robot,obstacle):
                        vitessed = 0
                        vitesseg = 0
                self.deplacement(robot,vitesseg,vitessed,0.01)       #deplace le robot (possibilite que le robot traverse un obstacle)
                #print("le robot s'est deplace en: ", robot.getPos())
                #sleep(1)
                
        def augVg(self):
            self.vitesseg +=5
        def augVd(self):
            self.vitessed +=5
        def dimVg(self):
            self.vitesseg +=-5
        def dimVd(self):
            self.vitessed +=-5



class Obstacle:
        """ 
        initialisation d'un obstacle avec ses differents parametres
        
        :param pos_x: position du point le plus en bas a gauche du rectangle en abscisse
        :param pos_y: position du point le plus en bas a gauche du rectangle en ordonne
        :param tailleX: taille du rectangle en abscisse
        :param tailleY: taille du rectangle en ordonne
        """
        def __init__(self,posx, posy, tailleX, tailleY,rayon,color):
            self.posx     = posx                     
            self.posy     = posy                    
            self.tailleX = tailleX                   
            self.tailleY  = tailleY 
            self.rayon = rayon
            self.color=color
        
        def getPos(self):
            """retourne la position du rectangle (le point le plus en bas a gauche)
            :retour: (posx,posy)
            """
            return (self.posx, self.posy)

        def getDimensions(self):
            """retourne les dimensions du rectangle 
            :retour: (tailleX,tailleY)
            """
            return self.tailleX, self.tailleY
            

        def ensPoints(self):
            """retourne la liste des points qu'occupe l'obstacle (innacessibles aux robots)
            :retour:ensemble
            """
            ensobs = set()
            a = self.posx
            b = self.posy
            for i in np.arange(self.posx-self.rayon, self.posx + self.rayon):
            	for j in np.arange(self.posy-self.rayon, self.posy + self.rayon):
            		if((i - a)**2 + (j - b)**2) <= self.rayon**2:
            			ensobs.add((i, j))
            return ensobs

