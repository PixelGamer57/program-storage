list = ["a"]

def lol():
    list.append(list)
    print(list)

x = 0

while x < 10:
    lol()
    x += 1