
import requests
from bs4 import BeautifulSoup

with open("data/times.html") as f:
    content = f.read()

soup = BeautifulSoup(content, "html.parser")
#print(soup.prettify())
print(soup.title)
print(soup.title.string)
print(soup.div)
#print(soup.find_all("div"))

for link in soup.find_all("a"):
    #print(link.get('href'))
    print(link.getText())
    
    
s = soup.find(id="videoPlayer")
s = soup.find(class_="videoPlayer")

print(s)
