import sys
sys.path.append("..")
from robot import Robot, angleVecteur
from environnement import Obstacle, Environnement
from simulationtkinter import Simulationtkinter
from time import sleep
import math
import random

class Simulationtest:

	def __init__(self,environnement,robot):
		self.robot = robot
		self.environnement = environnement
	def updatesimulationtest(self):
		self.simulationtkinter.start()

