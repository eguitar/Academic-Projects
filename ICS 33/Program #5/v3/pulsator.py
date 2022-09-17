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
        Simulton.__init__(self,x,y,20,20)
        self._counter = 30
        
    def update(self,model):
        preys = model.find(lambda x:isinstance(x,Prey))
        eaten = set([p for p in preys if self.contains(p.get_location())])
        print(eaten)
#         [model.remove(e) for e in eaten]
        return eaten