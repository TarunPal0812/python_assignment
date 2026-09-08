from analyzer import WordFrequencyAnalyzer


def main() -> None:
    text = """
    Python is easy.
    Python is powerful.
    Python is widely used.
    """

    analyzer = WordFrequencyAnalyzer(text)

    word_frequency = analyzer.get_word_frequency()
    most_common = analyzer.get_most_common_word()
    unique_words = analyzer.get_unique_words()

    print("Word Frequency:")
    print(word_frequency)

    print("\nMost Common Word:")
    print(most_common)

    print("\nUnique Words:")
    print(unique_words)


if __name__ == "__main__":
    main()

# Output match Day-2:
# Word Frequency:
# {'python': 3, 'is': 3, 'easy': 1, 'powerful': 1, 'widely': 1, 'used': 1}
#
# Most Common Word:
# python
#
# Unique Words:
# {'python', 'is', 'easy', 'powerful', 'widely', 'used'}
