# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 08:47:19 2018

@author: samba
"""
import scipy
import pandas
import sklearn
import numpy as np
import math
import nltk

#exemple mot
xmot1 = [0.1, 0.7, 0.8, 0.9, 0.1, 0.2]
xmot2 = [0.7, 0.9, 0.8, 0.9, 0.9]
ymot1 = [0.1, 0.1, 0.1, 0.9, 0.1, 0.2]
ymot2 = [0.7, 0.9, 0.8, 0.9, 0.9]
mot2


def tendance(mot1, mot2):
    test = scipy.stats.ttest_ind(mot1, mot2)
    if(test[1] < 0.05 and test[1] > 0.001): 
        if ((test[0] > 0)):
            return('Tendance en hausse')
        elif (test[0] < 0):
            return('Tendance en baisse')
    elif(test[1] < 0.001):
        if ((test[0] > 0)):
            return('Tendance fortemnt en hausse')
        elif (test[0] < 0):
            return('Tendance frotement en baisse')
    else:
        return('pas de tendance')
            
tendance(xmot1, xmot1)
tendance(ymot1, ymot2)       

from pprint import pprint

import json


json_data=open('C:/Users/samba/Desktop/info sid/M2/Projet_Inter/projet/futurasciences/artfusc22018-01-08_robot.json')
data = json.load(json_data)

week1={}
week1['mot1']=[[0.1, 0.7, 0.8, 0.9, 0.1, 0.2], [0.1, 0.1, 0.3, 0.4, 0.2, 0.2]]
week1['mot2']=[[0.7, 0.9, 0.8, 0.9, 0.9,0.9,0.8], [0.1, 0.2, 0.5, 0.1, 0.2,0.8,0.5]]
week1['mot3']=[[0.1, 0.3, 0.4, 0.9, 0.9,0.11,0.3], [0.9, 0.9, 0.8, 0.9, 0.9,0.8,0.7]]
week1['mot4']=[[0.7, 0.8, 0.8, 0.1, 0.5,0.5,0.8], [0.7, 0.8, 0.8, 0.1, 0.5,0.5,0.8]]
week1['mot5']=[[0.9, 0.5, 0.7, 0.8, 0.6,0.9,0.6,0.7], [0.9, 0.9, 0.7, 0.8, 0.6,0.9,0.9,0.9]]
week1['mot1'][0]

tendance(week1['mot1'][1],week1['mot1'][0])
tendance(week1['mot2'][1],week1['mot2'][0])

