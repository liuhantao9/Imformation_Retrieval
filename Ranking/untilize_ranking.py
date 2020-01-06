import rank
import re
import indexes
import external_lib as exl

class search:
    def __init__(self, index_file, term_id_file, document_id_file, output_file, query_file, files_content, k):
        self.indexer = indexes.indexes(index_file, term_id_file, document_id_file)
        self.op_file = output_file
        self.queries = query_file
        self.term_id = self.indexer.term_id
        self.document_id = self.indexer.document_id
        self.inverted_index = self.indexer.inverted_index
        self.file_contents = files_content
        self.k = int(k)

    def run_ranking(self):
        file = open(self.queries, "r")
        query = file.readline().rstrip()
        with open(self.op_file, "w+") as output:
            while query:
                rank_sys = rank.rank(self.indexer)
                list_top_k = rank_sys.get_top_k(self.k, query)
                self.record(rank_sys, query, list_top_k, output)
                print("Done with query: ", query)
                query = file.readline().rstrip()
                output.write("\n")
                output.write("\n")
        output.close()
        file.close()

    def record(self, rank_sys, query, top_k, output):
            output.write(query + "\n")
            output.write(str(query.split(" ")) + "\n")
            for r in top_k:
                score = r.score
                doc_id = r.id
                output.write("ID: " + doc_id + " Document Name: " + list(self.document_id[doc_id].keys())[0] + "\n")
                output.write(self.get_doc_info(doc_id) + "\n")
                output.write("Score: " + str(score) + "\n")
                output.write(self.get_contrib_by_term(rank_sys, doc_id, query) + "\n")
                output.write("\n")

    def get_doc_info(self, doc_id):
        name = self.file_contents + exl.count_digits(int(doc_id)) + doc_id + ".txt"
        file = open(name, "r")
        res = re.findall(r"<\s*p[^>]*>(((.)|(\s))*?)<\s*/\s*p>", file.read())
        sentence = ""
        for text in res:
            line = re.sub("<[^>]*>", "", text[0])
            line = line.replace('\n', '')
            sentence += line.rstrip()
        file.close()
        return sentence[0:200] + "..." if len(sentence) >= 200 else sentence[0:-1]

    def get_contrib_by_term(self, rank_sys, doc_id, query):
        word_contrib = rank_sys.doc_term_contrib[doc_id]
        terms = query.split(" ")
        res = ""
        for (term, contribution) in zip(terms, word_contrib):
             res += term + ": " + str(contribution) + "; "
        return res
