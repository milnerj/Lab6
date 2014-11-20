# Created by: Jacob Milner
# Assignment: TGIS 501A - Lab 6 - Part 1
# Purpose: use turtles to generate points, import points as a polygon into ArcGIS
# Input: User Input (sides, length)
# Output: Results/turtle_poly.shp

import arcpy
import fileinput
import string
import os
import turtle
from arcpy import env
env.workspace = "C:/Users/Jacob/Desktop/EsriPress/Python/Data/Exercise08"
env.overwriteOutput = True
env.SpatialReference("WGS1984")
sides = int(raw_input("How many sides should the polygon have? "))
length = int(raw_input("What length should the sides be? "))
window = turtle.Screen()
Burt = turtle.Turtle()
degrees = (180 - (180*(sides-2)/sides))
ptlist = []
for side in range(sides):
	Burt.forward(length)
	Burt.left(degrees)
	ptlist.append(Burt.pos())
outpath = "C:/Users/Jacob/Desktop/EsriPress/Python/Data/Exercise08"
newfc = "Results/turtle_poly.shp"
sr = arcpy.SpatialReference("C:/Users/Jacob/Desktop/EsriPress/Python/Data/Results/4326.prj")
arcpy.management.CreateFeatureclass(outpath, newfc, "Polygon", "", "", "", sr)
cursor = arcpy.da.InsertCursor(newfc, ["SHAPE@"])
array = arcpy.Array()
for x, y in ptlist:
	pt = arcpy.Point(x,y)
	array.append(pt)
poly = arcpy.Polygon(array)
cursor.InsertRow([poly])
del cursor