import unittest
import math
from robot import Robot
from environnement import Environnement
from environnement import Obstacle

class TestRobot(unittest.TestCase):
    def setUp(self):
        self.r = Robot(10,20,50,5,10)
        
    def test_parametreRobot(self):
        self.assertEqual(self.r.posx,10)
        self.assertEqual(self.r.posy,20)
        self.assertEqual(self.r.dirr,50)
        self.assertEqual(self.r.rayon,5)
        self.assertEqual(self.r.diamR,10)

    def test_rotation(self):
        angle = 20 ; tmp = self.r.dirr 
        self.r.rotation(angle)
        self.assertEqual(self.r.dirr,tmp + angle)
        angle = -10 ; tmp = self.r.dirr
        self.r.rotation(angle)
        self.assertAlmostEqual(self.r.dirr,tmp + angle)
    
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
        tmpX = r.posx ; tmpY = r.posy ; tmpDirr = r.dirr
        self.e.deplacement(0.01)
        self.assertEqual(r.posx, tmpX + (2*0.001)*math.cos(tmpDirr))
        self.assertEqual(r.posy, tmpY + (2*0.001)*math.sin(tmpDirr))
    
    def test_collision(self):
        self.assertFalse(self.e.collision())
        self.e.addObstacle(Obstacle(10,20,10,'red'))
        self.assertTrue(self.e.collision())
        
        


        
if __name__ == '__main__':
    unittest.main()
      
    
    
    
    
    
