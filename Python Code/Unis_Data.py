# -*- coding: utf-8 -*-
"""
Created on Wed Feb 08 15:21:10 2017

@author: Caroline Lee
         Read files of URLs in /top5_unis, create result files of counted and 
         sorted words(top 25) for each file(8 text files will be generated)
         
"""
import urllib, os


#write method to take string input, split it, and put in dictionary
def processData(s):
    dictionary = {}
    s = s.lower()
    s = s.replace(',', "")
    s = s.replace('\\',"")
    s = s.replace('<', "")
    s = s.replace('>', "")
    s = s.replace('/', "")
    s = s.replace(':', "")
    s = s.replace('=', "")
    s = s.replace('"', " ")
    words = s.split()
    
    #count words in dictionary(code from powerpoint slide example)
    for word in words:
        dictionary[word] = dictionary.get(word, 0) + 1 
    return dictionary 

#http://stackoverflow.com/questions/9001509/how-can-i-sort-a-dictionary-by-key    
#sort dictionary and write first 25 lines to file  
def writeToFile(dictionary, filename):
    sortedDictionary = sorted(dictionary, key = dictionary.get, reverse = True)
    dataFile = open(filename, "w+")
    i = 0
    for w in sortedDictionary:
        if i < 25:
         dataFile.write(str(w) + '\t' + str(dictionary[w]) + '\n')
         i += 1
    dataFile.close()

#open file to be processed
def openFiles():
    for file in os.listdir("top5_unis"):
        f = open("top5_unis\\" + file, "r")
        print "Opening file: " + file
        linesList = f.readlines()
        print "reading...\n"
        i = 0
        
        #open links in each file
        for linkLine in linesList:
            linkLine = linesList[i]
            print "    " + linkLine + "\n"
            try:
                stuff = urllib.urlopen(linkLine)
                content = stuff.read()
            except IOError:
                print "    ^Could not open link.^ \n"
            i += 1
            
        filename = file  + "result"#change the filename for result data
        filename = filename.replace(".txt", "_")
        filename = filename + ".txt"
        print "Writing to new file: " + filename + "\n\n"
        writeToFile(processData(content), filename)
    
#this does everything - "main method"   
#print statements have been added for seeing individual processes in execution 
openFiles()
print "Finished processing data."






