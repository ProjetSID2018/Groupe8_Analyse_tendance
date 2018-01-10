# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 10:29:31 2018

@author: Nicolas
"""
import json

'''
V1.1 : Nicolas Brouté
V1.2 : Nicolas Brouté, modification : delete one loop to run JSON File 
V1.3 : add condition on key of a dictionnary
V1.4 : add round at the agregate
'''

# Reading data 
with open('jour.json', 'r') as file:
    file = json.load(file)
           
def result_day (file):
    '''
Function calcultate sum of TF by word and by day
Function have one parameter : 
    file : JSON file
It returns dictionnary with word and sum of occurency by day
''' 
    result={}
    agregate=0
    result_day=[]
   
    #sum TF  by word
    for key,val in file.items():
        if (key == "period") :
            result[key]=file.get(key)
        else :
            for index1 in range (0,len(val)):
                for index2 in range (0,len(val[index1])):
                    agregate=round(agregate + val[index1][index2],2)
                result_day.append(agregate)
                agregate=0
            result[key]=result_day
            result_day=[]
    return(result)

print(result_day(file))




    



        
        
        
        
