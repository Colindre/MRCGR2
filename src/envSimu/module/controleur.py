class controleur_simu:
    def __init__(self,env):
        self.env   = env
        self.robot = env.robot

    def avance_droit(self, dps, dT):
        self.robot.dpsG = dps
        self.robot.dpsD = dps
        self.env.deplacement(dT)
    
    def tourne_droite(self, dps, dT):
        self.robot.dpsG = -dps
        self.robot.dpsD = dps
        self.env.deplacement(dT)

    def tourne_gauche(self, dps, dT):
        self.robot.dpsG = dps
        self.robot.dpsD = -dps
        self.env.deplacement(dT)

    def stop(self):
        self.robot.dpsG = 0
        self.robot.dpsD = 0


class controleur_reel:
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
        