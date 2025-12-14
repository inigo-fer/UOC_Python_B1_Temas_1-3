import string
TEXT = '''Are the following lines palindromes?
A man, a plan, a canal, Panama.
This line is not a palindrome
Don't nod
The next one might be my favorite
Taco Cat!'''

def is_space(character):
    # Do not change this method
    """ A function that detects if a character is an blank space.
    """
    return character == " "

def is_newline(character):
    # Do not change this method
    """ A function that detects the ending of a sentence. Here, the sentences are separated by a "\n". 
    If the character is this simbol it will return True.
    """
    return character == "\n"

def remove_punctuation_marks(cad):
    # Do not change this method
    """ A function that removes punctuation marks from a word or a text.
    """
    return cad.translate(str.maketrans('', '', string.punctuation))

word_list=[]
word=""
for character in TEXT:
    if (is_space(character)==True or is_newline(character)==True)and word!="":
        word_list.append(remove_punctuation_marks(word))
        word=""
    else:
        word+=character
if word!="":
    word_list.append(remove_punctuation_marks(word))
    
big_word=""
word_len=len(word_list[0])
for word in word_list:
    if len(word)>word_len:
        word_len=len(word)
        big_word=word

print(big_word)
