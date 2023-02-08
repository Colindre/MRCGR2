import unittest
from robot import Robot
from environnement import Environnement
from environnement import Obstacle

class TestRobot(unittest.TestCase):
    def setUp(self):
        self.p = Robot(10,20,30,40,False,False)
        
    def test_parametre(self):
        self.assertEqual(self.p.posx,10)
        self.assertEqual(self.p.posy,20)
        self.assertEqual(self.p.dirr,30)
        self.assertEqual(self.p.rayon,40)
        self.assertFalse(self.p.roueD)
        self.assertFalse(self.p.roueG)

    def test_ensPointsRobots(self):
        ens = self.p.ensPointsRobots()
        self.assertNotIn(self.p,ens)

    def test_collision(self):
        obstacle1 = Obstacle(10,20,30,10,3)
        obstacle2 = Obstacle(80,80,2,2,3)
        self.assertTrue(self.p.collision(obstacle1))
        self.assertFalse(self.p.collision(obstacle2))
    
    def test_angle(self):
        self.p.rotation(25)
        self.assertAlmostEqual(55,self.p.dirr)
        self.p.rotation(-40)
        self.assertAlmostEqual(15,self.p.dirr)


        


        
if __name__ == '__main__':
    unittest.main()
      
    
    
    
    
    
