from flask import Flask, request, render_template
from string import Template
import requests
from random import randint
import sys
import get_csv_samples
import get_trending_data

app = Flask(__name__)

def is_url_ok(url):
    return 200 == requests.head(url).status_code


@app.route('/getRandomID', methods=['POST'])
def get_random_id():
    sort = request.form.get("sort")
    file_object = ''
    num_lines = 0

    if sort == 'rando':
        file_object = open('rando_vids.txt', 'r')
        num_lines = sum(1 for line in open('rando_vids.txt'))
    elif sort == 'beast':
        file_object = open('rando_mrbeast_vid.txt', 'r')
        num_lines = sum(1 for line in open('rando_mrbeast_vid.txt'))
    elif sort == 'viral':
        file_object = open('./rando_viral_vids.txt', 'r')
        num_lines = sum(1 for line in open('./rando_viral_vids.txt'))

    # lines to print
    specified_line = randint(0, num_lines)
    
    # loop over lines in a file
    for pos, l_num in enumerate(file_object):
        # check if the line number is specified in the lines to read array
        if pos == specified_line:
            l_num = l_num.rstrip('\n')
            return l_num

@app.route('/select_how_many_words', methods=['POST', 'GET'])
def select_how_many_words():
    
    try:
        count = int(request.form.get("count"))
    except:
        count = 5
    comm_words = []

    file_object = open('most_common_words.txt', 'r', encoding="utf-8", errors='ignore')
    num_lines = sum(1 for line in open('most_common_words.txt', 'r', encoding="utf-8", errors='ignore'))
    specified_lines = set()

    while len(specified_lines) < count:
        specified_lines.add(randint(0, num_lines))

    #specified_line = randint(0, num_lines)
    for pos, l_num in enumerate(file_object):
        # check if the line number is specified in the lines to read array
        if pos in specified_lines:
            l_num = l_num.rstrip('\n')
            comm_words.append(l_num)
    return render_template('prompts.html', comm_words=comm_words)

@app.route('/thumbnail_data', methods=['POST', 'GET'])
def thumbnail_data():

    return render_template('thumbnail_data.html')

@app.route('/sentiment_analysis', methods=['POST', 'GET'])
def sentiment_analysis():

    return render_template('sentiment_analysis.html')

@app.route('/most_common', methods=['GET', 'POST'])
def most_common():

    with open('most_viewed_words.txt', 'r', encoding="utf-8", errors='ignore') as file:
        lines = file.readlines()
        viewed_words = [line.rstrip() for line in lines]

    with open('most_common_words.txt', 'r', encoding="utf-8", errors='ignore') as file:
        lines = file.readlines()
        words = [line.rstrip() for line in lines]

    with open('most_viewed_words_without_gaming.txt', 'r', encoding="utf-8", errors='ignore') as file:
        lines = file.readlines()
        no_games = [line.rstrip() for line in lines]
    return render_template('most_common.html', words=words, viewed=viewed_words, no_games=no_games)

@app.route('/trending', methods=['POST', 'GET'])
def trending():
    try:
        #trending = get_trending_data.trending_in_location()
        #trending_realtime = get_trending_data.realtime_trending() 
        countries = get_trending_data.countries_allowed
        try:
            country = request.form['country_select']
        except:
            country = 'United States'
            #print('TEST: ', request.form, file=sys.stderr)
            #print('LOG: ', get_trending_data.realtime_trending(country))
            if request.method == 'POST':
                trending_realtime = get_trending_data.realtime_trending(country)
                trending = get_trending_data.trending_in_location(country)
                return render_tmplate('trending.html')
    except:
        return 'hello'
    #return render_template('trending.html', countries=countries, trending=trending, country=country, rt_trend=trending_realtime)

@app.route('/no_gaming')
def no_gaming():
    return render_template('most_common.html')

@app.route('/giveaway')
def giveaway():
    return render_template('giveaway.html')

@app.route('/prompts')
def prompts():
    sort = request.form.get("sort")
    file_object = ''
    num_lines = 0

    file_object = open('most_common_words.txt', 'r')

    specified_line = randint(0, num_lines)
    comm_words=[]
    # loop over lines in a file
    for pos, l_num in enumerate(file_object):
        # check if the line number is specified in the lines to read array
        if True: #pos == specified_line:
            l_num = l_num.rstrip('\n')
            comm_words.append(l_num) 
    return render_template('prompts.html', comm_words=comm_words)

@app.route('/<word>', methods=['POST', 'GET'])
def command(word=None):

    ttt=get_csv_samples.provide_examples_list(word)
    return ttt 

@app.route('/index')
@app.route('/')
def index():
    vid='yMB_8_VZKSE'
    if get_random_id():
        vid = get_random_id()
    else:
        vid = 'yMB_8_VZKSE'
    
    youtube_url = 'https://www.youtube.com/watch?v=' + vid
    return render_template('index.html', youtube_id=vid)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')
