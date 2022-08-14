"""read plain file from data/plain.txt
get rotors number and how much shift each one
encript plain text basie on rotors and shift
write cipher text to data/cipher.txt file
"""

import sys

from enigma import ALPHABET
from enigma.plugboard import apply_swiches
from enigma.reflector import reflector


def read_rotors() -> list[str]:
    '''
    this function read rotors from file rotors.enigma and return list[str]
    '''
    rotors: list[str] = []
    try:
        with open('data/rotors.enigma', 'r', encoding='UTF-8') as rotors_file:
            rotors = rotors_file.readlines()
            del rotors_file
            rotors = [r.strip() for r in rotors]
    except FileNotFoundError:
        print('You have to create \'data/rotors.enigma\' file!')
        sys.exit()
    return rotors


def set_rotors(
        rotors_list: list[str],
        selected_rotors: list[int],
        shift: list[int]
) -> list[str]:
    '''
    rotors is list of rotors which generated with \'app/rotor.py\'
    selected_rotors list of number which told us which rotors we use
    shift how much we shift our selected rotors

    at the end return new rotors list with 3 item and shifted rotors
    '''
    rotors_list = [
        rotors_list[selected_rotors[0] - 1],
        rotors_list[selected_rotors[1] - 1],
        rotors_list[selected_rotors[2] - 1],
    ]

    for index, item in enumerate(rotors_list):
        rotors_list[index] = item[shift[0]:] + item[:shift[0]]

    return rotors_list


def rotate_rotors(rotors_list: list[str], shift_counter: int) -> None:
    ''' Every time we encode a word, the first rotor shifts a word, every
    26 times the second rotor shifts a word, and the third rotor finds a
    shift word every 26 * 26 times. '''
    rotors_list[0] = rotors_list[0][1:] + rotors_list[0][:1]
    if shift_counter % 26:
        rotors_list[1] = rotors_list[1][1:] + rotors_list[1][:1]
    if shift_counter % 676:
        rotors_list[2] = rotors_list[2][1:] + rotors_list[2][:1]


def read_plain_text() -> str:
    ''' read plain text from file data/plain.txt '''
    try:
        with open('data/plain.txt', 'r', encoding='UTF-8') as plain_file:
            plain = plain_file.read()
            del plain_file
    except FileNotFoundError:
        print('You have to create \'data/plain.txt\' file!')
        sys.exit()
    return plain


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


def check_user_input_for_rotor(
        selected_rotor_number: str,
        rotor_range: int,
        is_rotor: bool = False
) -> list[int]:
    ''' get two value
    1. selected_rotor_number: rotor number (which rotor is selected for using
    in encription)
    2. r_in_range: rotor range (is number between 1 to 26 or 1 to lenght of
    rotors list)

    split selected_rotor_number -> list[str]
    loop over selected_rotor_number and change type of all item to intger

    check all item in selected_rotor_number  is intger
    check any item in  selected_rotor_number  begger then r_in_range if
    check is number of item equal to 3
    check is there eny two equal number
    if one of this check fill then return ValueError()

    at the end return selected_rotor_number : list[int]
    '''
    try:
        selected_rotor_no_list = list(map(int, selected_rotor_number.split()))
    except ValueError:
        print('Your input should be integer!')
        sys.exit()

    if len(selected_rotor_no_list) != 3:
        print('You have to enter 3 number!')
        sys.exit()

    if any(int(i) > rotor_range for i in selected_rotor_no_list):
        print(f'Your items should be smaller then {rotor_range}!')
        sys.exit()

    if is_rotor:
        if selected_rotor_no_list[0] == selected_rotor_no_list[1] or \
                selected_rotor_no_list[0] == selected_rotor_no_list[2] or \
                selected_rotor_no_list[1] == selected_rotor_no_list[2]:
            print('Your input should not be equal!')
            sys.exit()

    return selected_rotor_no_list


def read_rotors_status(rotors):
    '''
    read rotors status from user input and return list[int]
    '''
    try:
        rotors_number = input(
            f"Enter 3 number for rotors (1 to {len(rotors)}): ")
        rotors_number = check_user_input_for_rotor(
            rotors_number,
            len(rotors),
            True
        )
        rotors_shift = input(
            'Enter your rotor shift (3 number between 1, 26): ')
        rotors_shift = check_user_input_for_rotor(rotors_shift, 26)
    except ValueError:
        sys.exit(0)
    return rotors_number, rotors_shift


def code_plain_txt(rotors_list: list[str], char: str) -> str:
    """ It takes a word from routers and reflectors """
    c_1 = rotors_list[0][ALPHABET.index(char)]
    c_2 = rotors_list[1][ALPHABET.index(c_1)]
    c_3 = rotors_list[2][ALPHABET.index(c_2)]
    reflected = reflector(c_3)
    c_3 = ALPHABET[rotors_list[2].index(reflected)]
    c_2 = ALPHABET[rotors_list[1].index(c_3)]
    c_1 = ALPHABET[rotors_list[0].index(c_2)]
    return c_1


def write_cipher(cipher_txt: str) -> None:
    ''' this function write your cipher to text file at \'data/cipher.txt\''''
    with open('data/cipher.txt', 'w', encoding='UTF-8') as cipher_file:
        cipher_file.write(cipher_txt)
        del cipher_file


def coding(plain: str, rotors: list[str]) -> str:
    '''
    :param plain: plain text
    :param rotors: list of rotors
    :return: cipher text
    get plain text and Each word passes it through the rotors and reflectors,
    and finally it rotates the rotors by one unit.
    '''
    cipher, counter = "", 1
    for char in plain:
        cipher += code_plain_txt(rotors, char)
        rotate_rotors(rotors, counter)
        counter += 1
    cipher += "\n"
    return cipher


def read_switches_from_file() -> dict:
    """
    read the switches from a file
    """
    switches_dict = {}
    with open('data/switches.txt', 'r', encoding='UTF-8') as file:
        for line in file:
            key, value = line.split()
            switches_dict[key] = value

    return switches_dict


def main():
    ''' run all functions '''

    plain_txt = read_plain_text()
    cleand_plain_txt = cleaning_plain_txt(plain_txt)

    rotors = read_rotors()
    rotors_number, rotors_shift = read_rotors_status(rotors)
    rotors = set_rotors(rotors, rotors_number, rotors_shift)

    switches = read_switches_from_file()
    code_or_dicode = input(
        'Do you want to code or decode? (code/decode): ').strip()

    if code_or_dicode == 'code':
        cipher = coding(cleand_plain_txt, rotors)
        cipher = apply_swiches(switches, cipher)
    elif code_or_dicode == 'decode':
        cipher = apply_swiches(switches, cleand_plain_txt)
        cipher = coding(cipher, rotors)
    else:
        print('Your input should be code or decode!')
        sys.exit()

    write_cipher(cipher)


if __name__ == '__main__':
    print('start')
    main()
    print('your cipher in \'data/cipher.txt\'\nDone!!')
