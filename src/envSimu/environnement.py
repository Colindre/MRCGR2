class Environnement:
    def __init__(self,max_x,max_y,listeObstacle):
        self.max_x= max_x 
        self.max_y=max_y  
        self.listeObstacle = []

    def getPos(self):
        return (self.max_x, self.max_y)


    def afficherEnv(self):
        rx , ry = self.getPos()
        env[rx][ry]
    
    def add(self,robot):
        rx , ry = robot.getPos()
        if((rx < 0) or (rx > self.max_x) or (ry < 0) or (ry > self.max_y)): #comparaison de la position du robot avec les limites du mondes
            print("Erreur : Les positions du robots sont en dehors du monde. Il n'a pas pu etre place")
            return
            
            
        print("Le robot a été placé dans le monde en ",robot.getPos()," et est dirigé vers ",robot.getDirr())

    def addObstacle(self,obstacle):
        ox , oy = obstacle.getPos()
        if((ox < 0) or (ox > self.max_x) or (0y < 0) or (oy > self.max_y)):
            print("Erreur : Les positions de l'obstacle sont en dehors du monde. Il n'a pas pu etre mis place")
            return
          
        for l in listeObstacle:
            if((ox,oy) == l):
                print("Erreur : il y a déjà un obstacle à cette position. Il n'a pas pu etre mis en place")
                return
        
        self.listeObstacle.append((ox,oy))
        print("L'obstacle a ete place en ",obstacle.getPos())
        
    def update(self,robot):
        rx , ry = robot.getPos()
        if((rx < 0) or (rx > self.max_x) or (ry < 0) or (ry > self.max_y)):
            print("Erreur : Le robot se trouve en dehors du monde")
            return
        print("Le robot se trouve désormais en ",robot.getPos()," et est dirigé vers ",robot.getDirr())
        
        
