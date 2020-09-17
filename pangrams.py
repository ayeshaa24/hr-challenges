#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(s):
    # s = s.lower()
    # alphabet = "qwertyuiopasdfghjklzxcvbnm"
    # for a in alphabet:
    #     if a not in s:
    #         return "not pangram"

    # return "pangram"

    # alphabet = set("qwertyuiopasdfghjklzxcvbnm")
    # s = set(s.lower())-set(" ")
    # return "pangram" if alphabet == s else "not pangram"

    return "pangram" if len(set(s.lower())-set(" ")) == 26 else "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
