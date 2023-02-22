class controleur:
    def init(self, robot):
        self.robot = robot

    def avance_droit(self, dps, dT):
        self.robot.set_motor_dps(self, self.robot.MOTOR_LEFT + self.robot.MOTOR_RIGHT, dps)

    def tourne_droite(self, dps, dT):
       self.robot.set_motor_dps(self, self.robot.MOTOR_LEFT, -dps)
       self.robot.set_motor_dps(self, self.robot.MOTOR_RIGHT, dps)

    def tourne_gauche(self, dps, dT):
       self.robot.set_motor_dps(self, self.robot.MOTOR_LEFT, dps)
       self.robot.set_motor_dps(self, self.robot.MOTOR_RIGHT, -dps)

    def stop(self):
         self.robot.stop()
