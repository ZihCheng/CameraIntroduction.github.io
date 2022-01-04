
from bs4 import BeautifulSoup
from urllib.request import urlopen
import os

path="/Users/zicheng/Desktop/CameraIntroduction.github.io-main/pages/canon"
a=os.listdir(path)
re=urlopen("file:change.html")
s=BeautifulSoup(re,'lxml')
r4=s.find("div",{"class":"wrapper row4 bgded overlay"})
for i in range(len(a)):
    if a[i][0]!="." and a[i][-5:]==".html" and a[i]!="change.html":
        response=urlopen("file:"+a[i])
        soup=BeautifulSoup(response,'lxml')
        for j in soup.findAll("div",{"class":"wrapper row4 bgded overlay"}):
            j.replace_with(r4)
        for k in soup.findAll("div",{"class":"wrapper row5"}):
            k.replace_with("")
    if a[i][0]!="." and a[i][-5:]==".html" and a[i]!="change.html":
        with open(a[i],'w')as wr:
            wr.write(str(soup.prettify()))
            
            
            
            
        