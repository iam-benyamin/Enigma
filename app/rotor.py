""" This module generate rotors """

from string import ascii_lowercase
from random import shuffle


ALPHABET = ascii_lowercase


def rotor_generator(rotors_number: int = 5, TEXT: str = "") -> str:
    """
    this function generate rotors with name
    ROTOR_I and 'I' is number in range 1 to
    NUMBER_OF_ROTORS like 'ROTOR_2'
    """

    for i in range(1, rotors_number + 1):
        ROTOR = list(ALPHABET)
        shuffle(ROTOR)
        ROTOR = "".join(ROTOR)
        TEXT += f"{ROTOR}\n"

    return TEXT


if __name__ == "__main__":
    try:
        print("Input should be number (intger)")
        NUMBER_OF_ROTORS = int(input(
            "Enter number of rotors you wont (default is 5): ")
        )
        if NUMBER_OF_ROTORS > 1:
            print("Okay your rotors are generated!!")
        elif NUMBER_OF_ROTORS == 1:
            print("Okay your rotor is generated!!")
        else:
            raise
        rotors = rotor_generator(NUMBER_OF_ROTORS)
    except:
        print("Your input is wrong! so number of rotors set on 5.")
        rotors = rotor_generator()

    try:
        with open("data/Rotors.enigma", "w") as file:
            file.write(rotors)
            print('your Roters are write to ../data/Rotors.enigma')
            print("Done!!")
    except:
        print("Something went wrong!!!")
