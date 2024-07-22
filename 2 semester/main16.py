import string
def count_words(input_string):
    words = input_string.split()
    return len(words)

def letter_frequency(input_string):
    clean_string = ''.join(e for e in input_string if e.isalnum()).lower()
    freq = {}
    for letter in clean_string:
        if letter.isalpha():
            freq[letter] = freq.get(letter, 0) + 1
    return freq

def common_words(string1, string2):
    words1 = set(string1.split())
    words2 = set(string2.split())
    return words1.intersection(words2)

def remove_punctuation(input_string):
    return input_string.translate(str.maketrans('', '', string.punctuation))


def __main():
    if __name__ != '__main__':
        print('ИДИ НАХУЙ')
    else:
        print("ХУЙ")


if __name__ == "__main__":
    __main()