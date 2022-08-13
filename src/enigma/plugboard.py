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
    switches_dict = {}
    for _ in range(10):
        key = random.choice(alphabet)
        value = random.choice(alphabet)
        while value == key:
            value = random.choice(alphabet)
        switches_dict[key] = value
        alphabet = alphabet.replace(key, '')
        alphabet = alphabet.replace(value, '')

    return switches_dict


def write_switches_to_file(switches: dict):
    """
    write the switches to a file
    """
    with open('data/switches.txt', 'w', encoding='UTF-8') as file:
        for key, value in switches.items():
            file.write(f'{key} {value}\n')


def apply_swiches(switches: dict, plaintext: str) -> str:
    """
    itrate on all letters in plaintext and if the letter in plaintext is in the
    switches dictionary, replace it with the value of the key and if letter in
    switches values replace it with the key
    """
    ciphertext = ''

    for letter in plaintext:
        if letter in switches:
            ciphertext += switches[letter]
        elif letter in switches.values():
            ciphertext += list(
                switches.keys())[list(switches.values()).index(letter)]
        else:
            ciphertext += letter
    return ciphertext


if __name__ == '__main__':
    generated_switches = switch_generator()
    write_switches_to_file(generated_switches)
