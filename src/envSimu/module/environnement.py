from module.robot import Robot
import random
import threading
import math
from time import sleep
from module.TMPia import *

class Environnement(threading.Thread) :
        """ 
        initialisation de notre environnement avec ses differents parametres
        
        :param max_x: max de l'environnement en x
        :param max_y: max de l'environnement en y
        :param dirr: direction du robot, angle en degre
        :param ensObstacle: ensemble des points ou se trouve un obstacle
        """
        def __init__(self,max_x,max_y,ia):
            threading.Thread.__init__(self)
            self.max_x= max_x 
            self.max_y=max_y
            self.robot= None 
            self.ensObstacle = set()
            self.ia = ia

        def getBordures(self):
            """retourne les bordure de l'environnement (arene)
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

        def deplacement(self,dT):       #dT en sec
            robot=self.robot  
            vD=robot.velocityD()            #vitesse linéaire roue droite
            vG=robot.velocityG()            #vitesse linéaire roue gauche
            #robot.lastposx = robot.posx
            #robot.lastposy = robot.posy
            dirr = math.radians(robot.dirr)	 
            if vD == 0 and vG == 0:         #2 roues eteintes donc le robot ne bougent pas    
                return
            if vD == vG:            	    #2 roues à la même vitesse donc avance tout droit
                robot.posx+= vD*dT *math.cos(dirr)
                robot.posy+= vD*dT *math.sin(dirr)
                return
            x, y = robot.getPos()
            w = (vD - vG) / robot.distR         #angle de rotation
            if vD == 0:
                icc = robot.getPosRd()          #point de rotation du robot:roue droite car éteinte
            elif vG == 0:
                icc = robot.getPosRg()          #point de rotation du robot:roue gauche car éteinte
            else:
                r = (robot.distR / 2) * ((vD + vG) / (vD - vG))         #distance entre ICC et milieu des deux roues
                icc = ((x - r * math.sin(dirr)), y + r * math.cos(dirr))   #calcul du point de rotation de la roue       


            #differential drive kinematics
            iccX, iccY = icc
            cos = math.cos(w*dT)
            sin = math.sin(w*dT)
            robot.posx = (cos * (x - iccX) - sin * (y - iccY)) + iccX       
            robot.posy = (sin * (x - iccX) + cos * (y - iccY)) + iccY
            robot.dirr = math.degrees(dirr + w*dT)%360


        def collision(self):	
            """détermine si le robot entre en collision avec un obstacle: si l'ensemble des points ou se trouve le robot rencontre l'ensemble des points ou se trouve un obstacle
        	:param Obstacle:ensemble des points ou se trouve un obstacle
        	:retour: True si collision, False sinon et affichage si collision ou non
        	"""
            robot = self.robot
            if robot == None: 
                print("pas de robot")
                return
            #gère les collisions avec les bordures
            if(robot.posx-robot.rayon <=0 or robot.posx + robot.rayon >= self.max_x):
                print("collision bordure")
                return True
            if (robot.posy-robot.rayon <=0 or robot.posy + robot.rayon >= self.max_y):
                print("collision bordure")
                return True

            for obstacle in self.ensObstacle:
                # Si la distance est inférieure à la somme des rayons, il y a collision
                if(robot.getDistance(obstacle.posx,obstacle.posy) <obstacle.rayon+robot.rayon):
                    print("collision obstacle")
                    return True	
            return False


            
        def add(self,robot1):
            """ajout d'un robot dans le monde
            :retour:rien, ajoute le robot dans ses position x,y et affiche message d'erreur si robot sort du monde
            """
            rx , ry = robot1.getPos()
            if((rx < 0) or (rx > self.max_x) or (ry < 0) or (ry > self.max_y)): #comparaison de la position du robot avec les limites du mondes
                print("Erreur : Les positions du robots sont en dehors du monde. Il n'a pas pu etre place")
                return 
                
            self.robot = robot1
            
        def addObstacle(self,obstacle):
            """ajout d'un obstacle dans le monde
            :retour:rien, ajoute l'obstacle dans ses position x,y et affiche message d'erreur si obstacle sort du monde
            """
            self.ensObstacle.add(obstacle)

        def update(self):
            """mise à jour des coordonnées du robot et vérifie s'il y a collision""" 
            
            robot = self.robot
            print("pos robot: ",robot.getPos())
            if self.collision():
                robot.dpsG = 0
                robot.dpsD = 0
            self.deplacement(0.01)      

        def run(self):
            """
            methode utilise lors de la simulation
            """
            while not (self.ia.done()):
                self.update()
                sleep(0.01)            

class Obstacle:
        """ 
        initialisation d'un obstacle avec ses differents parametres
        
        :param pos_x: position du point le plus en bas a gauche du rectangle en abscisse
        :param pos_y: position du point le plus en bas a gauche du rectangle en ordonne
        :param rayon: rayon de l'obstacle
        :param color: couleur de l'obstacle
        """
        def __init__(self,posx, posy, rayon, color):
            self.posx     = posx                     
            self.posy     = posy                    
            self.rayon    = rayon
            self.color    = color
        

        def getPos(self):
            """retourne la position du rectangle (le point le plus en bas a gauche)
            :retour: (posx,posy)
            """
            return (self.posx, self.posy)

