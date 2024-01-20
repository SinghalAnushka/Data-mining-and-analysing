import requests
from bs4 import BeautifulSoup
url="https://insights.blackcoffer.com/ai-in-healthcare-to-improve-patient-outcomes/"
page=requests.get(url)
soup=BeautifulSoup(page.content,"html.parser")
a=soup.title.string+soup.get_text()
b=a.split()


with open('.\StopWords_Geographic.txt',"r") as file:
  sgeo=file.read()
SGeo=sgeo.split()
with open('StopWords_GenericLong.txt',"r") as file:
  sgl=file.read()
SGL=sgl.split()
with open('StopWords_Generic.txt',"r") as file:
  sg=file.read()
SG=sg.split()
with open('StopWords_DatesandNumbers.txt',"r") as file:
  sdn=file.read()
SDN=sdn.split()
with open('/StopWords_Currencies.txt',"r",encoding="ISO-8859-1") as file:
  sc=file.read()
SC=sc.split()
with open('/StopWords_Auditor.txt',"r") as file:
  sa=file.read()
SA=sa.split()
S=SN+SGL+SG+SDN+SC+SA+SGeo
for i in p[:]:
  for j in S:
    if i==j:
      p.remove(i)
for i in N[:]:
  for j in S:
    if i==j:
      N.remove(i)
cp=0
for i in p:
  b.count(i)
  cp+=b.count(i)
print(cp)
cn=0
for i in N:
  b.count(i)
  cn+=b.count(i)
print(cn)