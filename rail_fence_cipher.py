# author: elia deppe
# date: 7/28

# difficulty: hard

# Wikipedia: https://en.wikipedia.org/wiki/Rail_fence_cipher
#   Read this for a better understanding of the cipher.

# Introduction
#
# Implement encoding and decoding for the rail fence cipher.
#
# The Rail Fence cipher is a form of transposition cipher that gets its name from the way in which it's encoded.
#   It was already used by the ancient Greeks.
#
# In the Rail Fence cipher, the message is written downwards on successive "rails" of an imaginary fence,
#   then moving up when we get to the bottom (like a zig-zag). Finally the message is then read off in rows.
#
# For example, using three "rails" and the message "WE ARE DISCOVERED FLEE AT ONCE", the cipher writes out:
#
# W . . . E . . . C . . . R . . . L . . . T . . . E
# . E . R . D . S . O . E . E . F . E . A . O . C .
# . . A . . . I . . . V . . . D . . . E . . . N . .
#
# Then reads off:
#
# WECRLTEERDSOEEFEAOCAIVDEN
#
# To decrypt a message you take the zig-zag shape and fill the ciphertext along the rows.
#
# ? . . . ? . . . ? . . . ? . . . ? . . . ? . . . ?
# . ? . ? . ? . ? . ? . ? . ? . ? . ? . ? . ? . ? .
# . . ? . . . ? . . . ? . . . ? . . . ? . . . ? . .
#
# The first row has seven spots that can be filled with "WECRLTE".
#
# W . . . E . . . C . . . R . . . L . . . T . . . E
# . ? . ? . ? . ? . ? . ? . ? . ? . ? . ? . ? . ? .
# . . ? . . . ? . . . ? . . . ? . . . ? . . . ? . .
#
# Now the 2nd row takes "ERDSOEEFEAOC".
#
# W . . . E . . . C . . . R . . . L . . . T . . . E
# . E . R . D . S . O . E . E . F . E . A . O . C .
# . . ? . . . ? . . . ? . . . ? . . . ? . . . ? . .
#
# Leaving "AIVDEN" for the last row.
#
# W . . . E . . . C . . . R . . . L . . . T . . . E
# . E . R . D . S . O . E . E . F . E . A . O . C .
# . . A . . . I . . . V . . . D . . . E . . . N . .
#
# If you now read along the zig-zag shape you can read the original message.
#
# Instructions
#   1 - The program should accept input in the form of a string, which will be the plain text. This is the text
#           to be encrypted.
#   2 - The program should also accept a key from the user, which will be the number of rails for the cipher.
#   2 - Convert the plain text into cipher text using the rail fence cipher, with the specified number of rails.
#   3 - Print the result to the user.
#
# WRITE CODE BELOW #
def get_key():
    while True:
        try:
            num_rails = input('>> key\n')

            if num_rails == '':
                return num_rails
            else:
                return int(num_rails)

        except ValueError:
            print('>> invalid value for key, must be an integer, or left blank if decrypting and key is unknown')
            print()


def get_mode():
    mode = ''
    while mode != 'encrypt' and mode != 'decrypt':
        mode = input('>> mode\n')

        if mode != 'encrypt' and mode != 'decrypt':
            print(
                '>> mode options' '\n'
                '>>     [encrypt, decrypt]' '\n'
            )
    return mode


def rail_fence(mode, text, key):
    if mode == 'encrypt' and type(key) == int:
        rails = [[] for i in range(key)]

        return encrypt(text, key, rails)

    else:
        length = len(text)

        if type(key) == int:
            return decrypt(text, key, length)

        else:
            text = ''
            for key in range(2, length + 1):
                text += decrypt(text, key, length, single_key=False)

            return text


def encrypt(plain_text, num_rails, rails):
    current_rail, direction = 0, 1

    for char in plain_text:
        for j in range(num_rails):
            if j == current_rail:
                rails[j].append(char)
            else:
                rails[j].append('')

        current_rail += direction
        if current_rail == 0 or current_rail == num_rails - 1:
            direction = -direction

    print_rails(rails, num_rails)
    return get_cipher_text(rails)


def print_rails(rails, num_rails):
    print()
    for i in range(num_rails):
        print('[', end='')

        for j in range(len(rails[i])):
            if rails[i][j] == '':
                print('-', end='')
            else:
                print(rails[i][j], end='')

        print(']')
    print()


def get_cipher_text(rails):
    cipher_text = ''
    for rail in rails:
        cipher_text += ''.join(rail)

    return cipher_text


def decrypt(cipher_text, key, length, single_key=True):
    plain_text = ['' for i in range(length)]
    spacing = [[] for i in range(key)]

    for i in range(key):
        if i == 0 or i == key - 1:
            spacing[i].append(2 * (key - 1))
        else:
            spacing[i].append(2 * (key - 1) - 2 * i)
            spacing[i].append(2 * i)

    current_rail = 0
    position = 0
    for i in range(length):
        plain_text[position] = cipher_text[i]
        position += spacing[current_rail][0]

        spacing[current_rail].reverse()

        if position >= length:
            current_rail += 1
            position = current_rail

    if single_key:
        return ''.join(plain_text)
    else:
        return f'key | {key} \t| text | {"".join(plain_text)}' + '\n'


def main():
    print('>> rail fence cipher' '\n')

    mode = get_mode()
    key = get_key()

    if mode == 'encrypt':
        text = input('>> plain text\n')

    else:
        text = input('>> cipher text\n')

    print(rail_fence(mode, text, key))

main()
