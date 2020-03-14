import os
os.system("pip install requests")
os.system("pip install html5lib")
os.system("pip install bs4")

import requests
from bs4 import BeautifulSoup

url="https://www.photographyblog.com/"
response=requests.get(url)
htmlcontent=response.content           ##extracting response into html format


soup=BeautifulSoup(htmlcontent,'html.parser')
anchors=soup.find_all('a')


all_links=set()         #all_links is an empty set

for link in anchors:
	if link.get('href')!='#':
		all_links.add(link.get('href'))

print(all_links)     #Now, all_links set of unique links




#Making a file out of all_links set:
#===================
new_string="\n"

for link in all_links:
	new_string+=str(link)+"\n"

	
file=open('all_links_file.txt','w')
file.write(new_string)
file.close()

import re
pattern = r'^https'
file=open('final_links.txt','w')

for i,line in enumerate(open('all_links_file.txt')):
	for match in re.finditer(pattern, line):
		file.write(line)


file.close()
import os
os.remove("all_links_file.txt")


