# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 08:47:19 2018
@author: samba
@Revised by: AïchaAminata

"""
import scipy
import json

def test_trend(Path, word, id_day):
    '''trend'''
    week_day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    with open(Path, 'r') as file:
        data = json.load(file)
    test = scipy.stats.ttest_ind(data[word][id_day], data[word][id_day-1])
    if(test[1] > 0.001 and test[1] < 0.05):
        if ((test[0] > 0)):
            return(word, 'Increasing trend', week_day[id_day])
        elif (test[0] < 0):
            return(word, 'Decreasing trend', week_day[id_day])
        else:
            return(word, 'No Trend', week_day[id_day])
    elif(test[1] < 0.001):
        if ((test[0] > 0)):
            return(word, 'Strongly increasing trend', week_day[id_day])
        elif (test[0] < 0):
            return(word, 'Strongly decreasing trend', week_day[id_day])
        else:
            return(word, 'No Trend', week_day[id_day])
    else:
        return(word, 'No Trend', week_day[id_day])
        
test_trend('C:/Users/samba/Desktop/info sid/M2/week1json.json', 'mot2', 3)

""" Trend second version """


def test_trend2(data, word, id_day):
    '''trend'''
    test = scipy.stats.ttest_ind(data[word][id_day], data[word][id_day-1])
    if(test[1] > 0.001 and test[1] < 0.05):
        if ((test[0] > 0)):
            return(word, 'Increasing trend')
        elif (test[0] < 0):
            return(word, 'Decreasing trend')
        else:
            return(word, 'No Trend')
    elif(test[1] < 0.001):
        if ((test[0] > 0)):
            return(word, 'Strongly increasing trend')
        elif (test[0] < 0):
            return(word, 'Strongly decreasing trend')
        else:
            return(word, 'No Trend')
    else:
        return(word, 'No Trend')


def file_trend(data):
    """ data preprocessing for groupe 9
    param : file -> json file
    return json with trend, period and most important word"""
    dict = {}
    for cle, value in data.items():
        if(cle != 'period'):
            for val in range(1, len(value)):
                word, trend = test_trend(data, cle, val)
            dict[cle] = trend
        else:
            dict[cle] = value
    return(dict)
""" Test  """
with open('C:/Users/samba/Groupe8_Analyse_tendance/Data/Test/jour.json', 'r') as file:
        data = json.load(file)
trend = file_trend(data)
trend



