def count_characters(text: str) -> int:
    """
    Count the number of characters in the text.

    Args:
        text: The text to analyze.

    Returns:
        Number of characters.
    """

    return len(text)


def count_words(text: str) -> int:
    """
    Count the number of words in the text.

    Args:
        text: The text to analyze.

    Returns:
        Number of words.
    """

    words = text.split()

    return len(words)


def count_sentences(text: str) -> int:
    """
    Count the number of sentences in the text.

    Args:
        text: The text to analyze.

    Returns:
        Number of sentences.
    """

    sentences = text.split(".")

    count = 0

    for sentence in sentences:
        if sentence.strip():
            count += 1

    return count


def get_unique_words(text: str) -> set[str]:
    """
    Find all unique words in the text.

    Args:
        text: The text to analyze.

    Returns:
        A set containing unique words.
    """

    words = text.lower().replace(".", "").split()

    return set(words)


def get_most_frequent_word(text: str) -> str:
    """
    Find the most frequently occurring word.

    Args:
        text: The text to analyze.

    Returns:
        The most frequently occurring word.
    """

    words = text.lower().replace(".", "").split()

    if not words:
        return ""

    most_frequent = words[0]
    highest_count = words.count(words[0])

    for word in words:
        count = words.count(word)

        if count > highest_count:
            highest_count = count
            most_frequent = word

    return most_frequent


def get_longest_word(text: str) -> str:
    """
    Find the longest word in the text.

    Args:
        text: The text to analyze.

    Returns:
        The longest word.
    """

    words = text.lower().replace(".", "").split()

    if not words:
        return ""

    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


def get_shortest_word(text: str) -> str:
    """
    Find the shortest word in the text.

    Args:
        text: The text to analyze.

    Returns:
        The shortest word.
    """

    words = text.lower().replace(".", "").split()

    if not words:
        return ""

    shortest = words[0]

    for word in words:
        if len(word) < len(shortest):
            shortest = word

    return shortest