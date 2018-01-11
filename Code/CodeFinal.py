#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 10:00:13 2018

@author: fannyrollet
@author: Nicolas Brouté
"""


def count_word (text):
    '''The function takes a text as a parameter and returns a dictionary whose key is the word and its value is the number of occurences in the text''''
    dict = {}
    for word in text:
        if word in dict:
            dict[word] = dict[word] + 1
        else:
            dict[word] = 1
    return dict



def recuperation(article):
    ''' This function retrieves the contents of the article and calls the count_word function, at finally returns the dictionary sorted   '''
    for keys in article:
        if keys=="content":
            contents=article[keys] 
    return(sorted(count_word(contents).items(),reverse=True, key=lambda t: t[1]))
    
    
    
def score_day_week_month (file,top_word):  
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


def result_day(file):
'''
Function calcultate sum of TF by word and per day
Function have one parameter :
   file : JSON file
It returns dictionnary with word and sum of occurency per day
'''
   result={}
   agregate=0
   result_day=[]
    for key,val in file.items():
       if (key == "period") :
           result[key]=file.get(key)
       else :
           for index1 in range (0,len(val)):
               for index2 in range (0,len(val[index1])):
                   agregate=round(agregate + val[index1][index2],2)
               result_day.append(agregate)
               agregate=0
           result[key]=result_day
           result_day=[]
   return(result)

print(result_day(data))


'''
@author: Fall and Samba
'''
def test_trend_day(Path, word, id_day):
''' This function has three parameters :
    Path : a path of file
    word : words to analyse 
    id_day : the day to analyse 
    This function calculate the T-test for the means of two independent samples and returns the conclusion of the test
'''
    week_day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    with open(Path, 'r') as file:
        data = json.load(file)
    test = scipy.stats.ttest_ind(data[word][id_day], data[word][id_day-1])
    if(test[1] > 0.001 and test[1] < 0.05):
        if ((test[0] > 0)):
            return(word, 'Rising trend', week_day[id_day])
        elif (test[0] < 0):
            return(word, 'Down trend', week_day[id_day])
        else:
            return(word, 'No trend', week_day[id_day])
    elif(test[1] < 0.001):
        if ((test[0] > 0)):
            return(word, 'Strongly rising trend', week_day[id_day])
        elif (test[0] < 0):
            return(word, 'Trend strongly down', week_day[id_day])
        else:
            return(word, 'No trend', week_day[id_day])
    else:
        return(word, 'No trend', week_day[id_day])


'''
@author: Jeremy
'''
def somme_tf_mots (json_tab):
    
    '''goal: give tf 's sum of each word
    param : json_tab ->a dictionnary with:
        -keys : words
        -values : tf
    return modified json_tab with:
        -keys:words
        -values:tf's sum'''

    for i in json_tab.keys() :
        val=0.0
        for j in json_tab[i]:
            val+=sum(j)
            
        json_tab[i]=val

        
        
        
        
'''goal : define which word is the most popular 
param : json_tab ->a dictionnary with:
-keys : words
-values : tf
return max_mot(String): contains the word which it has the biggest tf's sum'''
def popularite_max_mot (json_tab):


    somme_tf_mots(json_tab)
    maxi=0
    max_mot="error"
    for cle,valeur in json_tab.items():
        if valeur>maxi:
            maxi=valeur
            max_mot=cle
    return max_mot

     
