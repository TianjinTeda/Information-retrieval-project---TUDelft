from elasticsearch import Elasticsearch
import pandas as pd
import csv
from feature_util import *


def read_quries(file_path):
    query_dict = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        line = f.readline()
        i = 0
        while line != "":
            qid, query = line.split('\t')
            query_dict[qid] = query
            if i % 10000 == 0:
                print(i)
            i += 1
            line = f.readline()
    return query_dict


def make_data(query_file_path, train_file_path, data_file_path):
    es = Elasticsearch()
    query_dict = read_quries(query_file_path)
    with open(data_file_path, "w", encoding='utf-8') as fw:
        with open(train_file_path, 'r', encoding='utf-8') as f:
            l = f.readline()
            i = 0
            while l != '':
                qid, _, docid, _, _, _ = l.split(' ')
                query = query_dict[qid]
                search_document_result = es.search(index='ir_index', doc_type="_doc", body={"query": {"match": {"content": query}}}, size=200)
                search_document_title_result = es.search(index='ir_doc_title_index', doc_type="_doc", body={"query": {"match": {"content": query}}}, size=200)
                bm_25_document = get_bm_25(docid, search_document_result)
                bm_25_document_title = get_bm_25(docid, search_document_title_result)
                get_document_result = es.search(index='ir_index', doc_type="_doc", body={"query": {"match": {"pid": docid}}})['hits']['hits'][0]['_source']
                document = get_document_result['content']
                title = get_document_result['title']
                url = get_document_result['url']
                document_length = len(document.split(' '))
                title_length = len(title.split(' '))
                url_length = len(url)
                document_fr = document_frequency(query.split(' '), document.split(' '))
                title_fr = title_frequency(query.split(' '), title.split(' '))
                url_fr = url_frequency(query.split(' '), url.split('/'))
                fw.write(qid+'\t'+docid+'\t'+str(bm_25_document)+'\t'+str(bm_25_document_title)+'\t'+str(document_fr)+'\t'+str(title_fr)+'\t'+str(url_fr)+'\t'+
                         str(document_length)+'\t'+str(title_length)+'\t'+str(url_length)+'\n')

                for j in range(0, 9):
                    f.readline()
                    i += 1
                l = f.readline()
                i += 1
                if i % 10 == 0:
                    print(i)
                if i == 100000:
                    return


if __name__ == "__main__":
    make_data('../data/queries.doctrain.tsv', '../data/msmarco-doctrain-top100', '../data/train_8_features.tsv')