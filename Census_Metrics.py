# Script Name: Calc_Metrics
#
# Author: Angie Weddell
#
# This script calculates various metrics given census data
#
# Arguments: Input: table to be modified
#             Output: same as input, doesn't need to be specified in code          
#
#
# Created: October 2020
# Designed to work with Python 3.6 and ArcGIS Pro Ver. 2.4

#Import arcpy and Python libraries

import arcpy, sys, os

# Get data table from argument

census_table = sys.argv[1]

#create and calculate car mode share

rows = arcpy.UpdateCursor( census_table, "Suppressed IS NULL" )

arcpy.AddField_management( census_table, "Car_Share", "Double" )

for row in rows:
   total = row.Question_ID1931 + row.Question_ID1932 + row.Question_ID1933 + row.Question_ID1934 + row.Question_ID1935 + row.Question_ID1936
   row.Car_Share = (row.Question_ID1931 + row.Question_ID1932)/total
   rows.updateRow(row)

#create and calculate transit mode share

rows = arcpy.UpdateCursor( census_table, "Suppressed IS NULL" )

arcpy.AddField_management( census_table, "Transit_Share", "Double" )

for row in rows:
   total = row.Question_ID1931 + row.Question_ID1932 + row.Question_ID1933 + row.Question_ID1934 + row.Question_ID1935 + row.Question_ID1936
   row.Transit_Share = row.Question_ID1933/total
   rows.updateRow(row)

#create and calculate walk mode share

rows = arcpy.UpdateCursor( census_table, "Suppressed IS NULL" )

arcpy.AddField_management( census_table, "Walk_Share", "Double" )

for row in rows:
   total = row.Question_ID1931 + row.Question_ID1932 + row.Question_ID1933 + row.Question_ID1934 + row.Question_ID1935 + row.Question_ID1936
   row.Walk_Share = row.Question_ID1934/total
   rows.updateRow(row)

#create and calculate bike mode share

rows = arcpy.UpdateCursor( census_table, "Suppressed IS NULL" )

arcpy.AddField_management( census_table, "Bike_Share", "Double" )

for row in rows:
   total = row.Question_ID1931 + row.Question_ID1932 + row.Question_ID1933 + row.Question_ID1934 + row.Question_ID1935 + row.Question_ID1936
   row.Bike_Share = row.Question_ID1935/total
   rows.updateRow(row)

#create and calculate other mode share

rows = arcpy.UpdateCursor( census_table, "Suppressed IS NULL" )

arcpy.AddField_management( census_table, "Other_Share", "Double" )

for row in rows:
   total = row.Question_ID1931 + row.Question_ID1932 + row.Question_ID1933 + row.Question_ID1934 + row.Question_ID1935 + row.Question_ID1936
   row.Other_Share = row.Question_ID1936/total
   rows.updateRow(row)

