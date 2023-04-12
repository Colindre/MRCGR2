import time
import math

class proxy_physique:

    def __init__(self, robot):
        self.robot = robot
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

    def tourne_droite(self, dps):
       self.robot.set_motor_dps(self.robot.MOTOR_LEFT, dps)
       self.robot.set_motor_dps(self.robot.MOTOR_RIGHT, -dps)

    def tourne_gauche(self, dps):
       self.robot.set_motor_dps(self.robot.MOTOR_LEFT, -dps)
       self.robot.set_motor_dps(self.robot.MOTOR_RIGHT, dps)

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

    def angle_parcouru(self):
        ang_left, ang_right = self.robot.get_motor_position()
        print("!!!!!!!!!!!!!!!!!",ang_right)
        #Distance parcouru des deux roues
        dist_left = self.posRL[0] * self.robot.WHEEL_CIRCUMFERENCE / 360
        dist_right = self.posRL[1] * self.robot.WHEEL_CIRCUMFERENCE / 360
        angle_parcouru = math.degrees((dist_right - dist_left) / self.robot.WHEEL_BASE_WIDTH)
        print("angle parc droit: ",angle_parcouru)
        return angle_parcouru





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

    def tourne_droite(self, dps):
       self.robot.set_motor_dps(dps, -dps)
       self.angle_parcouru()

    def tourne_gauche(self, dps):
       self.robot.set_motor_dps(-dps, dps)
       self.angle_parcouru()

    def stop(self):
        self.robot.set_motor_dps(0, 0)

    def proche_obstacle(self):
        return self.env.get_distance() < 1

    def dist_parcourue(self):
        self.distfin +=self.robot.distance_parcourue(self.lastposx,self.lastposy)
        self.lastposx = self.robot.posx
        self.lastposy = self.robot.posy
        return self.distfin

    def angle_parcouru(self):
        RDx,RDy= self.robot.getPosRd()      #Position roue droite
        RGx,RGy= self.robot.getPosRg()      #Position roue gauche
        x , y = self.lastposx, self.lastposy        #Derniere pos du robot
        dirr = math.radians(self.lastdirr)
        lastRDx,lastRDy = x+self.robot.rayon*math.cos(dirr-math.radians(90)),y+self.robot.rayon*math.sin(dirr-math.radians(90))     #Derniere position roue droite
        lastRGx,lastRGy = x+self.robot.rayon*math.cos(dirr+math.radians(90)),y+self.robot.rayon*math.sin(dirr+math.radians(90))     #Derniere position roue gauche
        dRD = math.sqrt((RDx-lastRDx)**2+(RDy-lastRDy)**2)      #distance parcouru par la roue droite
        dRG = math.sqrt((RGx-lastRGx)**2+(RGy-lastRGy)**2)      #distance parcouru par la roue gauche
        
        self.anglefin += math.degrees((dRD-dRG)/self.robot.distR)
        self.lastdirr = self.robot.dirr
        return self.anglefin
        
        
