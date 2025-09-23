def count_words_in_file(filename):
    with open(filename, "r") as f:
        text = f.read()
    return len(text.split())
