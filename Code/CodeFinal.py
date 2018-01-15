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

    
    
 def score_day(file, top_word):
    """
    the function's objectives :
        This function allows you to show the most important words of a
        newspaper
        article and the TF of the previous day and the day for each word.
        We place the number of words what we want in parameters of the function
        when we call it.
    the function's parameters :
        The two function's parameters are
        - the file json which contains datas
        - the number of words what we want
    the function returns
        - a dictionnary which contains the key words and their mean on two days
        - a dictionnary wich contains the key words and all corresponding
        values
    """
    agregate = 0
    counter = 0
    key_word = {}
    dico_tf = {}
    list_mean_intermediate = []
    # calculate mean TF IDF by word
    for key, val in file.items():
        if key != "period":
            for index1 in range(len(val)):
                for index2 in range(len(val[index1])):
                    agregate = agregate + val[index1][index2]
                    counter = counter + 1
                list_mean_intermediate.append(agregate / counter)

            key_word[key] = numpy.mean(list_mean_intermediate)

            agregate = 0
            counter = 0

    # sort words in descending order
    key_word_sort = sorted(key_word.items(), reverse=True, key=lambda t: t[1])

    # get only the number of key word pick by user
    key_word = key_word_sort[0:top_word]

    # get TF IDF of key word
    dico_back = {}
    for k, v in key_word:
        dico_back[k] = v

    # construct the value dictionary for each word
    list_agregate = []
    dico = {}
    for key_dico_back in dico_back.keys():
        dico_tf[key_dico_back] = file.get(key_dico_back)
    for key, val in dico_tf.items():
        for index1 in range(len(val)):
            if len(val[index1]) != 0:
                for index2 in range(len(val[index1])):
                    list_agregate.append(val[index1][index2])
            else:
                list_agregate.append(0)
        dico[key] = list_agregate
        list_agregate = []

    return(dico_back, dico)


print(score_day(file, 10))



def score_week(file, top_word):
    '''
Function calculate mean TF IDF by word to built a dictionnary of word most
important
Function has two parameters:
    file : Json File
    top_word : number of important word which user would
It returns a dictionnary of top word with their mean TF IDF
A second dictionnary with top word with their TF values
'''''
    agregate = 0
    counter = 0
    key_word = {}
    dictionnary_intermediate = {}
    list_mean_intermediate = []

    # calculate mean TF IDF by word
    for key, val in file.items():
        if key[-3:] == "idf":
            for index1 in range(len(val)):
                for index2 in range(len(val[index1])):
                    agregate = agregate + val[index1][index2]
                    counter = counter + 1
                if counter == 0:
                    list_mean_intermediate.append(0)
                else:
                    list_mean_intermediate.append(agregate/counter)

            key_word[key[:-7]] = numpy.mean(list_mean_intermediate)
            agregate = 0
            counter = 0

    # sort words in descending order
    key_word_sort = sorted(key_word.items(), reverse=True, key=lambda t: t[1])

    # get only the number of key word pick by user
    key_word = key_word_sort[0:top_word]

    # get TF IDF of key word
    dico_back = {}
    for k, v in key_word:
        dico_back[k] = v

    # built a intermediate dictionnary of TF by word
    liste_agregate = []
    dico_tf = {}
    for key_dico_back in dico_back.keys():
        wrd = key_dico_back + "_tf"
        dictionnary_intermediate[wrd] = file.get(wrd)

    # built dictionnary of TF
    for key, val in dictionnary_intermediate.items():
        k = key[:-3]  # remove terminaison
        for index1 in range(len(val)):
            if len(val[index1]) != 0:
                for index2 in range(len(val[index1])):
                    agregate = agregate + val[index1][index2]
            else:
                agregate = 0
            liste_agregate.append(agregate)
            agregate = 0
        dico_tf[k] = liste_agregate
        liste_agregate = []
    return(dico_back, dico_tf)


print(score_week(file, 10))
     
