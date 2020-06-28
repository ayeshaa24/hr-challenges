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

if __name__ == '__main__':
    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    print(result)
