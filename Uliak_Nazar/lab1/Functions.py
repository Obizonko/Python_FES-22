import re


def read_file(file_path: str) -> tuple[str, int, int]:
    # Reads a file and returns the contents as a tuple of strings.
    with open(file_path, "r") as f:
        text = f.read()
        words_count = len(re.findall(r"\w+(?:['-.\/]\w+)*", text))
        sentences_count = len(re.findall(r'[.?!]+', text))

    return text, words_count, sentences_count


def get_palindromes(content: str) -> dict:
    # Returns a dictionary of palindromes in the given text.

    content = content.lower()
    words = re.findall(r'\b\w+\b', content)
    palindromes = {}

    for word in words:
        if word == word[::-1] and len(word) > 1:
            if word in palindromes:
                palindromes[word] += 1
            else:
                palindromes[word] = 1

    return palindromes


def get_palingrams(content: str) -> dict:
    # Returns a dictionary of palingrams in the given text.

    letters_only = re.sub(r'[^a-zA-Z\s]', "", content).lower()

    # Split the text into sentences
    sentences = re.split(r'[.?!]', letters_only)
    palingrams = {}
    for sentence in sentences:
        words = sentence.split()
        for i in range(len(words) - 1):
            left_word = words[i]
            right_word = words[i + 1]
            if len(left_word) == 1 or len(right_word) == 1:
                continue
            if left_word in right_word[::-1] or right_word in left_word[::-1]:
                word = left_word + " " + right_word
                if word in palingrams:
                    palingrams[word] += 1
                else:
                    palingrams[word] = 1

    return palingrams


def get_full_palingrams(content: str) -> dict:
    # Returns a dictionary of anagrams in the given text.

    content = content.lower()
    words = re.findall(r'\b\w+\b', content)
    full_palingrams = {}

    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word in full_palingrams and word not in full_palingrams[sorted_word]:
            full_palingrams[sorted_word].append(word)
        else:
            full_palingrams[sorted_word] = [word]

    list_of_full_palingrams = list(full_palingrams.items())
    real_full_palingrams = {}
    for i in range(len(list_of_full_palingrams)):
        if len(list_of_full_palingrams[i][1]) > 1:
            real_full_palingrams[list_of_full_palingrams[i][0]] = list_of_full_palingrams[i][1]

    return real_full_palingrams
