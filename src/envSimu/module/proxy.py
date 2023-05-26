import time
import math

class proxy_physique:

    def __init__(self, robot):
        self.robot = robot
        self.lastdirr = 0
        self.distance_parcourue = 0
        self.angle_parcouru = 0
        self.posRL = (0,0)
        
    def reset(self):
        self.robot.offset_motor_encoder(self.robot.MOTOR_LEFT,self.robot.read_encoders()[0])
        self.robot.offset_motor_encoder(self.robot.MOTOR_RIGHT,self.robot.read_encoders()[1])
        self.distance_parcourue = 0
        self.angle_parcouru = 0

    def avance_droit(self, dps):
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT + self.robot.MOTOR_RIGHT, dps)
        self.dist_parcourue()

    def test_cercle(self, dps1, dps2):
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT, dps1)
        self.robot.set_motor_dps(self.robot.MOTOR_RIGHT, dps2)
        self.dist_parcourue()

    def tourne_droite(self, dps):
       self.robot.set_motor_dps(self.robot.MOTOR_LEFT, dps)
       self.robot.set_motor_dps(self.robot.MOTOR_RIGHT, -dps)
       self.angle_parcouruD()

    def tourne_gauche(self, dps):
       self.robot.set_motor_dps(self.robot.MOTOR_LEFT, -dps)
       self.robot.set_motor_dps(self.robot.MOTOR_RIGHT, dps)
       self.angle_parcouruG()

    def stop(self):
         self.robot.stop()

    def proche_obstacle(self):
        self.robot.get_distance()< 100

    def dist_parcourue(self):
        self.posRL = self.robot.get_motor_position()
        dist_left = self.posRL[0] * self.robot.WHEEL_CIRCUMFERENCE / 360
        dist_right = self.posRL[1] * self.robot.WHEEL_CIRCUMFERENCE / 360
        distance_parcourue = (dist_left + dist_right) / 2
        print("dist parc ", distance_parcourue)
        return distance_parcourue

    def angle_parcouruD(self):
        diamRoue = self.WHEEL_DIAMETER/10
        rayonRobot = self.WHEEL_BASE_WIDTH/20
        posRoues = self.get_motor_position()
        pos = posRoues
        posG = pos[0]/360*diamRoue*math.pi
        posD = pos[1]/360*diamRoue*math.pi
        angle = (posD-posG)/(rayonRobot*2)

        last_dirr_rad = math.radians(self.lastdirr)
        x1, y1        = math.cos(last_dirr_rad), math.sin(last_dirr_rad)		#points du vecteur a partir de la derniere direction
        dirr_rad      = math.radians(angle)
        x2, y2        = math.cos(dirr_rad), math.sin(dirr_rad)					#points du vecteur a partir de la direction actuelle
        scalaire      = x1*x2 + y1*y2											#calcule produit le produit scalaire
        determinant   = x1*y2 - y1*x2											#calcule le determinant
        angle         = math.atan2(determinant, scalaire)						#calcule l'angle parcouru
        res = (360 - math.degrees(angle))%360

        self.anglefin += res
        self.lastdirr = angle
        return self.anglefin

    def angle_parcouruG(self):
        diamRoue = self.WHEEL_DIAMETER/10
        rayonRobot = self.WHEEL_BASE_WIDTH/20
        posRoues = self.get_motor_position()
        pos = posRoues
        posG = pos[0]/360*diamRoue*math.pi
        posD = pos[1]/360*diamRoue*math.pi
        angle = (posD-posG)/(rayonRobot*2)

        last_dirr_rad = math.radians(self.lastdirr)
        x1, y1        = math.cos(last_dirr_rad), math.sin(last_dirr_rad)		#points du vecteur a partir de la derniere direction
        dirr_rad      = math.radians(angle)
        x2, y2        = math.cos(dirr_rad), math.sin(dirr_rad)					#points du vecteur a partir de la direction actuelle
        scalaire      = x1*x2 + y1*y2											#calcule produit le produit scalaire
        determinant   = x1*y2 - y1*x2											#calcule le determinant
        angle         = math.atan2(determinant, scalaire)						#calcule l'angle parcouru
        res = math.degrees(angle)%360

        self.anglefin += res
        self.lastdirr = angle
        return self.anglefin



class proxy_virtuel:

    def __init__(self,env):
        self.env      = env
        self.robot    = env.robot
        self.lastposx = self.robot.posx
        self.lastposy = self.robot.posy
        self.lastdirr = self.robot.dirr
        self.lasttime = self.env.temps
        self.distfin  = 0
        self.anglefin = 0
        
    def reset(self):
        self.lastposx = self.robot.posx
        self.lastposy = self.robot.posy
        self.lastdirr = self.robot.dirr
        self.lasttime = self.env.temps
        self.distfin  = 0
        self.anglefin = 0
    
    def avance_droit(self, dps):
        self.robot.set_motor_dps(dps,dps)
        self.dist_parcourue()

    def test_cercle(self, dps1, dps2):
        self.robot.set_motor_dps(dps1,dps2)
        self.dist_parcourue()

    def tourne_droite(self, dps):
       self.robot.set_motor_dps(dps, -dps)
       self.angle_parcouruD()

    def tourne_gauche(self, dps):
       self.robot.set_motor_dps(-dps, dps)
       self.angle_parcouruG()

    def stop(self):
        self.robot.set_motor_dps(0, 0)

    def proche_obstacle(self):
        return self.env.get_distance() < 1

    def dist_parcourue(self):
        self.distfin +=self.robot.distance_parcourue(self.lastposx,self.lastposy)
        self.lastposx = self.robot.posx
        self.lastposy = self.robot.posy
        return self.distfin

    def angle_parcouruD(self):
        self.anglefin += self.robot.angle_parcouru_droit(self.lastdirr)
        self.lastdirr = self.robot.dirr
        return self.anglefin

    def angle_parcouruG(self):
        self.anglefin += self.robot.angle_parcouru_gauche(self.lastdirr)
        self.lastdirr = self.robot.dirr 
        return self.anglefin
