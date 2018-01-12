# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 15:18:49 2018

@author: Nicolas
"""

import json

# Reading JSON data
with open('jour.json', 'r') as file:
    file = json.load(file)


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
    # calculate mean TF IDF by word
    for key, val in file.items():
        if key != "period":
            for index1 in range(len(val)):
                for index2 in range(len(val[index1])):
                    agregate = agregate + val[index1][index2]
                    counter = counter + 1

            mean_word = round(agregate / counter, 2)

            key_word[key] = mean_word

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
<<<<<<< HEAD
        dico[key]=list_agregate
        list_agregate=[]
    dico["period"]=file.get("period")
=======
        dico[key] = list_agregate
        list_agregate = []

    return(dico_back, dico)
>>>>>>> 2047a1d4177dbffee0b67a4b8646981348ca317f


print(score_day(file, 10))
