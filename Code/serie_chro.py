# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 10:29:31 2018

@author: Nicolas
"""
import json
import numpy

# Reading data 
with open('serie_chrono.json', 'r') as fichier:
    data = json.load(fichier)
          


def resu_mensuel(fichier):
   resultat={}
   somme=0
   resultat_jour=[]
   for valeur in data.values():
       for cle,val in valeur.items(): #recuperer mot clé et leur apparition
           for i in range (0,len(val)):
               for j in range (0,len(val[i])):
                   somme=somme + val[i][j] #sommer le nombre d'apparition dans le mois
               resultat_jour.append(somme)
               somme=0
           resultat[cle]=resultat_jour
           resultat_jour=[]
   
   return(resultat)

print(resu_mensuel(data))




    



        
        
        
        
