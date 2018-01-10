#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 20:34:49 2017

@author: FALL
"""

def test_trend(data,id_day):
    
    test = scipy.stats.ttest_ind(data[id_day],data[id_day-1] )  
    
    if(test[1] > 0.001 and test[1] < 0.05):
        if ((test[0] > 0)):
            return('Tendance en hausse')
        elif (test[0] < 0):
            return('Tendance en baisse')
        
    elif(test[1]<0.001):
        if ((test[0] > 0)):
            return('Tendance fortement en hausse')
        elif (test[0] < 0):
            return('Tendance fortement en baisse')
    else:
        return('pas de tendance')

            
# Create dictionnary
# Semaine(day0,day1,day2,day3,day4)
week1={}
week1['mot1']=[[0.5,0.6,0.53,0.688,0.248,0.634,0.02322],[0.32456,0.48,0.89,0.456,0.89123,0.2348,0.123456],[0.1, 0.7, 0.8, 0.9, 0.1, 0.2], [0.1, 0.1, 0.3, 0.4, 0.2, 0.2],[0.48,0.10,0,942,0.47,0.87,0.27,0.0094]]
week1['mot2']=[[0.125,0.46,0.653,0.88,0.248,0.34,0.322],[0.983,0.542,0.93,0.24,0.855,0.8423,0.16],[0.7, 0.9, 0.8, 0.9, 0.9, 0.9, 0.8], [0.1, 0.2, 0.5, 0.1, 0.2, 0.8, 0.5],[0.5683,0.209,0,6792,0.3,0.8,0.58,0.85]]
week1['mot3']=[[0.36,0.6,0.53,0.688,0.248,0.634,0.02322],[0.12746,0.1275,0.1276,0.176,0.785645,0.04245,0.12457],[0.1, 0.3, 0.4, 0.9, 0.9, 0.11, 0.3], [0.9, 0.9, 0.8, 0.9, 0.9, 0.8, 0.7],[0.891,0.001,0,123,0.666,0.999,0.452,0.104,0.1932,0.479,0,203]]
week1['mot4']=[[0.536,0.96,0.153,0.4688,0.5248,0.34,0.102322],[0.12445,0.496,0.569,0.3365,0.368480,0.02234,0.5322],[0.7, 0.8, 0.8, 0.1, 0.5, 0.5, 0.8], [0.7, 0.8, 0.8, 0.1, 0.5, 0.5, 0.8],[0.349,0.129,0,479,0.382,0.2018,0.193]]
week1['mot5']=[[0.736,0.346,0.153,0.766,0.058,0.4,0.22],[0.3564736,0.235346,0.465153,0.36766,0.01558,0.2654,0.252],[0.9, 0.5, 0.7, 0.8, 0.6, 0.9, 0.6, 0.7], [0.9, 0.9, 0.7, 0.8, 0.6, 0.9, 0.9, 0.9],[0.45,0.0018,0,72,0.827,0.234,0.1034,0.93,0.8157,0.9127]]
