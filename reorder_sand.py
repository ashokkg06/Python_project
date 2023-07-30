from activity import *
import random
from schdule import ac
from datetime import date as d,timedelta
#from qwe import leadtime

# global storage

leadtime=int(input("Sand's leadtime: "))
def order_sand(a,strage,da):
    storag=0
    global leadtime
    order_place=11.32
    a=float("{:.3f}".format(a))
    if strage<a+1:
        storag=strage+order_place-a
        qw=da-timedelta(days=leadtime)
        storag=float("{:.3f}".format(storag))
        print(type(qw),type(da))
        return storag,order_place,qw,a
    storag=strage-a
    storag=float("{:.3f}".format(storag))
   
    qw='No Order'
    return storag,order_place,qw,a

# storage_sand=11.32-act['footingPCC'][1]
# storage_sand=order_sand(act['footingPCC'][1],0,ac['footingPCC'][1])
# print(f"Name of the Activity: FootingPCC\nUsage:{storage_sand[3]}\nstorage:{storage_sand[0]}\nDate:{storage_sand[2]}\n")
# storage_sand=order_sand(act['footingRCC'][1],storage_sand[0],ac['footingRCC'][1])
# print(f"Name of the Activity: FootingRCC\nUsage:{storage_sand[3]}\nstorage:{storage_sand[0]}\nDate:{date(storage_sand[2])}\n")
# storage_sand=order_sand(act['Basement_Column_Concrete'][1],storage_sand[0],ac['Basement_Column_Concrete'][1])
# print(f"Name of the Activity: Basement_Column_Concrete\nUsage:{storage_sand[3]}\nStorage:{storage_sand[0]}\nDate:{date(storage_sand[2])}\n")
# storage_sand=order_sand(act['Grade_Beam_PCC'][1],storage_sand[0],ac['Grade_Beam_PCC'][1])
# print(f"Name of the Activity: Grade_Beam_PCC\nUsage:{storage_sand[3]}\nStorage:{storage_sand[0]}\nDate:{date(storage_sand[2])}\n")
# storage_sand=order_sand(act['Grade_Beam_RCC'][1],storage_sand[0],ac['Grade_Beam_RCC'][1])
# print(f"Name of the Activity: Grade_Beam_RCC\nUsage:{storage_sand[3]}\nStorage:{storage_sand[0]}\nDate:{date(storage_sand[2])}\n")
# storage_sand=order_sand(act['Basement_BrickWork'][1],storage_sand[0],ac['Basement_BrickWork'][1])
# print(f"Name of the Activity: Basement_BrickWork\nUsage:{storage_sand[3]}\nStorage:{storage_sand[0]}\nDate:{date(storage_sand[2])}\n")
# storage_sand=order_sand(act['Basement_Belt_Beam_RCC'][1],storage_sand[0],ac['Basement_Belt_Beam_RCC'][1])
# print(f"Name of the Activity: Basement_Belt_Beam_RCC\nUsage:{storage_sand[3]}\nStorage:{storage_sand[0]}\nDate:{date(storage_sand[2])}\n")
# storage_sand=order_sand(act['Basement_floor_PCC_work'][1],storage_sand[0],ac['Basement_floor_PCC_work'][1])
# print(f"Name of the Activity: Basement_floor_PCC_work\nUsage:{storage_sand[3]}\nStorage:{storage_sand[0]}\nDate:{date(storage_sand[2])}\n")
# storage_sand=order_sand(act['Ground_Floor_Column_Concrete'][1],storage_sand[0],ac['Ground_Floor_Column_Concrete'][1])
# print(f"Name of the Activity: Ground_Floor_Column_Concrete\nUsage:{storage_sand[3]}\nStorage:{storage_sand[0]}\nDate:{date(storage_sand[2])}\n")
# storage_sand=order_sand(act['Ground_Floor_Lintel_Level_BrickWork'][1],storage_sand[0],ac['Ground_Floor_Lintel_Level_BrickWork'][1])
# print(f"Name of the Activity: Ground_Floor_Lintel_Level_BrickWork\nUsage:{storage_sand[3]}\nStorage:{storage_sand[0]}\nDate:{date(storage_sand[2])}\n")
# storage_sand=order_sand(act['Ground_Floor_lintel_Concrete'][1],storage_sand[0],ac['Ground_Floor_lintel_Concrete'][1])
# print(f"Name of the Activity: Ground_Floor_lintel_Concrete\nUsage:{storage_sand[3]}\nStorage:{storage_sand[0]}\nDate:{date(storage_sand[2])}\n")
# storage_sand=order_sand(act['Ground_Floor_Brickwork_Above_lintel'][1],storage_sand[0],ac['Ground_Floor_Brickwork_Above_lintel'][1])
# print(f"Name of the Activity: Ground_Floor_Brickwork_Above_lintel\nUsage:{storage_sand[3]}\nStorage:{storage_sand[0]}\nDate:{date(storage_sand[2])}\n")

