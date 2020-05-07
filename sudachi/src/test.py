from pprint import pprint
from build import INDEX_NAME, create_es

if __name__ == '__main__':
    phrase = 'KingGnuは歌が独特で良いね'
    body = {
        'analyzer': 'sudachi_analyzer',
        'text': phrase
    }
    es = create_es()
    pprint(es.indices.analyze(index=INDEX_NAME, body=body))