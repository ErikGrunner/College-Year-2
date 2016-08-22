__author__ = 'Ciaran'
import string

def Download():
    from urllib.request import urlretrieve
    html = "http://mf2.dit.ie/gettysburg.txt"
    urlretrieve(html,"text.txt")

    from urllib.request import urlretrieve
    html = "http://mf2.dit.ie/stopwords.txt"
    urlretrieve(html,"text2.txt")
def main(f,g):

    fl=open('wordcloud.html','w')
    fl.write('<!DOCTYPE html><html><head lang="en"><meta charset="UTF-8">'
             '<title>Tag Cloud Generator</title>'
             '</head><body>'
             '<div style="text-align: center; vertical-align: middle; font-family: arial; color: white; background-color:black; border:1px solid black">')

    speech = []  # list of speech words: initialized to be empty

    for lineString in f:
        lineList = lineString.strip(string.whitespace).split()  # split each line into a list of words and strip whitespace
        for word in lineList:
            word = word.lower()  # make words lower case (we consider a word in lowercase and uppercase to be equivalent)
            word = word.strip(string.punctuation)  # strip off punctuation
            if (word not in g) and (word not in string.punctuation):
                # if the word is not in the stop word list, add the word to the speech list
                speech.append(word)

    counts = {}
    for word in speech:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    for word in speech:
        fl.write('<span style="font-size: %ipx"> %s </span>\n' %((counts[word]*20),word))


    print("Finnished")
    fl.write('</div>'
             '</body>'
             '</html>')

try:
    f=open('text.txt','r')
    g=open('text2.txt','r')
    main(f,g)
    f.close()

except IOError:
    print ('File downloading ')
    Download()
    f=open('text.txt','r')
    g=open('text2.txt','r')
    main(f,g)
    f.close()
