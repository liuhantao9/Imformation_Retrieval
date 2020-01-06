import json
class indexes:

    def __init__(self, index_file, term_id_file, document_id_file):
        self.term_id = dict()
        self.document_id = dict()
        self.inverted_index = dict()
        self.read(index_file, term_id_file, document_id_file)


    def read(self, index_file, term_id_file, document_id_file):
        self.term_id = json.load(open(term_id_file, "r"))
        self.document_id = json.load(open(document_id_file, "r"))
        self.inverted_index = json.load(open(index_file, "r"))