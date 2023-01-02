# Bikeways
Distance to Bikeways

This is the python code I used to determine the distance from residential parcels to the nearest bikeway, using Network Analyst and ArcMap.
It uses a network dataset (streets), a feature class of parcel centroids, and a feature class of points generated every 50m along the bikeway network.
It outputs a feature class containing lines representing the route from each parcel point to the nearest bikeway node. This lenght of each route is then exported to a csv file.
