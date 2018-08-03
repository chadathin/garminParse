#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 20:20:12 2018

@author: Chad
"""
from math import radians, cos, sin, asin, sqrt

def getCoords(data):
    temp_array = []
    lat = []
    lon = []
    for line in data:
        if '<trkpt lat=' in line:
            line = line.strip()
            line = line.replace('<trkpt lat="','')
            line = line.replace('" lon="',':')
            line = line.replace('">','')
            temp_array = line.split(':')
            lat.append(float(temp_array[0]))
            lon.append(float(temp_array[1]))
    return lat,lon


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r

f = open('july-31-2018.gpx','r')

coords = getCoords(f)

def calcDistance(data):
    distance = 0.00
    for i in range(len(data[0])-1):
        distance += haversine(data[1][i],data[0][i],data[1][i+1],data[0][i+1])
    return distance

distance = calcDistance(coords)

#<trkpt lat="48.075926117599010467529296875" lon="-123.06351182051002979278564453125">

f.close()