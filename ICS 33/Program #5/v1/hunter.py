# The Hunter class is derived from Pulsator and Mobile_Simulton (in that order).
#   It updates/displays like its Pulsator base, but also is mobile (moving in
#   a straight line or in pursuit of Prey), like its Mobile_Simultion base.


from prey  import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2


class Hunter(Pulsator, Mobile_Simulton):  
    pass
