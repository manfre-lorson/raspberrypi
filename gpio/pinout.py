import pandas as pd

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


#plt.savefig(r'plt.png', dpi=300)




