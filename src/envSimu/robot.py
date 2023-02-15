import math


class Robot:
	""" 
	initialisation de notre robot avec ses différents paramètres
	
	:param posx: position en x du robot
	:param posy: position en y du robot
	:param dirr: direction du robot, angle en degré
	:param rayon: rayon du robot, qui est un cercle
	:param diamR: float representant le diametre des roues
	:param distR: float representant la distance entre les deux roues
	"""


	def __init__(self,posx, posy, dirr,rayon,diamR,dpsG,dpsD):

		self.posx = posx					
		self.posy = posy					
		self.dirr = dirr%360				
		self.rayon=rayon					
		self.diamR=diamR					
		self.distR=rayon*2
		self.dpsG=dpsG
		self.dpsD=dpsD			

	def getPos(self):
		""" retourne la position
		:retour: tuple (posx,posy)
		"""
		return (self.posx, self.posy)
		
	def getPosRd(self):
		""" retourne la pos de la roue droite
		"""
		x,y = self.getPos()
		dirr=math.radians(self.dirr)
		return x+self.rayon*math.cos(dirr-math.radians(90)),y+self.rayon*math.sin(dirr-math.radians(90))

	def getPosRg(self):
		""" retourne la pos de la roue droite
		"""
		x,y = self.getPos()
		dirr=math.radians(self.dirr)
		return x+self.rayon*math.cos(dirr+math.radians(90)),y+self.rayon*math.sin(dirr+math.radians(90))
		
	

	def rotation(self, angle):						
		"""fait tourner le robot (angle positif pour tourner a gauche, negatif pour a droite)
			:param angle: angle en degré du quel on veut faire tourner le robot
			:retour: rien, modifie la direction du robot
		"""
		if angle==None:
			return
		angle     = math.radians(angle % 360)
		cos       = math.cos(angle) 
		sin       = math.sin(angle)
		direction = math.radians(self.dirr)
		x, y      = math.cos(direction), math.sin(direction) 
		x         = x*cos-y*sin
		y         = x*sin+y*cos
		if(math.degrees(angle)+self.dirr) % 360 > 180:
			self.dirr = 360 - math.degrees(math.acos(x))
		elif(math.degrees(angle)+self.dirr) % 360 < (-180):
			self.dirr = 360 - math.degrees(math.acos(x))
		else:
			self.dirr = math.degrees(math.acos(x))
	
	def velocityD(self):
		"""
		retourne la vélocité de la roue droite en fonction du dps de celle-ci
		"""
		return self.rayon*(self.dpsD/360)*60*0.10472
		
	def velocityG(self):
		"""
		retourne la vélocité de la roue droite en fonction du dps de celle-ci
		"""
		return self.rayon*(self.dpsG/360)*60*0.10472
		
	

def angleVecteur(vecteur):	
	"""calcul l'angle positif du vecteur (par rapport a l'axe des abscisse)
		:param vecteur: vecteur (x,y)
		:retour: angle du vecteur
	"""
	if vecteur==(0,0):
		return None									
	x1, y1     = vecteur
	x2, y2     = 1, 0
	norme1     = math.sqrt(x1**2 + y1**2)
	norme2     = math.sqrt(x2**2 + y2**2)
	scalaire   = x1*x2 + y1*y2
	angle      = math.degrees(math.acos(scalaire / (norme1*norme2)))
	if y1 < 0:								# permet de calculer l'angle positif
		return 360-angle
	else:
		return angle
		
		
