from os import listdir
import xml.etree.ElementTree as ET
import csv
import re
import os

fd = open('text.csv','w')  
newFileWriter = csv.writer(fd)


def isBlank (myString):
    return not (myString and myString.strip())
    
for file in listdir("/home/haritha/Desktop/data/2018train/positive_examples/chunk1"):
  filename = "/home/haritha/Desktop/data/2018train/positive_examples/chunk1/"+file

  with open(filename, "rb") as data:
    tree = ET.parse(data)
    root = tree.getroot()
    

    for lst in root.findall('WRITING'):
        text = lst.find('TEXT').text
       
        text = os.linesep.join([s for s in text.splitlines() if s])
        cleanString = re.sub('[^a-zA-Z0-9\n\.]|[\\.]',' ', text )
        if isBlank(cleanString):
            continue
        newFileWriter.writerow([cleanString.lower()])
        
