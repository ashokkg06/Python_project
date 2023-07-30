from activity import *
from schdule import ac
from datetime import date as d,timedelta
#from qwe import leadtime_cement

safety_stock=25
order_place=[25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
leadtime_cement=int(input("Cement's leadtime: "))

def order_cement(a,strage,da):
    global leadtime_cement
    for j in range(len(order_place)):
        storag=0
        storag=strage+order_place[j]-a
        orderdate=da-timedelta(days=leadtime_cement)
        
        if storag<50 and storag>=25: 
            if order_place[j]>50:
                print("(Suggestion: Place two Order with Different Vendors)")
            return storag,order_place[j],orderdate
            
            

        
# print("Cement's OrderDates\n")
# storage_cement=50-act['footingPCC'][0]
# print(f"Name of the Activity: FootingPCC\nUsage: {act['footingPCC'][0]}\nStorage:{storage_cement}\nOrdered:50\nDate:{ac['footingRCC'][1].year}-{ac['footingRCC'][1].month}-{ac['footingRCC'][1].day}\n")
# storage_cement=order_cement(act['footingRCC'][0],storage_cement,ac['footingRCC'][1])
# print(f"Name of the Activity: FootingRCC\nStorage:{storage_cement[0]}\nUsage: {act['footingRCC'][0]}\nOrdered:{storage_cement[1]}\nDate:{storage_cement[2]}\n")
# storage_cement=order_cement(act['Basement_Column_Concrete'][0],storage_cement[0],ac['Basement_Column_Concrete'][1])
# print(f"Name of the Activity: Basement_Column_Concrete\nUsage: {act['Basement_Column_Concrete'][0]}\nStorage:{storage_cement[0]}\n\nOrdered:{storage_cement[1]}\nDate:{storage_cement[2]}\n")
# storage_cement=order_cement(act['Grade_Beam_PCC'][0],storage_cement[0],ac['Grade_Beam_PCC'][1])
# print(f"Name of the Activity: Grade_Beam_PCC\nUsage: {act['Grade_Beam_PCC'][0]}\nStorage:{storage_cement[0]}\n\nOrdered:{storage_cement[1]}\nDate:{storage_cement[2]}\n")
# storage_cement=order_cement(act['Grade_Beam_RCC'][0],storage_cement[0],ac['Grade_Beam_RCC'][1])
# print(f"Name of the Activity: Grade_Beam_RCC\nUsage: {act['Grade_Beam_RCC'][0]}\nStorage:{storage_cement[0]}\nOrdered:{storage_cement[1]},\nDate:{storage_cement[2]}\n")
# storage_cement=order_cement(act['Basement_BrickWork'][0],storage_cement[0],ac['Basement_BrickWork'][1])
# print(f"Name of the Activity: Basement_BrickWork\nUsage: {act['Basement_BrickWork'][0]}\nStorage:{storage_cement[0]}\nOrdered:{storage_cement[1]},\nDate:{storage_cement[2]}\n")
# storage_cement=order_cement(act['Basement_Belt_Beam_RCC'][0],storage_cement[0],ac['Basement_Belt_Beam_RCC'][1])
# print(f"Name of the Activity: Basement_Belt_Beam_RCC\nUsage: {act['Basement_Belt_Beam_RCC'][0]}\nStorage:{storage_cement[0]},\nOrdered:{storage_cement[1]},\nDate:{storage_cement[2]}\n")
# storage_cement=order_cement(act['Basement_floor_PCC_work'][0],storage_cement[0],ac['Basement_floor_PCC_work'][1])
# print(f"Name of the Activity: Basement_floor_PCC_work\nUsage: {act['Basement_floor_PCC_work'][0]}\nStorage:{storage_cement[0]}\nOrdered:{storage_cement[1]},\nDate:{storage_cement[2]}\n")
# storage_cement=order_cement(act['Ground_Floor_Column_Concrete'][0],storage_cement[0],ac['Ground_Floor_Column_Concrete'][1])
# print(f"Name of the Activity: Ground_Floor_Column_Concrete\nUsage: {act['Ground_Floor_Column_Concrete'][0]}\nStorage:{storage_cement[0]}\nOrdered:{storage_cement[1]},\nDate:{storage_cement[2]}\n")
# storage_cement=order_cement(act['Ground_Floor_Lintel_Level_BrickWork'][0],storage_cement[0],ac['Ground_Floor_Lintel_Level_BrickWork'][1])
# print(f"Name of the Activity: Ground_Floor_Lintel_Level_BrickWork\nUsage: {act['Ground_Floor_Lintel_Level_BrickWork'][0]}\nStorage:{storage_cement[0]}\nOrdered:{storage_cement[1]},\nDate:{storage_cement[2]}\n")
# storage_cement=order_cement(act['Ground_Floor_lintel_Concrete'][0],storage_cement[0],ac['Ground_Floor_lintel_Concrete'][1])
# print(f"Name of the Activity: Ground_Floor_lintel_Concrete\nUsage: {act['Ground_Floor_lintel_Concrete'][0]}\nStorage:{storage_cement[0]}\nOrdered:{storage_cement[1]},\nDate:{storage_cement[2]}\n")
# storage_cement=order_cement(act['Ground_Floor_Brickwork_Above_lintel'][0],storage_cement[0],ac['Ground_Floor_Brickwork_Above_lintel'][1])
# print(f"Name of the Activity: Ground_Floor_Brickwork_Above_lintel\nUsage: {act['Ground_Floor_Brickwork_Above_lintel'][0]}\nStorage:{storage_cement[0]}\nOrdered:{storage_cement[1]},\nDate:{storage_cement[2]}\n")

# storage_cement=order_cement(act['Ground_Floor_Roof_Slab_Concrete'][0],storage_cement[0],ac['Ground_Floor_Roof_Slab_Concrete'][1])
# print(f"Name of the Activity: Ground_Floor_Roof_Slab_Concrete\nUsage: {act['Ground_Floor_Roof_Slab_Concrete'][0]}\nStorage:{storage_cement[0]}\nOrdered:{storage_cement[1]},\nDate:{storage_cement[2]}\n")
# storage_cement=order_cement(act['First_Floor_Column_Concrete'][0],storage_cement[0],ac['First_Floor_Column_Concrete'][1])
# print(f"Name of the Activity: First_Floor_Column_Concrete\nUsage: {act['First_Floor_Column_Concrete'][0]}\nStorage:{storage_cement[0]}\nOrdered:{storage_cement[1]},\nDate:{storage_cement[2]}\n")
# storage_cement=order_cement(act['First_Lintel_Level_Brickwork'][0],storage_cement[0],ac['First_Lintel_Level_Brickwork'][1])
# print(f"Name of the Activity: First_Lintel_Level_Brickwork\nUsage: {act['First_Lintel_Level_Brickwork'][0]}\nStorage:{storage_cement[0]}\nOrdered:{storage_cement[1]},\nDate:{storage_cement[2]}\n")
# storage_cement=order_cement(act['First_Floor_Lintel_Concrete'][0],storage_cement[0],ac['First_Floor_Lintel_Concrete'][1])
# print(f"Name of the Activity: First_Floor_Lintel_Concrete\nUsage: {act['First_Floor_Lintel_Concrete'][0]}\nStorage:{storage_cement[0]}\nOrdered:{storage_cement[1]},\nDate:{storage_cement[2]}\n")
# storage_cement=order_cement(act['First_Floor_Brickwork_Above_Lintel'][0],storage_cement[0],ac['First_Floor_Brickwork_Above_Lintel'][1])
# print(f"Name of the Activity: First_Floor_Brickwork_Above_Lintel\nUsage: {act['First_Floor_Brickwork_Above_Lintel'][0]}\nStorage:{storage_cement[0]}\nOrdered:{storage_cement[1]},\nDate:{storage_cement[2]}\n")
# storage_cement=order_cement(act['First_Floor_Roof_Slab_Concrete'][0],storage_cement[0],ac['First_Floor_Roof_Slab_Concrete'][1])
# print(f"Name of the Activity: First_Floor_Roof_Slab_Concrete\nUsage: {act['First_Floor_Roof_Slab_Concrete'][0]}\nStorage:{storage_cement[0]}\nOrdered:{storage_cement[1]},\nDate:{storage_cement[2]}\n")
# storage_cement=order_cement(act['Parapet_BrickWork'][0],storage_cement[0],ac['Parapet_BrickWork'][1])
# print(f"Name of the Activity: Parapet_BrickWork\nUsage: {act['Parapet_BrickWork'][0]}\nStorage:{storage_cement[0]}\nOrdered:{storage_cement[1]},\nDate:{storage_cement[2]}\n")
# storage_cement=order_cement(act['External_Plastering'][0],storage_cement[0],ac['External_Plastering'][1])
# print(f"Name of the Activity: External_Plastering\nUsage: {act['External_Plastering'][0]}\nStorage:{storage_cement[0]}\nOrdered:{storage_cement[1]},\nDate:{storage_cement[2]}\n")
# storage_cement=order_cement(act['Interior_Plastering'][0],storage_cement[0],ac['Interior_Plastering'][1])
# print(f"Name of the Activity: Interior_Plastering\nUsage: {act['Interior_Plastering'][0]}\nStorage:{storage_cement[0]}\nOrdered:{storage_cement[1]},\nDate:{storage_cement[2]}\n")
# storage_cement=order_cement(act['Tiles'][0],storage_cement[0],ac['Tiles_innerworkandGranitework'][1])
# print(f"Name of the Activity: Tiles Work\nUsage: {act['Tiles'][0]}\nStorage:{storage_cement[0]}\nOrdered:{storage_cement[1]},\nDate:{storage_cement[2]}\n")


# print(f"cement:{order(act['Ground_Floor_Lintel_Level_BrickWork'][0],storage_cement)}")
# storage_cement=50-act['footingPCC'][0]
# print(f"cement:{order(act['Ground_Floor_lintel_Concrete'][0],storage_cement)}")
# storage_cement=50-act['footingPCC'][0]
# print(f"cement:{order(act['Ground_Floor_Brickwork_Above_lintel'][0],storage_cement)}")
# storage_cement=50-act['footingPCC'][0]
# print(f"cement1:{order(act['Ground_Floor_Roof_Slab_Concrete'][0],storage_cement)}")
# storage_cement=50-act['footingPCC'][0]
# print(f"cement:{order(act['First_Floor_Column_Concrete'][0],storage_cement)}")
# storage_cement=50-act['footingPCC'][0]
# print(f"cement:{order(act['First_Lintel_Level_Brickwork'][0],storage_cement)}")
# storage_cement=50-act['footingPCC'][0]
# print(f"cement:{order(act['First_Floor_Lintel_Concrete'][0],storage_cement)}")
# storage_cement=50-act['footingPCC'][0]
# print(f"cement:{order(act['First_Floor_Brickwork_Above_Lintel'][0],storage_cement)}")
# storage_cement=50-act['footingPCC'][0]
# print(f"cement1:{order(act['First_Floor_Roof_Slab_Concrete'][0],storage_cement)}")
# storage_cement=50-act['footingPCC'][0]
# print(f"cement:{order(act['Parapet_BrickWork'][0],storage_cement)}")
# storage_cement=50-act['footingPCC'][0]
# print(f"cement:{order(act['External_Plastering'][0],storage_cement)}")
# storage_cement=50-act['footingPCC'][0]
# print(f"cement:{order(act['Interior_Plastering'][0],storage_cement)}")
# storage_cement=50-act['footingPCC'][0]
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
