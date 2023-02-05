area = list(map(int, input("Enter the area: ").split("x")))
n_rooms = int(input("Enter the Number of Rooms "))
thickness_wall = float(0.3)
parapet = area[0]+area[1]+(4*thickness_wall)
dimensions = list()
print("Enter the dimension of room: ")
for i in range(n_rooms):
    a = input().split("x")
    dimensions.append([float(a[0]), float(a[1])])

di, b = list(), list()
for i in range(0, len(dimensions)):
    di.append(dimensions[i][0])
    b.append(dimensions[i][1])
ab = list(set(di+b))
l = []
for i in list(ab):
    beam = int(input(f"Enter the {i}m wall"))
    l.append(beam)

c_c_length = 0
no_of_horizontal_wall = int(input("Enter the horizontal wall: "))
no_of_vertical_wall = int(input("Enter the vertical wall: "))
print("Enter the wall length by horizontal to vertical: ")
for i in range(0, (no_of_vertical_wall+no_of_horizontal_wall)):
    c_c_length += float(input())
height_wall = float(input("Enter the height of wall: "))
t_juction = int(input("Enter no of T-juction: "))
no_of_column = int(input("Enter the no's of column"))
door = [1, 2.1]
doo = int(input("Enter no of other Doors without Entrance door: "))
doors = [0.9, 2.1]
windows = int(input("Enter no of windows: "))
window = [1.2, 1.4]
lintel = 0.18
ventilator = [0.6, 0.4]
height_parapet = 0.9


def Basement(c_c_length, t_juction, thickness_wall, door, doo, doors, dimensions):
    base = {}

    plinthbeam = 0
    e_ex, pcc,rcc_belt = 0, 0, 0
    for i in range(0, len(ab)):
        e_ex += ab[i]*l[i]*0.45*0.675
        pcc += ab[i]*l[i]*0.6*0.075
        plinthbeam += ab[i]*l[i]*0.3*0.45
        rcc_belt += ab[i]*l[i]*0.3*0.15

    earthwork_excavation = (no_of_column*(1.15*1.15*1.2))+e_ex
    base["Earthwork_excavation in m\u00b3"] = earthwork_excavation
    pcc_in_fnd = (no_of_column*(1.15*1.15*0.075))+pcc
    base["Pcc_in_fnd in m\u00b3"] = pcc_in_fnd
    columnbase = no_of_column*(1*1*0.25)
    columnstem = no_of_column*(0.3*0.3*1.35)
    base["Rcc_column in m\u00b3"] = columnbase+columnstem+rcc_belt
    base["RCC_plinthbeam in m\u00b3"] = plinthbeam
    brickwork_in_basement = ((
        c_c_length-(t_juction*(0.3/2)))*0.3*0.75)-(no_of_column*0.3*0.3*0.75)
    base["brickwork in m\u00b3"] = brickwork_in_basement
    # thickness_dpc = (c_c_length-(t_juction*(0.4/2)))*0.4*1
    # Deduction_EDoor = 1*(float(door[0]))*0.4
    # Deduction_Door = doo*(float(doors[0]))*0.4
    # base["2.5cm Thickness DPC in m\u00b2"] = thickness_dpc - \
    #     (Deduction_Door+Deduction_EDoor)
    total = 0
    totalfloor = 0
    totalfloorfinish = 0
    for i in range(0, len(dimensions)):
        r1 = 1*(int(dimensions[i][0])-(2*0.05)) * \
            (int(dimensions[i][1])-(2*0.05))*(0.6-0.025-.15)
        r2 = 1*(int(dimensions[i][0])-(2*0.05)) * \
            (int(dimensions[i][1])-(2*0.05))*(.15)
        r3 = 1*(int(dimensions[i][0]))*(int(dimensions[i][1]))
        total += r1
        totalfloor += r2
        totalfloorfinish += r3
    total, totalfloor = float("{:.3f}".format(
        total)), float("{:.3f}".format(totalfloor))
    area_of_Edoor = 1*(int(door[0])*(thickness_wall+0.05))
    area_of_door = doo*(int(door[0])*(thickness_wall))
    base["Sandfilling in plinth in m\u00b3"] = total
    base["Flooring concrete in m\u00b3"] = totalfloor
    base["Floor Finish in m\u00b2"] = totalfloorfinish + \
        area_of_Edoor+area_of_door

    return base


