__author__ = 'gray'

import json
import urllib, urllib2

BING_API_KEY = '7GCqlRSJT1lnL5sgFUGECpzBashS/rJljO2DwG5MPmE'

def run_search(term):
    root = 'https://api.datamarket.azure.com/Bing/SearchWeb/'
    source = 'web'
    results_per_page = 10
    offset = 0
