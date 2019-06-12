import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import requests
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

inputs = ""
string = 'https://parahumans.wordpress.com/2011/06/11/1-1/'
h = urllib.request.urlopen('https://parahumans.wordpress.com/2011/06/11/1-1').read()

soup = BeautifulSoup(h, 'html.parser')
count = 0
total = 0
output = ''
file = open('Worm.txt', 'w+')
listy = list()


    
tags = soup('p')
store = string

#print((tags))
for x in range(5):
    h = urllib.request.urlopen(string).read()

    #h = urllib.request.urlopen(string).read()
    soup = BeautifulSoup(h, 'html.parser')
    tags = soup('p')
    tag = soup('a')
    #string = loop(tags)
    for line in tags:
        #print(line)
        try:    
            output = str(line.contents[0])
            
            #file.write(output)
            print(output)
            for y in tag:
                if y.get("title", None) == "Next Chapter" and not string == str(y.get("href", None)):
                    
                    string = y.get("href", None)
                    #file.write("\n\nName of next page: " + string)
                    break
                    #print(string)
                    
                #print(string)
        except(UnicodeEncodeError):
            break
            #print(string)

        #string = loop(tags)

        #print(string)
        #print(string == store)
        #print(string)
    print()
    file.write("\n")
    file.write("\n")
    file.write("\n")
    print()
   # print(str(x))
print()
print()
print()
