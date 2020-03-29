#!/usr/bin/python3

"""
Created on Wed Mar 25 16:26:10 2020

@author: manfre-lorson
@work: ansteuern einer diode 10 mal blinken

"""
##########################################################################
##########################################################################

def schaltplan(save=False):
    import sys
    sys.path.append('~/git-projects/raspberrypi/')
    
    import gpio_board as gb
    
    # plot board
    gb.plot_board()
    
    # plot connections and elements
    gb.con([gb.pp.j, -3, gb.pp.m2, -3], 'b')
    gb.con([gb.pp.j, -35, gb.pp.m2, -35], 'b')
    gb.diode(gb.pp.g, -33)
    gb.resistor(gb.pp.h, -29, 'R1')
    gb.con([gb.pp.i, -29, gb.pp.i, gb.bcm('spice1')], 'y')
    
    gb.con([gb.pp.j, gb.bcm('gpio23'), gb.pp.j, -40], 'g')
    gb.resistor(gb.pp.h, -40, 'R2')
    gb.diode(gb.pp.g, -44, 'green')
    gb.con([gb.pp.j, -46, gb.pp.m2, -46], 'b')
    # plot legende
    gb.diode(gb.pp.j + 4, -3)
    gb.anno(gb.pp.j + 4, -4, 'LED red' )
    gb.resistor(gb.pp.j + 4, -6, 'R1')
    gb.anno(gb.pp.j + 4, - 8, '120 Ohm')
    
    if save:
        gb.plt.savefig(save, dpi=300)
# show schaltplan:
schaltplan(save= r'C:\tmp\test.png')
