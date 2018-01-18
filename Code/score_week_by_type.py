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
    liste_mot = []
    agregate = 0
    counter = 0
    key_word = {}
    list_mean_intermediate = []
    dico_mean = {}

    for key, val in dico_mean.items():
        if key != "Period" and key[-4:] != "type":
            dico_mean[key] = val[7:14]

    # recuperer les TF IDF des mots pour la categorie choisi par l'utilisateur
    # récuperer les TF des mots
    for cle in file.keys():
        if cle[-4:] == "type":
            if file.get(cle) == type_word:
                mot_TFIDF = cle[:-5]
                liste_mot.append(mot_TFIDF)

    # calculer la moyenne des TF IDF par mot
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

    # trier les mots par ordre décroissant
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
        dico_tf[key + "_type"] = file.get(key + "_type")
        liste_agregate = []

    return(dico_back, dico_tf)


print(score_week_by_type(file, 2, "nom propre"))
