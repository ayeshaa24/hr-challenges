#!/bin/python3

import math
import os
import random
import re
import sys

def caesarCipher(s, k):
    def get_cipher(c):
        if 65 <= ord(c) <= 90:
            base = 65 #A
        elif 97 <= ord(c) <= 122:
            base = 97 #a
        else:
            return c

        char = ord(c) - base
        return chr(((char+k)%26)+base)

    return "".join([get_cipher(c) for c in s])

# Complete the caesarCipher function below.
def altCaesarCipher(s, k):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    newAlphabet = alphabet[k%26:] + alphabet[:k%26]
    alphabet += alphabet.upper()
    newAlphabet += newAlphabet.upper()
    print(alphabet, newAlphabet)
    translate_table = str.maketrans(alphabet, newAlphabet)
    return s.translate(translate_table)

if __name__ == '__main__':
    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    print(result)
