#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 13:27:50 2018

@author: FALL
"""

import json
import scipy

def test_trend(Path, word, id_day):
    ''' Read file'''
    week_day = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
    with open(Path, 'r') as file:
        data = json.load(file)
        
    '''trend'''
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
        
