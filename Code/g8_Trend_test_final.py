# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 13:29:08 2018

@author: samba
"""
""" Trend second version """
import scipy
import json


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


def file_trend(file):
    """ data preprocessing for groupe 9
    param : file -> json file
    return json with trend, period and most important word"""
    with open(file, 'r') as file:
        data = json.load(file)
    dict = {}
    for cle, valeur in data.items():
        if(cle != 'period'):
            for val in range(1,len(valeur)):
                word, trend = test_trend2(data, cle, val)                
            dict[cle] = trend
        else:
            dict[cle] = valeur
    return(dict)
""" Test  """
trend = file_trend('C:/Users/samba/Groupe8_Analyse_tendance/Data/Test/jour.json')
trend
