import matplotlib.pyplot as plt
import numpy as np
import math 




def convergingradius(rc,rt,length, z):
    return rc-(rc-rt)*(z/length)**2



def iteratedata(rc,rt,length,n):
    lst = []
    zloc = np.linspace(0,length,n,endpoint=True)
    for zpoints in np.linspace(0, length, n, endpoint = True):
        lst.append(convergingradius(rc,rt,length,zpoints))
    
    return lst,zloc


def mirroredpair(rc,rt,length,n):
   for x in iteratedata(rc,rt,length,n)[0]:
       

   return a

def plotter(rc,rt,length,n):
    _,zloc = iteratedata(rc,rt,length,n)
    lst,_ = iteratedata(rc,rt,length,n)
    c = mirroredpair(rc,rt,length,n)
    plt.plot(zloc,lst)
    plt.plot(zloc,c)
    plt.show()


plotter(5,1,2,50)