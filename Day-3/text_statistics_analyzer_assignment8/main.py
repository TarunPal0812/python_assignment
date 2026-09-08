from analyzer import TextAnalyzer


def main() -> None:
    text = """
    Python is powerful.
    Python is simple.
    Python is popular.
    """

    analyzer = TextAnalyzer(text)
    analyzer.display_report()


if __name__ == "__main__":
    main()

# Output
# Number of characters: 65
# Number of words: 9
# Number of sentences: 3
# Number of unique words: 7
# Most frequent word: python
# Longest word: powerful
# Shortest word: is
