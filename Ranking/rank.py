import indexes
import math
import score_document
import heapq

class rank:

    # Initialize rank class
    def __init__(self, indexer):
        self.term_id = indexer.term_id
        self.document_id = indexer.document_id
        self.inverted_index = indexer.inverted_index
        self.score_ranking = list()
        self.doc_term_contrib = dict()

    def get_tf_by_term(self, term):
        sum_tf = 0
        for d in self.inverted_index.get(term).keys():
            sum_tf += 1 + math.log10(self.inverted_index.get(term).get(d))
        return sum_tf

    # Compute tf-idf score for one query
    def compute_query_tf_idf(self, query):
        list_term = query.split(" ")
        denominator = 0
        list_tf_idf = list()
        for term in list_term:
            if self.inverted_index.get(term) is None:
                list_tf_idf.append(0)
                continue
            idf = math.log10(len(self.document_id.keys())/len(self.inverted_index.get(term).keys()))
            tf = self.get_tf_by_term(term)
            denominator += (tf * idf) * (tf * idf)
            list_tf_idf.append((tf * idf))
        denominator = 1 if denominator == 0 else denominator
        return self.normalization(list_tf_idf, math.sqrt(denominator))

    def get_tf_by_document(self, query, d):
        list_term = query.split(" ")
        list_tf_idf = list()
        denominator = 0
        for term in list_term:
            if self.inverted_index.get(term) is None or self.inverted_index.get(term).get(d) is None:
                list_tf_idf.append(0)
                continue
            tf = 1 + math.log10(self.inverted_index.get(term).get(d))
            denominator += tf * tf
            list_tf_idf.append(tf)
        denominator = 1 if denominator == 0 else denominator
        return self.normalization(list_tf_idf, math.sqrt(denominator))

    # Get the score for the given query
    def get_score(self, query):
        query_tf_idf = self.compute_query_tf_idf(query)
        for d in self.document_id.keys():
            score = self.cosine_similarity(d, query_tf_idf, self.get_tf_by_document(query, d))
            sd = score_document.score_document(d, score)
            heapq.heappush(self.score_ranking, sd)

    def cosine_similarity(self, doc_id, query_tf_idf, document_tf_idf):
        if not len(query_tf_idf) == len(document_tf_idf):
            raise Exception('Two list should be the same length')
        score = 0
        word_contrib = list()
        for q, d in zip(query_tf_idf, document_tf_idf):
            score += q * d
            word_contrib.append(q * d)
        self.doc_term_contrib[doc_id] = word_contrib
        return score

    def get_top_k(self, k, query):
        self.get_score(query)
        top_k = list()
        for i in range(k):
            top_k.append(heapq.heappop(self.score_ranking))
        return top_k

    def normalization(self, list_tf_idf, normal_factor):
        normalized_tf_idf = list()
        for tfidf in list_tf_idf:
            normalized_tf_idf.append(tfidf / normal_factor)
        return normalized_tf_idf




