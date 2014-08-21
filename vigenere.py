#!/usr/bin/env python
from math import fmod

# The minimum and maximum valid char, ascii table defined order
ascii_min = ord(' ')
ascii_max = ord('~')

def decrypt_vigenere(phrase, key):
    # Generate a string of all the possible chars
    alpha = ""
    for printable in range(ascii_min, ascii_max+1):
        alpha = alpha + chr(printable)

    # Ensure the key is at least as long as the ciphertext by cat'ing it
    while len(key) < len(phrase):
       key = key + key
    key = key[0:len(phrase)]

    out = ""
    for i in range(len(phrase)):
	index_from_phrase = (ord(phrase[i]) - ascii_min)
	index_from_key = ord(key[i]) - ascii_min
        difference = (index_from_phrase - index_from_key)

        # We want the sign of the dividend so we use fmod()
        # Use the inverse of this result (I'm not certain why - is there a simpler way?
	intersect = int(fmod(index_from_phrase - index_from_key, (ascii_max - ascii_min + 1)) * -1)

        letter = alpha[intersect]
        out += letter

    return out, key

if __name__ == "__main__":
    phrase = '''&'{. t+:o(#).*r_d7t~/H?.rtrv,4|1~"3*f+,#e>v+}p3%UnL<:?\\tG2KAH;E6$} 2{$=u$~)'''
    key = '''This is our world now... the world of the electron and the switch, the'''

    if len(key.strip()) > 0:
        deciphered, with_key = decrypt_vigenere(phrase, key.strip())
        print "Msg:\n%s\nKey:\n%s" % (deciphered, with_key)
        print "---"
