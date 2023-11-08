from datetime import datetime
from elasticsearch import Elasticsearch 

es = Elasticsearch(hosts=('http://localhost:9200'))

doc = {
    'author': 'DMT',
    'text': 'ElasticSearch init',
    'timestamp': datetime.now(),
}

resp = es.index(index='test-index', id=1, document=doc)

print(resp['result'])

resp = es.get(index="test-index", id=1)
print(resp['_source'])

es.indices.refresh(index="test-index")

resp = es.search(index="test-index", query={"match_all": {}})
print("Got %d Hits:" % resp['hits']['total']['value'])
for hit in resp['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
