# Proximity to bike routes and mode share

This repository contains the code used to analyse the relationshiop between distance to bikeways and bike commute mode share, using data for the Metro Vancouver Area from 2016. See Proximity to bike routes and mode share - An analysis of the Metro Vancouver Area.pdf for the full results and discussion.

Distance_to_bike_routes.py
This is the python code I used to determine the distance from residential parcels to the nearest bikeway, using ArcMap and the Network Analyst extension.
It uses a network dataset (streets), a feature class of parcel centroids, and a feature class of points generated every 50m along the bikeway network.
It outputs a feature class containing lines representing the route from each parcel point to the nearest bikeway node. This lenght of each route is then exported to a csv file.

Bikeways_Metrics.py
This code takes the distance to bikeways csv from the Distance_to_bike_routes.py file, and calculates statistics (mean, median, standard deviation. min, maz, interquartile range, and count) for each census tract.

Census_Metrics.py
This python code parses Canadian Census data (downloaded form https://www12.statcan.gc.ca/census-recensement/2016/dp-pd/prof/details/page_Download-Telecharger.cfm?Lang=E&Tab=1&Geo1=CT&Code1=9320205.00&Geo2=CMACA&Code2=932&SearchText=9320205.00&SearchType=Begins&SearchPR=01&B1=Journey%20to%20work&TABID=3&type=0), returning a table of census tracts within the Vancouver Census Metropolitan Area and metrics related to commuting.

Please feel free to use this code/methodology to run your own analyse - I'd love to see the results!
