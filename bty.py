from bs4 import BeautifulSoup
import re
import requests

class TopProjects:
     def __init__(self,url):
          self.url=url
          self.r=requests.get(self.url)
          self.text=self.r.text
          self.projects=[]
          '''getTopProjects(self)
          printTopProjects(self)'''

     def getTopProjects(self):
          print("trying to get")
          soup=BeautifulSoup(self.text,"html.parser")
          allProjects=soup.find_all("li",attrs={"class": "col-12 d-block width-full py-4 border-bottom public source"})
          noOfProjects=len(allProjects)
          for i in range(0,noOfProjects):
              thisProject={}
              thisProject['ProjectName']=allProjects[i].div.h3.a.text
              atags=allProjects[i].find("div",attrs={"class":'f6 text-gray mt-2'}).find_all("a")
              thisProject['Forks']=atags[1].text
              #add the redirect link here to get the committees
              self.projects.append(thisProject)

     def printTopProjects(self):
          total=len(self.projects)
          print("trying to print")
          for i in range(0,total):
               print(self.projects[i]['ProjectName'])
               print(self.projects[i]['Forks'])
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
