# Created by: Jacob Milner
# Assignment: TGIS 501A - Lab 6 - Part 2 - Exercise 9, Challenge Exercise 2
# Purpose: copies all rasters in a workspace to a new file gdb
# Input: raster list in workspace
# Output: rasters.gdb

import arcpy
from arcpy import env
file_path = "C:/Users/Jacob/Desktop/EsriPress/Python/Data/Exercise09"
env.workspace = file_path
env.overwriteOutput = True
rastlist = arcpy.ListRasters()
arcpy.management.CreatePersonalGDB(file_path + "/Results", "rasters.gdb")
for raster in rastlist:
	desc = arcpy.Describe(raster)
	name = desc.baseName
	outraster = file_path + "/Results/rasters.gdb/" + name
	arcpy.CopyRaster_management(raster, outraster)
print "Finito!"