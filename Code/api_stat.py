import sys
import json
from itertools import chain
from collections import defaultdict

from flask import jsonify
from flask import Flask, request
from flask_restful import Resource, Api

sys.path.append('/var/www/html/projet2018/code/stat/static')

from function import test_trend, file_trend, score_week, score_week_by_type

app = Flask(__name__)
api = Api(app)

@app.route("/static_week/", methods = ['GET', 'POST'])
def api_static_week():
	week_st = request.get_json()
	score = score_week(week_st, 10)[1]
	score_word_cloud = score_week(week_st, 10)[0]
	result_trend = file_trend(score)
	result = defaultdict(list)
	for k, v in chain(score_word_cloud.items(), result_trend.items()):
   		 result[k].append(v)		
	return jsonify(result)


@app.route("/dynamic_week_them/", methods = ['GET', 'POST'])
def api_dynamic_week():
	week_th = request.get_json()

	top_score_word_cloud = score_week(week_st, 10)[0]

	best_verb = score_week_by_type(week_th, 1, 'VERB')[1]
        best_proper_noun = score_week_by_type(week_th, 1, 'PROPER_NOUN')[1]
	best_adj = score_week_by_type(week_th, 1, 'ADJ')[1]

        data_trend = {}
        for d in [best_verb, best_proper_noun, best_adj]:
        	data_trend.update(d)

	result_trend = file_trend(score)
	result = defaultdict(list)
	for k, v in chain(score_word_cloud.items(), result_trend.items()):
   		 result[k].append(v)		
	return jsonify(result)


if __name__ == '__main__':
    app.run(host = "130.120.8.250", port = 5002, debug = True)