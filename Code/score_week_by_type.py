# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 08:51:33 2018
@author: Nicolas
"""

import json
import numpy

with open('score_weekV2.json', 'r') as file:
    file = json.load(file)




def score_week_by_type(file, top_word, type_word):

    """
    the function's objectives :
        This function allows you to select a type of words (e. g. proper name
        or verb). As for version 1 of the function, the V2 returns to us the X
        words of the nature requested presents in the article which have the
        highest average, this same average and the initial data corresponding
        to the words present in the json file.
    the function's parameters :
        The two function's parameters are
        - the file json which contains datas
        - the number of words what we want
        -the nature of word
    the function returns
        - a dictionnary which contains the key words and their mean
        - a dictionnary wich contains the key words and all corresponding
        values

        adj=score_week_V2(file, 1, “ADJ”)[1]
        verb=score_week_V2(file, 1, “VERB”)[1]
        proper_noun=score_week_V2(file, 1, “PROPER_NOUN”)[1]

        #Concatenation des dictionnaires
        test = {}
        for d in [adj,verb,proper_noun]:
        test.update(d)
        
    """
	
    liste_mot = []
    agregate = 0
    counter = 0
    key_word = {}
    list_mean_intermediate = []

    # retrieve the TF IDF of the words for the category chosen by the user
    # retrieve word TFs
    for cle in file.keys():
        if cle[-4:] == "type":
            if file.get(cle) == type_word:
                mot_TFIDF = cle[:-5]
                liste_mot.append(mot_TFIDF)

    # calculate the average of TF IDF per word
    for mot_tfidf in liste_mot:
        valeur = file.get(mot_tfidf)
        for index1 in range(len(valeur)):
            for index2 in range(len(valeur[index1])):
                agregate = agregate + float(valeur[index1][index2])
                counter = counter + 1
            if counter == 0:
                list_mean_intermediate.append(0)
            else:
                list_mean_intermediate.append(agregate/counter)

        key_word[mot_tfidf] = numpy.mean(list_mean_intermediate)
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

    dictionnary_intermediate = {}
    for key_dico_back in dico_back.keys():
        dictionnary_intermediate[key_dico_back] = file.get(key_dico_back)

    dico_tf = {}
    liste_agregate = []

    for key, val in dictionnary_intermediate.items():
        for index1 in range(len(val)):
            if len(val[index1]) != 0:
                for index2 in range(len(val[index1])):
                    agregate = agregate + float(val[index1][index2])
            else:
                agregate = 0
            liste_agregate.append(agregate)
            agregate = 0
        dico_tf[key] = liste_agregate
        liste_agregate = []

    return(dico_back, dico_tf)

