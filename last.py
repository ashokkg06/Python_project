from activity import *
from schdule import *
from reorder_brick import *
from reorder_cement import *
from reorder_sand import *
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Alignment
from openpyxl.styles.alignment import Alignment

def date(d):
  if d == 'No Order':
    return 'No Order'
  else:
    return (
      f'{storage_sand[2].year}-0{storage_sand[2].month}-{storage_sand[2].day}')


def date_time(var):
  return (
    f'{storage_cement[2].year}-{storage_cement[2].month}-{storage_cement[2].day}'
  )

recipient_email=input("Enter the mail id: ")


data_cement, data_brick, data_sand = [], [], []
cement_, brick_, sand_ = [], [], []

order_dates = {
  'Basement_Column_Concrete':
  ac['Basement_Column_Concrete'][1],
  'Grade_Beam_PCC':
  ac['Grade_Beam_PCC'][1],
  'Grade_Beam_RCC':
  ac['Grade_Beam_RCC'][1],
  'Basement_BrickWork':
  ac['Basement_BrickWork'][1],
  'Basement_Belt_Beam_RCC':
  ac['Basement_Belt_Beam_RCC'][1],
  'Basement_floor_PCC_work':
  ac['Basement_floor_PCC_work'][1],
  'Ground_Floor_Column_Concrete':
  ac['Ground_Floor_Column_Concrete'][1],
  'Ground_Floor_Lintel_Level_BrickWork':
  ac['Ground_Floor_Lintel_Level_BrickWork'][1],
  'Ground_Floor_lintel_Concrete':
  ac['Ground_Floor_lintel_Concrete'][1],
  'Ground_Floor_Brickwork_Above_lintel':
  ac['Ground_Floor_Brickwork_Above_lintel'][1],
  'Ground_Floor_Roof_Slab_Concrete':
  ac['Ground_Floor_Roof_Slab_Concrete'][1],
  'First_Floor_Column_Concrete':
  ac['First_Floor_Column_Concrete'][1],
  'First_Lintel_Level_Brickwork':
  ac['First_Lintel_Level_Brickwork'][1],
  'First_Floor_Lintel_Concrete':
  ac['First_Floor_Lintel_Concrete'][1],
  'First_Floor_Brickwork_Above_Lintel':
  ac['First_Floor_Brickwork_Above_Lintel'][1],
  'First_Floor_Roof_Slab_Concrete':
  ac['First_Floor_Roof_Slab_Concrete'][1],
  'Parapet_BrickWork':
  ac['Parapet_BrickWork'][1],
  'Interior_Plastering':
  ac['Interior_Plastering'][1],
  'External_Plastering':
  ac['External_Plastering'][1],
  'Tiles':
  ac['Tiles_innerworkandGranitework'][1]
}
order_dates1 = {
  'Ground_Floor_Lintel_Level_BrickWork':
  ac['Ground_Floor_Lintel_Level_BrickWork'][1],
  'Ground_Floor_Brickwork_Above_lintel':
  ac['Ground_Floor_Brickwork_Above_lintel'][1],
  'First_Lintel_Level_Brickwork':
  ac['First_Lintel_Level_Brickwork'][1],
  'First_Floor_Brickwork_Above_Lintel':
  ac['First_Floor_Brickwork_Above_Lintel'][1],
  'Parapet_BrickWork':
  ac['Parapet_BrickWork'][1],
}

