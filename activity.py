a=int(input("Entering input return 1 or else 0: "))
if a==1:
    from inp import *
else:
    from input import *
from raqte import * 
import math

Brick,Cement,M_sand=0,0,0


def footing_PCC():
    global Cement,M_sand
    pcc=no_of_column*1.524*1.524*0.1016
    a=PCC(pcc)
    Cement+=a[0]
    M_sand+=a[1]
    return a

def footing_RCC():
    global Cement,M_sand
    rcc_base=no_of_column*1.524*1.524*0.1524
    rcc_slope=no_of_column*0.3063170282
    a=RCC(rcc_base+rcc_slope)
    Cement+=a[0]
    M_sand+=a[1]
    return a

def Basement_Column_Concrete():
    global Cement,M_sand
    rcc=no_of_column*0.3048*0.2286*2.489302
    a=RCC(rcc)
    Cement+=a[0]
    M_sand+=a[1]
    #return f'Cement={a[0]}\nM-Sand={a[1]}'
    return a

def Grade_Beam_PCC():
    global Cement,M_sand
    pcc=((c1+c2)-((t1+t2)*0.381/2))*0.381*0.1016
    a=PCC(pcc)
    Cement+=a[0]
    M_sand+=a[1]
    #return f'Cement={a[0]}\nM-Sand={a[1]}'
    return a

def Grade_Beam_RCC():
    global Cement,M_sand
    rcc=((c1+c2)-((t1+t2)*0.381/2))*0.381*0.2286
    a=RCC(rcc)
    Cement+=a[0]
    M_sand+=a[1]
    #return f'Cement={a[0]}\nM-Sand={a[1]}'
    return a

def Basement_BrickWork():
    global Brick,Cement,M_sand
    nineinch=((c1)-(t1*0.2286/2))*0.2286*0.6069
    fourfiveinch=((c2)-(t2*0.1143/2))*0.1143*0.6069
    column=columnwithoutt*0.3*.23*.6096
    a=Brickwork(nineinch+fourfiveinch-column)
    Cement+=a[0]
    M_sand+=a[1]
    Brick+=a[2]
    #return f'Cement={a[0]}\nM-Sand={a[1]}\nBrick={a[2]}'
    return a

def Basement_Belt_Beam_RCC():
    global Cement,M_sand
    rcc=((c1+c2)-((t1+t2)*0.381/2))*0.2286*0.2286
    a=RCC(rcc)
    Cement+=a[0]
    M_sand+=a[1]
    #return f'Cement={a[0]}\nM-Sand={a[1]}'
    return a

def Basement_floor_PCC_work():
    global Cement,M_sand
    r1 = 0
    for i in range(0, len(dimensions), 2):
        r1 += (dimensions[i]*dimensions[i+1])*0.1016
    a=PCC(r1)
    Cement+=a[0]
    M_sand+=a[1]
    #return f'Cement={a[0]}\nM-Sand={a[1]}'
    return a

def Ground_Floor_Column_Concrete():
    global Cement,M_sand
    rcc=no_of_column*0.3048*0.2286*3.3528
    a=RCC(rcc)
    Cement+=a[0]
    M_sand+=a[1]
    #return f'Cement={a[0]}\nM-Sand={a[1]}'
    return a

def Ground_Floor_Lintel_Level_BrickWork():
    global Brick,Cement,M_sand
    nineinch=((c1)-(t1*0.2286/2))*0.2286*2.1336
    fourfiveinch=((c2)-(t2*0.1143/2))*0.1143*2.1336
    column=columnwithoutt*0.3*.23*2.1336
    d1=door[0]*door[1]*.2286
    d2=doo*doors[0]*doors[1]*.2286
    w=windows*window[0]*window[1]*.2286
    v=noven*ventilator[0]*ventilator[1]*.2286
    a=Brickwork(nineinch+fourfiveinch-column-d1-d2-w-v)
    Cement+=a[0]
    M_sand+=a[1]
    Brick+=a[2]
    #return f'Cement={a[0]}\nM-Sand={a[1]}\nBrick={a[2]}'
    return a

def Ground_Floor_lintel_Concrete():
    global Cement,M_sand
    nineinch=((c1)-(t1*0.2286/2))*0.2286*0.1524
    fourfiveinch=((c2)-(t2*0.1143/2))*0.1143*0.1524
    w=windows*1.8*0.075
    v=noven*1.2*.075
    column=columnwithoutt*0.3*.23*0.1524
    a=RCC(nineinch+fourfiveinch-column+w+v)
    Cement+=a[0]
    M_sand+=a[1]
    #return f'Cement={a[0]}\nM-Sand={a[1]}'
    return a


