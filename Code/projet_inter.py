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

""" Trend second version """


def test_trend2(data, word, id_day):
    '''trend'''
    test = scipy.stats.ttest_ind(data[word][id_day], data[word][id_day-1])
    if(test[1] > 0.001 and test[1] < 0.05):
        if ((test[0] > 0)):
            return(word, 'Tendance_en_hausse')
        elif (test[0] < 0):
            return(word, 'Tendance_en_baisse')
        else:
            return(word, 'Pas_de_Tendance')
    elif(test[1] < 0.001):
        if ((test[0] > 0)):
            return(word, 'Tendance_fortement_en_hausse')
        elif (test[0] < 0):
            return(word, 'Tendance_fortement_en_baisse')
        else:
            return(word, 'Pas_de_Tendance')
    else:
        return(word, 'Pas_de_tendance')


def file_trend(data):
    """ data preprocessing for groupe 9
    param : file -> json file
    return json with trend, period and most important word"""
    dict = {}
    for cle, valeur in data.items():
        if(cle != 'period'):
            for val in range(1, len(valeur)):
                word, trend = test_trend(data, cle, val)
            dict[cle] = trend
        else:
            dict[cle] = valeur
    return(dict)
""" Test  """
with open('C:/Users/samba/Groupe8_Analyse_tendance/Data/Test/jour.json', 'r') as file:
        data = json.load(file)
trend = file_trend(data)
trend




