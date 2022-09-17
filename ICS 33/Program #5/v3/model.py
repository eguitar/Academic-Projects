import controller
import model   # See how update_all should pass on a reference to this module

# Use the reference to this module to pass it to update methods

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running     = False
cycle_count = 0
simultons   = set()
obj         = ''
names = ('Ball','Floater','Black_Hole','Pulsator','Hunter')

#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running,cycle_count,simultons
    running     = False
    cycle_count = 0
    simultons   = set()


#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#step just one update in the simulation
def step ():
    start()
    update_all()
    stop()


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global obj
    obj = kind


#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    if any([s.contains((x,y)) for s in simultons]):
        s_tuple = tuple(simultons)
        for s in s_tuple:
            if s.contains((x,y)):
                remove(s)
    elif obj in names:
        add(eval(obj + f'({x},{y})'))


#add simulton s to the simulation
def add(s):
    simultons.add(s)    

# remove simulton s from the simulation    
def remove(s):
    simultons.remove(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    s_set = set()
    for s in simultons:
        if p(s):
            s_set.add(s)
    return s_set


#call update for each simulton in this simulation (pass model as an argument) 
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def update_all():
    global cycle_count
    if running:
        cycle_count += 1
        s_set = set(simultons)
        for s in s_set:
            index = s.update(model)
            if index != None:
                for i in index:
                    remove(i)

#For animation: (1st) delete all simultons on the canvas; (2nd) call display on
#  all simulton being simulated, adding each back to the canvas, maybe in a
#  new location; (3rd) update the label defined in the controller for progress 
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
        
    for s in simultons:
        s.display(controller.the_canvas)

    controller.the_progress.config(text=str(cycle_count)+" updates/"+str(len(simultons))+" simultons")