import re
import external_lib as exlib
import os

# Class handles data transformation and tokenization
class Tokenization:

    def __init__(self, path, num_file):
        self.path = path
        self.num_file = num_file
        self.total_file_size = 0
        self.token_set = set()
        self.token_list = list()
        self.name_list = list()

    # Read every document, parses all the words and make them a list
    def read_file(self, file_name):
        # Record the file size
        self.record_size(file_name)
        file = open(file_name, "r")

        res = re.findall(r"<\s*p[^>]*>(((.)|(\s))*?)<\s*/\s*p>", file.read())
        sentence = list()
        for text in res:
            line = re.sub("<[^>]*>", "", text[0])
            sentence.append(line)

        wordList = list()
        for text in sentence:
            words = re.findall(r"((([\w/\-\$'])|(\.(?!$)))+)|([^\s\w\(\)/\-\$@#&'\"%;,.])|\.$", text)
            for word in words:
                if not word[0] == '' and not word[0] == '/' and not word[0] == '.':
                    word_to_save = word[0]
                    if word_to_save.endswith("."):
                        word_to_save = word_to_save[:-1]
                    wordList.append(word_to_save)
                    self.record_token(word_to_save)
        file.close()
        return wordList

    # Record size
    def record_size(self, file_name):
        file_size = os.stat(file_name)
        self.total_file_size += file_size.st_size

    # Record unique token
    def record_token(self, word):
        self.token_set.add(word)
        self.token_list.append(word)

    def get_name_list(self):
        return self.name_list

    def save_name(self, file_name):
        file = open(file_name, "r")
        # Get name
        title = re.findall(r"<title>.*<\/title>", file.read())
        title = re.sub("<[^>]*>", "", title[0])
        self.name_list.append(title)
        file.close()


    # Get the word list from every document
    def run(self):
        documentWrodList = list()
        for i in range(self.num_file):
            file_name = self.path + "/" + exlib.count_digits(i + 1) + str(i + 1) + ".txt"
            self.save_name(file_name)
            # Add every document's token into a list
            documentWrodList.append(self.read_file(file_name))
        return documentWrodList


