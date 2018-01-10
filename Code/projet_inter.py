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
import json


def test_trend(Path, word, id_day):
    '''trend'''
    week_day = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
    with open(Path, 'r') as file:
        data = json.load(file)
    test = scipy.stats.ttest_ind(data[word][id_day], data[word][id_day-1])
    if(test[1] > 0.001 and test[1] < 0.05):
        if ((test[0] > 0)):
            return(word, 'Tendance en hausse', week_day[id_day])
        elif (test[0] < 0):
            return(word, 'Tendance en baisse', week_day[id_day])
        else:
            return(word, 'Pas de Tendance', week_day[id_day])
    elif(test[1] < 0.001):
        if ((test[0] > 0)):
            return(word, 'Tendance fortement en hausse', week_day[id_day])
        elif (test[0] < 0):
            return(word, 'Tendance fortement en baisse', week_day[id_day])
        else:
            return(word, 'Pas deTendance', week_day[id_day])
    else:
        return(word, 'pas de tendance', week_day[id_day])
        
test_trend('C:/Users/samba/Desktop/info sid/M2/week1json.json', 'mot2', 3)
