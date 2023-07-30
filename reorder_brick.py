from activity import *
import random
from schdule import ac
from datetime import date as d,timedelta
#from qwe import leadtime_brick

global storage_brick
safety_stock=25
def dateq(st):
    if st[0]=='No':
        return 'No Order'
    elif len(st)==1:
        return (f'{st[0].year}-{st[0].month}-{st[0].day}')
    elif len(st)==2:
        return (f'{st[0].year}-{st[0].month}-{st[0].day},{st[1].year}-{st[1].month}-{st[1].day}')
    elif len(st)==3:
        return (f'{st[0].year}-{st[0].month}-{st[0].day},{st[1].year}-{st[1].month}-{st[1].day},{st[2].year}-{st[2].month}-{st[2].day}')
    

leadtime_brick=int(input("Brick's leadtime: "))
def order_brick(a,strage_rick,st):     
    global leadtime_brick
    b=a
    order=1
    while a>4000:
        order+=1
        a=a-4000
    storag_brick=0     
    
    if strage_rick>3000:
        order-=1
    storag_brick=strage_rick+(order*4000)-b     
    
    orderdate=[]
    if order==3:
        orderdate.append(st-timedelta(days=leadtime_brick+1))
        orderdate.append(st-timedelta(days=1))
        orderdate.append(st+timedelta(days=leadtime_brick+1))
    elif order==2:
        orderdate.append(st-timedelta(days=leadtime_brick+1))
        orderdate.append(st-timedelta(days=1))
    elif order==1:
        orderdate.append(st-timedelta(days=leadtime_brick+1))
    elif order==0:
        orderdate.append("No")
    if storag_brick<6000 and storag_brick>=500: 
        return storag_brick,orderdate,b
    
            
            

        
# print("Brick's OrderDates\n")
# storage_brick=0
# storage_brick=order_brick(act['Basement_BrickWork'][2],storage_brick,ac['Basement_BrickWork'][1])
# print(f"Name of the Activity: Basement_BrickWork\nUsage: {storage_brick[2]}\nstorage:{storage_brick[0]}\nOrderDates: {dateq(storage_brick[1])}\n")

# storage_brick=order_brick(act['Ground_Floor_Lintel_Level_BrickWork'][2],storage_brick[0],ac['Ground_Floor_Lintel_Level_BrickWork'][1])
# print(f"Name of the Activity: Ground_Floor_Lintel_Level_BrickWork\nUsage: {storage_brick[2]}\nstorage:{storage_brick[0]}\nOrderDates: {dateq(storage_brick[1])}\n")

# storage_brick=order_brick(act['Ground_Floor_Brickwork_Above_lintel'][2],storage_brick[0],ac['Ground_Floor_Brickwork_Above_lintel'][1])
# print(storage_brick)
# print(f"Name of the Activity: Ground_Floor_Brickwork_Above_lintel\nUsage: {storage_brick[2]}\nstorage:{storage_brick[0]}\nOrderDates: {dateq(storage_brick[1])}\n")


# storage_brick=order_brick(act['First_Lintel_Level_Brickwork'][2],storage_brick[0],ac['First_Lintel_Level_Brickwork'][1])
# print(f"Name of the Activity: First_Lintel_Level_Brickwork\nUsage: {storage_brick[2]}\nstorage:{storage_brick[0]}\nOrderDates: {dateq(storage_brick[1])}\n")

# storage_brick=order_brick(act['First_Floor_Brickwork_Above_Lintel'][2],storage_brick[0],ac['First_Floor_Brickwork_Above_Lintel'][1])
# print(f"Name of the Activity: First_Floor_Brickwork_Above_Lintel\nUsage: {storage_brick[2]}\nstorage:{storage_brick[0]}\nOrderDates: {dateq(storage_brick[1])}\n")

# storage_brick=order_brick(act['Parapet_BrickWork'][2],storage_brick[0],ac['Parapet_BrickWork'][1])
# print(f"Name of the Activity: Parapet_BrickWork\nUsage: {storage_brick[2]}\nstorage:{storage_brick[0]}\nOrderDates: {dateq(storage_brick[1])}\n")

# print(f"cement:{order(act['Ground_Floor_Lintel_Level_BrickWork'][0],storage)}")
# storage=50-act['footingPCC'][0]
# print(f"cement:{order(act['Ground_Floor_lintel_Concrete'][0],storage)}")
# storage=50-act['footingPCC'][0]
# print(f"cement:{order(act['Ground_Floor_Brickwork_Above_lintel'][0],storage)}")
# storage=50-act['footingPCC'][0]
# print(f"cement1:{order(act['Ground_Floor_Roof_Slab_Concrete'][0],storage)}")
# storage=50-act['footingPCC'][0]
# print(f"cement:{order(act['First_Floor_Column_Concrete'][0],storage)}")
# storage=50-act['footingPCC'][0]
# print(f"cement:{order(act['First_Lintel_Level_Brickwork'][0],storage)}")
# storage=50-act['footingPCC'][0]
# print(f"cement:{order(act['First_Floor_Lintel_Concrete'][0],storage)}")
# storage=50-act['footingPCC'][0]
# print(f"cement:{order(act['First_Floor_Brickwork_Above_Lintel'][0],storage)}")
# storage=50-act['footingPCC'][0]
# print(f"cement1:{order(act['First_Floor_Roof_Slab_Concrete'][0],storage)}")
# storage=50-act['footingPCC'][0]
# print(f"cement:{order(act['Parapet_BrickWork'][0],storage)}")
# storage=50-act['footingPCC'][0]
# print(f"cement:{order(act['External_Plastering'][0],storage)}")
# storage=50-act['footingPCC'][0]
# print(f"cement:{order(act['Interior_Plastering'][0],storage)}")
# storage=50-act['footingPCC'][0]
#print(f"cement:{order(act['First_Floor_Brickwork_Above_Lintel'][0])}")

#print(f"cement:{order(act['Ground_Floor_Roof_Slab_Concrete'][0])}")
#print(f"cement:{order(act['First_Floor_Roof_Slab_Concrete'][0])}")
# print(f"cement:{order(act['Parapet_BrickWork'][0])}") 
    
# -17
# -59
# -96
# -128
# -155
# -177
# -194
# -206
# -213
# -215
# -212
# -204
# -191
# -173
# -150
# -122