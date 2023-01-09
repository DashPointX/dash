# English to Pig latin
print('Enter english text to translate to PIg Latin')
message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pigLatin = [] # A list of words in PIg Latin
for word in message.split():
    # Seperate the non-letters at the start of the word:
    prefixNonletters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonletters += word[0]
        word = word[1:]
 
    if len(word) == 0:
        pigLatin.append(prefixNonletters)   
        continue

    #Seperate the non-letters at end of the word:
    suffixNonletters =  ''
    while not word[-1].isalpha():                                                                                                                              
        suffixNonletters += word[-1]
        word = word[:-1]
    
    #Remember if word was in uppercase or title case.
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower() # Make the word lowercase to     transtation

    #Separate the consonants at the start of this word:
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

    # Add the Pig latin ending of the word:
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'

    # Set the word back to uppercase or title case:
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    # Add the non-letters back to start or end of the word:
    pigLatin.append(prefixNonletters + word + suffixNonletters)

# Join all the words back together into a single string:
print(' '.join(pigLatin))