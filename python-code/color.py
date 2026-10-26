def color (col) :
    col = str(col)
    c = ["⬜️","⬛","🟥","🟩","🟦","🟨","🟧","🟪","🟫"]
    if(col.isnumeric() and int(col) <= 8):
            return(c[int(col)])
    elif(col.isalpha()):
        col = col.lower()
        if col == "white" or col == "w":
            return c[0]
        elif col == "black" or col == "k" or col == "bk" or col == "blk":
            return c[1]
        elif col == "red" or col == "r":
            return c[2]
        elif col == "green" or col == "g":
            return c[3]
        elif col == "blue" or col == "b":
            return c[4]
        elif col == "yellow" or col == "y":
            return c[5]
        elif col == "orange" or col == "o":
            return c[6]
        elif col == "purple" or col == "p":
            return c[7]
        elif col == "brown" or col == "br":
            return c[8]