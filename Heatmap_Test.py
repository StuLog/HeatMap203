import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import LinearNDInterpolator
from PIL import Image
def build_map():
    #math to create the map. sampeled from scipy documentation. Link: https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.LinearNDInterpolator.html
     X = np.linspace(min(x), max(x))
     Y = np.linspace(min(y), max(y))
     X, Y = np.meshgrid(X, Y)  # 2D grid for interpolation
     interp = LinearNDInterpolator(list(zip(x, y)), z)
     Z = interp(X, Y)


     #Printing the map
     plt.pcolormesh(X, Y, Z, shading='auto')
     plt.colorbar()
     plt.axis("equal")
     plt.savefig('heat.png')


x = [1,2,3,5,6,7,8,9,10,2,3,4,2,5,6,7,4,8,6,9,1]
y = [7,3,10,6,4,5,6,3,2,8,9,5,10,2,6,4,8,7,3,0,1]
#Co2 value at each coord 
z = [420,430,470,450,420,430,470,450,420,430,470,450,420,430,470,450,420,430,470,450,410]
build_map()