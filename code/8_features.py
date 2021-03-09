from elasticsearch import Elasticsearch
from feature_util import get_url_length

es = Elasticsearch()
with open("../data/200_test.dat", "r", encoding="utf-8") as f1:
    with open("../data/msmarco-doctest2019-top100", "r", encoding="utf-8") as f2:
        with open("../data/200_test_8_features.dat", "w", encoding="utf-8") as f3:
            line1 = f1.readline()[:-1]
            line2 = f2.readline()[:-1]
            i = 0
            while line1 != '':
                _, _, docid, _, _, _ = line2.split(' ')
                get_document_result = es.search(index='ir_index', doc_type="_doc", body={"query": {"match": {"pid": docid}}})['hits']['hits'][0]['_source']
                document = get_document_result['content']
                title = get_document_result['title']
                url = get_document_result['url']
                document_length = len(document.split(' '))
                title_length = len(title.split(' '))
                url_length = get_url_length(url)
                f3.write(line1+" 6:"+str(document_length)+" 7:"+str(title_length)+" 8:"+str(url_length)+"\n")
                line1 = f1.readline()[:-1]
                line2 = f2.readline()[:-1]
                i += 1
                if i % 1000 == 0:
                    print(i)
