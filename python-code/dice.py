import random

print("sides'd'number of dice  {A or D}")

inp = input()

numDie = 0
numSide = 0
split = 0

advan = 0

for i in range(len(inp)):
    if inp[i] == 'd':
        split = i

if inp[len(inp)-1] == "A":
    advan = 1
elif inp[len(inp)-1] == "D":
    advan = 2

numDie = int(inp[0:split])
if advan == 0:
    numSide = int(inp[split+1:len(inp)])
else:
    numSide = int(inp[split+1:len(inp)-1])


sum = 1

for i in range(numDie):
    roll = random.randint(1,numSide)

    if numDie <= 10:
        print(roll)
    else:
        if roll == 1:
            print("fail")
        elif roll == numSide:
            print("crit")

    if advan == 0:
        sum = sum + roll
    elif advan == 1:
        sum = max(sum,roll)
    else:
        sum = min(sum,roll)

print("roll : ", sum)
