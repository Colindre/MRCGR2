import math

class Robot:
	def __init__(self,posx, posy, dirr):
		self.posx = posx					#position du robot sur l'axe des abscisse 
		self.posy = posy					#position du robot sur l'axe des abscisse 
		self.dirr  = dirr%360				#direction du robot (angle en degre)
	
	def getPos(self):						#retourne la position
		return (self.posx, self.posy)
		
	def getDirr(self):						#retourne la direction
		return self.dirr

	def deplacement(self, vecteur):		#change direction du robot et le fait avancer, en prenant en compte que le point en bas a gauche est (0,0)

		angle = angleVecteur(vecteur)			#calcul la nouvelle direction du robot et le fait tourner en celle-ci
		self.rotation(angle - self.dirr)
												#effectu le deplacement
		vectX, vectY = vecteur
		self.posx = (self.posx + vectX)
		self.posy = (self.posy + vectY)
				
	def detecter(self, tabPoints):					#verifie si le robot detecte un objet devant lui. tabPoints est un tableau de tuple
	                                                        	#regarde si position du robot est dans le tableau de points
		for p in tabPoints: 
			if (p == self.getPos()):
				print("Robot est sur un obstacle. Suite des operations impossible")
				return True
			
			
		if(self.dirr==1):										#regarder direction du robot et prend la valeur de la position apres un avancement (l'avancement n'est pas realise)
			testPos = (self.posx, self.posy+1)
		elif(self.dirr==2):
			testPos = (self.posx+1, self.posy)
		elif(self.dirr==3):
			testPos = (self.posx, self.posy -1)
		else:
			testPos = (self.posx-1, self.posy)
		
		for p in tabPoints:										#regarde si la position est dans le tableau de points
			if (p == testPos):
				print("Obstacle devant le robot.")
				return True
		print("pas d'obstacle devant")
		return False

	def rotation(self, angle):						#fait tourner le robot (angle positif pour tourner a gauche, negatif pour a droite)
		angle     = math.radians(angle%360)
		cos       = math.cos(angle) 
		sin       = math.sin(angle)
		direction = math.radians(self.dirr)
		x, y      = math.cos(direction), math.sin(direction) 
		x         = x*cos-y*sin
		y         = x*sin+y*cos
		if(((math.degrees(angle)+self.dirr)%360 > 180)):
			self.dirr = 360 - math.degrees(math.acos(x))
		elif(((math.degrees(angle)+self.dirr)%(-360) < -180)):
			self.dirr = 360 - math.degrees(math.acos(x))
		else:
			self.dirr = math.degrees(math.acos(x))

def angleVecteur(vecteur):							#calcul l'angle positif du vecteur (par rapport a l'axe des abscisse)
	x1, y1     = vecteur
	x2, y2     = 1, 0
	norme1     = math.sqrt(x1**2 + y1**2)
	norme2     = math.sqrt(x2**2 + y2**2)
	scalaire   = x1*x2 + y1*y2
	angle      = math.degrees(math.acos(scalaire / (norme1*norme2)))
	if(x1>0 and y1>0):								#permet de calculer l'angle positif
		return angle
	elif(x1>0 and y1<0):
		return 360-angle
	elif(x1>0 and y1==0):
		return angle
	elif(x1<0 and y1>0):
		return angle
	elif(x1<0 and y1<0):
		return 360-angle
	elif(x1<0 and y1==0):
		return angle
	elif(x1==0 and y1>0):
		return angle
	elif(x1==0 and y1<0):
		return 360-angle
	else:
		return angle



#TEST 
robot = Robot(2,2,90)
print("direction robot: ",robot.getDirr())
print("position robot: ",robot.getPos())
robot.deplacement((1,-1))
print("angle du vecteur: ",angleVecteur((1,-1)))
print("apres deplacement:")
print("dir: ",robot.getDirr())
print("pos: ",robot.getPos())
