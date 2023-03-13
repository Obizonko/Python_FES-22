from typing import Tuple, Dict
import re


def read_file(file_path: str) -> Tuple[str, int, int]:
    with open(file_path, 'r') as file:
        content = file.read()
    words_count = len(re.findall(r'\b\w+\b', content))
    sentence_count = len(re.findall(r'[.!?]+', content))
    return content, words_count, sentence_count


def check_palindrome(word: str) -> bool:
    return word == word[::-1]


def get_all_palindromes(content: str) -> Dict[int, str]:
    palindromes = {}
    for word in re.findall(r'\b\w+\b', content):
        if check_palindrome(word):
            index = content.find(word)
            palindromes[index] = word
    return palindromes


def get_palingrams(content: str) -> Dict[int, str]:
    words = set(re.findall(r'\b\w+\b', content.lower()))
    palingrams = {}
    for word in words:
        for i in range(len(word)):
            if check_palindrome(word[:i+1]):
                suffix = word[i+1:][::-1]
                if suffix in words and suffix != word:
                    index = content.find(word + " " + suffix)
                    palingrams[index] = word + " " + suffix
                if suffix == '':
                    index = content.find(word)
                    palingrams[index] = word
            if check_palindrome(word[i:]):
                prefix = word[:i][::-1]
                if prefix in words and prefix != word:
                    index = content.find(prefix + " " + word)
                    palingrams[index] = prefix + " " + word
                if prefix == '':
                    index = content.find(word)
                    palingrams[index] = word
    return palingrams
file_path = 't.txt'
content, words_count, sentence_count = read_file(file_path)
print(f"All palindromes: {get_all_palindromes(content)}")
print(f"All palingrams: {get_palingrams(content)}")
