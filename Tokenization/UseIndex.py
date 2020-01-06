import index
import tokenization

def testIndex():
    path = "/Users/hantaoliu/Projects/Information_Retrieval/Crawler/HTML_files"
    num_file = 1000
    transformer = tokenization.Tokenization(path, num_file)
    indexer = index.Indexer(path, num_file, transformer)
    indexer.build_indexer()
    query = "crawler algorithm"
    check_query(indexer, query)

def get_term_ID(term, indexer):
    if term in indexer.term_id_file:
        return(list(indexer.term_id_file).index(term))

def get_ilist(term, indexer):
    return indexer.inverted_index[term]

def get_document_ID_list(term, indexer):
    list_document_id = list(indexer.inverted_index[term].keys())
    return list_document_id

def get_document_name(document_id, indexer):
    return list(indexer.document_id_file[document_id].keys())[0]

def check_query(indexer, query):
    word_list = query.split()
    for word in word_list:
        print_info(indexer, word, get_term_ID(word, indexer), get_ilist(word, indexer), get_document_ID_list(word, indexer))

def print_info(indexer, term, term_id, index_to_document, document_id_list):
    print("The term we search for is:                           ", term)
    print("The ID associated with the term is:                  ", term_id)
    print("The list of document that the term appears in are:   ", index_to_document)
    for id in document_id_list:
        print("ID: ", id, " Document Name: ", get_document_name(id, indexer))
    print()

if __name__ == "__main__":
    testIndex()
