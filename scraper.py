from bs4 import BeautifulSoup
from datetime import *
import requests

file = open("Headlines.txt","w")

url = "http://www.theonion.com/article/mar-lago-member-complains-about-loud-obnoxious-cab-55311"

r = requests.get(url)

html_doc = r.text

soup = BeautifulSoup(html_doc, "html.parser")

'''for link in soup.find_all('h2'):
    #file.write(link)
    print(link.get('href'))
'''

#headline = soup.find_all('h2',attrs={'class': 'headline'})
#for h in headline:
#    print(headline[h].text)

title = soup.title.string
datetime = datetime.now()

formatted_title = title + "\n" + str(datetime)

print(formatted_title)
file.write(formatted_title)

file.close()
