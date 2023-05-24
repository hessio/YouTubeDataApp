import pandas as pd
import sys
import json
from flask import jsonify, make_response, Response
import re

df = pd.read_csv('cleaned_data_set.csv')

def provide_examples_list(word):
	ret_string =''
	ret_dict = {}
	place_dict = {}
	total_dict = {}
	
	ttt = df[df['title'].str.contains(word)]['title'].tolist()
	thumb = df[df['title'].str.contains(word)]['thumbnail_link'].tolist()
	id_s = df[df['title'].str.contains(word)]['video_id'].tolist()
        	
	i = 0
	for t in range(len(ttt)):
		link = 'https://www.youtube.com/watch?v='+id_s[t]
				
		place_dict[thumb[t]] = ttt[t]
		total_dict[link] = place_dict
		ret_dict[t] = total_dict
		total_dict = {}
		place_dict = {}
	
	json__ = json.dumps(ret_dict, ensure_ascii=False).encode('utf8')

	return json__
