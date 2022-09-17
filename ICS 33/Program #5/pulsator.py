# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions 


from blackhole import Black_Hole


class Pulsator(Black_Hole): 
    radius = 10
    counter = 30
    
    def __init__(self,x,y):
        Black_Hole.__init__(self,x,y)
        self._count = 1
        
    def update(self,model):
        eaten = Black_Hole.update(self,model)
        if len(eaten) == 0:
            if self._count == Pulsator.counter:
                if self.get_dimension() == (1,1):
                    eaten.add(self)
                else:
                    x,y = self.get_dimension()
                    self.set_dimension(x-1,y-1)
                    self._count = 1            
            else:
                self._count += 1    
        else:
            x,y = self.get_dimension()
            self.set_dimension(x+len(eaten),y+len(eaten))
            self._count = 1
        return eaten