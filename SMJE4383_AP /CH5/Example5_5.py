data_file = open("SMJE4383_AP /CH5/dictionary.txt", 'r')

def clean_word(word): 
    return word.strip().lower()
def get_vowels_in_word(word): 
    vowel_str ="aeiou"
    vowels_in_words = ""
    for char in word: 
        if char in vowel_str: 
            vowels_in_words += char 
    return vowels_in_words
print("Find word containing vowels 'aeiou' in that order:")
for word in data_file:
    word = clean_word(word)
    if len(word) <= 6:
        continue
    vowel_str = get_vowels_in_word(word)
    if vowel_str =='aeiou':
        print(word)