import random

lang = {
    "print( ": ":O ",
    ")": ":/",
    "#": ":X",
    "input(": "?_?",
    "=": ":>",
    "+=": "+w+",
    "-=": "-w-",
    "int(": "0w0",
    "str(": "TwT",
    "for": "[|87",
    "in": "[00]",
    "if": ":33",
    "elif": ":))",
    "else": ":]]",
    "while": "88W88",
    "import": "UwU",
    "<": ";<",
    ">": ";>",
    "True": "=}",
    "False": "=,{",
    '"': ":P ",
    "random.randint(": "o_O"
}

filename = input("File Name:\n")

with open(filename) as f:
    code = f.read()   # read once

for py, sym in lang.items():
    code = code.replace(sym, py)

print("\nOutput:")
exec(code)
