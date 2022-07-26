"""
Reflector is responsible for mirror input charactor
i.e. You give b to reflector and it's return z
b is 2 word in english alphabet and z is 26 - 2
"""
from main import ALPHABET


def reflector(char: str) -> str:
    """ mirror characters """
    assert isinstance(char, str), "input should be instance of string"
    char_index = ALPHABET.index(char) + 1
    reflected_char = ALPHABET[-char_index]
    return reflected_char
