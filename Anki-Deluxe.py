# Make function to extract img files
from bs4 import BeautifulSoup as BSHTML

def extract(img_tag):
    htmlText = img_tag
    soup = BSHTML(htmlText)
    images = soup.findAll('img')
    for image in images:
        return str(image['src'])

# Read Anki text file, refine content

import csv

with open('C:/Users/______/AppData/Roaming/Anki2/_________.txt', encoding = 'utf-8') as file: 
    #The text file dir must be in the %appdata% folder, you find the name of the text you have exported
    new = file.readlines()
lines = [line.rstrip('\n').split('\t') for line in new]

# Make list of content to write in csv files
full = []
img_files = []
for line in lines:
    item = ['', '', '', '']

    for part in line:
        index = line.index(part)
        if 'src' in part:
            file = extract(part.replace('\"\"', '\"'))
            item[2 + index] = file
            img_files.append(file)
            print(file)
        else:
            item[0 + index] = part
    full.append(item)

# Get images to Flashcards Deluxe location
path = 'C:/Users/_________/AppData/Roaming/Anki2/User 1/collection.media/'
    #The dir also from %appdata% just like from line 15

import shutil
[shutil.copy(path+img, 'E:/AnkiDeluxe') for img in img_files]

# Write csv file to import in FD
with open('E:/AnkiDeluxe/deluxe.txt', 'w') as file:
    file_write = csv.writer(file, delimiter='\t')
    file_write.writerow(['Text 1', 'Text 2', 'Picture 1', 'Picture 2'])
    [file_write.writerow(line) for line in full]

