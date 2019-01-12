# encoding=utf8
from bs4 import BeautifulSoup
import io
import json
from xlsxwriter import Workbook



def read_file():
    data=''
    with io.open("D:\\neco skola i rabota\\rabota\\ScrapingFbFriends\\html Data\\Mathew James Stirland.html", "r", encoding="utf-8") as my_file:
        data = my_file.read()
    # file=open("C:\\Users\\Neco\\Downloads\\New folder\\Mathew James Stirland.html")
    # data=file.read()
    # file.close()
    return data

file=Workbook("friends.xlsx")

workSheet=file.add_worksheet()
workSheet.write(0,0,'Name')
workSheet.write(0,1,'Facebook Id')
workSheet.write(0,2,'Profile Link')

htmlContent=read_file()
soup=BeautifulSoup(htmlContent,'lxml')
#friends=soup.find_all('li',attrs={'class':'_698'}) #3033
#friends=soup.find_all('a',attrs={'class':['_5q6s','_8o','_8t','lfloat','_ohe']}) 3041
friends=soup.find_all('div',attrs={'class':['fsl','fwb','fcb']}) #3042
i=1
for friend in friends:
    if friend.a is not None:
        #print(friend.a.string)
        if(friend.a.get('data-gt') is not None):
            #print(friend.a['href'])
            #print(friend.a.get('data-gt'))
            python_dict = dict(json.loads(friend.a.get('data-gt')))
            #print(python_dict)
            pom_dict=python_dict['engagement']
            #print(pom_dict['eng_tid'])
            pLink=friend.a['href']
            name=friend.a.string
            fb_id=pom_dict['eng_tid']
            print(name+" "+fb_id+" "+pLink)
            workSheet.write(i,0,name)
            workSheet.write(i, 1, fb_id)
            workSheet.write(i, 2, pLink)
            i=i+1
            #break

file.close()
print("finished")