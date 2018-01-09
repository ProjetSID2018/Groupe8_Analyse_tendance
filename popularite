# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 10:27:07 2018

@author: jeremy
"""



# give tf 's sum of each word
def somme_tf_mots (json_tab):
    #json_tab is a dictionnary
    #keys :words
    #values :tf
    for i in json_tab.keys() :
        val=0.0
        for j in json_tab[i]:
            val+=sum(j)
            
        json_tab[i]=val
#json_tab is modified :
        #keys:words
        #values:tf 's sum 
        
        
######################################        
        
# define which word is the most popular  
def popularite_max_mot (json_tab):
    #json_tab is a dictionnary
    #keys :words
    #values :tf
    somme_tf_mots(json_tab)
    maxi=0
    max_mot="error"
    for cle,valeur in json_tab.items():
        if valeur>maxi:
            maxi=valeur
            max_mot=cle
    return max_mot
#max_mot contains the word which it has the biggest tf's sum
     


###################################

#print the dictionnary on screen
def afficher_dico (json_tab):
    for cle,valeur in json_tab.items():
        print(cle,valeur)

#################################
        
        
        
        
        
        
        
        

json_tableau={"azerty":[[0,0.5,0.25],[0.1,0.8],[0.3,0.4,0.1,0.15]],"uiop":[[0,0.4,0.25],[0.1,0.6],[0.3,0.4,0.1,0.15]],"lala":[[0.2,0.5,0.25],[0.1,0.8],[0.3,0.4,0.1,0.15]]}
print ("avant modification")
afficher_dico(json_tableau)
mot_populaire=popularite_max_mot(json_tableau)
print ("après modification")
afficher_dico(json_tableau)
print ("le mot le plus populaire sur cette période est : ",mot_populaire)
