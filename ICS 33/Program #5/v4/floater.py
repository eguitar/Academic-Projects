# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage 


# from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random


class Floater(Prey): 
    radius = 5
    
    def __init__(self,x,y):
        Prey.__init__(self,x,y,2*Floater.radius,2*Floater.radius,0,5)
        self.randomize_angle()
        
    def update(self,model):
        if random() <= 0.3:
            s = random() - 0.5
            if 3 <= self.get_speed() + s <= 7:
                self.set_speed(self.get_speed() + s)
            else:
                self.set_speed(self.get_speed() - s)
            a = random() - 0.5
            self.set_angle(self.get_angle() + a)
        self.move()
    
    def display(self,canvas):
        wh = self.get_dimension()
        canvas.create_oval(self._x-wh[1]/2,self._y-wh[0]/2,
                           self._x+wh[1]/2,self._y+wh[0]/2,fill='#FF0000')
