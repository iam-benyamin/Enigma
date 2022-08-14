# Enigma Machine

![enigma image](docs/Enigma.jpg)
![secret key list](docs/keylist.jpg) \
The Enigma machine is a cipher device developed and used in the early-to
mid-20th century to protect commercial, diplomatic, and military communication.
It was employed extensively by Nazi Germany during World War II, in all
branches of the German military. The Enigma machine was considered so secure
that it was used to encipher the most top-secret messages.

![scheme](docs/kleur.png)
![rotors](docs/rotors.jpg)
![rotors workflows](docs/Enigma-action.png) \
The Enigma has an electromechanical rotor mechanism that scrambles the 26 letters
of the alphabet. In typical use, one person enters text on the Enigma's keyboard
and another person writes down which of the 26 lights above the keyboard
illuminated at each key press. If plain text is entered, the illuminated
letters are the ciphertext. Entering ciphertext transforms it back into
readable plaintext. The rotor mechanism changes the electrical connections
between the keys and the lights with each keypress.

The security of the system depends on machine settings that were generally
changed daily, based on secret key lists distributed in advance, and on other
settings that were changed for each message. The receiving station would have
to know and use the exact settings employed by the transmitting station to
successfully decrypt a message.

While Nazi Germany introduced a series of improvements to the Enigma over the
years, and these hampered decryption efforts, they did not prevent Poland from
cracking the machine as early as December 1932 and reading messages prior to
and into the war. Poland's sharing of her achievements enabled the western
Allies to exploit Enigma-enciphered messages as a major source of intelligence.
Many commentators say the flow of Ultra communications intelligence from the
decrypting of Enigma, Lorenz, and other ciphers shortened the war substantially
and may even have altered its outcome.


# operation
Basic operation
Enciphering and deciphering using an Enigma machine

A German Enigma operator would be given a plaintext message to encrypt. After
setting up his machine, he would type the message on the Enigma keyboard.
For each letter pressed, one lamp lit indicating a different letter according
to a pseudo-random substitution determined by the electrical pathways inside
the machine. The letter indicated by the lamp would be recorded, typically by
a second operator, as the cyphertext letter. The action of pressing a key also
moved one or more rotors so that the next key press used a different electrical
pathway, and thus a different substitution would occur even if the same
plaintext letter were entered again. For each key press there was rotation
of at least the right hand rotor and less often the other two, resulting in
a different substitution alphabet being used for every letter in the message.
This process continued until the message was completed. The cyphertext recorded
by the second operator would then be transmitted, usually by radio in Morse code,
to an operator of another Enigma machine. This operator would type in the
cyphertext and — as long as all the settings of the deciphering machine were
identical to those of the enciphering machine — for every key press the reverse
substitution would occur and the plaintext message would emerge.

# insatlling & useing

## by makefile

create virtual enviroment and install dependencies

do all stepes one by one

```
make build
```

create rotors
```
make rotor
```
create plugboard switches
```
make switch
```

run app
```
make run
```

do all steps together
```
make all
```

These commands are only for the first time and for the next times you only need
to type the following command
```
make run
```

# Testing

for test this code run below command in root dirctory

```
tox
```
or run
```
make test
```
