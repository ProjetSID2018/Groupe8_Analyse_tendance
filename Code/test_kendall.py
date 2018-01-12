"""
Created on Thu Jan 11 11:02:03 2018

@author: jeremy
"""

import scipy.stats as stats
import statsmodels.stats.stattools as modele
import json


with open('serie_chrono.json', 'r') as fichier:
    data = json.load(fichier)

def kendall_semaine (data):
    
    dico = {}
    for val in data.values():
        
        for cle,valeur in val.items():
                tab_sem_1=valeur[0]
                tab_sem_2=valeur[1]
    tau,p_value=stats.kendalltau(tab_sem_1,tab_sem_2)
    dico = {"tau":tau, "p_value": p_value}
    return dico
    

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
