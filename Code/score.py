# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 13:34:57 2018

@author: Nicolas
"""
import json

'''
V1 : Nicolas Brouté
V2 : Nicolas Brouté, modification : delete one loop to run JSON File 
'''

# Reading JSON data 
with open('score_test.json', 'r') as file:
    file = json.load(file)
    

def score (file,top_word):  
    '''
Function calculate mean TF IDF by word, return a dictionnary of word most important
Function has two parameters:
    file : Json File 
    top_word : number of word which user would
It returns a dictionnary of top word and their TF IDF values 
'''
    agregate=0
    counter=0
    key_word={}
    #calculate mean TF IDF by word 
    for key,val in file.items():
        if key[-3:]=="IDF":
            for index1 in range(0,len(val)):
                for index2 in range(0,len(val[index1])):
                    agregate=agregate+val[index1][index2]
                    counter=counter+1
                if counter == 0 : 
                    mean_word=0
                else:
                    mean_word=round(agregate/counter,2)
                key_word[key]=mean_word
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

print(score(file,5))
