# author:
# date:

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

