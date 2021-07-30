# author: elia deppe
# date: 7/28

# difficulty: medium

# Wikipedia: https://en.wikipedia.org/wiki/Caesar_cipher
#   Read this for a better understanding of the cipher.

# Introduction
#
# Create an implementation of the rotational cipher, also sometimes called the Caesar cipher.
#
# The Caesar cipher is a simple shift cipher that relies on transposing all the letters in the alphabet using
#   an integer key between 0 and 26. Using a key of 0 or 26 will always yield the same output due to modular
#   arithmetic. The letter is shifted for as many values as the value of the key.
#
# The general notation for rotational ciphers is ROT + <key>. The most commonly used rotational cipher is ROT13.
#
# A ROT13 on the Latin alphabet would be as follows:
#
# Plain:  abcdefghijklmnopqrstuvwxyz
# Cipher: nopqrstuvwxyzabcdefghijklm
#
# It is stronger than the Atbash cipher because it has 27 possible keys, and 25 usable keys.
#
# Ciphertext is written out in the same formatting as the input including spaces and punctuation.
# Examples
#
#     ROT5 omg gives trl
#     ROT0 c gives c
#     ROT26 Cool gives Cool
#     ROT13 The quick brown fox jumps over the lazy dog. gives Gur dhvpx oebja sbk whzcf bire gur ynml qbt.
#     ROT13 Gur dhvpx oebja sbk whzcf bire gur ynml qbt. gives The quick brown fox jumps over the lazy dog.
#
# Instructions
#   1 - The program should accept input in the form of a string, which will be the plain text. This is the text
#           to be encrypted.
#   2 - The program should also accept a key from the user, which will be the shift for the rotational cipher.
#   2 - Convert the plain text into cipher text using the rotational cipher, shifting by the amount specified
#           by the user.
#   3 - Print the result to the user.
#
# WRITE CODE BELOW #
lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
upper_alphabet = lower_alphabet.upper()
alphabet = lower_alphabet + upper_alphabet


def get_shift():
    while True:
        try:
            shift = int(input('>> shift | '))
            return shift
        except ValueError:
            print('>> invalid value for shift, must be an integer')


def rotational_cipher(plain_text, shift):
    cipher_text = ''

    for char in plain_text:
        if char in alphabet:
            position = lower_alphabet.find(char.lower())
            position = (position + shift) % len(lower_alphabet)

            if char in lower_alphabet:
                cipher_text += lower_alphabet[position]
            else:
                cipher_text += upper_alphabet[position]
        else:
            cipher_text += char

    return cipher_text


def main():
    plain_text = input('>> rotational cipher' '\n' '>> plain text | ')
    shift = get_shift()

    cipher_text = rotational_cipher(plain_text, shift)

    print(
        f'>> plain text  | {plain_text}' '\n'
        f'>> cipher text | {cipher_text}'
    )


main()
