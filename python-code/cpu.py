instr = open("cpu_instr.txt","rt").read().splitlines()

pc = 0

reg = ["00000000"] * 4
ram = ["00000000"] * 8

while pc >= 0 and pc < len(instr):
    byte = instr[pc]
    a35
    a323 = int(byte[3:5],2)
    b323 = int(byte[5:8],2)
    match byte[0:3]:
        case "000": # jump 3 5
            pc = int(a35,2)
            break
        case "001": # jump if zero 3 2 3
            if reg[a323] == "00000000":
                pc = b323
            else:
                pc += 1
            break
        case "010": # load 3 2 3
            ram[int(reg[a323],2)] = "00000"+byte[5:8]
            break
        case "011": # shift left 3 2 3
            ram[int(reg[a323],2)] = "000"+ram[int(reg[a323],2)][5:8]+"0"
            break

        case "100": #
            break
        case "101": #
            break
        case "110": #
            break
        case "111": #
            break

