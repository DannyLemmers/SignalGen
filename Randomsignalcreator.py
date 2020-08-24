# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 09:54:39 2020

@author: Danny
"""
import numpy as np
import matplotlib.pyplot as plt


scaler=[]
bounds=[]
maxvalx = np.random.randint(10,25) 
dividor = np.random.randint(2,5)
for i in range(dividor):
    adder = np.random.randint(1,10)
    scaler.append(adder)
randconval= round(np.random.randint(1,250),-1)

dt=1
startx=0

def scaleval(step, scaler = scaler):
    length = len(bounds)
    for i in range(length):
        if bounds[i] > step:
            scale=scaler[i-1]
            #print(bounds[i], step, scale)
            return scale
    
def stepscalc(step,time, y):
    scale=scaleval(step)
    newval = y+scale
    return newval

def stepper(dt):
    steps = int(maxvalx-startx/dt)
    yval = np.zeros(steps+1)
    yval[0]=0+randconval
    for i in range(steps):
        time = i*dt
        yval[i+1]=stepscalc(i, time, yval[i])
    return yval

def boundaries(maxvalx, dividor):
    for i in range(dividor):
        bounds.append(np.round(i*maxvalx/dividor))
    bounds.append(maxvalx)
    return

boundaries(maxvalx, dividor)
yval=stepper(dt)

x = np.linspace(startx,maxvalx,int((maxvalx-startx/dt)+1))
plt.close('all')
plt.figure()
plt.plot(x,yval,label='$y$',marker='o',linestyle='-')
plt.xlabel('$x$')
plt.ylabel('$y(t)$')
plt.title('Signal Simulation')
plt.legend()