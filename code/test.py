import constants
from elasticsearch import Elasticsearch

def getTermVector(doc_id):
    temp = dict()
    a = constants.ES_CLIENT.termvector(index = constants.INDEX_NAME,
                                    doc_type = constants.TYPE_NAME,
                                    id = doc_id,
                                    field_statistics = True,
                                    fields = ['text._analyzed'],
                                    term_statistics = True
                                )
    curr_termvec = a["term_vectors"]["text._analyzed"]["terms"]
    tokens = curr_termvec.keys()
    [temp.update({token : {"tf": curr_termvec[token]["term_freq"]}}) for token in tokens]
    return a["_id"], temp



