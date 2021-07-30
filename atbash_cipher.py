# author: elia deppe
# date: 7/28

# difficulty: easy

# Wikipedia: https://en.wikipedia.org/wiki/Atbash
#   Read this for a better understanding of the cipher.

# Introduction
#
# Create an implementation of the atbash cipher, an ancient encryption system created in the Middle East.
#
# The Atbash cipher is a simple substitution cipher that relies on transposing all the letters in the alphabet such
#   that the resulting alphabet is backwards. The first letter is replaced with the last letter,
#   the second with the second-last, and so on.
#
# An Atbash cipher for the Latin alphabet would be as follows:
#
# Plain:  abcdefghijklmnopqrstuvwxyz
# Cipher: zyxwvutsrqponmlkjihgfedcba
#
# It is a very weak cipher because it only has one possible key, and it is a simple monoalphabetic substitution
#   cipher. However, this may not have been an issue in the cipher's time.
#
# Ciphertext is written out in groups of fixed length, the traditional group size being 5 letters, and
#   punctuation is excluded. This is to make it harder to guess things based on word boundaries.
#
# Examples
#
#     Encoding test gives gvhg
#     Decoding gvhg gives test
#     Decoding gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt gives thequickbrownfoxjumpsoverthelazydog
#
#
# Program Requirements:
#   1 - The program should accept input in the form of a string, which will be the plain text. This is the text
#           to be encrypted.
#   2 - Convert the plain text into cipher text using the atbash cipher.
#   3 - Print the result to the user.
#
# HINTS:
#   1 - It may be helpful to tell the program what the plain alphabet is, as well as the cipher.
#   2 - Remember that lists can be built up, meaning it may be useful to start with an empty list.
#
# WRITE DOWN THE STEPS BEFORE ATTEMPTING THE PROGRAM
alphabet = 'abcdefghijklmnopqrstuvwxyz'


# function / mode
#   parameter(s)
#       none
#   return value(s)
#       mode | string | which mode to use the cipher in, encryption or decryption.
#
# description: get the mode from the user, in order to encrypt or decrypt the text
def mode():
    mode = ''
    while mode != 'encrypt' and mode != 'decrypt':
        mode = input('>> mode\n')

        if mode != 'encrypt' and mode != 'decrypt':
            print(
                '>> mode options' '\n'
                '>>     [encrypt, decrypt]' '\n'
            )
    return mode


# function / atbash
#   parameter(s)
#       plain_text | string | the text to be encrypted (or unencrypted)
#   return value(s)
#       ciphertext | string | the encrypted (or unencrypted) text
# description: encrypts plain_text using the atbash cipher, a weak transposition cipher.
def atbash(plain_text, lower_alphabet=alphabet):
    lower_cipher = lower_alphabet[::-1]  # the cipher, which is the string but backwards

    upper_alphabet = lower_alphabet.upper()  # our alphabet for upper case letters
    upper_cipher = upper_alphabet[::-1]  # the cipher to match

    cipher_text = ''  # we start with an empty cipher

    for char in plain_text:
        # if the character is a letter, we encrypt it
        if char in lower_alphabet + upper_alphabet:
            # if-else to maintain case sensitivity
            if char in lower_alphabet:
                position = lower_alphabet.find(char)  # get the character's position from the regular alphabet
                cipher_char = lower_cipher[position]  # use that position for the transposed character
            else:
                position = upper_alphabet.find(char)
                cipher_char = upper_cipher[position]

            cipher_text += cipher_char  # append the transposed character to cipher text

        # otherwise we just attach it to the string
        else:
            cipher_text += char

    return cipher_text


def main():
    print('>> atbash cipher')

    if mode() == 'encrypt':
        plain_text = input('>> plain text' '\n' '>> ')
        cipher_text = atbash(plain_text)
    else:
        cipher_text = input('>> cipher text' '\n' '>> ')
        plain_text = atbash(cipher_text, lower_alphabet=alphabet[::-1])

    print(
        f'>> plain text  | {plain_text}' '\n'
        f'>> cipher text | {cipher_text}'
    )


main()
