#from activity import Brick,Cement,M_sand
Brick,Cement,M_sand=0,0,0
import math

def PCC(arg):
    global Cement,M_sand
    cement=math.ceil(66*arg/10)
    M_Sand=4.342857143*arg/10
    Cement+=cement
    M_sand+=M_Sand
    return cement,M_Sand


def RCC(arg):
    global Cement,M_sand
    cement=math.ceil(84*arg/10)
    M_Sand=4.145454545*arg/10
    Cement+=cement
    M_sand+=M_Sand

    return cement,M_Sand

def Brickwork(arg):
    global Brick,Cement,M_sand
    cement=math.ceil(14/10*arg)
    M_Sand=2.742857143/10*arg
    brick=math.ceil(5000/10*arg)
    Cement+=cement
    M_sand+=M_Sand
    Brick+=brick

    return cement,M_Sand,brick


def Plastering(arg):
    global Cement,M_sand
    cement=math.ceil(9/100*arg)
    M_Sand=1.714285714/100*arg
    Cement+=cement
    M_sand+=M_Sand

    return cement,M_Sand

def Tilesr(arg):
    global Cement,M_sand
    cement=math.ceil(3.390089723*arg/100)
    M_Sand=0.353075681*arg/100
    Cement+=cement
    M_sand+=M_Sand

    return cement,M_Sand



#print(f'Cement={Cement}\nM_Sand={M_sand}\nBrick={Brick}')