def superstructure(c_c_length, thickness_wall, height_wall, doo, door, doors, windows, window, lintel, height_parapet, no_of_vertical_wall, no_of_horizontal_wall, n_rooms, dimensions, area, parapet):
    super = {}
    BW_in_superWall = (
        (c_c_length-(t_juction*(thickness_wall/2)))*thickness_wall*height_wall)
    Deduction_EDoor = 1*(float(door[0])*(float(door[1])))*thickness_wall
    Deduction_Door = doo*(float(doors[0])*(float(doors[1])))*thickness_wall
    Deduction_Window = windows * \
        (float(window[0]))*(float(window[1]))*thickness_wall
    Deduction_Ventilator = 1 * \
        (float(ventilator[0]))*(float(ventilator[1]))*thickness_wall
    Deduction_lintel = 1 * \
        (c_c_length-(t_juction*(thickness_wall/2)))*thickness_wall*lintel
    Column=(no_of_column*thickness_wall*thickness_wall*height_wall)
    add_parapet = 1*(2*((area[0]+(2*thickness_wall))+area[1] +
                     (2*thickness_wall)))*thickness_wall*height_parapet
    Deduction_Parapet=(4*thickness_wall*thickness_wall*height_parapet)
    total = (BW_in_superWall+add_parapet)-(Deduction_Door+Deduction_EDoor +
                                           Deduction_Window+Deduction_Ventilator+Deduction_lintel+Column+Deduction_Parapet)
    super["I_class_BW_Supersturcture in m\u00b3"] = float(
        "{:.3f}".format(total))
    RCC_in_roofSlab = 1*(area[0]+((no_of_horizontal_wall-1)*thickness_wall)) * \
        (area[1]+(no_of_vertical_wall*thickness_wall))*0.125
    RCC_in_sunshade_W = (windows-1)*(float(window[0])+(2*thickness_wall))*0.075
    RCC_in_sunshade_V = 1*(float(ventilator[0])+(2*thickness_wall))*0.075
    RCC_in_sunshade_front = 1*3.5*0.075
    RCC_in_lintel = 1 * \
        (c_c_length-(t_juction*(thickness_wall/2)))*thickness_wall*lintel
    RCC_work_in_slabAndBeam = RCC_in_lintel+RCC_in_roofSlab + \
        RCC_in_sunshade_front+RCC_in_sunshade_V+RCC_in_sunshade_W
    super["RCC_work_in_slabAndBeam in m\u00b3"] = float(
        "{:.3f}".format(RCC_work_in_slabAndBeam))
    Weathering_Couarse = 1*(area[0]+thickness_wall) * \
        (area[1]+thickness_wall)*0.075
    super["Weathering_Couarse in m\u00b3"] = float(
        "{:.3f}".format(Weathering_Couarse))
    Pressed_tiles = 1*(area[0]+thickness_wall)*(area[1]+thickness_wall)
    super["Pressed_tiles in m\u00b2"] = float("{:.3f}".format(Pressed_tiles))
    Interior_plastering = 0
    for i in range(0, n_rooms):
        Interior_plastering += (int(dimensions[i][0]) +
                                int(dimensions[i][1]))*height_wall*2
    above_plinth_wall = ((area[0]+(3*thickness_wall))+(area[1] +
                         (3*thickness_wall)))*2*(height_wall+0.125+height_parapet)
    top_of_parapet = (area[0]+(2*thickness_wall)) + \
        (area[1]+(2*thickness_wall))*2*thickness_wall
    inner_surface_of_parapet = (
        area[0]+(2*thickness_wall)+area[1]+(2*thickness_wall))*2*(height_parapet-0.075-0.025)
    below_plinth = ((area[0]+(no_of_vertical_wall*thickness_wall)+(0.4-thickness_wall))+(
        area[1]+(no_of_vertical_wall*thickness_wall)+(0.4-thickness_wall)))*2*0.7
    Deduction_EDoor = 1*(float(door[0])*(float(door[1])))
    Deduction_Door = doo*(float(doors[0])*(float(doors[1])))
    Deduction_Window = windows*(float(window[0]))*(float(window[1]))
    Exterior_plastering = (above_plinth_wall+top_of_parapet+inner_surface_of_parapet +
                           below_plinth)-(Deduction_EDoor+Deduction_Door+Deduction_Window)
    super["Plastering in m\u00b2"] = float(
        "{:.3f}".format(Interior_plastering+Exterior_plastering))
    return super


b=Basement(c_c_length,t_juction,thickness_wall,door,doo,doors,dimensions)
a=superstructure(c_c_length,thickness_wall,height_wall,doo,door,doors,windows,window,lintel,height_parapet,no_of_vertical_wall,no_of_horizontal_wall,n_rooms,dimensions,area,parapet)

print("\n----------- Basement -----------\n")

for i,j in b.items():
      print(f"{i} = {j}")
