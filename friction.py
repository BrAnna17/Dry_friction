import numpy as np
import matplotlib.pyplot as plt
from math import *
from scipy.integrate import odeint
k=10000
a=1.2
w=1
n=6
t = np.linspace(0,6*pi,10000)
def f(v,t):
    return -(2/pi)*atan(1000*v)+a*cos(w*t)
v = odeint(f,0,t)
plt.plot(t,v,lw=2)
plt.xlabel('t')
plt.ylabel('v')
plt.xlim(0,n*pi)
plt.grid()
plt.savefig('example9.png', fmt="png")