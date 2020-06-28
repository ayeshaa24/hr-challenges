import timeit

# _ = hour
# ^ = minute
# * = past/to

def timeInWords(h, m):
    words = [
        "one", "two", "three", "four", "five", "six", "seven",
        "eight", "nine", "ten", "eleven", "twelve", "thirteen",
        "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
        "nineteen", "twenty", "twenty one", "twenty two", "twenty three",
        "twenty four", "twenty five", "twenty six", "twenty seven",
        "twenty eight", "twenty nine",
    ]

    form = {
        0 : "_ o' clock",
        1: "one minute past _",
        59: "one minute to _",
        15: "quarter past _",
        30: "half past _",
        45: "quarter to _"
    }

    ans = form.get(m, "^ minutes * _")
    replace = ["past", words[h-1], ""]
    if m > 30:
        replace[0] = "to"
        if h == 12:
            replace[1] = "one"
        else:
            replace[1] = words[h]
        replace[2] = words[(60-m)-1]
    elif m < 30:
        replace[2] = words[m-1]

    ans = ans.replace("*", replace[0])
    ans = ans.replace("_", replace[1])
    ans = ans.replace("^", replace[2])
    return(ans)

def altTimeInWords(h, m):
    words = {1: "one", 2: "two",   3: "three", 4: "four",  5: "five",
         6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
         11: "eleven",   12: "twelve",  13: "thirteen",   14: "fourteen",
         15: "fifteen",  16: "sixteen", 17: "seventeen",  18: "eighteen",
         19: "nineteen", 20: "twenty",  21: "twenty one", 22: "twenty two",
         23: "twenty three", 24: "twenty four",  25: "twenty five",
         26: "twenty six",   27: "twenty seven", 28: "twenty eight",
         29: "twenty nine"}
    h = 12
    m = 31
    if m == 0:
        return words[h], "o' clock"
    elif m == 30:
        return "half past", words[h]
    if m < 30:
        if m == 1:
            return "one minute past", words[h]
        elif m == 15:
            return "quarter past", words[h]
        else:
            return words[m], "minutes past", words[h]
    else:
        m = 60 - m
        h += 1
        if m == 1:
            return "one minute to", words[h]
        elif m == 15:
            return "quarter to", words[h]
        else:
            return words[m], "minutes to", words[h]

if __name__ == '__main__':
    setup = """
import random
from __main__ import timeInWords
"""
    test = """
h = random.randint(1, 12)
m = random.randint(0, 60)
timeInWords(h, m)
"""
    times = timeit.repeat(setup = setup,
                          stmt = test,
                          repeat = 5,
                          number = 100000)

    # printing minimum exec. time
    print('Calculation: {}'.format(min(times)))

    setup = """
import random
from __main__ import altTimeInWords
"""
    test = """
h = random.randint(1, 12)
m = random.randint(0, 60)
altTimeInWords(h, m)
"""
    times = timeit.repeat(setup = setup,
                          stmt = test,
                          repeat = 5,
                          number = 100000)

    print('Calculation: {}'.format(min(times)))
