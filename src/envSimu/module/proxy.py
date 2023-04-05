import time

class proxy_physique:

    def __init__(self, robot):
        self.robot = robot
        self.distance_parcourue = 0
        self.angle_parcouru = 0
        self.posRL = (0,0)
        
    def reset(self):
        self.robot.offset_motor_encoder(self.robot.MOTOR_LEFT,self.robot.get_motor_position())
        self.robot.offset_motor_encoder(self.robot.MOTOR_RIGHT,self.robot.get_motor_position())
        self.distance_parcourue = 0

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
        
        return distance_parcourue

    def angle_parcouru_gauche(self):
        ang_left, ang_right = self.robot.get_motor_position()

        angpar_left = ang_left / 360 * self.robot.WHEEL_CIRCUMFERENCE 
        
        angle_parcouru = (angpar_left) / self.robot.WHEEL_DIAMETER
        
        if(angle_parcouru !=0):
            self.resetAng()
        
        return angle_parcouru

    def angle_parcouru_droit(self):
    
        ang_left, ang_right = self.robot.get_motor_position()

        angpar_right = ang_right / 360 * self.robot.WHEEL_CIRCUMFERENCE 
        
        angle_parcouru = (angpar_right) / self.robot.WHEEL_DIAMETER
        
        if(angle_parcouru !=0):
            self.resetAng()
        
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
       self.angle_parcouru_droit()

    def tourne_gauche(self, dps):
       self.robot.set_motor_dps(-dps, dps)
       self.angle_parcouru_gauche()

    def stop(self):
        self.robot.set_motor_dps(0, 0)

    def proche_obstacle(self):
        return self.env.get_distance() < 1

    def dist_parcourue(self):
        self.distfin +=self.robot.distance_parcourue(self.lastposx,self.lastposy)
        self.lastposx = self.robot.posx
        self.lastposy = self.robot.posy
        return self.distfin

    def angle_parcouru_droit(self):
        self.anglefin +=self.robot.angle_parcouru_droit(self.lastdirr)
        self.lastdirr = self.robot.dirr
        return self.anglefin

    def angle_parcouru_gauche(self):
        self.anglefin +=self.robot.angle_parcouru_gauche(self.lastdirr)
        self.lastdirr = self.robot.dirr
        return self.anglefin
