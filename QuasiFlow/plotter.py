import matplotlib.pyplot as plt
import numpy as np
import math 



"""
Initialize plot with 2d nozzle specifications

"""
def divergingradius(rt,re,length, z):
    return rt-(re-rt)*(z/length)**2


def iteratedata(rt,re,length,n):
    lst = []
    zloc = np.linspace(0,length,n,endpoint=True)
    for zpoints in np.linspace(0, length, n, endpoint = True):
        lst.append(divergingradius(rt,re,length,zpoints))
    
    return lst,zloc

def getarearatio(rt,re,length,n):
    radius_list, zloc = iteratedata(rt, re, length, n)
    
    # Compute area at each point
    area_list = [math.pi * r**2 for r in radius_list]
    
    # Throat area (minimum area)
    throat_area = min(area_list)
    
    # Compute area ratio A/A*
    area_ratios = [A / throat_area for A in area_list]
    
    return area_ratios, zloc


def area_mach_relation(M, area_ratio, gamma=1.4):
    """Area-Mach equation residual."""
    return (1/M) * ((2/(gamma+1))*(1 + (gamma-1)/2 * M**2))**((gamma+1)/(2*(gamma-1))) - area_ratio

def plotter(rt,re,length,n):
    _,zloc = iteratedata(rt,re,length,n)
    lst,_ = iteratedata(rt,re,length,n)
    plt.plot(lst,zloc, color = 'blue')
    plt.plot(lst,-1*zloc, color = 'blue')
    plt.title("Diverging Nozzle Section")
    plt.show()

###  TO DO:
"""
We have nozzle envelope and area ratio. next steps are to numerically
solve area mach rlation for mach to get mach number at area ratio, and then
use the mach number we get to solve for pressure at given x value
"""

plotter(5,1,2,50)