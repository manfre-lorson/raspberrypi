#!/usr/bin/python3

"""
Created on Wed Mar 25 16:26:10 2020

@author: manfre-lorson
@work: ansteuern einer diode 10 mal blinken

"""
##########################################################################
##########################################################################

def schaltplan():
    import sys
    sys.path.append(r'H:\git-projects\raspberry')
    
    import gpio_board as gb
    
    # plot board
    gb.plot_board()
    
    # plot connections and elements
    gb.con([gb.pp.j, -3, gb.pp.j, -35], 'b')
    gb.diode(gb.pp.g, -33)
    gb.resistor(gb.pp.h, -29, 'R1')
    gb.con([gb.pp.i, -29, gb.pp.i, gb.bcm('spice1')], 'y')
    
    # plot legende
    gb.diode(gb.pp.j + 4, -3)
    gb.anno(gb.pp.j + 4, -4, 'LED red' )
    gb.resistor(gb.pp.j + 4, -6, 'R1')
    gb.anno(gb.pp.j + 4, - 8, '120 Ohm')

# show schaltplan:
schaltplan()
##########################################################################
##########################################################################


import RPi.GPIO as gpio
import time


if __name__=="__main__":
    gpio.setmode(gpio.BOARD)
    gpio.setup(26, gpio.OUT)
    for i in range(10):
        gpio.output(26, gpio.HIGH)
        time.sleep(1)
        gpio.output(26, gpio.LOW)
        time.sleep(1)
    gpio.cleanup()
    