from bs4 import BeautifulSoup
from operator import itemgetter
import re
import requests

class TopProjects:
     def __init__(self,url):
          self.url=url
          self.r=requests.get(self.url,verify=True)
          #print(self.r)
          #print(self.r.content)
          self.text=self.r.content
          self.projects=[]
          '''getTopProjects(self)
          printTopProjects(self)'''
     def convertToNum(self,text):
          strnum=''
          for i in text:
               if i.isdigit():
                    strnum+=i;
          return int(strnum)

     def getTopProjects(self):
          print("trying to get")
          soup=BeautifulSoup(self.text,"html.parser")
          allProjects=soup.find_all("li",attrs={"class": "col-12 d-block width-full py-4 border-bottom public fork"})
          noOfProjects=len(allProjects)
          for i in range(0,noOfProjects):
              thisProject={}
              thisProject['Contributors']=[]
              thisProject['ProjectName']=allProjects[i].div.h3.a.text
              atags=allProjects[i].find("div",attrs={"class":'f6 text-gray mt-2'}).find_all("a")
              thisProject['Forks']=self.convertToNum(atags[1].text)#int(filter(str.isdigit, atags[1].text))
              thisProject['Link']=allProjects[i].div.h3.find("a")['href']
              thisProject['Link']="http://www.github.com"+thisProject['Link']
              projRequest=requests.get(thisProject['Link'])
             # print(projRequest)
              projContent=projRequest.content
              subSoup=BeautifulSoup(projContent,"html.parser")
              contributeLink=subSoup.find("div",attrs={"overall-summary overall-summary-bottomless"})
              #print(contributeLink)
              li_tag=contributeLink.find_all("li")
              c_link=li_tag[3].find("a")['href']
              c_link="http://www.github.com"+c_link
              projRequest=requests.get(c_link)
              print("the thrid request")
              print(projRequest)
              projContent=projRequest.content
              subSoup=BeautifulSoup(projContent,"html.parser")
              print(subSoup.find("div",attrs={"class":"graphs"}))
              #add the redirect link here to get the committees
              self.projects.append(thisProject)
          l=sorted(self.projects,key=itemgetter('Forks'),reverse=True)
          self.projects=l[0:5]
          

     def printTopProjects(self):
          total=len(self.projects)
          print("trying to print")
          for i in range(0,total):
               print(self.projects[i]['ProjectName'])
               print(self.projects[i]['Forks'])
               print(self.projects[i]['Link'])
               print('*****************')
          
          
url = raw_input("Enter a website to extract the URL's from: ")
o1=TopProjects(url)
o1.getTopProjects()
o1.printTopProjects()
              
"""
r  = requests.get("http://" +url)

data = r.text
#print(data)

soup = BeautifulSoup(data,"html.parser")

projects = soup.find_all("li",attrs={"class": "col-12 d-block width-full py-4 border-bottom public source"})

print(type(projects))
noOfProjects=len(projects)

print(projects[0].div.h3.a.text)
ace=projects[0].find("div",attrs={"class":'f6 text-gray mt-2'}).find_all("a")
print(ace[1])
print(ace[1].text)
#.find("svg",attrs={"svg":"octicon octicon-repo-forked"}))
print(projects[0].find("a",text=re.compile('>*<')))
print("************************")
print(projects[1])

'''
"""
