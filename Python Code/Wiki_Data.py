# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 17:14:16 2017

@author: Caroline Lee

Read from a URL using MediaWiki API

This program answers research question:
    "Do wikipedia articles use different terms to describe items in the same 
    category?"
        Category Chosen: Musical Periods
"""
import requests

#Medieval Era
response = requests.get(
    'https://en.wikipedia.org/w/api.php',
    params={
            'action': 'query',
            'format': 'json',
            'titles': 'Medieval_music',
            'prop': 'extracts',
            'exintro': False,
            'explaintext': True,
           }
    ).json()
page1 = next(iter(response['query']['pages'].values()))

#Renaissance
response = requests.get(
    'https://en.wikipedia.org/w/api.php',
    params={
            'action': 'query',
            'format': 'json',
            'titles': 'Renaissance_music',
            'prop': 'extracts',
            'exintro': False,
            'explaintext': True,
           }
    ).json()
page2 = next(iter(response['query']['pages'].values()))

#Baroque Era
response = requests.get(
    'https://en.wikipedia.org/w/api.php',
    params={
            'action': 'query',
            'format': 'json',
            'titles': 'Baroque_music',
            'prop': 'extracts',
            'exintro': False,
            'explaintext': True,
           }
    ).json()
page3 = next(iter(response['query']['pages'].values()))

#Classical Era
response = requests.get(
    'https://en.wikipedia.org/w/api.php',
    params={
            'action': 'query',
            'format': 'json',
            'titles': 'Classical_period_(music)',
            'prop': 'extracts',
            'exintro': False,
            'explaintext': True,
           }
    ).json()
page4 = next(iter(response['query']['pages'].values()))

#Romantic Era
response = requests.get(
    'https://en.wikipedia.org/w/api.php',
    params={
            'action': 'query',
            'format': 'json',
            'titles': 'Romantic_music',
            'prop': 'extracts',
            'exintro': False,
            'explaintext': True,
           }
    ).json()
page5 = next(iter(response['query']['pages'].values()))

#20th Century
response = requests.get(
    'https://en.wikipedia.org/w/api.php',
    params={
            'action': 'query',
            'format': 'json',
            'titles': '20th-century_classical_music',
            'prop': 'extracts',
            'exintro': False,
            'explaintext': True,
           }
    ).json()
page6 = next(iter(response['query']['pages'].values()))


#process words
def processData(s):
    #create an empty dictionary
    dictionary = {}
    
    
    #get rid of unnecessary symbols and split string, put in a list
    s = s.lower()
    s = s.replace(',', "")
    s = s.replace('(', "")
    s = s.replace(')', "")
    s = s.replace('.', "")
    words = s.split()
    
    
    #count word frequencies using code from lab3_p1
    i = 0
    for word in words:
        dictionary[word] = dictionary.get(word, 0) + 1

    #sort the dictionary
    sortedDictionary = sorted(dictionary, key = dictionary.get, reverse = True)
    
    #format sorted dictionary for output --> turn into a string again
    wordString = ""
    for w in sortedDictionary:
        if i < 45:
            wordString = wordString + (w + '\t' + str(dictionary[w]) + '\n')
            i += 1
    return wordString
  
print "Medieval Era" + '\n' + processData(page1['extract'])
print "Renaissance" + '\n' + processData(page2['extract'])
print "Baroque Era" + '\n' + processData(page3['extract'])   
print "Classical Era" + '\n' + processData(page4['extract'])
print "Romantic Era" + '\n' + processData(page5['extract'])
print "20th Century" + '\n' + processData(page6['extract'])



