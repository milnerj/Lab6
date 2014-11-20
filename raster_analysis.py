# Created by: Jacob Milner
# Assignment: TGIS 501A - Lab 6 - Part 2 - Exercise 9, Challenge Exercise 1
# Purpose: determine which areas in a raster meet specified slope, aspect, and forested conditions
# Input: landcover.tif
# Output: ex01.tif

import arcpy
from arcpy import env
from arcpy.sa import env.workspace = "C/Users/Jacob/Desktop/EsriPress/Python/Data/Exercise09"
env.overwriteOutput = True
if arcpy.CheckExtension("spatial") == "Available":
	arcpy.CheckOutExtension("spatial")
	elev = arcpy.Raster("elevation")
	land = arcpy.Raster("landcover.tif")
	slope = Slope(elev)
	aspect = Aspect(elev)
	sloperange = ((slope > 5) & (slope < 20))
	aspectrange = ((aspect >150) & (aspect < 270))
	forest = ((land == 41) | (land == 42) | (land == 43))
	outraster = (sloperange & aspectrange & forest)
	outraster.save("C/Users/Jacob/Desktop/EsriPress/Python/Data/Exercise09/Results/ex01")
	arcpy.CheckInExtension("spatial")
else:
	print = "Spatial Analyst license is not available.  Sad."