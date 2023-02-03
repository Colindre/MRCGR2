from robot import Robot, angleVecteur

class Environnement:
        """ 
        initialisation de notre environnement avec ses differents parametres
        
        :param max_x: max de l'environnement en x
        :param max_y: max de l'environnement en y
        :param dirr: direction du robot, angle en degre
        :param ensPointsObstacle: ensemble des points ou se trouve un obstacle
        """
        def __init__(self,max_x,max_y):
            self.max_x= max_x 
            self.max_y=max_y  
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

        def deplacement(self, robot, vecteur):		
            """ effectue un déplacement du robot selon un vecteur
                :param robot: robot qui effectue le deplacement
                :param vecteur: vecteur (x,y)
                :retour: rien, cela effectue directement le changement de posx et posy
            """

            angle = angleVecteur(vecteur)			#calcul la nouvelle direction du robot et le fait tourner en celle-ci
            robot.rotation(angle - robot.getDirr())
                                                    #effectue le deplacement
            vectX, vectY = vecteur
            posx, posy = robot.getPos()
            robot.setPos(posx+vectX, posy+vectY)
            
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
            ox , oy = obstacle.getPos()
            if((ox < 0) or (ox > self.max_x) or (oy < 0) or (oy > self.max_y)):
                print("Erreur : Les positions de l'obstacle sont en dehors du monde. Il n'a pas pu etre mis place")
                return
            
            for l in self.listeObstacle:
                if((ox,oy) == l):
                    print("Erreur : il y a deja un obstacle a cette position. Il n'a pas pu etre mis en place")
                    return
            self.ensPointsObstacle.add((ox,oy))
            print("L'obstacle a ete place en ",obstacle.getPos())
            
        def update(self,robot):
            """nouvel affichage de notre monde
            affiche si erreur avec le deplacement du robot
            """
            rx , ry = robot.getPos()
            if((rx < 0) or (rx > self.max_x) or (ry < 0) or (ry > self.max_y)):
                print("Erreur : Le robot se trouve en dehors du monde")

                return
            print("Le robot se trouve desormais en ",robot.getPos()," et est dirige vers ",robot.getDirr())
            
        
      
      
      
     
class Obstacle:
        """ 
        initialisation d'un obstacle avec ses differents parametres
        
        :param pos_x: position du point le plus en bas a gauche du rectangle en abscisse
        :param pos_y: position du point le plus en bas a gauche du rectangle en ordonne
        :param tailleX: taille du rectangle en abscisse
        :param tailleY: taille du rectangle en ordonne
        """
        def __init__(self,posx, posy, tailleX, tailleY):
            self.posx     = posx                     
            self.posy     = posy                    
            self.tailleX = tailleX                   
            self.tailleY  = tailleY 
        
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
            ens=set()
            for i in range(self.posx, self.posx + self.tailleX + 1):
                for j in range(self.posy, self.posy + self.tailleY + 1):
                    ens.add((i,j))
            return ens
