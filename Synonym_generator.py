import nltk 
import re
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
from nltk.corpus import wordnet 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 
stop_words = set(stopwords.words('english')) 
synonyms = [] 
list2 = []

fd = open("final.txt","a")
def unique(list1): 
    unique_list = [] 
    for x in list1: 
        if x not in unique_list: 
            unique_list.append(x) 
    return unique_list

def postag(txt):
    list1 = []
    adj = []
    cnt =0
    tokenized = sent_tokenize(txt) 
    for i in tokenized: 
          
        wordsList = nltk.word_tokenize(i) 
        wordsList = [w for w in wordsList if not w in stop_words]  
        tagged = nltk.pos_tag(wordsList) 
        

    for i in range(0,len(tagged)):
        if(tagged[i][1] == "JJ"):
            adj.append(tagged[i][0]) 
            


    for item in adj:
        if(cnt<=3):
            for syn in wordnet.synsets(item): 
                for l in syn.lemmas(): 
                    if(l.name() not in list1):
                        list1.append(l.name())
                        synonyms = l.name() 
                        newstr = txt.replace(item,synonyms)
                        fd.write(newstr)
                        cnt+=1




with open("sample1.txt","r") as s1:
    line = s1.readline()
    cnt = 1
    while(line):
        postag(line)
        line = s1.readline()
        cnt+=1


