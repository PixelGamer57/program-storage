import math

ONES = ["", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine "]
TEENS = ["ten ", "eleven ", "twelve ", "thirteen ", "fourteen ", "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen "]
TENS = ["", "ten ", "twenty ", "thirty ", "forty ", "fifty ", "sixty ", "seventy ", "eighty ", "ninety "]
BIGS = ["hundred ", "thousand ", "million ", "billion ", "trillion"]

def dig (num) :
    match len(num):
        case 1:
            if num == "0": return "zero"
            return ONES[int(num[-1])]
        case 2:
            if num[-2] == "1": return TEENS[int(num[-1])]
            return TENS[int(num[-2])] + ONES[int(num[-1])]
        case 3:
            if num[-3] == "0": return dig(num[-2:])
            return ONES[int(num[-3])] + BIGS[0] + dig(num[-2:])
        case 4 | 5 | 6:
            if num[0] == "0": return dig(num[1:])
            return dig(num[:-3]) + BIGS[1] + dig(num[-3:])
        case 7 | 8 | 9:
            if num[0] == "0": return dig(num[1:])
            return dig(num[:-6]) + BIGS[2] + dig(num[-6:])
        case 10 | 11 | 12:
            if num[0] == "0": return dig(num[1:])
            return dig(num[:-9]) + BIGS[3] + dig(num[-9:])
        case _:
            return

while True:

    inp = input().replace(",","")

    if(inp.isdigit() == False) :
        break

    print(dig(inp))

