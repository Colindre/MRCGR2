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
            if not self.secondary_action.running:
                self.secondary_action.start()
            self.secondary_action.update()
        else:
            self.main_action.update()

    def done(self):
        return self.main_action.done() or self.secondary_action.done()

    

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
        return self.index >= len(self.list)

    


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
        return False



class ParcourirDistance:

    def __init__(self, proxy, distance, dps):

        self.proxy    = proxy
        self.distance = distance
        self.dps      = dps
        self.running  = False
        self.lastposx = self.proxy.robot.posx
        self.lastposy = self.proxy.robot.posy
        
    def start(self):
        self.running = True

    def update(self):
        if self.done(): 
            return None
        self.proxy.avance_droit(self.dps)
        
    def done(self):
        distance_parcourue = self.proxy.dist_parcourue(self.lastposx,self.lastposy)
        return distance_parcourue >= self.distance


class Arrete:
    def __init__(self, proxy):
        self.proxy   = proxy
        self.running = False

    def start(self):
        self.proxy.stop()
        self.running = True

    def update(self):
        if self.done(): return

    def done(self):
        return self.running

    



class TournerDroite:
    def __init__(self, proxy, angle, dps):
        self.proxy   = proxy
        self.angle   = angle
        self.dps     = dps
        self.running = False



    pass    #necessite angle_parcourue











