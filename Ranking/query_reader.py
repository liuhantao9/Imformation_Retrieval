class query_reader:

    def __init__(self, document):
        self.document = document
        self.queries = list()
        self.read()

    def read(self):
        with open(self.document, "r") as file:
            line = file.readline()
            while line:
                self.queries.append(line)
                line = file.readline()
        file.close()

