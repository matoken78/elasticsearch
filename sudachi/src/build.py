import json
from elasticsearch import Elasticsearch

INDEX_NAME = 'test'

def create_es():
    return Elasticsearch(['192.168.99.100'],
                         port=9200,
                         use_ssl=False,
                         verify_certs=False)

def main(es, index_name):
    with open('.\index.json', mode='r', encoding='utf-8') as f:
        dic = json.load(f)
        if es.indices.exists(index_name):
            es.indices.delete(index_name)
        es.indices.create(index_name, dic)

if __name__ == '__main__':
    es = create_es()
    main(es, INDEX_NAME)
