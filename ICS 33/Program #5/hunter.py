# The Hunter class is derived from Pulsator and Mobile_Simulton (in that order).
#   It updates/displays like its Pulsator base, but also is mobile (moving in
#   a straight line or in pursuit of Prey), like its Mobile_Simultion base.


from prey  import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2


class Hunter(Pulsator, Mobile_Simulton):  
    distance = 200
    
    def __init__(self,x,y):
        Pulsator.__init__(self,x,y)
        Mobile_Simulton.__init__(self,x,y,*self.get_dimension(),0,5)
        Mobile_Simulton.randomize_angle(self)
    
    def update(self,model):
        Mobile_Simulton.move(self)
        eaten = Pulsator.update(self,model)
        preys = model.find(lambda x:isinstance(x,Prey) and Prey.distance(x,self.get_location())<=Hunter.distance)
        preys = dict([(Prey.distance(p,self.get_location()),p) for p in preys])
        if preys != {}:
            food = preys[min(preys)]
            angle = atan2(food.get_location()[1]-self.get_location()[1],food.get_location()[0]-self.get_location()[0])
            Mobile_Simulton.set_angle(self,angle)
        return eaten