# storage_sand=order_sand(act['Ground_Floor_Roof_Slab_Concrete'][1],storage_sand[0],ac['Ground_Floor_Roof_Slab_Concrete'][1])
# print(f"Name of the Activity: Ground_Floor_Roof_Slab_Concrete\nUsage:{storage_sand[3]}\nStorage:{storage_sand[0]}\nDate:{date(storage_sand[2])}\n")
# storage_sand=order_sand(act['First_Floor_Column_Concrete'][1],storage_sand[0],ac['First_Floor_Column_Concrete'][1])
# print(f"Name of the Activity: First_Floor_Column_Concrete\nUsage:{storage_sand[3]}\nStorage:{storage_sand[0]}\nDate:{date(storage_sand[2])}\n")
# storage_sand=order_sand(act['First_Lintel_Level_Brickwork'][1],storage_sand[0],ac['First_Lintel_Level_Brickwork'][1])
# print(f"Name of the Activity: First_Lintel_Level_Brickwork\nUsage:{storage_sand[3]}\nStorage:{storage_sand[0]}\nDate:{date(storage_sand[2])}\n")
# storage_sand=order_sand(act['First_Floor_Lintel_Concrete'][1],storage_sand[0],ac['First_Floor_Lintel_Concrete'][1])
# print(f"Name of the Activity: First_Floor_Lintel_Concrete\nUsage:{storage_sand[3]}\nStorage:{storage_sand[0]}\nDate:{date(storage_sand[2])}\n")
# storage_sand=order_sand(act['First_Floor_Brickwork_Above_Lintel'][1],storage_sand[0],ac['First_Floor_Brickwork_Above_Lintel'][1])
# print(f"Name of the Activity: First_Floor_Brickwork_Above_Lintel\nUsage:{storage_sand[3]}\nStorage:{storage_sand[0]}\nDate:{date(storage_sand[2])}\n")
# storage_sand=order_sand(act['First_Floor_Roof_Slab_Concrete'][1],storage_sand[0],ac['First_Floor_Roof_Slab_Concrete'][1])
# print(f"Name of the Activity: First_Floor_Roof_Slab_Concrete\nUsage:{storage_sand[3]}\nStorage:{storage_sand[0]}\nDate:{date(storage_sand[2])}\n")
# storage_sand=order_sand(act['Parapet_BrickWork'][1],storage_sand[0],ac['Parapet_BrickWork'][1])
# print(f"Name of the Activity: \nUsage:{storage_sand[3]}\nStorage:{storage_sand[0]}\nDate:{date(storage_sand[2])}\n")
# storage_sand=order_sand(act['External_Plastering'][1],storage_sand[0],ac['External_Plastering'][1])
# print(f"Name of the Activity: External_Plastering\nUsage:{storage_sand[3]}\nStorage:{storage_sand[0]}\nDate:{date(storage_sand[2])}\n")
# storage_sand=order_sand(act['Interior_Plastering'][1],storage_sand[0],ac['Interior_Plastering'][1])
# print(f"Name of the Activity: Interior_Plastering\nUsage:{storage_sand[3]}\nStorage:{storage_sand[0]}\nDate:{date(storage_sand[2])}\n")
# storage_sand=order_sand(act['Tiles'][1],storage_sand[0],ac['Tiles_innerworkandGranitework'][1])
# print(f"Name of the Activity: Tiles Works\nUsage:{storage_sand[3]}\nStorage:{storage_sand[0]}\nDate:{date(storage_sand[2])}\n")



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