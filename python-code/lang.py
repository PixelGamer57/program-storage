import time
program = []

with open("lang.txt") as file:
    for line in file.readlines():
        program.append(line.strip().lower())


RAM = [0]*65536
PC = 1
running = True

while running:
    if PC-1 < len(program):
        instr = program[PC-1].split()
        jumped = False
        match instr[0]:
            case "say":
                print(chr(RAM[int(instr[1])]), end="")
            case "read":
                print(RAM[int(instr[1])], end=" ")
            case "set":
                RAM[int(instr[1])] = int(instr[2])
            case "add":
                RAM[int(instr[1])] += int(instr[2])
            case "addram":
                RAM[int(instr[1])] += RAM[int(instr[2])]
            case "jif":
                if RAM[int(instr[1])] == int(instr[2]):
                    PC = int(instr[3])
                    jumped = True
            case "jiq":
                if RAM[int(instr[1])] == RAM[int(instr[2])]:
                    PC = int(instr[3])
                    jumped = True
            case "jump":
                PC = int(instr[1])
                jumped = True
            case "inp":
                RAM[int(instr[1])] = int(input("Input: "))
            case "#":
                pass
            case "end":
                running = False
            case _:
                running = False
                print("Unknown instruction at line " + str(PC))
        PC += int(not jumped)
    else:
        running = False