import tokenization as tk
import sys
import external_lib as exlib

def run_data_transformer(argv):
    transformer = tk.Tokenization(argv[1], int(argv[2]))
    transformer.run()
    exlib.record_transformer(transformer.total_file_size, len(transformer.token_set), len(transformer.token_list))
    print("Done!")


if __name__== "__main__":
    run_data_transformer(sys.argv)
