# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 09:00:19 2018

@author: Groupe 8
"""


import sys
import json
from itertools import chain
from collections import defaultdict

import numpy as np
from statsmodels.api import OLS



from flask import jsonify
from flask import Flask, request
from flask_restful import Resource, Api

sys.path.append('/var/www/html/projet2018/code/stat/static')

from function import test_trend, file_trend, score_week, score_week_by_type, trend_with_moving_average, moving_average, extract_keys_values

app = Flask(__name__)
api = Api(app)

@app.route("/static_week/", methods = ['GET', 'POST'])
def api_static_week():
	week_st = request.get_json()
	score = score_week(week_st, 10)[1]
	score_word_cloud = score_week(week_st, 10)[0]

	result_trend = trend_with_moving_average(score)
	result = defaultdict(list)
	for k, v in chain(score_word_cloud.items(), result_trend.items()):
    		result[k].append(v)

	#prepare the JSON formatting of top 10 words
	result_back = {}
	result_intermediate = {}
	indice = 0
	for k, v in result.items():
   		result_intermediate['text'] = k
   		result_intermediate['weigth'] = v[0]
   		result_intermediate['trend'] = v[1]
   		result_back[indice] = result_intermediate
   		indice = indice + 1
   		result_intermediate = {}
		
	return jsonify(result_back)


@app.route("/dynamic_week_label/", methods = ['GET', 'POST'])
def api_dynamic_week():
	week_th = request.get_json()
	score_word_cloud = score_week(week_th, 10)[0]
	score = score_week(week_th, 10)[1]
	
	best_verb = score_week_by_type(week_th, 1,'VERB')[1]
	best_proper_noun = score_week_by_type(week_th, 1,'PROPER_NOUN')[1]
	best_adj = score_week_by_type(week_th, 1,'ADJ')[1]

	#get top verb, adj and proper_noun to get trend
	data_trend = {}
	dico_intermediate1 = {}
	for d in [best_verb, best_proper_noun, best_adj]:
    		for cle, val in d.items():
        		if cle[-4:] != "type":
            			dico_intermediate1[cle] = val
            			data_trend.update(dico_intermediate1)

	trend = trend_with_moving_average(data_trend)
	dico_intermediate2 = {}
	for cle, val in trend.items():
    		dico_intermediate2[cle + "_type"] = week_th.get(cle + "_type")
    		dico_intermediate2[cle] = val
	
	#prepare the JSON formatting of top verb, adj, proper noun
	result_top_back = {}
	result_intermediate = {}
	indice = 0
	for k, v in dico_intermediate2.items():
    		if k[-5:] == k:
        		result_intermediate["text"] = k
        		result_intermediate["type"] = week_th.get(k + "_type")
        		result_intermediate["trend"] = v
        		result_top_back[indice] = result_intermediate
        		indice = indice + 1
        		result_intermediate = {}

	result_trend = trend_with_moving_average(score)
	result = defaultdict(list)
	for k, v in chain(score_word_cloud.items(), result_trend.items()):
    		result[k].append(v)

	#prepare the JSON formatting of top 10 words
	result_back = {}
	result_intermediate = {}
	indice = 0
	for k, v in result.items():
    		result_intermediate['text'] = k
    		result_intermediate['weigth'] = v[0]
    		result_intermediate['trend'] = v[1]
    		result_back[indice] = result_intermediate
    		indice = indice + 1
    		result_intermediate = {}		
	return jsonify(result_top_back, result_back)

if __name__ == '__main__':
    app.run(host = "130.120.8.250", port = 5002, debug = True)