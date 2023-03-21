import time

class proxy_physique:

    def __init__(self, robot):
        self.robot = robot

    def reset(self):
        pass

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

        pass



    def angle_parcouru_droit(self):

        pass



    def angle_parcouru_gauche(self):

        pass





class proxy_virtuel:

    def __init__(self,env):
        self.env      = env
        self.robot    = env.robot
        self.lastposx = self.robot.posx
        self.lastposy = self.robot.posy
        self.lastdirr = self.robot.dirr
        
    def reset(self):
        self.lastposx = self.robot.posx
        self.lastposy = self.robot.posy
        self.lastdirr = self.robot.dirr
    
    def avance_droit(self, dps):
        self.robot.avance_tout_droit(dps)

    def tourne_droite(self, dps):
       self.robot.set_motor_dps(dps, -dps)

    def tourne_gauche(self, dps):
       self.robot.set_motor_dps(-dps, dps)

    def stop(self):
        self.robot.set_motor_dps(0, 0)

    def proche_obstacle(self):
        return self.env.get_distance() < 2

    def dist_parcourue(self,lastposx,lastposy):
        return self.robot.distance_parcourue(lastposx,lastposy)

    def angle_parcouru_droit(self, last_dirr):
        return self.robot.angle_parcouru_droit(last_dirr)

    def angle_parcouru_gauche(self, last_dirr):
        return self.robot.angle_parcouru_gauche(last_dirr)
