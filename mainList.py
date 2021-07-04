#Webscrapping vagas Gupy

import requests, json, copy
from bs4 import BeautifulSoup

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

#extrator Gupy
def consultaVagas(companycode):
    print("################")
    print("CONSULTANDO COMPANY CODE: "+str(companycode))
    print("################")
    if companycode == 1:
        companyName = 'randon'
    elif companycode == 2:
        companyName = 'soprano'
    elif companycode == 3:
        companyName = 'promob'
    elif companycode == 4:
        companyName = 'totvs'
    else:
        print ("companycode non ecziste!")

    url = 'https://'+companyName+'.gupy.io/'

    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')

    # find a list of all span elements
    spans = soup.find_all('span', {'class' : 'title'})

    # create a list of lines corresponding to element texts
    lines = [span.get_text() for span in spans]

    #coletando job link
    data = soup.findAll('a',attrs={'class':'job-list__item'})
    #coletando job description
    spans = soup.findAll('span', {'class' : 'title'})

    #coletando e tratando a localizacao
    dataLocal = soup.findAll('tr')#,attrs={'data-workplace':'Caxias do Sul'})

    my_listLocal = []
    for t in dataLocal:
        linkos = t.findAll('td')
        counti = 1
        for x in linkos:
            linkas = x.findAll('strong')
            #print(linkas)
            linkasF = str(linkas).replace("<strong>","").replace("</strong>","").replace("[]","")#.replace("]","").replace("[","")

            linkasF = ' '.join(linkasF.split())

            if linkasF == '[ ]':
                linkasF = "Verificar"

            linkasG = linkasF.replace("]","").replace("[","")
            
            #print(linkasG[0:30])

            #indexando as localizacao
            my_listLocal.append(linkasG)

            counti = counti + 1

#finalmente vou passar para a lista
    my_listLocalB = []
    countii = 0
    while countii < len(my_listLocal):
    
        if len(my_listLocal[countii]) < 1:
            ok = 1
        else:
            my_listLocalB.append(my_listLocal[countii])
            #print(my_listLocal[countii] + " " +str(countii))

        countii = countii + 1

    contaNo = 0
    while contaNo < len(my_listLocalB):
        #print("Looooop do my_listLocalB")
        #print(my_listLocalB[contaNo])
        contaNo = contaNo + 1

#indexando as URLS
    my_listURL = []
    for a in data:
        links = a.findAll('href')
        my_listURL.append(a['href'])
        #print(a['href'])


#indexando os titulos das vagas
    my_listTituloVaga = []
    for a in spans:
        links = a.findAll('title')
        my_listTituloVaga.append(a.text)

#para verificar se tem os cadastros
    #print('***********Tamanho das listas***********')
    #print("Lista de Titutos de Vagas: " + str(len(my_listTituloVaga)))
    #print("Lista de URLs: " + str(len(my_listURL)))
    #print("Lista de Localizacoes: " + str(len(my_listLocalB)))

#indexando todas as listas de cima
    a_dict = {}
    keyList = ["title", "url", "localizacao"]
    for i in keyList: 
        a_dict[i] = None

    finalList = []
    conta = 0
    while conta < len(my_listURL):
        #finalList.append(my_listTituloVaga[conta]+';'+url+my_listA[conta])
        
        a_dict = {'companyName': companyName,'title': my_listTituloVaga[conta],'url': url+my_listURL[conta], 'localizacao': my_listLocalB[conta]}
        finalList.append(dict(a_dict))
        #print(a_dict)
        conta += 1
    
    return finalList

contador = 1
while contador < 7:
    your_list_as_json = json.dumps(consultaVagas(contador),indent=1, sort_keys=True, ensure_ascii=False) 
    print(your_list_as_json)
    contador = contador + 1

y = json.loads(your_list_as_json)

#print(y)