print("\n----------- SuperStructure -----------\n")
for i,j in a.items():
      print(f"{i} = {j}")
      
      
b.update(a)

cement,sand,Brick=0,0,0
def earthwork(e1):
    cubemetic=28.34
    men,female=6,4
    a=int((men*e1)/cubemetic)+1
    b=int((female*e1)/cubemetic)+1
    total=(a*400)+(b*350)
    total*=1.03         #3% for water and other charges
    return int(total)
#earthworkval=b.get("Earthwork_excavation in m³")
#print(earthwork(b.get("Earthwork_excavation in m³")))
def pcc(p1):
    global cement,sand,Brick
    p1*=1.52            #for total dry ingredients
    VolumeOfCement=int((1/7)*p1*30)
    print(VolumeOfCement)
    cement+=VolumeOfCement
    VolumeOfSand=(2/7)*p1
    sand+=VolumeOfSand
    VolumeOfStoneBallast=(4/7)*p1
    total=(VolumeOfCement*430)+(VolumeOfSand*1500)+(VolumeOfStoneBallast*1000)
    labour=19956.67
    total+=(labour*p1/15.2)
    total*=1.015
    return int(total)
#print(pcc(b.get("Pcc_in_fnd in m³")))
def BrickWork(b1):
    global cement,sand,Brick
    VolumeOfMortar=0.3025
    brick=(VolumeOfMortar*b1)
    brick=float("{:.3f}".format(brick))
    VolumeOfCement=int((1/7)*brick*30)+1
    cement+=VolumeOfCement
    VolumeOfSand=(6/7)*brick
    sand+=VolumeOfSand
    Brick=int(b1*410)+1
    total=((b1*410)*12)+(VolumeOfSand*1500)+(VolumeOfCement*430)
    Labour=(17135*b1)/10
    total+=Labour
    total*=1.015
    
    return int(total)
b11=(b.get("brickwork in m³"))+b.get("I_class_BW_Supersturcture in m³")
#print(BrickWork(b1))

def plastering(p1):
    global cement,sand,Brick
    val=0.02*p1
    VolumeOfCement=int((1/7)*val*30)
    cement+=VolumeOfCement
    VolumeOfPsand=(6/7)*val
    sand+=VolumeOfPsand
    total=(VolumeOfCement*430)+(VolumeOfPsand*1255)
    Labour=165.125*p1
    total+=Labour
    total*=1.015
    return int(total)
#print(plastering(b.get("Plastering in m²"))

def beam(b1):
    global cement,sand,Brick
    val=1.52*b1
    VolumeOfCement=int((1/5.5)*val*30)
    cement+=VolumeOfCement
    VolumeOfSand=(1.5/5.5)*val
    sand+=VolumeOfSand
    VolumeOfStoneBallast=(3/5.5)*val
    steel=(15.7*7000)
    total=(VolumeOfCement*430)+(VolumeOfSand*1500)+(VolumeOfStoneBallast*1400)+steel+150
    Labour=1988.5*b1
    BarbendingAndShuttering=38540.502
    total+=Labour+BarbendingAndShuttering
    total*=1.015
    return int(total)

totalCost=beam(b.get("RCC_work_in_slabAndBeam in m³"))+plastering(b.get("Plastering in m²"))+BrickWork(b11)+pcc(b.get("Pcc_in_fnd in m³"))+earthwork(b.get("Earthwork_excavation in m³"))+beam(b.get("Rcc_column in m³"))+beam(b.get("RCC_plinthbeam in m³"))
print("\n----------- Totalcost -----------\n")
print(f"Total Cost: ₹{totalCost}")


# one unit sand = 2.83168m³8
print("\n----------- Rate of materials -----------\n")
sand=float("{:.3f}".format(sand))
print(f"Cement:{cement} No's\nSand: {sand} m³\nBrick: {Brick} No's\n")

# Earthwork_excavation in m³ = 31.36125
# Pcc_in_fnd in m³ = 3.2868749999999998
# Rcc_column in m³ = 3.715
# RCC_plinthbeam in m³ = 6.885
# brickwork in m³ = 11.407499999999999
# 2.5cm Thickness DPC in m² = 19.88
# Sandfilling in plinth in m³ = 29.172
# Flooring concrete in m³ = 10.296
# Floor Finish in m² = 73.25

# ----------- SuperStructure -----------

# I_class_BW_Supersturcture in m³ = 54.412
# RCC_work_in_slabAndBeam in m³ = 14.941
# Weathering_Couarse in m³ = 5.789
# Pressed_tiles in m² = 77.19
# Plastering in m² = 460.37