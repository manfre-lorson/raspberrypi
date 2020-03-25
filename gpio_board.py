# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 09:23:52 2020

@author: fw56moba
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


#general settings
def plot_board():
    xlim = 26
    ylim = -64
    plt.ylim(ylim,1) # limits of the plot
    plt.xlim(0, xlim) # limits of the plot
    plt.gca().set_aspect('equal', adjustable='box') # make scale x,y steps equal
    plt.gcf().set_size_inches(11.5, 15.5)
    
    #bread board
    y_dim = [1,ylim]
    x_dim = [1,20]
    
    for x in np.arange(x_dim[0]-.5, x_dim[1]-.5, 1):
        if x>8 and x<11:
            pass
        else:
            plt.plot([x,x],[y_dim[0]-.5-1,y_dim[1]-1-.5],  color='g',lw=.3 )
    
    for y in np.arange(y_dim[0]-.5-1, y_dim[1]-.5, -1):
        plt.plot([x_dim[0]-.5, x_dim[0]+7-.5],[y,y], color='r',lw=.3)
        plt.plot([x_dim[0] +7+ 4-.5, x_dim[1]-1-.5],[y,y], color='r',lw=.3)
    
    # label board positions
    for a in psd:
        lable_x(a)
    
    # lable gpio pins
    for ix in df.index:
        ds = df.iloc[ix]
        #print(ds.bcm, (ds.x, ds.y), ds.x+.5, ds.y -.25)
        if ds.board%2==0:
            x_off = -4
        else:
            x_off = 0
        plt.annotate(ds.bcm, (ds.x, ds.y), xytext=(ds.x+.5 + x_off, ds.y -.25))
        plt.plot(ds.x, ds.y, 'o', color='b' )
    
    con([pp.c-.5 ,-.5,
         pp.c-.5 , -20.5,
         pp.h -5, -20.5, 
        ])
    con([pp.c-.5,-.5,pp.c-.5, -20.5, pp.h -.5, -20.5, pp.h -.5, -.5])
    
def con(vals,color ='black'):
    x = vals[::2]
    y = vals[1::2]
    plt.plot(x, y, color = color, lw=2)
    

def lable_x(key):
    y_pos = -.5
    x_pos = psd[key] 
    if len(key)==1:
        value = key
    elif key.startswith('p'):
        value = '+'
    else:
        value = '-'        
    plt.annotate(value, (x_pos, y_pos), xytext=(x_pos -.3, 0))

def bcm(y):
    return df.loc[df['bcm'] == y.upper()]['y'].values[0]
 
# definitions
psd = {'p1':1, # plus pol 1
                'm1':2, # minus pol 1
                'a':3, # position a
                'b':4,
                'c':5,
                'd':6,
                'e':7,
                'f':8+4,
                'g':9+4,
                'h':10+4,
                'i':11+4,
                'j':12+4,
                'p2':13+4,
                'm2':14+4}

pp = pd.Series(psd) # pin x-position by name 

pin_bcm = '3V3 5V0 SDA1 5V0 SCL1 gnd gpio4 txdo gnd rxdo gpio17\
 gpio18 gpio27 gnd gpio22 gpio23 3v3 gpio24 spmosi gnd spmiso\
 gpio25 spisclk spiceo gnd spice1 id_sd id_sc gpio5 gnd gpio6\
 gpio12 gpio13 gnd gpio9 gpio16 gpio26 gpio20 gnd gpio21'.upper().split(' ')
pin_board = list(range(1,len(pin_bcm)+1))

pin_pos_x = [psd['c'], psd['g']] * (len(pin_board)//2)
pin_pos_y = []
y_pos = list(range(-1,-1*(len(pin_board)//2)-1, -1))
for x in list(zip(y_pos, y_pos)):
    pin_pos_y.extend(x)
    
 
 
df = pd.DataFrame(list(zip(pin_board, pin_bcm, pin_pos_x, pin_pos_y)),
                  columns = ['board', 'bcm', 'x', 'y'])

def diode(x,y):
    con([x, y, x, y-2], color='gray')
    plt.plot(x-.05, y -.9 , 'v' , color='red', ms=15)
    con([x-.5, y -1.5 , x + .5 , y -1.5])
    

def resistor(x,y,anno):
    ''' x and y are start coorinates'''
    con ([x, y, x, y - 4], color='gray')
    plt.plot(x, y - 1.4, 's', color = 'b', ms=15)
    plt.plot(x, y - 2.4, 's', color = 'b', ms=15)
    plt.annotate(anno, (pp.h, y - 1.5), xytext=(x-.4, y-1.7 ), color='w')

def anno(x,y, text):
    plt.annotate(text, (x,y), xytext=(x+1.5, y))

plot_board()
diode(pp.h, -30)


#plt.savefig(r'D:\florian_wolf\tmp\plt.png', dpi=300)




