
# Add your imports here
from util_package import text_manager
from util_package.text_manager import TEXT, is_newline, is_space, remove_punctuation_marks,clean_word_list,clean_sentence_list

def find_largest_word(text):
    word_list=clean_word_list(text)

    longest_word=""
    word_len=len(word_list[0])
    for word in word_list:
        if len(word)>word_len:
            word_len=len(word)
            longest_word=word
    return longest_word

def is_palindrome_word(word):
    word=remove_punctuation_marks(word)
    if len(word)<=1:
        return True
    else:
        prim_letra = 0
        ult_letra = len(word)
        if word[prim_letra:prim_letra+1].lower() == word[ult_letra-1].lower():
            prim_letra+=1
            ult_letra-=1
            is_palindrome_word(word[prim_letra:ult_letra])
            return True
        else:
            return False

def count_palindrome_words(text):
    word_list=clean_word_list(text)
    counter=0
    for word in word_list:
        if is_palindrome_word(word)==True:
            counter+=1
    return counter

def find_size_largest_sentence(text, filter):
    all_sentence_list=clean_sentence_list(text)
    filtered_sentence_list=[]

    for sentence in all_sentence_list:
        if filter in sentence:
            filtered_sentence_list.append(sentence)

    longest_sentence=""
    sentence_len=len(filtered_sentence_list[0])
    for sentence in filtered_sentence_list:
        if len(sentence)>sentence_len or len(filtered_sentence_list)==1:
            sentence_len=len(sentence)
            longest_sentence=sentence
    return len(longest_sentence)

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# print("La palabra mas larga es:", find_largest_word(TEXT))
# print("'aa' es un palíndromo su resultado es:", is_palindrome_word("aa"))
# print("'abx' no un palíndromo su resultado es:", is_palindrome_word("abx"))
# print("'Ababa' es palíndromo su resultado es:", is_palindrome_word("Ababa"))
# print("El número de palabras identificadas como palíndromos es:", count_palindrome_words(TEXT))
# print("El tamaño de la oración más larga con el filtro='melon', es :", find_size_largest_sentence(TEXT, "melon"))

# Ejercicio completado por el alumno FERNANDEZ RODRIGUEZ, Iñigo
