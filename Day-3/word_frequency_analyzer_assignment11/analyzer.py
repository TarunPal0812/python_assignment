class WordFrequencyAnalyzer:
    """
    Object-Oriented Word Frequency Analyzer.
    """

    def __init__(self, text: str) -> None:
        self.text: str = text
        self._frequency: dict[str, int] | None = None

    def get_word_frequency(self) -> dict[str, int]:
        """Calculate and cache word frequency dictionary."""
        if self._frequency is None:
            clean_text = self.text.lower().replace(".", "")
            words = clean_text.split()

            self._frequency = {}
            for word in words:
                self._frequency[word] = self._frequency.get(word, 0) + 1

        return self._frequency.copy()

    def get_most_common_word(self) -> str:
        """Return the word with the highest frequency."""
        freq = self.get_word_frequency()
        if not freq:
            raise ValueError("Text cannot be empty.")
        return max(freq, key=freq.get)

    def get_unique_words(self) -> set[str]:
        """Return set of all unique words."""
        freq = self.get_word_frequency()
        return set(freq.keys())
