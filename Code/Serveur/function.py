import numpy as np
import scipy.stats


def score_day(file,top_word):
    
    """
    the function's objectives :
        This function allows you to show the most important words of a newspaper 
        article and the TF of the previous day and the day for each word.
        
        We place the number of words what we want in parameters of the function 
        when we call it.
        
    the function's parameters : 
        The two function's parameters are 
        - the file json which contains datas
        - the number of words what we want
        
    the function returns 
        - a dictionnary which contains the key words and their mean on two days
        - a dictionnary wich contains the key words and all corresponding values 
    
    """
    agregate=0
    counter=0
    key_word={}
    dico_tf={}
    #calculate mean TF IDF by word 
    for key,val in file.items():
        if key!="period" :
            for index1 in range(len(val)):
                for index2 in range(len(val[index1])):
                    agregate=agregate+val[index1][index2]
                    counter=counter+1
                   
            mean_word=round(agregate/counter,2)

            key_word[key]=mean_word

            agregate=0
            counter=0
            
    #sort words in descending order
    key_word_sort=sorted(key_word.items(),reverse=True, key=lambda t: t[1])
    
    #get only the number of key word pick by user
    key_word=key_word_sort[0:top_word]
    
    #get TF IDF of key word 
    dico_back={}
    for k, v in key_word:
        dico_back[k] = v

    #construct the value dictionary for each word        
    list_agregate=[]
    dico={}
    for key_dico_back in dico_back.keys():
        dico_tf[key_dico_back]=file.get(key_dico_back)
    for key,val in dico_tf.items():
        for index1 in range(len(val)):
            if len(val[index1])!= 0 :
                for index2 in range(len(val[index1])):
                    list_agregate.append(val[index1][index2])
            else :
                list_agregate.append(0)
        dico[key]=list_agregate
        list_agregate=[]
    dico["period"]=file.get("period")

    
    return(dico_back,dico)


def test_trend(data, word, id_day):
    '''trend
    This function has three parameters :
    data : json data
    word : words to analyse
    id_day :  day to analyse
    This function calculate the T-test for the means of two independent samples and returns the conclusion of the test
    '''
    test = scipy.stats.ttest_ind(data[word][id_day], data[word][id_day - 1])
    test = scipy.stats.ttest_ind(data[word][id_day], data[word][id_day-1])
    if(test[1] > 0.001 and test[1] < 0.05):
        if ((test[0] > 0)):
            return(word, 'Increasing_trend')
        elif (test[0] < 0):
            return(word, 'Decreasing_trend')
        else:
            return(word, 'No_trend')
    elif(test[1] < 0.001):
        if ((test[0] > 0)):
            return(word, 'Strongly_increasing_trend')
        elif (test[0] < 0):
            return(word, 'Strongly_decreasing_trend')
        else:
            return(word, 'No_trend')
    else:
        return(word, 'No_trend')


def file_trend(data):
    """ data preprocessing for groupe 9
    param : data -> json data
    return json with trend, period and most important word"""
    dict = {}
    for cle, valeur in data.items():
        if(cle != 'period'):
            for val in range(1, len(valeur)):
                word, trend = test_trend(data, cle, val)
            dict[cle] = trend
        else:
            dict[cle] = valeur
    return(dict)


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
    dico_back = {}
    list_mean_intermediate = []
    dico_mean = {}

    for key, val in file.items():
        if key != "Period" and key[-4:] != "type":
            dico_mean[key] = val[7:14]

    # calculate mean TF IDF by word
    for key, val in dico_mean.items():
        for index1 in range(len(val)):
            if key != "Period" and key[-4:] != "type":
                for index2 in range(len(val[index1])):
                    agregate = agregate + float(val[index1][index2])
                    counter = counter + 1
                if counter == 0:
                    list_mean_intermediate.append(0)
                else:
                    list_mean_intermediate.append(agregate/counter)

                key_word[key] = np.mean(list_mean_intermediate)
                agregate = 0
                counter = 0

    # sort words in descending order
    key_word_sort = sorted(key_word.items(), reverse=True, key=lambda t: t[1])

    # get only the number of key word pick by user
    key_word = key_word_sort[0:top_word]

    # get TF IDF of key word

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

def score_week_by_type(file, top_word, type_word):
    liste_mot = []
    agregate = 0
    counter = 0
    key_word = {}
    list_mean_intermediate = []
    dico_mean = {}

    for key, val in file.items():
        if key != "Period" and key[-4:] != "type":
            dico_mean[key] = val[7:14]

    # recuperer les TF IDF des mots pour la categorie choisi par l'utilisateur
    # r�cuperer les TF des mots
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

        key_word[mot_tfidf] = np.mean(list_mean_intermediate)
        agregate = 0
        counter = 0

    # trier les mots par ordre d�croissant
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


def extract_keys_values(data):
    """
    goal of this function :
        - to extract keys (ie. words) and values from the json file
    input parameter :
        - json file's content (data)
    output :
        - two lists (keys and values)
    """
    
    #initialisation
    keys = []
    values = []
    
    #for each entry in the json file
    for k, v in data.items():
        keys.append(k)
        values.append(v)
    
    return(keys, values)


def moving_average(seq, order) :
    """
    goal of this function :
        - to calculate the moving average
    input parameters :
        - list of values (seq)
        - interger (order)
    output :
        - list of values (moving_avg)
    """
    
    moving_avg = np.cumsum(seq, dtype = float)
    moving_avg[order:] = moving_avg[order:] - moving_avg[:-order]

    return moving_avg[order - 1:] / order


def trend_with_moving_average(data_v2):
    """
    goal of this function :
        - to calculate the moving average for each word
            (ie. each entry in the json file)
        - to determine the trend (increasing or decreasing)
    input parameters :
        - data (json format)
    intermediary actions :
        - extraction of keys and values (function)
    output :
        - dict with many words and their trend (cf. file_trend function)
    """
    
    keys, values = extract_keys_values(data_v2)
    
    mavg_series = []
    dict_word_mavg = {}

    #for each word in the json file (ie. data_v2)
    for j in range(len(values)):
        mavg_series = moving_average(values[j], 3).tolist()
        splt_series = [mavg_series[0:5], mavg_series[6:11]]
        dict_word_mavg[keys[j]] = splt_series
    
    return(file_trend(dict_word_mavg))


