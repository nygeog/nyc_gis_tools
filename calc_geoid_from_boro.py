import arcpy

print 'create and calc geoid for nyc dcp census 2010 tract and block'
input_tract_file = "C:.......tract_file.shp"
new_field_name = "geoid"
field_type = "TEXT"

CalcBorotoCountyExpr  = "boroCountyFIPS(int(!BoroCode!), !CT2010!)"
CalcBorotoCountyBlock = """def boroCountyFIPS(boro,tract):
  st = '36'
  if boro == 1:
    return st + '061' + tract
  elif boro == 2:
    return st + '005' + tract
  elif boro == 3:
    return st + '047' + tract
  elif boro == 4:
    return st + '081' + tract
  elif boro == 5:
    return st + '085' + tract
  else:
    return 'X' + tract """

print 'add field and calc - tract geoid'
arcpy.AddField_management(input_tract_file,new_field_name,field_type,"#","#","#","#","NULLABLE","NON_REQUIRED","#")
#arcpy.AddField_management(input_tract_file,new_field_name+"_int)",field_type,"#","#","#","#","NULLABLE","NON_REQUIRED","#")
arcpy.CalculateField_management(input_tract_file,new_field_name,CalcBorotoCountyExpr, "PYTHON_9.3",CalcBorotoCountyBlock)

print 'create and calc geoid for nyc dcp census 2010 block'
input_block_file = "C:.......block_file.shp"
new_field_name = "geoid"
field_type = "TEXT"

CalcBorotoCountyExpr  = "boroCountyFIPS(int(!BoroCode!), !CT2010!, !CB2010!)"
CalcBorotoCountyBlock = """def boroCountyFIPS(boro,tract, block):
  st = '36'
  if boro == 1:
    return st + '061' + tract + block
  elif boro == 2:
    return st + '005' + tract + block
  elif boro == 3:
    return st + '047' + tract + block
  elif boro == 4:
    return st + '081' + tract + block
  elif boro == 5:
    return st + '085' + tract + block
  else:
    return 'X' + tract + block"""
    
print 'add field and calc - block geoid'
arcpy.AddField_management(input_block_file,new_field_name,field_type,"#","#","#","#","NULLABLE","NON_REQUIRED","#")
arcpy.CalculateField_management(input_block_file,new_field_name,CalcBorotoCountyExpr, "PYTHON_9.3",CalcBorotoCountyBlock)
