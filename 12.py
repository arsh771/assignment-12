#Q1
import datetime as d
date=d.date.today()
print('DATE IS:',date)
print('WEEKDAY IS:',date.strftime("%A"))


#Q2
import webbrowser
webbrowser.open("https://www.w3schools.com/python/default.asp")


#Q3

import os,sys
folder = r'C:\Users\toshibap750\Desktop\assignment12'
for file in os.listdir(folder):
    infile = os.path.join(folder,file)
    if not os.path.isfile(infile):
        continue
    oldbase = os.path.splitext(file)
    newname = infile.replace('.txt', '.jpg')
    output = os.rename(infile, newname)
