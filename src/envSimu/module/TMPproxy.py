class proxy_physique:

    def init(self, robot):
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



    def proche_mur(self):

        pass



    def dist_parcourue(self):

        pass



    def angle_parcouruD(self):

        pass



    def angle_parcouruG(self):

        pass





class proxy_virtuel:

    def init(self, env):

        self.robot = env.robot
        self.env   = env



    def avance_droit(self, dps):

        self.robot.set_motor_dps(dps, dps)



    def tourne_droite(self, dps):

       self.robot.set_motor_dps(-dps, dps)



    def tourne_gauche(self, dps):

       self.robot.set_motor_dps(dps, -dps)



    def stop(self):

        self.robot.set_motor_dps(0, 0)



    def proche_mur(self):

        pass



    def dist_parcourue(self, last_pos):

        pass



    def angle_parcouruD(self, last_angle):

        pass



    def angle_parcouruG(self, last_angle):

        pass