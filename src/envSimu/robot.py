import math
import numpy as np
class Robot:
	""" 
	initialisation de notre robot avec ses différents paramètres
	
	:param posx: position en x du robot
	:param posy: position en y du robot
	:param dirr: direction du robot, angle en degré
	:param rayon: rayon du robot, qui est un cercle
	:param roueD: True si la roue droite est en marche,False sinon
	:param roueG: True si la roue gauche est en marche,False sinon
	"""


	def __init__(self,posx, posy, dirr,rayon,roueD,roueG):

		self.posx = posx					#position du robot sur l'axe des abscisse 
		self.posy = posy					#position du robot sur l'axe des abscisse 
		self.dirr  = dirr%360				#direction du robot (angle en degre)
		self.rayon=rayon					#rayon du robot (que l'on considère désormais comme un cercle)
		self.roueD=roueD					#la roue droite tourne-t-elle ? (True pour oui et False pour non)
		self.roueG=roueG					#la roue gauche tourne-t-elle ? (True pour oui et False pour non)

	def getPos(self):
		""" retourne la position
		:retour: tuple (posx,posy)
		"""
		return (self.posx, self.posy)
	
	def setPos(self, x, y):
		""" modifie la position
		:param x: nouvelle position du robot en abscisse
		:param y: nouvelle position du robot en ordonne
		:retour: vide
		"""
		self.posx = x
		self.posy = y
			
	def getDirr(self):
		""" retourne la direction
		:retour: int, direction du robot
		"""
		return self.dirr
			
	def getRayon(self):
		"""	retourne le rayon
		:retour: int, rayon du robot
		"""
		return self.rayon
	
	def getRoueD(self):	
		"""retourne si la roue droite est en marche ou non
			:retour: True si elle est en marche,False sinon
		"""
	
		return self.roueD
		
	def getRoueG(self):
		"""retourne si la roue gauche est en marche ou non
			:retour: True si elle est en marche,False sinon
		"""
		return self.roueG
			
	def ensPointsRobots(self): 
		""" rend l'ensemble des points ou se trouve le robot
			:retour: ensemble ens des points ou se trouve le robot
		"""
		ens=set()
		a=self.posx
		b=self.posy
		for i in np.arange(self.posx-self.rayon, self.posx + self.rayon):
			for j in np.arange(self.posy-self.rayon, self.posy + self.rayon):
				if(((i - a)**2 + (j - b)**2 )<= self.rayon**2):
					ens.add((i,j))
		return ens
					
	def collision(self, ensPointsObstacle):				
			                                                    		
		"""détermine si le robot entre en collision avec un obstacle: si l'ensemble des points ou se trouve le robot rencontre l'ensemble des points ou se trouve un obstacle
			:param ensPointsObstacle:ensemble des points ou se trouve un obstacle
			:retour: True si collision, False sinon et affichage si collision ou non
		"""
		for p in ensPointsObstacle: 
			for q in self.ensPointsRobots():
				if (p == q):
					print("Robot est sur un obstacle.")
					return True
		print("le robot ne se trouve pas sur un obstacle")
		return False


	def rotation(self, angle):						
		"""fait tourner le robot (angle positif pour tourner a gauche, negatif pour a droite)
			:param angle: angle en degré du quel on veut faire tourner le robot
			:retour: rien, modifie la direction du robot
		"""
		angle     = math.radians(angle%360)
		cos       = math.cos(angle) 
		sin       = math.sin(angle)
		direction = math.radians(self.dirr)
		x, y      = math.cos(direction), math.sin(direction) 
		x         = x*cos-y*sin
		y         = x*sin+y*cos
		if(((math.degrees(angle)+self.dirr)%360 > 180)):
			self.dirr = 360 - math.degrees(math.acos(x))
		elif((math.degrees(angle)+self.dirr)%360 < (-180)):
			self.dirr = 360 - math.degrees(math.acos(x))
		else:
			self.dirr = math.degrees(math.acos(x))

def angleVecteur(vecteur):	
	"""calcul l'angle positif du vecteur (par rapport a l'axe des abscisse)
		:param vecteur: vecteur (x,y)
		:retour: angle du vecteur
	"""
											
	x1, y1     = vecteur
	x2, y2     = 1, 0
	norme1     = math.sqrt(x1**2 + y1**2)
	norme2     = math.sqrt(x2**2 + y2**2)
	scalaire   = x1*x2 + y1*y2
	angle      = math.degrees(math.acos(scalaire / (norme1*norme2)))
	if(y1<0):										#permet de calculer l'angle positif
		return 360-angle
	else:
		return angle
			
	"""def deplacement_avec_roues(self, vecteur):
		if (not self.roueD and not self.roueG):
			print("pas de déplacement effectué, les roues ne sont pas en marche")
			
		if (self.roueD and not self.roueG):
			angle = angleVecteur(vecteur)			#calcul la nouvelle direction du robot et le fait tourner en celle-ci
			self.rotation(angle - self.dirr-90)
												#effectue le deplacement
			vectX, vectY = vecteur
			self.posx = (self.posx + vectX)
			self.posy = (self.posy + vectY)"""

			

			


