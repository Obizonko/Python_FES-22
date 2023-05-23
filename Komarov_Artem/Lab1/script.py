import re
from typing import Tuple, Dict

def read_file(file_path: str) -> Tuple[str, int, int]:
    with open(file_path, 'r') as file:
        content = file.read()
    words = content.split()
    words_count = len(words)
    sentence_count = content.count('.') + content.count('?') + content.count('!')
    return content, words_count, sentence_count

def check_palindrome(word: str) -> bool:
    return word == word[::-1]

def get_all_palindromes(content: str) -> Dict[int, str]:
    palindromes = {}
    for i, word in enumerate(content.split()):
        if check_palindrome(word):
            palindromes[i] = word
    return palindromes


def get_palingrams(content: str) -> Dict[int, str]:
    words = set(re.findall(r'\b\w+\b', content.lower()))
    palingrams = {}
    for word in words:
        for i in range(len(word)):
            if  (len(word) != 1) :
                if check_palindrome(word[:i + 1]):
                    suffix = word[i + 1:][::-1]
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


content, words_count, sentence_count = read_file('words.txt')
print(f"Number of words: {words_count}")
print(f"Number of sentences: {sentence_count}")
print(f"Palindromes: {get_all_palindromes(content)}")
print(f"Palingrams: {get_palingrams(content)}")