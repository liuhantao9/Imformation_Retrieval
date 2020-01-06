import index
import tokenization
import external_lib as exlib
import sys

def create_index(agrv):
    transformer = tokenization.Tokenization(agrv[1], int(agrv[2]))
    indexer = index.Indexer(agrv[1], int(agrv[2]), transformer)
    # Build the record
    exlib.record_inderex(transformer.total_file_size, len(transformer.token_set), len(transformer.token_list), indexer.record_size_index())
    print("Done!")

if __name__ == "__main__":
    create_index(sys.argv)




