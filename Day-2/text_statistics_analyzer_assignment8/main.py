# 8. Text Statistics Analyzer 
# Given: 
# text = """ 
# Python is powerful. 
# Python is simple. 
# Python is popular. 
# """ 
# Create functions to calculate: 
# ● Number of characters 
# ● Number of words 
# ● Number of sentences 
# ● Number of unique words 
# ● Most frequently occurring word 
# ● Longest word 
# ● Shortest word 

from utils import count_characters,count_words,count_sentences,get_unique_words,get_most_frequent_word,get_longest_word,get_shortest_word

def main() -> None:
    """
    Analyze the given text and display the results.
    """

    text = """
    Python is powerful.
    Python is simple.
    Python is popular.
    """

    print("Number of characters:", count_characters(text))
    print("Number of words:", count_words(text))
    print("Number of sentences:", count_sentences(text))
    print("Number of unique words:", len(get_unique_words(text)))
    print("Most frequent word:", get_most_frequent_word(text))
    print("Longest word:", get_longest_word(text))
    print("Shortest word:", get_shortest_word(text))


if __name__ == "__main__":
    main()


# Output
#
# Number of characters: 65
# Number of words: 9
# Number of sentences: 3
# Number of unique words: 7
# Most frequent word: python
# Longest word: powerful
# Shortest word: is