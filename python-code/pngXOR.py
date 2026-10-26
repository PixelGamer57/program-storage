from PIL import Image
from urllib.request import urlopen

file1 = input("File 1: ")
file2 = input("File 2: ")

img1 = Image.open(urlopen(file1)).convert("RGBA")
img2 = Image.open(urlopen(file2)).convert("RGBA")

w = min(img1.width, img2.width)
h = min(img1.height, img2.height)

out = Image.new("RGBA", (w, h))

p1 = img1.load()
p2 = img2.load()
po = out.load()

for y in range(h):
    for x in range(w):
        r1,g1,b1,a1 = p1[x,y]
        r2,g2,b2,a2 = p2[x,y]
        po[x,y] = (
            r1 ^ r2,
            g1 ^ g2,
            b1 ^ b2,
            a1 | a2
        )

out.save("test.png")
