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
        Prey.__init__(self,x,y,10,10,0,5)
        self.randomize_angle()
        
    def update(self,model):
        if random() <= 0.3:
            s = random() - 0.5
            a = random() - 0.5
            if 3 <= self.get_speed() + s <= 7 and \
               3 <= self.get_angle() + a <= 7:
                self.set_speed(self.get_speed() + s)
                self.set_angle(self.get_angle() + a)
                r = False
        self.move()
        self.wall_bounce()
    
    def display(self,canvas):
        canvas.create_oval(self._x-Floater.radius      , self._y-Floater.radius,
                                self._x+Floater.radius, self._y+Floater.radius,
                                fill='#FF0000')
        
