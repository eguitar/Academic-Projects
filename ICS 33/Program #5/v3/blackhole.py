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
        Simulton.__init__(self,x,y,20,20)
        
    def update(self,model):
        preys = model.find(lambda x:isinstance(x,Prey))
        eaten = set([p for p in preys if self.contains(p.get_location())])
        print(eaten)
#         [model.remove(e) for e in eaten]
        return eaten
    
    def display(self,canvas):
        canvas.create_oval(self._x-Black_Hole.radius      , self._y-Black_Hole.radius,
                                self._x+Black_Hole.radius, self._y+Black_Hole.radius,
                                fill='#000000')
        
    def contains(self,xy):
        if self.distance(xy) <= Black_Hole.radius:
            return True
        else:
            return False
