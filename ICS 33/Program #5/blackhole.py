# The Black_Hole class is derived from Simulton; it updates by finding+removing
#   any class derived from Prey whose center is contained inside its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):  
    radius = 10
    
    def __init__(self,x,y):
        Simulton.__init__(self,x,y,2*Black_Hole.radius,2*Black_Hole.radius)
        
    def update(self,model):
        preys = model.find(lambda x:isinstance(x,Prey))
        return set([p for p in preys if self.contains(p.get_location())])
    
    def display(self,canvas):
        wh = self.get_dimension()
        canvas.create_oval(self._x-wh[1]/2,self._y-wh[0]/2,
                           self._x+wh[1]/2,self._y+wh[0]/2,fill='#000000')
            
    def contains(self,xy):
        if Simulton.distance(self,xy) <= self.get_dimension()[0]/2:
            return True
        else:
            return False

