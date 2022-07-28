""" main """

import sys

from string import ascii_lowercase


ALPHABET = ascii_lowercase


rotors: list[str] = []
with open('data/rotors.enigma', 'r', encoding='UTF-8') as rotors_file:
    rotors = rotors_file.readlines()
    del rotors_file
    rotors = [r.strip() for r in rotors]


def set_rotors(rotors: list[str], selected_rotors: list[int], shift: list[int]) -> list[str]:
    '''
    rotors is list of rotors which generated with \'app/rotor.py\'
    selected_rotors list of number which told us which rotors we use
    shift how much we shift our selected rotors

    at the end return new rotors list with 3 item and shifted rotors
    '''
    rotors = [
        rotors[selected_rotors[0] - 1],
        rotors[selected_rotors[1] - 1],
        rotors[selected_rotors[2] - 1],
    ]

    for index, item in enumerate(rotors):
        rotors[index] = item[shift[0]:] + item[:shift[0]]

    return rotors


with open('data/plain.txt', 'r', encoding='UTF-8') as plain_file:
    plain_txt = plain_file.read()
    del plain_file


def cleaning_plain_txt(plain: str) -> str:
    """ this function remove all whith space and make all letter lowercase """
    plain = plain.lower()
    cleand_plain = ""
    for char in plain:
        if char in ALPHABET:
            cleand_plain += char

    print('jast lowercase english alphbet are accepted and other characters'
          ' is removed!')
    return cleand_plain


cleand_plain_txt = cleaning_plain_txt(plain_txt)


def write_cipher(cipher_txt: str) -> None:
    ''' this function write your cipher to text file at \'data/cipher.txt\''''
    with open('data/cipher.txt', 'w', encoding='UTF-8') as cipher:
        cipher.write(cipher_txt)
        del cipher


write_cipher(cleand_plain_txt)


def check_user_input_for_rotor(r: str, r_in_range, is_rotor: bool = False) -> list[int]:
    ''' get two value
    1. r: rotor number (which rotor is selected for using in encription)
    2. r_in_range: rotor range (is number between 1 to 26 or 1 to lenght of
    rotors list)

    split r -> list[str]
    loop over r and change type of all item to intger

    check all item in r is intger
    check any item in r begger then r_in_range if
    check is number of item equal to 3
    check is there eny two equal number
    if one of this check fill then return ValueError()

    at the end return r: list[int]
    '''
    r = r.split()
    try:
        r = list(map(int, r))
    except ValueError:
        print('Your input should be integer!')

    if len(r) != 3:
        print('You have to enter 3 number!')
        raise ValueError()

    if any(int(i) > r_in_range for i in r):
        print(f'Your items should be smaller then {r_in_range}!')
        raise ValueError()

    if is_rotor:
        if r[0] == r[1] or r[0] == r[2] or r[1] == r[2]:
            print('Your input should not be equal!')
            raise ValueError()

    return r


try:
    rotors_number = input(f"Enter 3 number for rotors (1 to {len(rotors)}): ")
    rotors_number = check_user_input_for_rotor(
        rotors_number,
        len(rotors),
        True
    )

    rotors_shift = input('Enter your rotor shift (3 number between 1, 26): ')
    rotors_shift = check_user_input_for_rotor(rotors_shift, 26)

except ValueError:
    sys.exit(0)

rotors = set_rotors(rotors, rotors_number, rotors_shift)

print('your cipher in \'data/cipher.txt\'')
print('done!!')
