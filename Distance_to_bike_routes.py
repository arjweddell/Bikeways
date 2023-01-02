# Script Name: Distance_to_bike_routes.py
#
# Author: Angie Weddell
#
# This python script is used for completeing multiple closest
# facility analyses, with one set of points used for the facilities
# and an unlimited set of points used for incidents. Routes for each set
# of points are saved to a feature class, and then exported as csv files.
#
# Arguments: Input:  network dataset
#                    facilities feature class (points)
#                    any number of incients feature classes (points)
#            Output: routes feature class for each incident feature class (lines)
#                    routes csv for each incident feature class         
#
# Created: November 2020
# Designed to work with Python 3.6 and ArcGIS Desktop Ver. 10.8

# Import libraries, check out Network Analyst, and set workspace

import os
import sys
import arcpy
from arcpy import env
arcpy.CheckOutExtension("Network")
env.workspace = "Z:\Scratch\Scratch.gdb"
env.overwriteOutput = True

# Set up closest facility layer

inNetworkDataset = "Roads\Roads_ND" #Name of your network dataset
outNALayerName = "Test" #Name of output layer
impedanceAttribute = "Length" #attribute used to determine shortest path, here we use distance
inFacilities = "Bike_Routes_All_Points_50m" #input facilities (end points) layer
NAResultObject = arcpy.na.MakeClosestFacilityLayer(inNetworkDataset,outNALayerName,impedanceAttribute,"TRAVEL_TO")
outNALayer = NAResultObject.getOutput(0)
subLayerNames = arcpy.na.GetNAClassNames(outNALayer)
facilitiesLayerName = subLayerNames["Facilities"]
incidentsLayerName = subLayerNames["Incidents"]
arcpy.na.AddLocations(outNALayer, facilitiesLayerName, inFacilities, "", "")

# Iterate through incident feature classes

routesLayerName = subLayerNames["CFRoutes"]
points = arcpy.ListFeatureClasses(feature_dataset="Parcel_Points") #feature dataset containing incident (start) points 

for fc in points:
    inIncidents = fc
    arcpy.na.AddLocations(outNALayer, incidentsLayerName, inIncidents, append = "CLEAR")
    arcpy.na.Solve(outNALayer)
    routes_name = os.path.join(fc + "_All")
    arcpy.CopyFeatures_management(routesLayerName, routes_name)

# Export routes as csv

routes = (arcpy.ListFeatureClasses("T933*")) #list all output features
for fc in routes:
    inTable = fc
    outLoc = "Z:\Scratch"
    outTable = os.path.join(fc + "_table.csv")
    arcpy.TableToTable_conversion(inTable,outLoc,outTable)
