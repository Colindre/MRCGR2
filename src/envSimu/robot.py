class Robot:
	def __init__(self,posx, posy, dirr):
		self.posx = posx					#position du robot sur l'axe des abscisse 
		self.posy = posy					#position du robot sur l'axe des abscisse 
		self.dirr  = dirr					#direction du robot (1 pour haut, 2 pour droite, 3 pour bas, 4 pour gauche)
	
	def getPos(self):						#retourne la position
		return (self.posx, self.posy)
		
	def getDirr(self):						#retourne la direction
		return self.dirr
		
	def avancer(self):                                      	#avance le robot de 1 (en fonction de sa direction) 
									#en prenant en compte que le point en bas a gauche est (0,0)
		if(self.dirr==1):
			self.posy +=1
		elif(self.dirr==2):
			self.posx +=1

		elif(self.dirr==3):
			self.posy -=1

		else:
			self.posx -=1
	
	def reculer(self):						#recule le robot (similairement a avancer)

		if(self.dirr==1):
			self.posy -=1

		elif(self.dirr==2):
			self.posx -=1

		elif(self.dirr==3):
			self.posy +=1

		else:
			self.posx +=1
	
	def tourner(self, direction):					#tourne le robot selon une direction
			if (direction == "d"):                                  	#cas "d" pour droite 
					self.dirr = (self.dirr%4) + 1
			elif (direction == "g"):                                	#cas "g" pour gauche
				if (self.dirr == 1): 
					self.dirr=4
				else:
					self.dirr -= 1
 		
            
			else:                                                   	#cas argument non valide
				print("Mauvais argument, le robot n'a pas tourne. Les parametres possibles sont: 'd' ou 'g'")
			
	
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
