import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Alignment
from openpyxl.styles.alignment import Alignment
from input import data_cement


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




#[{'Name of the Activity': 'FootingPCC', 'Usage in Nos': 21, 'Storage in Nos': 29, 'Ordered in Nos': 50, 'Date': datetime.date(2023, 2, 11)}, {'Name of the Activity': 'FootingRCC', 'Usage in Nos': 73, 'Storage in Nos': 26, 'Ordered in Nos': 70, 'Date': datetime.date(2023, 2, 13)}, {'Name of the Activity': 'Basement_Column_Concrete', 'Storage in Nos': 32, 'Usage in Nos': 19, 'Ordered in Nos': 25, 'Date': datetime.date(2023, 2, 16)}, {'Name of the Activity': 'Grade_Beam_PCC', 'Storage in Nos': 42, 'Usage in Nos': 15, 'Ordered in Nos': 25, 'Date': datetime.date(2023, 2, 20)}, {'Name of the Activity': 'Grade_Beam_RCC', 'Storage in Nos': 29, 'Usage in Nos': 43, 'Ordered in Nos': 30, 'Date': datetime.date(2023, 2, 23)}, {'Name of the Activity': 'Basement_BrickWork', 'Storage in Nos': 45, 'Usage in Nos': 9, 'Ordered in Nos': 25, 'Date': datetime.date(2023, 2, 24)}, {'Name of the Activity': 'Basement_Belt_Beam_RCC', 'Storage in Nos': 44, 'Usage in Nos': 26, 'Ordered in Nos': 25, 'Date': datetime.date(2023, 2, 28)}, {'Name of the Activity': 'Basement_floor_PCC_work', 'Storage in Nos': 27, 'Usage in Nos': 42, 'Ordered in Nos': 25, 'Date': datetime.date(2023, 3, 5)}, {'Name of the Activity': 'Ground_Floor_Column_Concrete', 'Storage in Nos': 26, 'Usage in Nos': 26, 'Ordered in Nos': 25, 'Date': datetime.date(2023, 3, 9)}, {'Name of the Activity': 'Ground_Floor_Lintel_Level_BrickWork', 'Storage in Nos': 25, 'Usage in Nos': 26, 'Ordered in Nos': 25, 'Date': datetime.date(2023, 3, 11)}, {'Name of the Activity': 'Ground_Floor_lintel_Concrete', 'Storage in Nos': 28, 'Usage in Nos': 22, 'Ordered in Nos': 25, 'Date': datetime.date(2023, 3, 20)}, {'Name of the Activity': 'Ground_Floor_Brickwork_Above_lintel', 'Storage in Nos': 39, 'Usage in Nos': 14, 'Ordered in Nos': 25, 'Date': datetime.date(2023, 3, 22)}, {'Name of the Activity': 'Ground_Floor_Roof_Slab_Concrete', 'Storage in Nos': 25, 'Usage in Nos': 114, 'Ordered in Nos': 100, 'Date': datetime.date(2023, 3, 31)}, {'Name of the Activity': 'First_Floor_Column_Concrete', 'Storage in Nos': 27, 'Usage in Nos': 28, 'Ordered in Nos': 30, 'Date': datetime.date(2023, 4, 26)}, {'Name of the Activity': 'First_Lintel_Level_Brickwork', 'Storage in Nos': 26, 'Usage in Nos': 26, 'Ordered in Nos': 25, 'Date': datetime.date(2023, 4, 28)}, {'Name of the Activity': 'First_Floor_Lintel_Concrete', 'Storage in Nos': 31, 'Usage in Nos': 20, 'Ordered in Nos': 25, 'Date': datetime.date(2023, 5, 5)}, {'Name of the Activity': 'First_Floor_Brickwork_Above_Lintel', 'Storage in Nos': 42, 'Usage in Nos': 14, 'Ordered in Nos': 25, 'Date': datetime.date(2023, 5, 7)}, {'Name of the Activity': 'First_Floor_Roof_Slab_Concrete', 'Storage in Nos': 28, 'Usage in Nos': 114, 'Ordered in Nos': 100, 'Date': datetime.date(2023, 5, 14)}, {'Name of the Activity': 'Parapet_BrickWork', 'Storage in Nos': 44, 'Usage in Nos': 9, 'Ordered in Nos': 25, 'Date': datetime.date(2023, 6, 6)}, {'Name of the Activity': 'Interior_Plastering', 'Storage in Nos': 37, 'Usage in Nos': 32, 'Ordered in Nos': 25, 'Date': datetime.date(2023, 6, 13)}, {'Name of the Activity': 'External_Plastering', 'Storage in Nos': 29, 'Usage in Nos': 33, 'Ordered in Nos': 25, 'Date': datetime.date(2023, 6, 23)}, {'Name of the Activity': 'Tiles', 'Storage in Nos': 29, 'Usage in Nos': 40, 'Ordered in Nos': 40, 'Date': datetime.date(2023, 7, 4)}]
