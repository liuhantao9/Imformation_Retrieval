import untilize_ranking as ur
import sys

def main(argv):
    index_folder = argv[1]
    index_file = index_folder + "/inverted_index.json"
    document_id = index_folder + "/document_id_file.json"
    term_id = index_folder + "/term_id_file.json"
    search = ur.search(index_file, term_id, document_id, "Output.txt", argv[3], argv[2]+"/", argv[4])
    search.run_ranking()

if __name__ == "__main__":
    main(sys.argv)