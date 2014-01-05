nyc_gis_tools
=============

assortment of gis scripts specific to nyc data

calc_geoid_from_boro.py 
  This tool takes NYC DCP Block and Tract data and generates a GEOID to match US Census GEOIDs for joining (merging) Census data. The DCP data has a boro - tract or boro tract+block coding so this uses the boro to add the proper county FIPS - the data resides here: http://www.nyc.gov/html/dcp/html/bytes/districts_download_metadata.shtml
