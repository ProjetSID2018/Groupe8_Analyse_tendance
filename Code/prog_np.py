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
        over time ; and the regression line
    - to define the trend (rise, drop) according to the coefficient value
    - (...)

"""

#packages
import json
import scipy.stats
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.stats.stattools

from statsmodels.api import OLS
from statsmodels.graphics.regressionplots import abline_plot

#dataset (example)
#words and their sum of tf per day
data = {"trump" : [0, 1, 1, 3, 2, 4, 5, 5, 6, 8, 7, 9, 11, 10, 11, 13, 13, 15],
        "macron" : [17, 15, 14, 15, 13, 12, 10, 9, 9, 8, 8, 7, 8, 6, 5, 4, 3, 2],
        "university" : [0, 0, 2, 1, 3, 4, 5, 6, 6, 5, 4, 4, 3, 3, 2, 1, 1, 0],
        "airport" : [3, 3, 2, 3, 3, 4, 2, 2, 4, 3, 3, 3, 4, 4, 2, 3, 2, 2],
        "storm" : [5, 5, 5, 4, 5, 4, 4, 5, 5, 6, 6, 5, 5, 4, 4, 4, 5, 4],
        "tax" : [20, 18, 19, 17, 16, 16, 15, 13, 13, 12, 10, 9, 10, 8, 6, 5, 3, 2]}

#write the json file
with open('H:/SID Toulouse/Projet inter-promo/code/data.json', 'w', encoding = "utf-8") as file:
    data = json.dump(data, file, indent = 4)

#read the json file
with open('H:/SID Toulouse/Projet inter-promo/code/data.json', 'r') as file:
    data = json.load(file)

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

keys, values = extract_keys_values(data)

#line plot depicting the sum of tf per day for each word
for i in range(len(data)):
    print(keys[i])
    plt.plot(values[i], color = 'r', lw = 2)
    plt.figure()

#multiple lines (all words existing in the json file)
plt.plot(np.transpose(values))

#linear regression
def linear_regression(data):
    reg_coeff = []
    reg_intercept = []
    dict_linreg = {}
    
    #intercept value and coefficient calculation
    #addition of the regression line on the plot
    for k, v in data.items():
        mat_x = np.ones((len(v), 2))
        mat_x[:,1] = np.arange(0, len(v))
        
        reg = OLS(v, mat_x)
        results = reg.fit()
        
        reg_coeff.append(results.params[1])
        reg_intercept.append(results.params[0])
        
        dict_linreg[k] = [results.params[1], results.params[0]]
        
        fig = abline_plot(model_results = results, color = 'r', lw = 2)
        
        reg_plot = fig.axes[0]
        reg_plot.plot(mat_x[:,1], v, color = 'b')
        reg_plot.margins(.1)
        
        #results.summary()
        
        print("r² :")
        print(results.rsquared)

    return(dict_linreg)

dict_linreg = linear_regression(data)
dict_linreg

#trend (increase, decrease) according to the coefficient value
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

#trend(data)



def moving_average(seq, order) :
    moving_avg = np.cumsum(seq, dtype = float)
    moving_avg[order:] = moving_avg[order:] - moving_avg[:-order]
    return moving_avg[order - 1:] / order

data_v2 = {"parcoursup": [0, 1, 1, 3, 3, 4, 5, 7, 7, 8, 10, 9, 11, 12],
           "airport": [8, 8, 7, 6, 6, 4, 5, 3, 3, 2, 1, 1, 0, 0],
           "lactalis": [5, 3, 3, 2, 2, 1, 2, 2, 3, 3, 4, 5, 5, 6],
           "avalanche": [6, 6, 7, 6, 6, 6, 5, 6, 6, 7, 6, 6, 6, 6]}

keys, values = extract_keys_values(data_v2)
linear_regression(data_v2)
mavg_series = []
for j in range(len(values)):
    test = []
    mavg_series.append(moving_average(values[j], 3))
    splt_series = [mavg_series[j][0:5], mavg_series[j][6:11]]
    test = scipy.stats.ttest_ind(splt_series[1], splt_series[0])
    print("")
    print("word :")
    print(keys[j])
    print("p-value :")
    print(test[1])



"""

(...)

"""

#test de durbin-watson
#(...)

def durbin_watson_test(data):
    residuals = OLS(data, np.ones(len(data))).fit()
    return statsmodels.stats.stattools.durbin_watson(residuals.resid)

print("durbin_watson of range = %f" %durbin_watson_test(np.arange(2000)))
print("durbin_watson of rand = %f" %durbin_watson_test(np.random.randn(2000)))



"""

(...)

"""

#dataset (example)
#words and their sum of tf for two weeks (sub lists)
data_v3 = {"avalanche": [[1, 1, 2, 2, 3, 4, 3], [3, 4, 5, 5, 6, 7, 8]],
           "job": [[2, 2, 3, 2, 2, 2, 2], [1, 2, 2, 2, 3, 4, 4]],
           "lactalis": [[8, 6, 4, 5, 2, 1, 0], [3, 2, 3, 2, 1, 1, 1]]}

#write the json file
with open('H:/SID Toulouse/Projet inter-promo/code/data_v2.json', 'w', encoding = "utf-8") as file:
    data_v3 = json.dump(data_v3, file, indent = 4)

#read the json file
with open('H:/SID Toulouse/Projet inter-promo/code/data_v2.json', 'r') as file:
    data_v3 = json.load(file)

#kendall test
def kendall_test_week(data_v3):
    keys_v3 = []
    dict_kendall_test = {}

    for k, v in data_v3.items():
        keys_v3.append(k)
        week_1 = v[0]
        week_2 = v[1]
    
    for i in range(len(data_v3)):
        tau, p_val = scipy.stats.kandalltau(week_1, week_2)
        dict_kendall_test = {"tau": tau, "p-value": p_val}
        
    return(dict_kendall_test)