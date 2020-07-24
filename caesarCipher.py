#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
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
