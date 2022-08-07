""" This module generate rotors """

from random import shuffle

from enigma import ALPHABET


def rotor_generator(rotors_number: int = 5, text: str = "") -> str:
    """
    this function generate rotors with name
    ROTOR_I and 'I' is number in range 1 to
    NUMBER_OF_ROTORS like 'ROTOR_2'
    """
    assert isinstance(rotors_number, int), 'rotor number should be intger'
    for _ in range(1, rotors_number + 1):
        rotor = list(ALPHABET)
        shuffle(rotor)
        rotor = "".join(rotor)
        text += f"{rotor}\n"

    return text


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
            raise ValueError
        rotors = rotor_generator(NUMBER_OF_ROTORS)
    except ValueError:
        print("Your input is wrong! so number of rotors set on 5.")
        rotors = rotor_generator()

    try:
        with open("data/rotors.enigma", "w", encoding='UTF-8') as file:
            file.write(rotors)
            print('your Roters are write to \'data/Rotors.enigma\'')
            print("Done!!")
    except IOError:
        print("Something went wrong!!!")
