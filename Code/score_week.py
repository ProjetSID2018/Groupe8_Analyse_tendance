# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 15:15:24 2018

@author: Nicolas
"""

import json

# Reading JSON data 
with open('score_test.json', 'r') as file:
    file = json.load(file)
    
def score_week(file,top_word):
    '''
Function calculate mean TF IDF by word to built a dictionnary of word most important
Function has two parameters:
    file : Json File 
    top_word : number of important word which user would
It returns a dictionnary of top word with their mean TF IDF 
A second dictionnary with top word with their TF values 
'''''
    agregate=0
    counter=0
    key_word={}
    dictionnary_intermediate={}
    
    #calculate mean TF IDF by word 
    for key,val in file.items():
        if key[-3:]=="IDF" :
            for index1 in range(len(val)):
                for index2 in range(len(val[index1])):
                    agregate=agregate+val[index1][index2]
                    counter=counter+1
            mean_word=round(agregate/counter,2)
            key_word[key[:-6]]=mean_word
            agregate=0
            counter=0
            
    #trier les mots par ordre décroissant
    key_word_sort=sorted(key_word.items(),reverse=True, key=lambda t: t[1])
    
    #get only the number of key word pick by user
    key_word=key_word_sort[0:top_word]
    
    #get TF IDF of key word 
    dico_back={}
    for k, v in key_word:
        dico_back[k] = v

    #built a intermediate dictionnary of TF by word
    liste_agregate=[]
    dico_tf={}
    for key_dico_back in dico_back.keys():
        wrd=key_dico_back+ "_TF"
        dictionnary_intermediate[wrd]=file.get(wrd)
    
    #built dictionnary of TF
    for key,val in dictionnary_intermediate.items():
        k=key[:-3] #remove terminaison
        for index1 in range(len(val)):
            if len(val[index1])!= 0 :
                for index2 in range(len(val[index1])):
                    liste_agregate.append(val[index1][index2])
            else :
                liste_agregate.append(0)

        dico_tf[k]=liste_agregate
        liste_agregate=[]
       
    return(dico_back,dico_tf)

print(score_week(file,2))

liste=[1,2,3]
liste.append(0)