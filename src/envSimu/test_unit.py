import unittest
import math
import random
from module.robot import Robot
from module.environnement import Environnement, Obstacle
from module.ia import *
from module.proxy import proxy_virtuel

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
    
    def test_distanceparcourue(self):
        self.e = Environnement(100,100,None)
        self.e.add(self.r)
        lastX = self.r.posx
        lastY = self.r.posy
        self.r.posx = 15
        self.r.posy = 23
        self.assertAlmostEqual(self.r.distance_parcourue(lastX,lastY),5.830951895)

    def test_angle_parcouru_droit(self):
        self.r.lastdirr = self.r.dirr
        self.r.dirr = 120
        self.assertEqual(self.r.angle_parcouru_droit(self.r.lastdirr),330)

    def test_angle_parcouru_gauche(self):
        self.r.lastdirr = self.r.dirr
        self.r.dirr = 60
        self.assertEqual(self.r.angle_parcouru_gauche(self.r.lastdirr),330)

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
        self.e = Environnement(100,100,None)
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
        f = random.uniform(0.01,5.0)
        self.e.add(r)
        self.e.robot.augDPSd() ; self.e.robot.augDPSg()
        tmpX = self.e.robot.posx ; tmpY = self.e.robot.posy
        self.e.deplacement(f)
        self.e.update()
        self.assertNotEqual(tmpX , self.e.robot.posx)
        self.assertNotEqual(tmpY , self.e.robot.posy)

class TestIACarre2(unittest.TestCase):
    def setUp(self):
        rbt = Robot(250,250,90,50,100)
        rbt_simu = proxy_virtuel(rbt)
        carre2 = Carre2(rbt_simu, 100, 50)
        self.ia = IA(rbt_simu,carre2)

    def test_IACarre2_start(self):
        self.ia.start()
        self.assertTrue(self.ia.action.start)

    def test_IACarre2_update(self):
        self.ia.update()
        self.assertTrue(self.ia.action.update)
    
    def test_IACarre2_done(self):
        self.ia.action.done
        self.assertFalse(self.ia.done())

    def test_IACarre2_run(self):
        self.ia.start() 
        time.sleep(0.1)
        self.ia.update()
        self.ia.action.done = True
        time.sleep(0.1)
        self.assertTrue(self.ia.done)
    
class TestParcourirDistance(unittest.TestCase):
    def setUp(self):
        rbt = Robot(250,250,90,50,100)
        rbt_simu = proxy_virtuel(rbt)
        self.d = ParcourirDistance(rbt_simu,20,50)

        def test_ParcourirDistance_start(self):
            self.d.start
            self.assertTrue(self.d.running)

        def test_ParcourirDistance_done(self):
            posfinal = (math.sqrt((self.d.rbt_simu.rbt.posx)**2+(self.d.rbt_simu.rbt.posy)**2) + self.d.distance)*(math.cos(self.d.rbt_simu.rbt.dirr)+math.sin(self.d.rbt_simu.rbt.dirr))
            self.d.done()
            self.assertEqual(posfinal,self.d.rbt_simu.dist_parcourue(self.d.rbt_simu.lastposx,self.d.rbt_simu.lastposy))
            self.assertFalse(self.d.running)

     

    
    

    
    

        
        


        
if __name__ == '__main__':
    unittest.main()
      
    
    
    
    
    
