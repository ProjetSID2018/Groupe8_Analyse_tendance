# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 13:34:57 2018

@author: Nicolas
"""
import json
import math

'''
V1 : Nicolas Brouté
V1.1 : Nicolas Brouté, modification : delete one loop to run JSON File 
V1.2 : Nicolas Brouté, add condition in calculate mean of TF IDF
'''

# Reading JSON data 
with open('score_test.json', 'r') as file:
    file = json.load(file)

key_word={}

def score (file,top_word):  
    '''
Function calculate mean TF IDF by word, return a dictionnary of word most important
Function has two parameters:
    file : Json File 
    top_word : number of word which user would
It returns a dictionnary of top word and their TF IDF values 
'''''
    agregate=0
    counter=0
    key_word={}
    #calculate mean TF IDF by word 
    for key,val in file.items():
        if key[-3:]=="IDF" or (key!="period" and key[-2:]!="TF"):
            for index1 in range(len(val)):
                for index2 in range(len(val[index1])):
                    agregate=agregate+val[index1][index2]
                    counter=counter+1
            if counter == 0 : 
                mean_word=0
            else:
                mean_word=round(agregate/counter,2)
            key_word[key]=mean_word
            print(key_word)
            agregate=0
            counter=0
            
    key_word_sort=sorted(key_word.items(),reverse=True, key=lambda t: t[1])
    
    #get only the number of key word pick by user
    key_word=key_word_sort[0:top_word]
    
    #get TF IDF of key word 
    dico_back={}
    for k, v in key_word:
        dico_back[k] = file.get(k)
    return(dico_back)

print(score(file,3))


