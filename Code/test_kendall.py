"""
Created on Thu Jan 11 11:02:03 2018

@author: jeremy
"""

import scipy.stats as stats
import statsmodels.stats.stattools as modele
import json
import numpy as np
import matplotlib.pyplot as plt

with open('serie_chrono.json', 'r') as fichier:
    data = json.load(fichier)
""" lire data_tmp.json"""
with open('C:/Users/samba/Desktop/info sid/M2/score_test.json', 'r') as file:
        data = json.load(file)
len(data['Trump'])

data2={'Trump': [7,1,1,1,5,0,3,1,20,15,18,19,12,13,15]}
len(data2['Trump'])
def kendall_week(data):
    dico = {}
    for key, val in data.items():
        week_1 = val[0:7]
        week_2 = val[7:14]
        tau, p_value = stats.kendalltau(week_1, week_2)
        print(p_value)
        if (p_value < 0.05 and tau < 0):
            dico[key] = "drop"
        elif (p_value < 0.05 and tau > 0):
            dico[key] = "rise"
        else:
            dico[key] = "no_trend"
    return dico
kendall_week(data2)
stats.linregress(data2['Trump'][0:7], data2['Trump'][7:14])
plt.plot(data2['Trump'][0:7])
plt.plot(data2['Trump'][7:14])
x = np.random.random ( 10 ) 
y = np .random.random ( 10 ) 
pente ,ordonne, r_value , p_value , std_err = stats.linregress ( x ,  y )
plt . plot ( x ,  y )
'''tableau_p_value=kendall_semaine(data)
print ("tableau des tau :")
print (tableau_tau)
print ("tableau des p_values : ")
print (tableau_p_value)'''


def kendall_mois (data):
    dico = {}
    for val in data.values():
        
        for cle,valeur in val.items():
                tab_mois_1=valeur[0]
                tab_mois_2=valeur[1]
    tau,p_value=stats.kendalltau(tab_mois_1,tab_mois_2)
    dico = {"tau":tau, "p_value": p_value}
    return dico
    
    
'''def kendall_s (x,y):
    
    dico = {}
    
    tab_sem_1=x
    tab_sem_2=y
    tau,p_value=stats.kendalltau(tab_sem_1,tab_sem_2)
    dico = {"tau":tau, "p_value": p_value}
    return dico

tableau_p_value=kendall_semaine(data)
print ("tableau des tau :")
print (tableau_tau)
print ("tableau des p_values : ")
print (tableau_p_value)

x1 = [12, 2, 1, 12, 2]
x2 = [1, 4, 7, 1, 0]
tableau_x=kendall_s(x1,x2)

t1=[3.1101,4.1008,4.7876,7.0677,6.0858,4.9309,4.0449,3.0101,5.9495,6.8729,1.0898,1.9868,2.9853,10.0080,8.9052,8.0411,2.0826,1.0536,9.0649,10.0826]
t2=[0.8970,2.049,3.0307,4.0135,5.0515,6.0261,6.9059,7.9838,8.9854,9.9468,11.1682,11.9124,12.8516,13.9288,14.8826,15.9808,16.9726,18.1530,18.9751,19.8936]
d=kendall_s (t1,t2)'''
x1=[1,8,4,6,5,3]
x2=[2,6,11,2,3,6]

x=modele.durbin_watson(x2+x1+x2)
print (x)
