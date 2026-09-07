# Given: 
# text = """ 
# Python is easy. 
# Python is powerful. 
# Python is widely used. 
# """ 
# Return: 
# { 
# } 
# "python": 3, 
# "is": 3, 
# "easy": 1, 
# "powerful": 1, 
# "widely": 1, 
# "used": 1 
# Create functions: 
# get_word_frequency() 
# get_most_common_word() 
# get_unique_words() 

def get_word_frequency(text: str) -> dict[str, int]:
    """
    Calculate the frequency of each word in the given text.

    Args:
        text: The input text whose words will be counted.

    Returns:
        A dictionary where keys are words and values are
        their frequencies.
    """

    text = text.lower()
    text = text.replace(".", "")
    words: list[str] = text.split()

    frequency: dict[str, int] = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency


def get_most_common_word(text: str) -> str:
    """
    Find the most frequently occurring word in the text.

    Args:
        text: The input text to analyze.

    Returns:
        The word with the highest frequency.

    Raises:
        ValueError: If the provided text contains no words.
    """

    frequency: dict[str, int] = get_word_frequency(text)

    if not frequency:
        raise ValueError("Text cannot be empty.")

    return max(frequency, key=frequency.get)


def get_unique_words(text: str) -> set[str]:
    """
    Get all unique words from the given text.

    Args:
        text: The input text to analyze.

    Returns:
        A set containing all unique words.
    """

    frequency: dict[str, int] = get_word_frequency(text)

    return set(frequency.keys())



text = """
Python is easy.
Python is powerful.
Python is widely used.
"""



word_frequency: dict[str, int] = get_word_frequency(text)

most_common: str = get_most_common_word(text)

unique_words: set[str] = get_unique_words(text)


print("Word Frequency:")
print(word_frequency)

print("\nMost Common Word:")
print(most_common)

print("\nUnique Words:")
print(unique_words)


# Output

# Word Frequency:
# {'python': 3, 'is': 3, 'easy': 1, 'powerful': 1, 'widely': 1, 'used': 1}

# Most Common Word:
# python

# Unique Words:
# {'powerful', 'used', 'is', 'easy', 'widely', 'python'}
