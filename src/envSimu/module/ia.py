import threading
import time



class IA(threading.Thread):

    def __init__(self, proxy, action):

        threading.Thread.__init__(self)
        self.action = action
        self.proxy  = proxy

    def start(self):
        return self.action.start()
    
    def update(self):
        self.action.update()

    def done(self):
        return self.action.done()

    def run(self):
        self.start()
        while not (self.done()):
            self.update()
            time.sleep(0.05)





class IAifte:

    def __init__(self, proxy, main_action, secondary_action, condition):

        self.proxy            = proxy
        self.main_action      = main_action         #example: ParcourirDistance
        self.secondary_action = secondary_action    #example: TournerDroite
        self.condition        = condition
        self.running          = False

    def start(self):

        self.main_action.start()
        self.running = True

    def update(self):

        if self.done():
            self.main_action.running      = False 
            self.secondary_action.running = False
            return

        if self.condition(self.proxy):              #example: distance_parcourue() > 100
            #self.main_action.running = False       | /!\ : à tester
            if not self.secondary_action.running:
                self.secondary_action.start()
            self.secondary_action.update()
        else:
            self.main_action.update()

    def done(self):
        self.running = not (self.main_action.done() or self.secondary_action.done())
        return not self.running

    

class IAseq:

    def __init__(self, proxy, list):
        self.proxy   = proxy
        self.list    = list
        self.index   = 0
        self.running = False

    def start(self):
        self.index   = 0
        self.list[self.index].start()
        self.running = True

    def update(self):
        if self.list[self.index].done():
            self.index += 1
            if self.done():
                return
            self.list[self.index].start()
        self.list[self.index].update()

    def done(self):
        self.running = self.index < len(self.list)
        return not self.running

    


class IAloop:

    def __init__(self, proxy, loop_action):

        self.proxy            = proxy
        self.loop_action      = loop_action
        self.running          = False

    def start(self):

        self.main_action.start()
        self.running = True

    def update(self):

        if self.done():
            return

        if self.loop_action.done():
            self.loop_action.start()

        else:
            self.loop_action.update()

    def done(self):
        return not self.running



class ParcourirDistance:

    def __init__(self, proxy, distance, dps):
        self.proxy    = proxy
        self.distance = distance
        self.dps      = dps
        self.running  = False

    def start(self):
        self.proxy.reset()
        self.running = True

    def update(self):
        if self.done(): 
            return
        self.proxy.avance_droit(self.dps)
        
    def done(self):
        distance_parcourue = self.proxy.dist_parcourue(self.proxy.lastposx,self.proxy.lastposy)
        self.running = distance_parcourue < self.distance
        return not (self.running)


class Arrete:
    def __init__(self, proxy):
        self.proxy   = proxy
        self.running = False

    def start(self):
        self.running = True

    def update(self):
        self.proxy.stop()
        if self.done(): return

    def done(self):
        self.running = False
        return not (self.running)


class TournerDroiteAngle:
    def __init__(self, proxy, angle, dps):
        self.proxy    = proxy
        self.angle    = angle
        self.dps      = dps
        self.running  = False

    def start(self):
        self.proxy.reset()
        self.running = True


    def update(self):
        if self.done():
            return
        self.proxy.tourne_droite(self.dps)

    def done(self):
        angle_parcouru = self.proxy.angle_parcouru_droit(self.proxy.lastdirr)
        #print("LAST DIRECTION = ",self.proxy.lastdirr)
        #print("angle parc = ",angle_parcouru)
        #print("DIRECTION = ",self.proxy.robot.dirr)
        self.running = angle_parcouru < self.angle
        return not (self.running) 
    

class TournerGaucheAngle:
    def __init__(self, proxy, angle, dps):
        self.proxy    = proxy
        self.angle    = angle
        self.dps      = dps
        self.running  = False

    def start(self):
        self.proxy.reset()
        self.running = True

    def update(self):
        if self.done():
            return
        self.proxy.tourne_gauche(self.dps)

    def done(self):
        angle_parcouru = self.proxy.angle_parcouru_gauche(self.proxy.lastdirr)
        self.running = angle_parcouru < self.angle
        return not (self.running)  
    











