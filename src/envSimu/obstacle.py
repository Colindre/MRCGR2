class Obstacle:
    def __init__(self,posx, posy, tailleX, tailleY):
        self.posx     = posx                    #position du point le plus en bas a gauche du rectangle en abscisse 
        self.posy     = posy                    #position du point le plus en bas a gauche du rectangle en ordonne
        self.tailleX  = tailleX                    #taille du rectangle en abscisse
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

#TEST
o = Obstacle(0,0,2,4)
print(o.ensPoints())
