import arcpy

input_tract_file = "C:.......file.shp"
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

arcpy.AddField_management(input_tract_file,new_field_name,field_type,"#","#","#","#","NULLABLE","NON_REQUIRED","#")
#arcpy.AddField_management(input_tract_file,new_field_name+"_int)",field_type,"#","#","#","#","NULLABLE","NON_REQUIRED","#")
arcpy.CalculateField_management(input_tract_file,new_field_name,CalcBorotoCountyExpr, "PYTHON_9.3",CalcBorotoCountyBlock)
