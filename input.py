import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Alignment
from openpyxl.styles.alignment import Alignment


area = input("Enter the area: ").split('x')
print("Ground Floor")
n_rooms = int(input("Enter the Number of Rooms: "))
dimensions = list()
print("Enter the dimension of room: ")


columnwithoutt=6
columnwithoutt1=9
def fttoin(l1, qq):
    rooms = list()
    if (qq) == 2:
        for i in range(0, len(l1)):  
            l = str(l1[i]).split("'")
            q = ((int(l[0])*12))+int(l[1])
            rooms.append(((q*0.0254)))
    else:
        for i in range(0, len(l1)):  
            for j in range(0, len(l1[i])):
                l = str(l1[i][j]).split("'")
                q = ((int(l[0])*12))+int(l[1])
                rooms.append(((q*0.0254)))

    return rooms



area = fttoin(area, 2)
for i in range(n_rooms):
    a = input().split("x")
    dimensions.append(a)
dimensions = fttoin(dimensions, 0)  # , len(dimensions))
no_of_column = int(input("Enter the no's of column: "))
print('Ground Floor 9" thickness wall')
def cc_length():
    c_c_length = 0
    no_of_horizontal_wall = int(input("Enter the horizontal wall: "))
    no_of_vertical_wall = int(input("Enter the vertical wall: "))
    print("Enter the wall length by horizontal to vertical: ")
    ll = list()
    for i in range(0, (no_of_vertical_wall+no_of_horizontal_wall)):
        # c_c_length += float(input())
        ll.append(input())
    ll = fttoin(ll, 2)
    for i in range(0, len(ll)):
        c_c_length += ll[i]

    t_juction = int(input("Enter no of T-juction: "))

    return c_c_length, t_juction


c1 = cc_length()
t1 = c1[1]
c1 = c1[0]
print('Ground Floor 4.5" thickness wall')
c2 = cc_length()
t2, c2 = c2[1], c2[0]
doo = int(input("Enter no of other Doors without Entrance door: "))
windows = int(input("Enter no of windows: "))
noven = int(input("Enter no of Ventilators: "))


door = [1, 2.1]
doors = [0.9, 2.1]
window = [1.2, 1.4]
lintel = 0.18
ventilator = [0.6, 0.4]
height_parapet = 0.9
height_wall = 10.5156


print("\nFirst Floor\n")
n_rooms1 = int(input("Enter the no of rooms: "))
dimensions1 = list()
print("Enter the dimension of room: ")
for i in range(n_rooms1):
    a = input().split("x")
    dimensions1.append(a)
dimensions1 = fttoin(dimensions1, 0)
print('Ground Floor 9" thickness wall')
c11 = cc_length()
t11 = c11[1]
c11 = c11[0]
print('Ground Floor 4.5" thickness wall')
c12 = cc_length()
t12, c12 = c12[1], c12[0]
doo1 = int(input("Enter no of other Doors: "))
windows1 = int(input("Enter no of windows: "))
noven1 = int(input("Enter no of Ventilators: "))

data_cement=[{'Name':'area','Values':area},{'Name':'n_rooms','Values':n_rooms},{'Name': 'dimensions', 'Values': dimensions},{'Name': 'no_of_column', 'Values': no_of_column}, {'Name': 'c1', 'Values': c1}, {'Name': 'c2', 'Values': c2}, {'Name': 'columnwithoutt', 'Values': columnwithoutt}, {'Name': 't1', 'Values': t1}, {'Name': 't2', 'Values': t2}, {'Name': 'doo', 'Values': doo}, {'Name': 'windows', 'Values': windows}, {'Name': 'noven', 'Values': noven}, {'Name': 'door', 'Values': door}, {'Name': 'doors', 'Values': doors}, {'Name': 'window', 'Values': window}, {'Name': 'lintel', 'Values': lintel}, {'Name': 'ventilator', 'Values': ventilator}, {'Name': 'n_rooms1', 'Values': n_rooms1}, {'Name': 'dimensions1', 'Values': dimensions1}, {'Name': 'c11', 'Values': c11}, {'Name': 'c12', 'Values': c12}, {'Name': 'columnwithoutt1', 'Values': columnwithoutt1}, {'Name': 't11', 'Values': t11}, {'Name': 't12', 'Values': t12}, {'Name': 'doo1', 'Values': doo1}, {'Name': 'windows1', 'Values': windows1}, {'Name': 'noven1', 'Values': noven1}]




df = pd.DataFrame(data_cement)
# df.style.set_properties(subset=df.columns, text_align='left').hide_index()
writer1 = pd.ExcelWriter('Input.xlsx', engine='openpyxl')
df.to_excel(writer1, sheet_name='Inputs', index=False)
workbook = writer1.book
worksheet = writer1.sheets['Inputs']
worksheet.column_dimensions['A'].width = 35
worksheet.column_dimensions['B'].width = 20
worksheet.column_dimensions['C'].width = 20
worksheet.column_dimensions['D'].width = 20
worksheet.column_dimensions['E'].width = 30
# Set text alignment to left for all columns
# for col in worksheet.columns:
#     for cell in col:
#         cell.alignment = cell.alignment.copy(horizontal='left')
align_left = Alignment(horizontal='left')
for col in worksheet.columns:
    for cell in col:
        cell.alignment = align_left
# Save the workbook
writer1.close()