def Ground_Floor_Brickwork_Above_lintel():
    global Brick,Cement,M_sand
    nineinch=((c1)-(t1*0.2286/2))*0.2286*0.9144
    fourfiveinch=((c2)-(t2*0.1143/2))*0.1143*0.9144
    column=columnwithoutt*0.3*.23*0.9144
    a=Brickwork(nineinch+fourfiveinch-column)
    Cement+=a[0]
    M_sand+=a[1]
    Brick+=a[2]
    #return f'Cement={a[0]}\nM-Sand={a[1]}\nBrick={a[2]}'
    return a

def Ground_Floor_Roof_Slab_Concrete():
    global Cement,M_sand
    rcc=area[0]*area[1]*0.1524
    column=13*0.3*0.23*.1524
    a=RCC(rcc-column)
    Cement+=a[0]
    M_sand+=a[1]
    #return f'Cement={a[0]}\nM-Sand={a[1]}'
    return a

def First_Floor_Column_Concrete():
    global Cement,M_sand
    rcc=(no_of_column-4)*0.3048*0.2286*3.3528
    rccparapet=4*0.3048*0.2286*4.1148
    a=RCC(rcc+rccparapet)
    Cement+=a[0]
    M_sand+=a[1]
    #return f'Cement={a[0]}\nM-Sand={a[1]}'
    return a


def First_Lintel_Level_Brickwork():
    global Brick,Cement,M_sand
    nineinch=((c11)-(t11*0.2286/2))*0.2286*2.1336
    fourfiveinch=((c12)-(t12*0.1143/2))*0.1143*2.1336
    column=columnwithoutt1*0.3*.23*2.1336
    d2=doo1*doors[0]*doors[1]*.2286
    w=windows1*window[0]*window[1]*.2286
    v=noven1*ventilator[0]*ventilator[1]*.2286
    a=Brickwork(nineinch+fourfiveinch-column-d2-w-v)
    Cement+=a[0]
    M_sand+=a[1]
    Brick+=a[2]
    #return f'Cement={a[0]}\nM-Sand={a[1]}\nBrick={a[2]}'
    return a

def First_Floor_Lintel_Concrete():
    global Cement,M_sand
    nineinch=((c11)-(t11*0.2286/2))*0.2286*0.1524
    fourfiveinch=((c12)-(t12*0.1143/2))*0.1143*0.1524
    w=windows1*1.8*0.075
    v=noven1*1.2*.075
    column=columnwithoutt1*0.3*.23*0.1524
    a=RCC(nineinch+fourfiveinch-column+w+v)
    Cement+=a[0]
    M_sand+=a[1]
    #return f'Cement={a[0]}\nM-Sand={a[1]}'
    return a


def First_Floor_Brickwork_Above_Lintel():
    global Brick,Cement,M_sand
    nineinch=((c11)-(t11*0.2286/2))*0.2286*0.9144
    fourfiveinch=((c12)-(t12*0.1143/2))*0.1143*0.9144
    column=columnwithoutt1*0.3*.23*0.9144
    a=Brickwork(nineinch+fourfiveinch-column)
    Cement+=a[0]
    M_sand+=a[1]
    Brick+=a[2]
    #return f'Cement={a[0]}\nM-Sand={a[1]}\nBrick={a[2]}'
    return a

def First_Floor_Roof_Slab_Concrete():
    global Cement,M_sand
    rcc=area[0]*area[1]*0.1524
    column=no_of_column*0.3*0.23*0.1524
    a=RCC(rcc-column)
    Cement+=a[0]
    M_sand+=a[1]
    #return f'Cement={a[0]}\nM-Sand={a[1]}'
    return a


def Parapet_BrickWork():
    global Brick,Cement,M_sand
    brick=(area[0]-0.23+area[1]-0.23)*2*0.2286*0.762
    column=4*.3*.23*0.762
    a=Brickwork(brick-column)
    Cement+=a[0]
    M_sand+=a[1]
    Brick+=a[2]
    #return f'Cement={a[0]}\nM-Sand={a[1]}\nBrick={a[2]}'
    return a

def External_Plastering():
    global Cement,M_sand
    plastering=(area[0]+area[1])*2*8.6868
    top=(area[0]+area[1]-0.23)*2*0.23
    inner=(area[0]-0.23+area[1]-0.23)*2*0.762
    a=Plastering(plastering+top+inner)
    Cement+=a[0]
    M_sand+=a[1]
    #return f'Cement={a[0]}\nM-Sand={a[1]}'
    return a

