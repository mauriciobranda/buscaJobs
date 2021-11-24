#Our Python  Application will be our Web Framework and we will render our html files using jinja templates.
import json 
from flask import Flask, render_template, request
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch()

@app.route('/')
def home():
    cidades = ['Santos/SP','Caxias do Sul/RS'] #teria que ser dinamico
    data_size = len(cidades)
    return render_template('search.html', cidades=cidades, data_size=data_size)


@app.route('/search/results', methods=['GET', 'POST'])
def search_request():
    search_term = request.form["input"]
    search_term_location = request.form["input-location"]
    print(search_term)

    # Abaixo o que vai devolver para o results.html
    # Lembrar de trocar o meu INDEX
    res1 = es.search(index="gupy", doc_type='vagas', body={
        "size": 10000,
        'query': {
            'multi_match': {
                    "query": str(search_term), 
                    "fields": [
                        "title", "companyName"
                    ] , "fuzziness": 2
                }
        }   
    })
    

    for hit in res1['hits']['hits']:
        print(hit['_source']['title'])
        print(hit['_score'])
        print('*********************')
   
    response_hits = res1['hits']['hits']

    if len(response_hits) > 1:

        response_hits = res1['hits']['hits']
        #print ('\nnumber of hits:', len(response_hits))

        # use enumerate() to iterate list of documents:
        for num, doc in enumerate(response_hits):
            # get the document ID
            print ('title:', doc['_source']['title'], 'score:', doc['_score']) 

    return render_template('results.html', res=res1, search_term=search_term )

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host='0.0.0.0', port=5000)

