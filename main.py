#UNIVERSIDAD DEL VALLE DE GUATEMALA
#SR4
#CARLOS CHEW - 17507

import sys
import random
from bm import Render

def cube():

    r = Render(800, 600)
    r.load('./modelos/cube.obj', (4, 3, 3), (100, 100, 100))
    r.display('output.bmp')

print(cube())
