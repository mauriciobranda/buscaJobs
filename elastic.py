# CARGA de Vagas no ES
# https://medium.com/naukri-engineering/elasticsearch-tutorial-for-beginners-using-python-b9cb48edcedc
# 
# 
# from datetime import datetime
import mainList, json, datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()
countEmp = 1

while countEmp < 100:
    mlista = mainList.consultaVagas(countEmp) # EMPRESA QUE VAI SER LISTADA 
    your_list_as_json = json.dumps(mlista,indent=1, sort_keys=True, ensure_ascii=False)
    y = json.loads(your_list_as_json)
    print(y)
    tamanhoList = len(y)
    print(tamanhoList)
    count = 0
    while count < tamanhoList :
        #indexando resultados
        es.index(index="gupy", doc_type='vagas', id=str(count)+str(countEmp), body=y[count])
        print(y[count])

        count=count+1

    countEmp=countEmp+1