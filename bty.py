from bs4 import BeautifulSoup
from operator import itemgetter
import re
import requests
''' The following class extracts the top 5 projects along with top commitees
     Beautiful soup has been used to parse the html content '''
class TopProjects:
     def __init__(self,url):
          self.url=url
          self.r=requests.get(self.url,verify=True)
          print(self.r)
          #print(self.r.content)
          self.text=self.r.content
          self.projects=[]
         
     '''The following convertToNum function return the number in the given text - this was necessary to
                                                                                                                                                 get the number of forks and commits only '''     
     def convertToNum(self,text):
          strnum=''
          for i in text:
               if i.isdigit():
                    strnum+=i;
          return int(strnum)
     '''The function that accesses the html content on the webpage of the given organization
               projects are obtained and then they are sorted based on the number of forks'''
     def getTopProjects(self):
          print("trying to get")
          soup=BeautifulSoup(self.text,"html.parser")
          allProjects=soup.find_all("li",attrs={"class": "col-12 d-block width-full py-4 border-bottom public fork"}) #extracts all the projects
          
          noOfProjects=len(allProjects)
          print(noOfProjects)
          for i in range(0,noOfProjects):
               
               thisProject={}
               thisProject['Contributors']=[]
               thisProject['ProjectName']=allProjects[i].div.h3.a.text
               atags=allProjects[i].find("div",attrs={"class":'f6 text-gray mt-2'}).find_all("a")
               thisProject['Forks']=self.convertToNum(atags[1].text)
               thisProject['Link']=allProjects[i].div.h3.find("a")['href']
               thisProject['Link']="http://www.github.com"+thisProject['Link']+"/graphs/contributors"       #link to access the contritors page       
               '''
               projRequest=requests.get(thisProject['Link'])
               print(projRequest)
               c=projRequest.content
               soup=BeautifulSoup(c,"html.parser")
               print(soup)'''
               self.projects.append(thisProject)
          l=sorted(self.projects,key=itemgetter('Forks'),reverse=True)#sorts the projects according to forks
          self.projects=l[0:5]#obtains the top most projects by forks
          

     def printTopProjects(self):
          total=len(self.projects)
          print("trying to print")
          for i in range(0,total):
               print(self.projects[i]['ProjectName'])
               print(self.projects[i]['Forks'])
               print(self.projects[i]['Link'])
               print('*****************')
          
          
url = raw_input("Enter an organization's name to extract from: ")
url="https://github.com/"+url+"?utf8=%E2%9C%93&q=&type=fork&language="
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
