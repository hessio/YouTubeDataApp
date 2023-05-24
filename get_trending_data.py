import pandas as pd
from pytrends.request import TrendReq
#from pycountry_convert import country_name_to_country_alpha
import pycountry
import sys
pytrend = TrendReq()
from serpapi import GoogleSearch

countries_allowed = ['Ireland', 'Canada', 'New Zealand', 'South Africa', 'Taiwan', 'United Kingdom', 'United States']
selected_country = 'United States'

def trending_in_location(loc='United States'):
        trending=[]
        loc = loc.lower()
        loc = loc.replace(' ', '_')
        trendingtoday = pytrend.trending_searches(pn=loc)
        for i, row in trendingtoday.iterrows():
                trending.append(row[0])
        return trending

def get_top_stories(query):
    params = {
            "q": query,
            "hl": "en",
            "gl": "us",
            "google_domain": "google.com",
            "api_key": "ac832214c92301652f65975677b493c1e44acfcfe44bf9181a16f57b8eafd768"
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    #top = results['top_stories']
    
    print(results)
    try:
        print(results['top_stories'])
        top = results['top_stories']
    except:
        top = []
        print(results['organic_results'])
        top.append(results['organic_results'][0])
        top.append(results['organic_results'][1])
        top.append(results['organic_results'][2])
        top.append(results['organic_results'][3])

    return top

def realtime_trending(loc='United States'):
    trending = []
    countries = {}
    
    for country in pycountry.countries:
        countries[country.name] = country.alpha_2

    code = countries.get(loc, 'Unknown code')
    if loc == 'Taiwan':
        code = 'TW'

    trend = pytrend.realtime_trending_searches(pn=code)
    #print(type(trend['entityNames']))
    for row in trend['entityNames'].head(3):
        for topic in row:
            print('\n\n\n\n\n', topic, '\n\n\n\n\n')
            trending.append(get_top_stories(topic))
        #trending.append(get_top_stories(row[0]))
        #trending.append(row[0])
     
    return trending
#print(realtime_trending())
