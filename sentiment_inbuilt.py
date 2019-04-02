from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()
fd = open("output1.txt","w")
def analyse(sentence,sentiment):
    score = analyser.polarity_scores(sentence)
    fd.write(sentiment)
    fd.write(str(score[sentiment]))
    fd.write("\n")

with open("content.txt","r") as tf1,open("result1.txt","r") as tf2:
    cnt = 1
    line = tf1.readline()
    line2 = tf2.readline()
    while line:
    	if(line2=="negative\n"):
    		analyse(line,'pos')
    	elif(line2=="positive\n"):
    		analyse(line,'neg')
    	line = tf1.readline()
    	line2 = tf2.readline()
    	cnt+=1