while True:
  inpu = int(
    input(
      "1. Cement's Order\n2. Brick's Order\n3. Sand Order\n4. Exit\nEnter the Choice: "
    ))
  if inpu == 1:
    print("Cement's OrderDates\n")
    storage_cement = 50 - act['footingPCC'][0]
    print(
      f"Name of the Activity: FootingPCC\nUsage: {act['footingPCC'][0]}\nStorage:{storage_cement}\nOrdered:50\nDate:{ac['footingPCC'][1]-timedelta(days=leadtime_cement)}\n"
    )
    data_cement.append({
      'Name of the Activity':'FootingPCC',
      'Usage in Nos':act['footingPCC'][0],
      'Storage in Nos':storage_cement,
      'Ordered in Nos': 50,
      'Date':ac['footingPCC'][1] - timedelta(days=leadtime_cement)
    })
    cement_.append({
      'Name of the Activity':'FootingPCC',
      'Usage in Nos':act['footingPCC'][0],
      'Storage in Nos':storage_cement,
      'Ordered in Nos': 50,
      'Date':ac['footingPCC'][1] - timedelta(days=leadtime_cement)
    })
    storage_cement = order_cement(act['footingRCC'][0], storage_cement,ac['footingRCC'][1])
    print(      f"Name of the Activity: FootingRCC\nStorage:{storage_cement[0]} Nos\nUsage: {act['footingRCC'][0]} Nos\nOrdered:{storage_cement[1]} Nos\nDate:{storage_cement[2]}\n"  )
    data_cement.append({
      'Name of the Activity': 'FootingRCC',
      'Usage in Nos': act['footingRCC'][0],
      'Storage in Nos': storage_cement[0],
      'Ordered in Nos': storage_cement[1],
      'Date': storage_cement[2]
    })
    cement_.append({
      'Name of the Activity': 'FootingRCC',
      'Usage in Nos': act['footingRCC'][0],
      'Storage in Nos': storage_cement[0],
      'Ordered in Nos': storage_cement[1],
      'Date': storage_cement[2]
    })
    for key, value in order_dates.items():
      storage_cement = order_cement(act[key][0], storage_cement[0], value)
      print(
        f"Name of the Activity: {key}\nStorage:{storage_cement[0]} Nos\nUsage: {act[key][0]} Nos\nOrdered:{storage_cement[1]} Nos\nDate:{storage_cement[2]}\n"
      )
      data_cement.append({
        'Name of the Activity': key,
        'Storage in Nos': storage_cement[0],
        "Usage in Nos": act[key][0],
        "Ordered in Nos": storage_cement[1],
        'Date': storage_cement[2]
      })
      cement_.append({
        'Name of the Activity': key,
        'Storage in Nos': storage_cement[0],
        "Usage in Nos": act[key][0],
        "Ordered in Nos": storage_cement[1],
        'Date': storage_cement[2]
      })
    print("For Vendor's Details visit this site: https://constructioncart.store/\n")
    df = pd.DataFrame(data_cement)
    # df.style.set_properties(subset=df.columns, text_align='left').hide_index()
    writer1 = pd.ExcelWriter('Cement.xlsx', engine='openpyxl')
    df.to_excel(writer1, sheet_name='Cement', index=False)
    workbook = writer1.book
    worksheet = writer1.sheets['Cement']
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

  elif inpu == 2:
    print("Brick's OrderDates\n")
    storage_brick = 0
    storage_brick = order_brick(act['Basement_BrickWork'][2], storage_brick,
                                ac['Basement_BrickWork'][1])
    print(
      f"Name of the Activity: Basement_BrickWork\nUsage: {storage_brick[2]} Nos\nstorage:{storage_brick[0]} Nos\nOrderDates: {dateq(storage_brick[1])}\n"
    )
    data_brick.append({
      'Name of the Activity': 'Basement_BrickWork',
      'Usage in Nos': storage_brick[2],
      "Storage in Nos": storage_brick[0],
      'Order Dates': dateq(storage_brick[1]),
    })
    brick_.append({
      'Name of the Activity': 'Basement_BrickWork',
      'Usage in Nos': storage_brick[2],
      "Storage in Nos": storage_brick[0],
      'Order Dates': storage_brick[1],
    })
    for key, value in order_dates1.items():
      storage_brick = order_brick(act[key][2], storage_brick[0], value)
      print(
        f"Name of the Activity: {key}\nUsage: {act[key][2]} Nos\nStorage:{storage_brick[0]} Nos\nOrderDates:{dateq(storage_brick[1])}\n"
      )
      data_brick.append({
        'Name of the Activity': key,
        'Usage in Nos': storage_brick[2],
        "Storage in Nos": storage_brick[0],
        'Order Dates': dateq(storage_brick[1]),
      })
      brick_.append({
        'Name of the Activity': key,
        'Usage in Nos': storage_brick[2],
        "Storage in Nos": storage_brick[0],
        'Order Dates': storage_brick[1],
      })
    dg = pd.DataFrame(data_brick)
    writer2 = pd.ExcelWriter('Brick.xlsx', engine='openpyxl')
    dg.to_excel(writer2, sheet_name='Brick', index=False)
    workbook = writer2.book
    worksheet = writer2.sheets['Brick']
    worksheet.column_dimensions['A'].width = 35
    worksheet.column_dimensions['B'].width = 20
    worksheet.column_dimensions['C'].width = 20
    worksheet.column_dimensions['D'].width = 34
    align_left = Alignment(horizontal='left')
    for col in worksheet.columns:
      for cell in col:
        cell.alignment = align_left
    writer2.close()

    print(
      "For Vendor's Details visit this site: https://constructioncart.store/\n"
    )

  elif inpu == 3:
    storage_sand = 11.32 - act['footingPCC'][1]
    storage_sand = order_sand(act['footingPCC'][1], 0, ac['footingPCC'][1])
    sand_.append({
      'Name of the Activity': 'FootingPCC',
      'Usage in m³': storage_sand[3],
      'Storage in m³': storage_sand[0],
      'Date': storage_sand[2],
    })
    print(
      f"Name of the Activity: FootingPCC\nUsage:{storage_sand[3]} m³\nstorage:{storage_sand[0]} m³\nDate:{date(storage_sand[2])}\n"
    )
    data_sand.append({
      'Name of the Activity': 'FootingPCC',
      'Usage in m³': storage_sand[3],
      'Storage in m³': storage_sand[0],
      'Date': date(storage_sand[2]),
    })
    
    storage_sand = order_sand(act['footingRCC'][1], storage_sand[0],
                              ac['footingRCC'][1])
    sand_.append({
      'Name of the Activity': 'FootingRCC',
      'Usage in m³': storage_sand[3],
      'Storage in m³': storage_sand[0],
      'Date': storage_sand[2],
    })
    print(
      f"Name of the Activity: FootingRCC\nStorage:{storage_sand[0]}\nUsage: {storage_sand[3]} m³\nDate:{date(storage_sand[2])}\n"
    )
    data_sand.append({
      'Name of the Activity': 'FootingRCC',
      'Usage in m³': storage_sand[3],
      'Storage in m³': storage_sand[0],
      'Date': date(storage_sand[2]),
    })
    
    
    for key, value in order_dates.items():
      storage_sand = order_sand(act[key][1], storage_sand[0], value)
      sand_.append({
      'Name of the Activity': key,
        'Usage in m³': storage_sand[3],
        'Storage in m³': storage_sand[0],
        'Date': storage_sand[2],
    })
      print(
        f"Name of the Activity: {key}\nStorage:{storage_sand[0]} m³\nUsage: {storage_sand[3]} m³\nDate:{date(storage_sand[2])}\n"
      )
      data_sand.append({
        'Name of the Activity': key,
        'Usage in m³': storage_sand[3],
        'Storage in m³': storage_sand[0],
        'Date': date(storage_sand[2]),
      })
    print(data_cement)
    dg = pd.DataFrame(data_sand)
    writer3 = pd.ExcelWriter('Sand.xlsx', engine='openpyxl')
    dg.to_excel(writer3, sheet_name='Sand', index=False)
    workbook = writer3.book
    worksheet = writer3.sheets['Sand']
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
    writer3.close()

  elif inpu == 4: break
