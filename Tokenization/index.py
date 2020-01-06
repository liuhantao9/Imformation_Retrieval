import sys
import json

class Indexer:

    # Initialize an indexer
    def __init__(self, path, num_file, transformer):
        self.path = path
        self.num_file = num_file
        self.transformer = transformer
        self.document_word_list = transformer.run()
        self.term_id_file = dict()
        self.document_id_file = dict()
        self.inverted_index = dict()

    def record_size_index(self):
        return sys.getsizeof(self.inverted_index)

    def build_indexer(self):

        # Go over every word list in every document
        for i, word_list in enumerate(self.document_word_list, 0):
            document_id = i + 1

            # Document ID File
            self.update_document_id(document_id, self.transformer.get_name_list()[i], len(word_list))

            # Term ID File
            self.update_term_file(word_list)
            for word in word_list:
                if word not in self.inverted_index:
                    # If the word is not int the dictionary
                    dn_dict = dict()
                    dn_dict[document_id] = 1
                    self.inverted_index[word] = dn_dict
                elif document_id not in self.inverted_index[word]:
                    self.inverted_index[word][document_id] = 1
                else:
                    self.inverted_index[word][document_id] = self.inverted_index[word][document_id] + 1

        # Create Json file store data
        self.dump_data()


    def update_term_file(self, word_list):
        unique_word = set()
        for word in word_list:
            if word not in unique_word:
                unique_word.add(word)
                # print(word)
                if word not in self.term_id_file:
                    self.term_id_file[word] = 1
                else:
                    self.term_id_file[word] = self.term_id_file[word] + 1

    def update_document_id(self, document_id, document_name, size):
        name_to_size = dict()
        name_to_size[document_name] = size
        self.document_id_file[document_id] = name_to_size

    def dump_data(self):
        with open("term_id_file.json", "w") as termID:
            json.dump(self.term_id_file, termID)
        termID.close()
        with open("document_id_file.json", "w") as documentID:
            json.dump(self.document_id_file, documentID)
        documentID.close()
        with open("inverted_index.json", "w") as inverIndex:
            json.dump(self.inverted_index, inverIndex)
        inverIndex.close()



