from PIL import Image
import math

# For Grayscale image
# img = Image.open("lenna.png")


# width, height = img.size 
# print(width)

# for x in range(width): 
#     for y in range(height): 
#         (r,g,b) = img.getpixel((x,y))
#         avg = math.floor((r + g + b)/3)
#         img.putpixel((x, y), (avg, avg, avg))

# img.show() 

img = Image.open("lenna.png")
im = Image.new(mode="RGB", size=(256, 256))

for x in range(256): 
    for y in range(256): 
        (r,g,b) = img.getpixel((x*2, y*2))
        im.putpixel((x,y), (r,g,b))
im.show()





## second method from first method:
# img = Image.open("lenna.png")
# width, height = img.size #don't hardcode the values
# im = Image.new(mode="RGB", size=(width/2, height/2))

# for x in range(256): 
#     for y in range(256): 
#         (r,g,b) = img.getpixel((x*2, y*2))
#         im.putpixel((x,y), (r,g,b))
# im.show()
    