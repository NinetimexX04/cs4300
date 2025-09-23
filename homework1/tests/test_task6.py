from src.task6 import count_words_in_file

def test_count_words_in_file():
    count = count_words_in_file("task6_read_me.txt")
    assert count == 162

def test_count_words_in_small_file():
    with open("small.txt", "w") as f:
        f.write("hello world")
    assert count_words_in_file("small.txt") == 2