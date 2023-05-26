import unittest
import math
import random
from module.robot import Robot
from module.environnement import Environnement, Obstacle

class TestRobot(unittest.TestCase):
    def setUp(self):
        self.r = Robot(10,20,90,5,10)
        
    def test_parametreRobot(self):
        self.assertEqual(self.r.posx,10)
        self.assertEqual(self.r.posy,20)
        self.assertEqual(self.r.dirr,90)
        self.assertEqual(self.r.rayon,5)
        self.assertEqual(self.r.diamR,10)

    def test_rotation(self):
        angle = 20 ; tmp = self.r.dirr 
        self.r.rotation(angle)
        self.assertEqual(self.r.dirr,tmp + angle)
        angle = -10 ; tmp = self.r.dirr
        self.r.rotation(angle)
        self.assertAlmostEqual(self.r.dirr,tmp + angle)
    
    def testdistanceparcouru(self):
        self.e = Environnement(100,100)
        self.e.add(self.r)
        print("\n avant deplacement:",self.r.getPos())
        self.r.dpsD =10
        self.r.dpsG =5
        self.e.deplacement(10)
        print("distance :",self.r.distance_parcourue())
        print("\n apres deplacement:",self.r.getPos())
        self.r.dpsD =10
        self.r.dpsG =10
        self.e.deplacement(10)
        print("distance2 :",self.r.distance_parcourue())
        print("\n apres deplacement2:",self.r.getPos())


class TestObstacle(unittest.TestCase):
    def setUp(self):
        self.o = Obstacle(30,20,5,'red')
    
    def test_parametreObstacle(self):
        self.assertEqual(self.o.posx,30)
        self.assertEqual(self.o.posy,20)
        self.assertEqual(self.o.rayon,5)
        self.assertEqual(self.o.color,'red')
    
    
class TestEnvironnement(unittest.TestCase):
    def setUp(self):
        self.e = Environnement(100,100)
        self.e.addObstacle(Obstacle(50,40,5,'red'))

    def test_parametreEnvironnement(self):
        self.assertEqual(self.e.max_x,100)
        self.assertEqual(self.e.max_y,100)
    
    def test_deplacement(self):
        r = Robot(10,20,50,5,10)
        r.augDPSd = 45 ; r.augDPSg = 45
        tmpX = r.posx ; tmpY = r.posy ; tmpDirr = math.radians(r.dirr) ; dT = 1
        self.e.add(r)
        self.e.deplacement(dT)
        self.assertEqual(r.posx , tmpX + (r.velocityD() * dT * math.cos(tmpDirr)))
        self.assertEqual(r.posy , tmpY + (r.velocityG() * dT * math.cos(tmpDirr)))
    
    def test_collision(self):
        r = Robot(10,20,50,5,10)
        self.e.add(r)
        self.assertFalse(self.e.collision())
        self.e.addObstacle(Obstacle(10,20,10,'red'))
        self.assertTrue(self.e.collision())

    def test_add(self):
        r = Robot(10,20,50,5,10)
        self.e.add(r)
        self.assertIsNotNone(self.e.robot)

    def test_addObstacle(self):
        o = Obstacle(10,20,10,'red')
        self.assertEqual(self.e.ensObstacle.add(o) , self.e.addObstacle(o))
    
    def test_update(self):
        r = Robot(10,20,50,5,10)
        self.e.add(r)
        self.e.robot.augDPSd() ; self.e.robot.augDPSg()
        tmpX = self.e.robot.posx ; tmpY = self.e.robot.posy
        r = random.uniform(0.01,5.0)
        self.e.deplacement(r)
        self.e.update()
        self.assertNotEqual(tmpX , self.e.robot.posx)
        self.assertNotEqual(tmpY , self.e.robot.posy)
    

    
    

        
        


        
if __name__ == '__main__':
    unittest.main()
      
    
    
    
    
    
