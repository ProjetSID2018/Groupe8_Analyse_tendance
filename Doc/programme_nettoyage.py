# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 16:25:39 2018

@author: Nicolas
"""
import nltk
import scipy.stats
import json
from nltk.tokenize import sent_tokenize, word_tokenize



######### Nettoyage d'article

def nettoyage (texte):
    contenu=texte.split(" ")
    liste_indesirable=["«","»","les","pas","dans","or","une","ni","un",",","car","a","je","tu","de","en","la","le","qui","que","à","est","et","l'","au","des"]
    for element in liste_indesirable:
        contenu=[i for i in contenu if i != element] #garder les mots différents des indésirables
    return (contenu)

def compter_mot (texte):
    texte=nettoyage(texte)
    dict = {}
    for mot in texte:
        if mot in dict:
            dict[mot] = dict[mot] + 1
        else:
            dict[mot] = 1
    return dict


#######

def recuperation(article):
    
    for cle in article:
        if cle=="content":
            contenu=article[cle]
           
    return(sorted(compter_mot(contenu).items(),reverse=True, key=lambda t: t[1]))


#lire les articles disponibles
with open('fichier/arttera4262018-01-08_robot.json', 'r', encoding="utf-8") as fichier:
     data = json.load(fichier)
#print(data)

print(recuperation(data))



######### Récuperer données des JSONS

# Reading data 
with open('data.json', 'r') as fichier:
     data = json.load(fichier)
print(data)

     
#annalyse de tendance :
def tendance (fichier):
    tendance=[]
    for valeur in fichier.values():
        for val in valeur.values():
            tendance.append(val) #ajouter les valeurs du mot dans une liste tendance
    test=scipy.stats.ttest_ind(tendance[0],tendance[1],equal_var=True) 
    
    if test[0]<0 and test[1]<0.05 :
        return("tendance significativement en baisse")
    else: 
        return("tendance en baisse non significative")
        
    if  test[0] > 0 and test[1]<0.05 :
        return ("tendance significativement en baisse")
    else :
        return("tendance en baisse non significative") 

print(tendance(data))


'''
########## Writing JSON data
    
data ={
  "L'Equipe": { "MOT":"Joueur", "FREQUENCE":12, "DATE":"Sep. 25, 2009"},
  "Le Monde": { "MOT":"Test", "FREQUENCE":5, "DATE":"Sep. 27, 2009"}
}

with open('data_retourner.json', 'w') as fichier:
     json.dump(data, fichier)

'''



