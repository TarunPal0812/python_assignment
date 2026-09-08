class TextAnalyzer:
    """
    Object-Oriented Text Analyzer for computing textual statistics.
    """

    def __init__(self, text: str) -> None:
        self.text: str = text

    def count_characters(self) -> int:
        """Count total characters in the text."""
        return len(self.text)

    def count_words(self) -> int:
        """Count total words in the text."""
        return len(self.text.split())

    def count_sentences(self) -> int:
        """Count sentences delimited by periods."""
        sentences = self.text.split(".")
        return sum(1 for s in sentences if s.strip())

    def get_clean_words(self) -> list[str]:
        """Extract lowercase words with trailing punctuation removed."""
        return self.text.lower().replace(".", "").split()

    def get_unique_words(self) -> set[str]:
        """Return set of unique words in text."""
        return set(self.get_clean_words())

    def get_most_frequent_word(self) -> str:
        """Return the most frequently occurring word."""
        words = self.get_clean_words()
        if not words:
            return ""

        freq: dict[str, int] = {}
        for word in words:
            freq[word] = freq.get(word, 0) + 1

        return max(freq, key=freq.get)

    def get_longest_word(self) -> str:
        """Return the longest word in text."""
        words = self.get_clean_words()
        if not words:
            return ""
        return max(words, key=len)

    def get_shortest_word(self) -> str:
        """Return the shortest word in text."""
        words = self.get_clean_words()
        if not words:
            return ""
        return min(words, key=len)

    def display_report(self) -> None:
        """Print summary report of all text metrics."""
        print("Number of characters:", self.count_characters())
        print("Number of words:", self.count_words())
        print("Number of sentences:", self.count_sentences())
        print("Number of unique words:", len(self.get_unique_words()))
        print("Most frequent word:", self.get_most_frequent_word())
        print("Longest word:", self.get_longest_word())
        print("Shortest word:", self.get_shortest_word())
