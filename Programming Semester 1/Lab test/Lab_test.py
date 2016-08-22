def Download():
    from urllib.request import urlretrieve
    html = "http://mf2.dit.ie/gettysburg.txt"
    urlretrieve(html,"text.txt")

def makeWordList(f):
    speech = []  # list of speech words: initialized to be empty
    """Create a list of words from the file while excluding stop words."""

    for lineString in f:
        lineList = lineString.strip()
            string.whitespace.split()  # split each line into a list of words and strip whitespace
        for word in lineList:
            word = word.lower()  # make words lower case (we consider a word in lowercase and uppercase to be equivalent)
            word = word.strip(string.punctuation)  # strip off punctuation
            if (word not in stopWords) and (word not in string.punctuation):
                # if the word is not in the stop word list, add the word to the speech list
                speech.append(word)
    return speech


def countWords(speech):
    """Create a dictionary and count the occurrences of each word.
    If a word already exists in the dictionary, add 1 to its counter
    otherwise set a counter for to to an initial value of 1"""
    counts = {}
    for word in speech:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

try:
    f=open('text.txt','r')
    speech=makeWordList(f)
    words = countWords(speech)
    print(words)
    f.close()
          
except IOError:
    print ('File downloading ')
    Download()
    f=open('text.txt','r')
    Main()
    f.close()


 
 
        
    
   


