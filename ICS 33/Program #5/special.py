# The Hunter class is derived from Pulsator and Mobile_Simulton (in that order).
#   It updates/displays like its Pulsator base, but also is mobile (moving in
#   a straight line or in pursuit of Prey), like its Mobile_Simultion base.

# In comparison to Hunters which seeks Prey instances, objects of the Special class
# avoid all other simultons. By looking around them and finding the closest Simulton
# these objects will travel in the opposite direction that it "found" the other.

from prey import Prey
from simulton import Simulton
import model,math


class Special(Prey):  
    distance = 200
    
    def __init__(self,x,y):
        Prey.__init__(self,x,y,10,10,0,5)
        self.randomize_angle()
        
    def update(self,model):
        self.move()
        predator = model.find(lambda x:isinstance(x,Simulton))
        scary = model.find(lambda x:x != self and Prey.distance(x,self.get_location())<=Special.distance)
        scary = dict([(Prey.distance(s,self.get_location()),s) for s in scary])
        if scary != {}:
            dead = scary[min(scary)]
            angle = math.pi + math.atan2(dead.get_location()[1]-self.get_location()[1],dead.get_location()[0]-self.get_location()[0])
            self.set_angle(angle)
    
    def display(self,canvas):
        wh = self.get_dimension()
        canvas.create_oval(self._x-wh[1]/2,self._y-wh[0]/2,
                           self._x+wh[1]/2,self._y+wh[0]/2,fill='#00FF00')