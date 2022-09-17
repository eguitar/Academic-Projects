# The Hunter class is derived from Pulsator and Mobile_Simulton (in that order).
#   It updates/displays like its Pulsator base, but also is mobile (moving in
#   a straight line or in pursuit of Prey), like its Mobile_Simultion base.


from simulton import Simulton
import model


class Special(Simulton):  
    
    
    def __init__(self,x,y):
        Pulsator.__init__(self,x,y)
        self.randomize_angle()
        self.set_speed(5)
    
    def update(self,model):
        pass
    
#         
#     def update(self,model):
#         preys = model.find(lambda x:isinstance(x,Prey))
#         
#         self.move()
#         self.wall_bounce()
# #         for p in preys if self.distance(p.get_location)
        
