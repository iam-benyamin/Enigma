"""
Reflector is responsible for mirror input charactor
i.e. You give b to reflector and it's return z
b is 2 word in english alphabet and z is 26 - 2
"""
from enigma import ALPHABET


def reflector(char: str) -> str:
    """ mirror characters """
    if not isinstance(char, str):
        raise ValueError("reflector() argument must be str")
    if len(char) != 1:
        raise ValueError("reflector() argument must be 1 character")
    char_index = ALPHABET.index(char) + 1
    reflected_char = ALPHABET[-char_index]
    return reflected_char
