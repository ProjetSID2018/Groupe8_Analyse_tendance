# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 15:55:43 2018

@author: valentin
@groupe : 8
"""
import scipy
import statsmodels.api as sm
from statsmodels.tsa.stattools import acf


data_add = {"mot": [10, 11, 15, 12, 13, 18, 15, 10, 11, 15, 12, 13, 18, 15]}
data_mult = [10, 11, 15, 12, 13, 18, 15, 100, 110, 150, 120, 130, 180, 150]
data_add2 = [10, 11, 15, 12, 13, 18, 15, 10, 11, 15, 12, 13, 18, 15]
data_mult = {
    "mot1": [
        10,
        11,
        15,
        12,
        13,
        18,
        15,
        100,
        110,
        150,
        120,
        130,
        180,
        150,
        15,
        14,
        15,
        14,
        18,
        19,
        20,
        205,
        260,
        280,
        14,
        18,
        16,
        14,
        25,
        28,
        31,
        10,
        11,
        15,
        12,
        13,
        18,
        15,
        100,
        110,
        150,
        120,
        130,
        180,
        150,
        15,
        14,
        15,
        14,
        18,
        19,
        20,
        205,
        260,
        280,
        14,
        18,
        16,
        14,
        25,
        28,
        31]}
data_test = [
    10,
    11,
    15,
    12,
    13,
    18,
    15,
    100,
    110,
    150,
    120,
    130,
    180,
    150,
    15,
    14,
    15,
    14,
    18,
    19,
    20,
    205,
    260,
    280,
    14,
    18,
    16,
    14,
    25,
    28,
    31,
    10,
    11,
    15,
    12,
    13,
    18,
    15,
    100,
    110,
    150,
    120,
    130,
    180,
    150,
    15,
    14,
    15,
    14,
    18,
    19,
    20,
    205,
    260,
    280,
    14,
    18,
    16,
    14,
    25,
    28,
    31]
data_mult2 = {
    "mot1": [
        10,
        11,
        15,
        12,
        13,
        18,
        15,
        100,
        110,
        150,
        120,
        130,
        180,
        150,
        15,
        14,
        15,
        14,
        18,
        19,
        20,
        205,
        260,
        280,
        14,
        18,
        16,
        14,
        25,
        28,
        31,
        100,
        110,
        150,
        120,
        130,
        180,
        150,
        1000,
        1100,
        1500,
        1200,
        1300,
        1800,
        1500,
        150,
        140,
        150,
        140,
        180,
        190,
        200,
        2050,
        2600,
        2800,
        140,
        180,
        160,
        140,
        250,
        280,
        310]}

res = sm.tsa.seasonal_decompose(data_test, freq=31,
                                model='multiplicative')

res.residual


def trend_by_period(data, interest_period):
    '''To get the trend of time series
    param : data -> dictionary of list of values (tf values)
    in chronological order by word
    interest_period -> integer, number of day by period
    7 for week, 31 for month
    period : month, week. Use to add residual values
    return list of dictionary wich contains trend and word
    '''

    # first step : check if the model is addive or multiplicative
    for key, val in data.items():
        values_serie = val
        word = key
    res_additive = sm.tsa.seasonal_decompose(
        values_serie, freq=interest_period, model='additive')
    res_multiplicative = sm.tsa.seasonal_decompose(
        values_serie, freq=interest_period, model='multiplicative')
    # recover residual by model
    if interest_period == 7:
        residual_additive = res_additive.resid[3:11]
        residual_multiplicative = res_multiplicative.resid[3:11]
        # check autocorrelation of the residual by model
        cor_add = acf(residual_additive)
        cor_mult = acf(residual_multiplicative)
        if sum(residual_additive) > 0:
            if sum(cor_add**2) >= sum(cor_mult**2):
                print('additive')
                sum(cor_add**2)
                trend_values = {
                    word: [res_additive.trend[3:6], res_additive.trend[7:10]]}
                test_trend = file_trend(trend_values)
                print(trend_values)
            else:
                print('mult')
                sum(cor_mult**2)
                trend_values = {
                    word: [res_multiplicative.trend[3:6], res_multiplicative.trend[7:10]]}
                test_trend = file_trend(trend_values)
                print(trend_values)
        else:
            test_trend = {word: 'Pas_de_Tendance'}
    else:
        residual_additive = res_additive.resid[15:46]
        residual_multiplicative = res_multiplicative.resid[15:46]
        if sum(residual_additive) > 0:
            cor_add = acf(residual_additive)
            cor_mult = acf(residual_multiplicative)
            if sum(cor_add**2) >= sum(cor_mult**2):
                print('additive')
                print(residual_additive)
                trend_values = {
                    word: [res_additive.trend[15:31], res_additive.trend[32:47]]}
                test_trend = file_trend(trend_values)
            else:
                print('mult')
                trend_values = {
                    word: [res_multiplicative.trend[15:31], res_multiplicative.trend[32:47]]}
                test_trend = file_trend(trend_values)
        else:
            test_trend = {word: 'Pas_de_Tendance'}
    return test_trend


def test_trend(data, word, id_day):
    '''trend
    This function has three parameters :
    data : json data
    word : words to analyse
    id_day :  day to analyse
    This function calculate the T-test for the means of two independent samples and returns the conclusion of the test
        '''
    test = scipy.stats.ttest_ind(data[word][id_day], data[word][id_day - 1])
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


trend = res.trend
resplot = res.plot()
