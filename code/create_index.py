from datetime import datetime
from elasticsearch import Elasticsearch

def build_index(file_path):
    es = Elasticsearch()
    #es.indices.delete(index='ir_doc_title_index')
    es.indices.create(index="ir_doc_title_index")
    with open(file_path, 'r', encoding='utf-8') as f:
        line = f.readline()
        i = 1
        while line != '':
            line = line[:-1]
            pid, url, title, content = line.split('\t')
            es.index(index='ir_doc_title_index', doc_type='_doc', id=i, body={'pid': pid, 'url':url, 'content': title + " " + content})
            line = f.readline()
            if i % 10000 == 0:
                result = es.get(index='ir_doc_title_index', id=i)
                print(result)
                print(i)
            i += 1


if __name__ == '__main__':
    build_index('../data/msmarco-docs.tsv')

