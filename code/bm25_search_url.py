from datetime import datetime
from elasticsearch import Elasticsearch
from feature_util import frequency_in_title, frequency_in_url, url_frequency


def BM25_search_title(test_file_path, result_file_path):
    es = Elasticsearch()
    print(datetime.now())
    with open(test_file_path, 'r', encoding='utf-8') as fr:
        with open(result_file_path, 'w', encoding='utf-8') as fw:
            lines = fr.read().splitlines(keepends=False)
            for line in lines:
                qid, query = line.split('\t')
                result = es.search(index='ir_index', doc_type="_doc", body={"query": {"match": {"content": query}}}, size=100)
                rank_list = []
                for answer in result['hits']['hits']:
                    BM25_score = answer['_score']
                    url_score = frequency_in_url(query.split(' '), answer['_source']['url'])
                    rank_list.append((BM25_score+url_score, answer['_source']['pid'], answer['_score']))
                rank_list.sort()
                rank_list = rank_list[::-1]
                rank = 1
                for result in rank_list[:10]:
                    fw.write(qid + '\t'
                                 + 'Q0\t'
                                 + result[1] + '\t'
                                 + str(rank) + '\t'
                                 + str(result[2]) + '\t'
                                 + 'IndriQueryLikelihood' + '\n')
                    rank += 1
                #print(query)
    print(datetime.now())

if __name__ == '__main__':
    BM25_search_title('../data/msmarco-test2019-queries.tsv', '../result/result_200_bm25_url_top10.txt')