"""

inter-promo project
group n°8

author: nicolas paillier

this program aims:
    - to read a json file containing the whole of relevant terms
        and their sum of term frequencies per day
    - to apply a linear regression ; ie. to calculate the coefficient and
        the intercept value of the regression line
    - to display the line plot depicting the evolution of the sum_tf
        over time ; and the regression line also
    - to define the trend (rise, drop) according to the coefficient value
    - to calculate the moving average series for each word
    - to lead statistical tests in order to determine the trend
        (increasing, decreasing) according to the p-value

"""



"""

packages

"""
import json
import scipy.stats
import numpy as np

from statsmodels.api import OLS



"""

dataset (example)

"""
#words and their sum of tf per day
data = {"trump" : [0, 1, 1, 3, 2, 4, 5, 5, 6, 8, 7, 9, 11, 10, 11, 13, 13, 15],
        "macron" : [17, 15, 14, 15, 13, 12, 10, 9, 9, 8, 8, 7, 8, 6, 5, 4, 3, 2],
        "university" : [0, 0, 2, 1, 3, 4, 5, 6, 6, 5, 4, 4, 3, 3, 2, 1, 1, 0],
        "airport" : [3, 3, 2, 3, 3, 4, 2, 2, 4, 3, 3, 3, 4, 4, 2, 3, 2, 2],
        "storm" : [5, 5, 5, 4, 5, 4, 4, 5, 5, 6, 6, 5, 5, 4, 4, 4, 5, 4],
        "tax" : [20, 18, 19, 17, 16, 16, 15, 13, 13, 12, 10, 9, 10, 8, 6, 5, 3, 2]}

data_v2 = {"parcoursup": [0, 1, 1, 3, 3, 4, 5, 7, 7, 8, 10, 9, 11, 12],
           "airport": [8, 8, 7, 6, 6, 4, 5, 3, 3, 2, 1, 1, 0, 0],
           "lactalis": [5, 3, 3, 2, 2, 1, 2, 2, 3, 3, 4, 5, 5, 6],
           "avalanche": [6, 6, 7, 6, 6, 6, 5, 6, 6, 7, 6, 6, 6, 6]}

#words and their sum of tf for two weeks (sub lists)
data_v3 = {"avalanche": [[1, 1, 2, 2, 3, 4, 3], [3, 4, 5, 5, 6, 7, 8]],
           "job": [[2, 2, 3, 2, 2, 2, 2], [1, 2, 2, 2, 3, 4, 4]],
           "lactalis": [[8, 6, 4, 5, 2, 1, 0], [3, 2, 3, 2, 1, 1, 1]]}

#write the json file
with open('H:/SID Toulouse/Projet inter-promo/code/data.json', 'w', encoding = "utf-8") as file:
    data = json.dump(data, file, indent = 4)

with open('H:/SID Toulouse/Projet inter-promo/code/data_v2.json', 'w', encoding = "utf-8") as file:
    data_v2 = json.dump(data_v2, file, indent = 4)

with open('H:/SID Toulouse/Projet inter-promo/code/data_v3.json', 'w', encoding = "utf-8") as file:
    data_v3 = json.dump(data_v3, file, indent = 4)

#read the json file
with open('H:/SID Toulouse/Projet inter-promo/code/data.json', 'r') as file:
    data = json.load(file)

with open('H:/SID Toulouse/Projet inter-promo/code/data_v2.json', 'r') as file:
    data_v2 = json.load(file)

with open('H:/SID Toulouse/Projet inter-promo/code/data_v3.json', 'r') as file:
    data_v3 = json.load(file)



"""

functions

"""
#extract keys and values from the json file
#input: json file's content
#output: two lists (keys and values)
def extract_keys_values(data):
    #initialisation of the "keys" and "values" lists
    keys = []
    values = []
    
    #for each entry in the json file
    for k, v in data.items():
        keys.append(k)
        values.append(v)
    
    return(keys, values)

#linear regression
def linear_regression(data):
    reg_coeff = []
    reg_intercept = []
    dict_linreg = {}
    
    #intercept value and coefficient calculation
    for k, v in data.items():
        mat_x = np.ones((len(v), 2))
        mat_x[:,1] = np.arange(0, len(v))
        
        reg = OLS(v, mat_x)
        results = reg.fit()
        
        reg_coeff.append(results.params[1])
        reg_intercept.append(results.params[0])
        
        dict_linreg[k] = [results.params[1], results.params[0]]
        
        #r² value
        results.rsquared

    return(dict_linreg)

#trend (increase, decrease) according to the coefficient value
#input : data (json format)
#output : trend for each word
def trend(data):
    dict_trend = {}
    dict_linreg = linear_regression(data)
    for k, v in dict_linreg.items():
        for j in range(1, len(v)):
            if v[0] > 0:
                dict_trend[k] = "rise"
            else:
                dict_trend[k] = "drop"
    return(dict_trend)

#moving_average
#input parameters : list of values, order (interger)
#output : list of values (moving average)
def moving_average(seq, order) :
    moving_avg = np.cumsum(seq, dtype = float)
    moving_avg[order:] = moving_avg[order:] - moving_avg[:-order]
    return moving_avg[order - 1:] / order

#test_trend
#this function determine the trend (rise, drop) according to the p-value
#three parameters required : data, word, id_day
#this function calculate the t-test for the means of two independant samples
#and returns the trend (increasing or decreasing)
def test_trend(data, word, id_day):
    test = scipy.stats.ttest_ind(data[word][id_day], data[word][id_day - 1])
    if (test[1] > 0.001 and test[1] < 0.05):
        if ((test[0] > 0)):
            return(word, "increasing_trend")
        elif (test[0] < 0):
            return(word, "decreasing_trend")
        else:
            return(word, "no_trend")
    elif (test[1] < 0.001):
        if ((test[0] > 0)):
            return(word, "strongly_increasing_trend")
        elif (test[0] < 0):
            return(word, "strongly_decreasing_trend")
        else:
            return(word, "no_trend")
    else:
        return(word, "no_trend")

#data preprocessing for group n°9
#input parameter : json file
#output : dict containing the trend for each word
def file_trend(data):
    output_trend = {}
    for key, value in data.items():
        if(key != 'period'):
            for val in range(1, len(value)):
                word, trend = test_trend(data, key, val)
            output_trend[key] = trend
        else:
            output_trend[key] = value

#input : data (json format)
#intermediary actions : extraction of keys and values, linear regression (functions)
#goal : to calculate the moving average for each word, to determine the trend
#output : dict with many words and their trend
def trend_with_moving_average(data_v2):
    keys, values = extract_keys_values(data_v2)
    linear_regression(data_v2)
    mavg_series = []
    dict_word_mavg = {}
    #for each word in the json file (ie. data_v2)
    for j in range(len(values)):
        mavg_series = moving_average(values[j], 3).tolist()
        splt_series = [mavg_series[0:5], mavg_series[6:11]]
        dict_word_mavg[keys[j]] = splt_series
    
    return(file_trend(dict_word_mavg))