import os, bases

os.system("cls")

file = open('test.txt','r').read().split(' ')

run = True
var1 = 0
var2 = 0
count = 0

instr = {
    '0000':'run = False',
    '0001':'print(var1);\nprint(var2)',
    '0010':'count += 1;\nvar1 = file[count]',
    '0011':'count += 1;\nvar2 = file[count]',
    '0100':'var1 = (bases.baseNum(2,var1) + bases.baseNum(2,var2)).format(4);\nvar2 = bases.baseNum(2,0).format()',
    '0101':'',
    '0110':'',
    '0111':'',
    '1000':'',
    '1001':'',
    '1010':'',
    '1011':'',
    '1100':'',
    '1101':'',
    '1110':'',
    '1111':''
}

while run:
    if count < len(file):
        exec(instr[file[count]])
        count += 1
    else:
        count = 0