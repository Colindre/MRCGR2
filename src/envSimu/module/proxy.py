import time

class proxy_physique:

    def __init__(self, robot):
        self.robot = robot
        self.distance_parcourue = 0
        self.angle_parcouru = 0

    def resetDist(self):
        self.robot.offset_motor_encode(self.robot.MOTOR_LEFT,self.robot.read_encoders()[0])
        self.robot.offset_motor_encode(self.robot.MOTOR_RIGHT,self.robot.read_encoders()[1])
        self.distance_parcourue = 0

    def resetAng(self):
        self.robot.offset_motor_encode(self.robot.MOTOR_LEFT,self.robot.read_encoders()[0])
        self.robot.offset_motor_encode(self.robot.MOTOR_RIGHT,self.robot.read_encoders()[1])

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
        pass

    def dist_parcourue(self):
        pos_left, pos_right = self.robot.get_motor_position()

        dist_left = pos_left * self.robot.WHEEL_CIRCUMFERENCE / 360
        dist_right = pos_right * self.robot.WHEEL_CIRCUMFERENCE / 360
        
        distance_parcourue = (dist_left + dist_right) / 2
        
        return distance_parcourue

    def ang_parcouru(self):
        ang_left, ang_right = self.robot.get_motor_position()

        angpar_left = ang_left / 360 * self.robot.WHEEL_CIRCUMFERENCE 
        angpar_right = ang_right / 360 * self.robot.WHEEL_CIRCUMFERENCE 
        
        angle_parcouru = (angpar_left - angpar_right) / self.robot.WHEEL_DIAMETER
        
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
        
    def reset(self):
        self.lastposx = self.robot.posx
        self.lastposy = self.robot.posy
        self.lastdirr = self.robot.dirr
        self.lasttime = self.env.temps
    
    def avance_droit(self, dps):
        self.robot.set_motor_dps(dps,dps)

    def tourne_droite(self, dps):
       self.robot.set_motor_dps(dps, -dps)

    def tourne_gauche(self, dps):
       self.robot.set_motor_dps(-dps, dps)

    def stop(self):
        self.robot.set_motor_dps(0, 0)

    def proche_obstacle(self):
        return self.env.get_distance() < 1

    def dist_parcourue(self):
        return self.robot.distance_parcourue(self.lastposx,self.lastposy)

    def angle_parcouru_droit(self):
        return self.robot.angle_parcouru_droit(self.lastdirr)

    def angle_parcouru_gauche(self):
        return self.robot.angle_parcouru_gauche(self.lastdirr)
