from PIL import Image
import numpy as np
import sys

filename = sys.argv[1]

im = Image.open(filename)

(width, height) = im.size   #tuple: (width, height)

print "----------", im.mode, im.format, (width, height), "-------------"
print "------------original matrix-----------"
pix = np.array(im)

print pix



print"----------------store---------------------"

img = Image.new("L",(width, height),"white")

for y in range (height):
	for x in range (width):
		l1 = pix[height-1-y][width-1-x]
		img.putpixel((x,y), l1)



img.save("ans2.png")


