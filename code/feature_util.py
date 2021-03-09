from spellchecker import SpellChecker


def calculate_p_score(query, document):
    p_score = 1
    for query_term in query:
        if query_term in document:
            p_score += (document.index(query_term) + 1) / len(document)
        else:
            p_score += 1
    return p_score


def frequency_in_title(query, title):
    count = 0
    for query_term in query:
        if query_term in title:
            count += 1
    return count

def frequency_in_url(query, url):
    count = 0
    for query_term in query:
        if query_term in url:
            count += 1
    return count

def correct_query(query):
    spell = SpellChecker()
    new_query = []
    for term in query.split(' '):
        new_query.append(spell.correction(term))
    return ' '.join(new_query)


def document_frequency(query, document):
    count = 0
    for query_term in query:
        for document_term in document:
            if query_term == document_term:
                count += 1
    return count


def title_frequency(query, title):
    count = 0
    for query_term in query:
        for title_term in title:
            if query_term == title_term:
                count += 1
    return count


def url_frequency(query, url):
    count = 0
    for query_term in query:
        for url_term in url:
            if query_term in url_term:
                count += 1
    return count


def get_bm_25(pid, search_result):
    for document in search_result['hits']['hits']:
        if document['_source']['pid'] == pid:
            return document['_score']
    return 0


def get_url_length(url):
    url = url.split('/')[3:]
    count = 0
    for part in url:
        count += len(part.split('-'))
    return count
