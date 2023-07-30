from datetime import date as d, timedelta

  
# # creating the date object of today's date
# todays_date = date.today()
# print(type(todays_date))
# # printing todays date
# print("Current date: ", todays_date)
# a=3
  
# # fetching the current year, month and day of today
# print("Current year:", todays_date.year)
# print("Current month:", todays_date.month)
# print("Current day:", todays_date+timedelta(days=a))

def change(str1,str2):
    #print(str2)
    if str2 =='GF_roof_slab_deshuttering1' or str2=='FF_roof_slab_deshuttering':
        st=str1[2]+timedelta(days=22)
        aaa=ac[str2][0]-1
        et=st+timedelta(days=aaa)
        
        ac.update({str2:[ac[str2][0],st,et]})
        
    else:
        a=ac[str2][0]       
        et=str1[2]+timedelta(days=a)
        
        st=str1[2]+timedelta(days=1)
        ac.update({str2:[a,st,et]})

b=input("\nEnter the Starting Date: \n").split(' ')
a=[]
for i in range(0,len(b)):
    a.append(int(b[i]))
#a=[2023,2,11]
ac={
    'Footing_Marking':[1,d(a[0],a[1],a[2]),d(a[0],a[1],a[2])],
    'Earthwork_Excavation':	[1],
    'footingPCC':	[1],
    'RCC_Reinforcement':	[1],
    'footingRCC':	[1],
    'Column_Reinforcement':	[1],
    'Column_Shuttering':	[1],
    'Basement_Column_Concrete':	[1],
    'soil_Backfilling':	[1],
    'consolidation':	[1],
    'Grade_beam_EarthworkExcavation': [1],
    'Grade_Beam_PCC':	[1],
    'Grade_beam_Reinforcement':	[1],
    'grade_beam_shuttering':	[1],
    'Grade_Beam_RCC':	[1],
    'Basement_BrickWork':	[2],
    'Basement_belt_beam_reinforcement':	[1],
    'Basement_belt_beam_shuttering':	[1],
    'Basement_Belt_Beam_RCC':	[1],
    'Basement_innerwall_plastering':	[1],
    'Basement_gravel_Filling':	[1],
    'Basement_consolidation_work':	[2],
    'Basement_floor_PCC_work':	[1],
    'Ground_floor_column_starter_markingandconcrte':	[1],
    'Ground_floor_column_reinforcement_work':	[1],
    'Ground_column_shutteringwork':	[1],
    'Ground_Floor_Column_Concrete':	[2],
    'Ground_Floor_Lintel_Level_BrickWork':	[5],
    'GF_lintel_Shutteringwork':	[2],
    'GF_lintel_Reinforcementwork':	[2],
    'Ground_Floor_lintel_Concrete':	[2],
    'Ground_Floor_Brickwork_Above_lintel':	[3],
    'GF_Roof_Slab_Shutteringwork':	[3],
    'GF_Roof_Slab_Reinforcementwork':	[3],
    'Ground_Floor_Roof_Slab_Concrete': [1],
    'GF_roof_slab_deshuttering1': [1],
    'FirstFloorCloumnStarter':	[1],
    'FF_cloumn_shutteringwork':	[1],
    'FF_cloumn_reinforcementwork':	[1],
    'First_Floor_Column_Concrete': [2],
    'First_Lintel_Level_Brickwork':	[3],
    'FF_lintel_shuttering_work':	[2],
    'FF_lintel_Reinforcementwork':	[2],
    'First_Floor_Lintel_Concrete': 	[2],
    'First_Floor_Brickwork_Above_Lintel':	[3],
    'FF_Roof_slab_shutteringwork':	[2],
    'FF_roof_slab_Reinforcement':	[2],
    'First_Floor_Roof_Slab_Concrete':	[1],
    'FF_roof_slab_deshuttering':	[1],
    'Parapet_BrickWork':	[1],
    'GF_electrical_wallchasingandpipefixingworks':	[2],
    'FF_electrical_wallchasingandpipefixingworks':	[2],
    'GF_and_FF_button_mark_fixingwork':	[1],
    'GF_and_FF_foor_frame_fixingwork':	[1],
    'Interior_Plastering':	[8],
    'External_scaffoldingworks':	[2],
    'External_Plastering':	[6],
    'Internal_plumbing_work':	[4],
    'Internal_water_proffing':	[1],
    'Tiles_innerworkandGranitework':	[7],
    'Inner_wall_Painting': [1],
    'Inner_wall_Pettywork':	[2],
    'Inner_primer_work':	[5],
    'External_Whitecementandprimer':	[1],
    'Weathering_tiles':	[2],
    'External_primerwork':	[4],
    'UPuc_windowfixing':	[3],
    'External_plumingwork':	[1],
    'Door_shutter_fixingwork':	[5],
    'Electrical_wire_pullingwork':	[3],
    'Internal_Emulsionwork': 	[3],
    'External_Emulsionwork':	[5],
    'Elecrical_switchandsocketfiting':	[4],
    'Sanitaryfittings':	[2],
    'SS_handRail':	[2],
    'Ladder_fixing':	[2],
    'Setback_ExternalSeptictank':	[7],

}
aaaa=['Footing_Marking', 'Earthwork_Excavation', 'footingPCC', 'RCC_Reinforcement', 'footingRCC', 'Column_Reinforcement', 'Column_Shuttering', 'Basement_Column_Concrete', 'soil_Backfilling', 'consolidation', 'Grade_beam_EarthworkExcavation', 'Grade_Beam_PCC', 'Grade_beam_Reinforcement', 'grade_beam_shuttering', 'Grade_Beam_RCC', 'Basement_BrickWork', 'Basement_belt_beam_reinforcement', 'Basement_belt_beam_shuttering', 'Basement_Belt_Beam_RCC', 'Basement_innerwall_plastering', 'Basement_gravel_Filling', 'Basement_consolidation_work', 'Basement_floor_PCC_work', 'Ground_floor_column_starter_markingandconcrte', 'Ground_floor_column_reinforcement_work', 'Ground_column_shutteringwork', 'Ground_Floor_Column_Concrete', 'Ground_Floor_Lintel_Level_BrickWork', 'GF_lintel_Shutteringwork', 'GF_lintel_Reinforcementwork', 'Ground_Floor_lintel_Concrete', 'Ground_Floor_Brickwork_Above_lintel', 'GF_Roof_Slab_Shutteringwork', 'GF_Roof_Slab_Reinforcementwork', 'Ground_Floor_Roof_Slab_Concrete', 'GF_roof_slab_deshuttering1', 'FirstFloorCloumnStarter', 'FF_cloumn_shutteringwork', 'FF_cloumn_reinforcementwork', 'First_Floor_Column_Concrete', 'First_Lintel_Level_Brickwork', 'FF_lintel_shuttering_work', 'FF_lintel_Reinforcementwork', 'First_Floor_Lintel_Concrete', 'First_Floor_Brickwork_Above_Lintel', 'FF_Roof_slab_shutteringwork', 'FF_roof_slab_Reinforcement', 'First_Floor_Roof_Slab_Concrete', 'FF_roof_slab_deshuttering', 'Parapet_BrickWork', 'GF_electrical_wallchasingandpipefixingworks', 'FF_electrical_wallchasingandpipefixingworks', 'GF_and_FF_button_mark_fixingwork', 'GF_and_FF_foor_frame_fixingwork', 'Interior_Plastering', 'External_scaffoldingworks', 'External_Plastering', 'Internal_plumbing_work', 'Internal_water_proffing', 'Tiles_innerworkandGranitework', 'Inner_wall_Painting', 'Inner_wall_Pettywork', 'Inner_primer_work', 'External_Whitecementandprimer', 'Weathering_tiles', 'External_primerwork', 'UPuc_windowfixing', 'External_plumingwork', 'Door_shutter_fixingwork', 'Electrical_wire_pullingwork', 'Internal_Emulsionwork', 'External_Emulsionwork', 'Elecrical_switchandsocketfiting', 'Sanitaryfittings', 'SS_handRail', 'Ladder_fixing', 'Setback_ExternalSeptictank']
    
for i in range(0,len(aaaa)-1):
    
    change(ac[aaaa[i]],aaaa[i+1])
    
    
    
