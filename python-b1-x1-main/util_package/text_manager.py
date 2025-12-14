import string
# Do not change the following lines

TEXT = '''Are the following lines palindromes?
A man, a plan, a canal, Panama.
This line is not a palindrome
Don't nod
The next one might be my favorite
Taco Cat!
Another non-palindrome
Rats live on no evil star.
If your program finds this line, it's not working
Neil, a trap! Sid is part alien!
Step on no pets.
Dammit, I'm mad!
Madam, I'm Adam.
Madam, in Eden, I'm Adam.
Rise to vote, sir.
Never odd or even
If I had a hi-fi
Yo, banana boy!
Do geese see God?
No devil lived on.
Ah, Satan sees Natasha.
Lewd did I live & evil I did dwel!
A dog, a panic in a pagoda
Was it a cat I saw?
Was it a car or a cat I saw?
A Toyota's a Toyota.
Another non-palindrome
No lemons, no melon
Now I see bees, I won.
Ma is as selfless as I am.
Nurse, I spy gypsies-run!
The next one isn't as cool as the Panama one
A dog, a plan, a canal, pagoda
Was it Eliot's toilet I saw?
Some of these are hilarious. Papaya war?!
No, sir, away! A papaya war is on!
Go hang a salami, I'm a lasagna hog.
I, madam, I made radio! So I dared! Am I mad? Am I?
Swap God for a janitor, rot in a jar of dog paws.
Eva, can I see bees in a cave?
Not a palindrome
So many dynamos!
Red rum, sir, is murder.
'''


def is_newline(character):
    # Do not change this method
    """ A function that detects the ending of a sentence. Here, the sentences are separated by a "\n". 
    If the character is this simbol it will return True.
    """
    return character == "\n"


def is_space(character):
    # Do not change this method
    """ A function that detects if a character is an blank space.
    """
    return character == " "


def remove_punctuation_marks(cad):
    # Do not change this method
    """ A function that removes punctuation marks from a word or a text.
    """
    return cad.translate(str.maketrans('', '', string.punctuation))

# Nueva función para crear una lista limpia de palabras contenidas en la variable TEXT
def clean_word_list(text):
    # Variables vacías para lista y para acumular caracteres
    word_list=[]
    word=""
    ''' Bucle para detectar palabras.

        Recorre cada caracter de TEXT.

        Si encuentra un espacio o salto de línea y la palabra acumulada no está vacía:
            * Añade la palabra limpia a la lista
            * Reinicia la variable 'word'

        Si no es espacio ni salto de línea:
            * Acumula el carácter en 'word'
            * Continúa hasta encontrar el siguiente espacio o salto de línea

        También elimina puntuación usando la función remove_punctuation_marks(cad).
    '''
    for character in text:
        if (is_space(character)==True or is_newline(character)==True)and word!="":
            word_list.append(remove_punctuation_marks(word))
            word=""
        else:
            word+=character
    ''' Este if sirve para añadir la última palabra que queda después de recorrer el bulce.
        Al hacer pruebas vi que si el último caracter no era espacio o salto de línea, no se añadía la última palabra
    '''
    if word!="":
        word_list.append(remove_punctuation_marks(word))
    # La función devuelve una lista limpia de las palabras contenidas en la variable inicial
    return word_list

# Nueva función para crear una lista limpia de frases contenidas en la variable TEXT
# Misma lógica que clean_word_list(text)
def clean_sentence_list(text):
    sentence_list=[]
    sentence=""
    for character in text:
        if is_newline(character)==True and sentence!="":
            sentence_list.append(sentence)
            sentence=""
        else:
            sentence+=character
    if sentence!="":
        sentence_list.append(sentence)
    return sentence_list
