def get_vowels_in_word(word): 
    vowel_str ="aeiou"
    vowels_in_words = ""
    for char in word: 
        if char in vowel_str: 
            vowels_in_words += char 
        return vowels_in_words