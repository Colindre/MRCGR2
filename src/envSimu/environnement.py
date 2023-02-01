class Environnement:
    def __init__(self,max_x,max_y):
        self.max_x= max_x 
        self.max_y=max_y  
        self.ensPointsObstacle = set()

    def getPos(self):
        return (self.max_x, self.max_y)
    
    def add(self,robot):
        rx , ry = robot.getPos()
        if((rx < 0) or (rx > self.max_x) or (ry < 0) or (ry > self.max_y)): #comparaison de la position du robot avec les limites du mondes
            print("Erreur : Les positions du robots sont en dehors du monde. Il n'a pas pu etre place")
            return
            
            
        print("Le robot a ete place dans le monde en ",robot.getPos()," et est dirige vers ",robot.getDirr())

    def addObstacle(self,obstacle):
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
        rx , ry = robot.getPos()
        if((rx < 0) or (rx > self.max_x) or (ry < 0) or (ry > self.max_y)):
            print("Erreur : Le robot se trouve en dehors du monde")

            return
        print("Le robot se trouve desormais en ",robot.getPos()," et est dirige vers ",robot.getDirr())
        
      
      
      
      
     
class Obstacle:
    def __init__(self,posx, posy, tailleX, tailleY):
        self.posx     = posx                    #position du point le plus en bas a gauche du rectangle en abscisse 
        self.posy     = posy                    #position du point le plus en bas a gauche du rectangle en ordonne
        self.tailleX = tailleX                    #taille du rectangle en abscisse
        self.tailleY  = tailleY                    #taille du rectangle en ordonne
	
    def getPos(self):                            #retourne la position du rectangle (le point le plus en bas a gauche)
        return (self.posx, self.posy)

    def getDimensions(self):                    #retourne les dimensions du rectangle (tailleX, tailleY)
        return self.tailleX, self.tailleY
        

    def ensPoints(self):                      #retourne la liste des points qu'occupe l'obstacle (innacessibles aux robots)
        ens=set()
        for i in range(self.posx, self.posx + self.tailleX + 1):
            for j in range(self.posy, self.posy + self.tailleY + 1):
                ens.add((i,j))
        return ens
