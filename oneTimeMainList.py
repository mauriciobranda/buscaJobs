import requests 
from bs4 import BeautifulSoup 


url = 'https://www.gupy.io/login/'
reqs = requests.get(url) 
soup = BeautifulSoup(reqs.text, 'html.parser') 


urls = []
my_listURL = []
count = 0
for link in soup.find_all('a'): 
	#print(link.get('href'))
    #links = a.findAll('href')
    my_listURL.append(link.get('href'))


contaaa = 0
while  contaaa < len(my_listURL):
    print(my_listURL[contaaa])

contaaa = contaaa + 1
