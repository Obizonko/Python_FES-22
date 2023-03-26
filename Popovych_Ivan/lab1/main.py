import re
from typing import Tuple, Dict


def read_file(file_path: str) -> Tuple[str, int, int]:
    """
    Reads the contents of a file and returns the content,
    number of words, and number of sentences.

        Args:
            file_path (str): The path to the file to read.

        Returns:
            A tuple containing the following values:
            - content (str): The contents of the file.
            - words (int): The number of words in the file.
            - sentences (int): The number of sentences in the file.

        Raises:
            IOError: If the file could not be read.
    """

    with open(file_path, 'r') as file:
        content = file.read()

    # Count the number of words in the file
    word_regex = re.compile(r'\b\w+\b')
    words = len(word_regex.findall(content))

    # Count the number of sentences in the file
    sentence_regex = re.compile(r'([^\s][.?!])\s')
    sentences = len(sentence_regex.findall(content))

    return content, words, sentences


def get_all_palindromes(file_path: str) -> Dict[str, int]:
    """
    Finds all palindromes in a file and returns a dictionary of palindrome words and their frequency.

        Args:
            file_path (str): The path to the file to read.

        Returns:
            A dictionary containing the following key-value pairs:
            - palindrome word (str): The palindrome word found in the file.
            - frequency (int): The number of times the palindrome word appears in the file.
    """
    with open(file_path, 'r') as file:
        content = file.read()

    palindromes = {}
    words = content.split()
    for word in words:
        if check_pallindrome(word) & (len(word) > 2):
            if word in palindromes:
                palindromes[word] += 1
            else:
                palindromes[word] = 1
    return palindromes


def check_pallindrome(word: str) -> bool:
    return word == word[::-1]


def get_palingrams(file_path: str) -> dict[str, list[str]]:
    """
        Returns a dictionary of palingrams in the specified file.


        Args:
            file_path (str): The path to the file to be searched.

        Returns:
            dict[str, list[str]]: A dictionary of palingrams found in the file, where each key is a palingram and the
            corresponding value is a list of words that can be combined with the key to form a palingram.
    """

    with open(file_path, 'r') as file:
        content = file.read()

    palingrams = {}
    words = content.split()
    for i in range(len(words)):
        if len(words[i]) < 2:
            continue
        for j in range(len(words)):
            if j == i:
                continue
            if words[i] in words[j][::-1]:
                if words[i] in palingrams:
                    palingrams[words[i]].append(words[j])
                else:
                    palingrams[words[i]] = [words[j]]

    return palingrams


def get_same_letters_word(file_path: str) -> dict[str, list[str]]:
    """
        Returns a dictionary of words that contain the same letters.

        Args:
            file_path (str): The path of the file to read.

        Returns:
            A dictionary where the keys are sorted strings of unique
            letters that appear in one or more words in the file,
            and the values are lists of words that contain exactly those letters.

        Raises:
            FileNotFoundError: If the specified file does not exist.
    """

    with open(file_path, 'r') as file:
        content = file.read()

    result = {}
    words = content.split()

    for i in range(len(words)):
        key = ''.join(sorted(words[i]))
        if key in result:
            continue
        else:
            result[key] = [words[i]]
        for j in range(i + 1, len(words)):
            if key == ''.join(sorted(words[j])):
                result[key].append(words[j])

        if len(result[key]) == 1:
            result.pop(key)

    return result


while True:
    print("1 - read_file")
    print("2 - get_all_palindromes")
    print("3 - get_palingrams")
    print("4 - get_same_letters_word")
    choice = input("choose the option: ")

    if choice == "1":
        print(read_file('index.txt'))
    elif choice == "2":
        print(get_all_palindromes('index.txt'))
    elif choice == "3":
        print(get_palingrams('index.txt'))
    elif choice == "4":
        print(get_same_letters_word('index.txt'))
    else:
        break
