"""
this file is used to generate the plugboard switches
and to encrypt the message based on the switches
"""
import random


def switch_generator() -> dict:
    '''
    generates a random dictionary of lowercase letters without repeats and
    lenght 10 items, key and value are not same and are both lowercase letters
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    switches = {}
    for i in range(10):
        key = random.choice(alphabet)
        value = random.choice(alphabet)
        while value == key:
            value = random.choice(alphabet)
        switches[key] = value
        alphabet = alphabet.replace(key, '')
        alphabet = alphabet.replace(value, '')

    return switches


def plugboard(plaintext: str) -> str:
    """
    itrate on all letters in plaintext and if the letter in plaintext is in the
    switches dictionary, replace it with the value of the key
    """
    switches = switch_generator()
    ciphertext = ''
    for letter in plaintext:
        if letter in switches:
            ciphertext += switches[letter]
        else:
            ciphertext += letter
    return ciphertext
