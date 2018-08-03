#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 19:50:04 2018

@author: Chad
"""


class Activity(object):
  
  def __init__(self, file_name):
    self.file_name = file_name+'.gpx'
    self.time = 0
    #A helper function to pull HR data from the file and put it into a dictionary of time at intensity.
    def stress_index(file_name):
      stress_index = {1:0,2:0,3:0,4:0,5:0}
      activity = open(file_name,'r')
      for line in activity: #Iterate over each line
        
        if '<ns3:hr>' in line: #Find the HR lines
          self.time += 1
          line = line.strip() #Strip empty spaces before data
          line = line.replace('<ns3:hr>','') #Get rid of open tag
          line = line.replace('</ns3:hr>','') #get rid of close tag
          line = int(line) #Turn HR into an int
          
          #Now categorize the HR int into appropriate intensities
          if line < 151:
            stress_index[1] += 1/60
          elif line < 161:
            stress_index[2] += 2/60
          elif line < 170:
            stress_index[3] += 3/60
          elif line < 180:
            stress_index[4] += 4/60
          else:
            stress_index[5] += 5/60
      activity.close()
      
      for k in stress_index:
        stress_index[k] = round(stress_index[k],2)
      
      return stress_index
  
    def stress_score(aDict):
        stress_score = 0
        for k in aDict:
            stress_score += aDict[k]
        stress_score = round(stress_score,2)
        return stress_score
    
    
    self.stress_index = stress_index(self.file_name)
    self.stress_score = stress_score(self.stress_index)

  def get_stress_score(self):
    return self.stress_score

  def get_stress_index(self):
    return self.stress_index





#hr_array = get_hr_data('31_JUL_18.gpx')
#self.hr_data = get_hr_data(self.file_name)
'''
    #A helper function to generate a dictionary of time at intensity
    def stress_index(array):
      s_index = {1:0,2:0,3:0,4:0,5:0}
      for point in array:
        if point < 151:
          s_index[1] += 1/60
        elif point < 161:
          s_index[2] += 2/60
        elif point < 170:
          s_index[3] += 3/60
        elif point < 180:
          s_index[4] += 4/60
        else:
          s_index[5] += 5/60
      
      for k in s_index:
        s_index[k] = round(s_index[k],3)
      
      return s_index
      
      
  def set_stress_score(self):
    stress_score = 0
    for k in self.stress_index:
      stress_score += self.stress_index[k]
    self.stress_score = stress_score
    
      def get_hrs(self):
    return self.hr_data

    '''