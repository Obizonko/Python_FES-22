import re
from Functions import read_file, get_palindromes, get_palingrams, get_full_palingrams

file_path = "3000words.txt"
text, words_count, sentences_count = read_file(file_path)
print(f'The number \nof words: {words_count} \nof sentences: {sentences_count}')

palindromes = get_palindromes(text)
list_of_palindromes = list(palindromes.items())
print("of palindromes:", len(list_of_palindromes))
for i in range(min(10, len(list_of_palindromes))):
    print(list_of_palindromes[i], end=" ")

palingrams = get_palingrams(text)
list_of_palingrams = list(palingrams.items())
print("\nof palingrams:", len(list_of_palingrams))
for i in range(min(10, len(list_of_palingrams))):
    print(list_of_palingrams[i], end=" ")


anagrams = get_full_palingrams(text)
list_of_full_palingrams = list(anagrams.items())
print("\nof full_palingrams:", len(list_of_full_palingrams))
for i in range(min(10, len(list_of_full_palingrams))):
    print(list_of_full_palingrams[i], end=" ")
