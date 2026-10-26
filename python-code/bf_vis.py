import math
import tkinter as tk

OPSPEED = 20

memsize = 64

text_file = input("Input BF code (.txt will be added automatically)\n")
OP_inp = input ("Operations per second: (default is 20)\n")
Mem_inp = input ("Number of memory cells: (default is 64)\n")

if OP_inp.isdigit() and len(OP_inp) > 0:
    OPSPEED = int(OP_inp)

if Mem_inp.isdigit() and len(Mem_inp) > 0:
    memsize = int(Mem_inp)

mem = [0] * memsize


bfcode = []
BFCHARS = ['+','-','<','>','[',']','.',',']

with open(text_file+".txt", "r") as file:
    content = file.read()

for i in content:
    if i in BFCHARS:
        bfcode.append(i)

running = True

pointer = 0
codeloc = 0

loops = []

root = tk.Tk()

root.geometry("500x500")

memframe = tk.Frame(root)
memframe.pack()

memlabels = []
for i in range(0,len(mem)):
    memlabels.append(tk.Label(memframe, text = f"{mem[i]}", width = 3))
    memlabels[i].grid(column = i%math.ceil(math.sqrt(memsize)), row = math.floor(i/math.ceil(math.sqrt(memsize))))


codeframe = tk.Frame(root)
codeframe.pack()

codelabels = []
for i in range(0,len(bfcode)):
    codelabels.append(tk.Label(codeframe, text = f"{bfcode[i]}", width = 1))
    codelabels[i].grid(column = i%20, row = math.floor(i/20))


entry = tk.Entry(root, width=30)
entry.pack(pady=10)

output = tk.Label(root, width=30, height=2, text="Program Output:\n")
output.pack(pady=10)

def get_input():
    global mem
    global codeloc
    global pointer

    inp = entry.get()
    if inp.isdigit:
        mem[pointer] = int(inp)%255
        codeloc += 1
        button.pack_forget()


button = tk.Button(root, text="Submit", command=get_input)

def loop():
    global running
    global pointer
    global codeloc
    global loops

    if codeloc < len(bfcode):
            
        for i in range(len(codelabels)):
            if i == codeloc:
                codelabels[i].config(bg = "blue")
            else:
                codelabels[i].config(bg = "white")
            
        match bfcode[codeloc]:
            case '+':
                mem[pointer] = (mem[pointer]+1)%255
                codeloc += 1
            case '-':
                mem[pointer] = (mem[pointer]-1)%255
                codeloc += 1
            case '>':
                pointer = (pointer+1)%memsize
                codeloc += 1
            case '<':
                pointer = (pointer-1)%memsize
                codeloc += 1
            case '.':
                print(f"{pointer}: {mem[pointer]}, {chr(mem[pointer])}")
                newtext = output.cget("text") + chr(mem[pointer])
                output.configure(text=newtext)
                codeloc += 1
            case ',':
                button.pack()
            case '[':
                loops.append(codeloc)
                codeloc += 1
            case ']':
                if mem[pointer] != 0:
                    codeloc = loops[-1] + 1
                else:
                    loops.pop()
                    codeloc += 1
            case _ :
                pass

        for i in range(len(memlabels)):
            memlabels[i].config(text = f"{mem[i]}")
            if i == pointer:
                memlabels[i].config(bg = "blue")
            else:
                memlabels[i].config(bg = "white")


        root.after(int(1000/OPSPEED), loop)
    else:
        return

root.after(int(1000/OPSPEED), loop)

root.mainloop()