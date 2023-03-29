import re  
from typing import Tuple, Dict  
from collections import defaultdict  
import pprint 
 
 
  
# Step 1  
def read_file(file_path: str) -> Tuple[str, int, int]:  
    """Reads a text file and returns its content, number of words, and number of sentences.  
      
    Args:  
        file_path (str): The path to the text file to read.  
      
    Returns:  
        A tuple containing the file content (str), number of words (int), and number of sentences (int).  
    """  
    with open(file_path, 'r') as file:  
        content = file.read()  
    words_count = len(re.findall(r'\b\w+\b', content))  
    sentence_count = len(re.findall(r'[.!?]+', content))  
    return content, words_count, sentence_count  
  
# Step 2  
def check_pallindrome(word: str) -> bool:  
    """  
    Checks if a given word is a palindrome.  
  
    Args:  
    word (str): The word to check.  
  
    Returns:  
    bool: True if the word is a palindrome, False otherwise.  
    """  
    return word == word[::-1]  
  
def get_all_palindromes(content: str) -> Dict[str, int]:  
    """  
    Finds all palindromes in content.  
  
    Args:  
    content (str): The input text.  
  
    Returns:  
    Dict[str, int]: A dictionary containing all the palindromes found in content and their frequency.  
    """  
    palindromes = defaultdict(int)  
    words = re.findall(r'\b\w+\b', content)  
    for word in words:  
        if check_pallindrome(word):  
            palindromes[word] += 1  
    return dict(palindromes)  
  
# Step 3  
def get_palingrams(content: str) -> Dict[str, int]:  
    """  
    Finds all palingrams in the content.  
  
    Args:  
    content (str): The input text.  
  
    Returns:  
    Dict[str, int]: A dictionary containing all the palingrams found in the content and their frequency.  
    """  
    palingrams = defaultdict(int)  
    words = re.findall(r'\b\w+\b', content)  
    word_set = set(words)  
    for word in words:  
        for i in range(1, len(word)):  
            if check_pallindrome(word[:i]):  
                suffix = word[i:]  
                if suffix[::-1] in word_set:  
                    palingram = f"{suffix[::-1]} {word}"  
                    palingrams[palingram] += 1  
            if check_pallindrome(word[i:]):  
                prefix = word[:i]  
                if prefix[::-1] in word_set:  
                    palingram = f"{word} {prefix[::-1]}"  
                    palingrams[palingram] += 1  
    return dict(palingrams)  
  
file_path = 'text.txt'  
content, words_count, sentence_count = read_file(file_path)  
print(f"Number of words:\n{words_count}")  
print("Palindroms:") 
pprint.pprint(get_all_palindromes(content))  
print("Palingrams:")
pprint.pprint(get_palingrams(content))
