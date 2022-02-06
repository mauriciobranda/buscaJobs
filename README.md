# buscaJobs

Mais um projeto que eu mesmo criei com o objetivo de "raspar" vagas dos portais de clientes da Gupy.

#Steps
##a) elastic.py - Servico deve estar no ar

##a.1) mainList.py - Raspagem no site da Gupy

##b) executar o app.py - front

#Como ?
Atraves de webscrapping em python com a lib BeautifulSoup4, o script acessa cada um dos sites dos  clientes e extrai dados como: nome da vaga e local.
Todos os registros sao salvos em um banco de dados ElasticSearch, o qual utilizo para consultas posteriormente.
Na parte de front end, atraves de Flask + HTML criei uma tela de buscas, a qual exibe os registros e atraves de um clique, voce pode chegar na fonte (vagas).
Todo o processo de busca ocorre utilizando query em Elastic Search.

.Tela Inicial

![Busca_Jobs_Tela_1](https://user-images.githubusercontent.com/36780203/124399942-566cc800-dcf5-11eb-9b1f-87d4f639648a.jpg)

.Resultados

![Busca_Jobs_Results](https://user-images.githubusercontent.com/36780203/124399946-5bca1280-dcf5-11eb-9b14-1a25ae591ec6.jpg)