def Interior_Plastering():
    global Cement,M_sand
    r1 = 0
    for i in range(0, len(dimensions), 2):
        r1 += ((dimensions[i]+dimensions[i+1])*2)*3.048
    d1=door[0]*door[1]
    d2=doo*doors[0]*doors[1]
    w=windows*window[0]*window[1]
    v=noven*ventilator[0]*ventilator[1]
    r2 = 0
    for i in range(0, len(dimensions1), 2):
        r2 += ((dimensions1[i]+dimensions1[i+1])*2)*3.048
    d12=doo1*doors[0]*doors[1]
    w1=windows1*window[0]*window[1]
    v1=noven1*ventilator[0]*ventilator[1]
    a=Plastering(r1+r2-d1-d2-w-v-d12-w1-v1)
    Cement+=a[0]
    M_sand+=a[1]
    #return f'Cement={a[0]}\nM-Sand={a[1]}'
    return a
def Tiles():
    global Cement,M_sand
    r1 = 0
    for i in range(0, len(dimensions), 2):
        r1 += (dimensions[i]*dimensions[i+1])
    r2 = 0
    for i in range(0, len(dimensions1), 2):
        r2 += (dimensions1[i]*dimensions1[i+1])
    aa=(r1+r2)*10.7639
    a=Tilesr(aa)
    Cement+=a[0]
    M_sand+=a[1]
    return a



# print(footing_PCC())
# print(footing_RCC())
# print(Basement_Column_Concrete())
# print(Grade_Beam_PCC())
# print(Grade_Beam_RCC())
#print(Basement_BrickWork())
# print(Basement_Belt_Beam_RCC())
# print(Basement_floor_PCC_work())
# print(Ground_Floor_Column_Concrete())
#print(Ground_Floor_Lintel_Level_BrickWork())
# print(Ground_Floor_lintel_Concrete())
#print(Ground_Floor_Brickwork_Above_lintel())
# print(Ground_Floor_Roof_Slab_Concrete())
# print(First_Floor_Column_Concrete())
#print(First_Lintel_Level_Brickwork())
# print(First_Floor_Lintel_Concrete())
#print(First_Floor_Brickwork_Above_Lintel())
# print(First_Floor_Roof_Slab_Concrete())
#print(Parapet_BrickWork())
# print(External_Plastering())
# print(Interior_Plastering())
# print(Tiles())





act={
    'footingPCC':footing_PCC(),
    'footingRCC':footing_RCC(),
    'Basement_Column_Concrete':Basement_Column_Concrete(),
    'Grade_Beam_PCC':Grade_Beam_PCC(),
    'Grade_Beam_RCC':Grade_Beam_RCC(),
    'Basement_BrickWork':Basement_BrickWork(),
    'Basement_Belt_Beam_RCC':Basement_Belt_Beam_RCC(),
    'Basement_floor_PCC_work':Basement_floor_PCC_work(),
    'Ground_Floor_Column_Concrete':Ground_Floor_Column_Concrete(),
    'Ground_Floor_Lintel_Level_BrickWork':Ground_Floor_Lintel_Level_BrickWork(),
    'Ground_Floor_lintel_Concrete':Ground_Floor_lintel_Concrete(),
    'Ground_Floor_Brickwork_Above_lintel':Ground_Floor_Brickwork_Above_lintel(),
    'Ground_Floor_Roof_Slab_Concrete':Ground_Floor_Roof_Slab_Concrete(),
    'First_Floor_Column_Concrete':First_Floor_Column_Concrete(),
    'First_Lintel_Level_Brickwork':First_Lintel_Level_Brickwork(),
    'First_Floor_Lintel_Concrete':First_Floor_Lintel_Concrete(),
    'First_Floor_Brickwork_Above_Lintel':First_Floor_Brickwork_Above_Lintel(),
    'First_Floor_Roof_Slab_Concrete':First_Floor_Roof_Slab_Concrete(),
    'Parapet_BrickWork':Parapet_BrickWork(),
    'External_Plastering':External_Plastering(),
    'Interior_Plastering':Interior_Plastering(),
    'Tiles':Tiles(),
}


M_sand=float("{:.3f}".format(M_sand/2.83))
#print(f"\nCement:{Cement} No's\nSand: {M_sand*2.83} m³ ({math.ceil(M_sand)} units)\nBrick: {Brick} No's\n")

cost=(Cement*430)+(Brick*10)+(M_sand*4750)
#print(f'Cost of Cement: ₹ {Cement*430}\nCost of Brick: ₹ {Brick*10}\nCost of M-Sand: ₹ {M_sand*4750}\nTotal Cost of Materials: ₹ {cost}\n')





