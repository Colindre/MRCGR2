import time

class proxy_physique:

    def __init__(self, robot):
        self.robot = robot



    def avance_droit(self, dps):

        self.robot.set_motor_dps(self.robot.MOTOR_LEFT + self.robot.MOTOR_RIGHT, dps)



    def tourne_droite(self, dps):
       
       self.robot.set_motor_dps(self.robot.MOTOR_LEFT, -dps)
       self.robot.set_motor_dps(self.robot.MOTOR_RIGHT, dps)



    def tourne_gauche(self, dps):

       self.robot.set_motor_dps(self.robot.MOTOR_LEFT, dps)
       self.robot.set_motor_dps(self.robot.MOTOR_RIGHT, -dps)



    def stop(self):

         self.robot.stop()



    def proche_obstacle(self):

        pass



    def dist_parcourue(self):

        pass



    def angle_parcouruD(self):

        pass



    def angle_parcouruG(self):

        pass





class proxy_virtuel:

    def __init__(self,robot):
        self.robot = robot

    def avance_droit(self, dps):
        self.robot.avance_tout_droit(dps)

    def tourne_droite(self, dps):
       self.robot.set_motor_dps(-dps, dps)


    def tourne_gauche(self, dps):
       self.robot.set_motor_dps(dps, -dps)

    def stop(self):
        self.robot.set_motor_dps(0, 0)

    def proche_obstacle(self):
        pass

    def dist_parcourue(self,lastposx,lastposy):
        return self.robot.distance_parcourue(lastposx,lastposy)

    def angle_parcouruD(self, last_dirr):
        return self.robot.angle_parcourueD(last_dirr)

    def angle_parcouruG(self, last_dirr):
        return self.robot.angle_parcourueD(last_dirr)
