from datetime import datetime
from elasticsearch import Elasticsearch


def BM25_search(test_file_path, result_file_path):
    es = Elasticsearch()
    print(datetime.now())
    with open(test_file_path, 'r', encoding='utf-8') as fr:
        with open(result_file_path, 'w', encoding='utf-8') as fw:
            lines = fr.read().splitlines(keepends=False)
            for line in lines:
                qid, query = line.split('\t')
                result = es.search(index='ir_index', doc_type="_doc", body={"query": {"match": {"content": query}}}, size=10)
                rank = 1
                for answer in result['hits']['hits']:
                    fw.write(qid + "\t"
                                 + "Q0\t"
                                 + answer['_source']['pid'] + "\t"
                                 + str(rank) + "\t"
                                 + str(answer['_score']) + "\t"
                                 + "IndriQueryLikelihood" + "\n")
                    rank += 1
                #print(query)
    print(datetime.now())

if __name__ == '__main__':
    BM25_search('../data/msmarco-test2019-queries.tsv', '../result/result_200_bm25_top10.txt')



