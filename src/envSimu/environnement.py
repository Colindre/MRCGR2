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
        else: 
            print("Le robot a été placé dans le monde en ",robot.getPos()," et est dirigé vers ",robot.getDirr())

    def addObstacle(self,obstacle):
        ox, oy = obstacle.getPos()
          
        if((ox,oy) in self.ensPointsObstacle):
            print("Erreur : il y a déjà un obstacle à cette position. Il n'a pas pu etre mis en place")
            return
        
        self.ensPointsObstacle.add((ox,oy))
        print("L'obstacle a ete place en ",obstacle.getPos())
        
    def update(self,robot):
        rx , ry = robot.getPos()
        if((rx < 0) or (rx > self.max_x) or (ry < 0) or (ry > self.max_y)):
            print("Erreur : Le robot se trouve en dehors du monde")
        else:
            print("Le robot se trouve désormais en ",robot.getPos()," et est dirigé vers ",robot.getDirr())
        
        
