def isnumber(word):
    try:
        float(word)
        return True
    except ValueError:
        return False

# Count the digits
def count_digits(num):
    prefix = "000"
    if len(str(abs(num))) == 4:
        prefix = ""
    elif len(str(abs(num))) == 3:
        prefix = "0"
    elif len(str(abs(num))) == 2:
        prefix = "00"
    elif len(str(abs(num))) == 1:
        prefix = "000"
    return prefix

def record_transformer(file_size, unique_token, num_token):
    file = open("stats_tokenization.txt", "w+")
    file.write("Total file size:        " + str(file_size) + "\n")
    file.write("Number of unique Token: " + str(unique_token) + "\n")
    file.write("Number of tokens:       " + str(num_token) + "\n")


def record_inderex(file_size, unique_token, num_token, index_size):
    file = open("stats.txt", "w+")
    file.write("Total file size:        " + str(file_size) + "\n")
    file.write("Number of unique Token: " + str(unique_token) + "\n")
    file.write("Number of tokens:       " + str(num_token) + "\n")
    file.write("Size of index:          " + str(index_size) + "\n")
    file.write("Ratio of index to file: " + str(index_size / file_size) + "\n")
    file.close()