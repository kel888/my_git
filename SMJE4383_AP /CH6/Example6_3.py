def are_anagram(word1,word2): 
    word1_sorted =sorted(word1) 
    word2_sorted = sorted (word2) 

    return word1_sorted == word2_sorted 

print ("Anagram Test")

valid_input_bool = False 
while not valid_input_bool: 
    try: 
        two_words = input ("Enter two space seperated words: ")
        word1,word2 = two_words.split()

        valid_input_bool = True 
        