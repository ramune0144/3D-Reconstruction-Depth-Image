from PIL import Image
import numpy as np
r = 10
g = 1
b = 0
color = [(r,g,b)]
rgb = Image.open(input("color"))
def img_scan(rgb,color):
    cod = []
    v_point = True
    u_start = False
    for v in range(rgb.size[1]):# height
        for u in range(rgb.size[0]):# width
             if(rgb.getpixel((u,v)) == color[0]):
                cod.append([u,v])
                break       
    return cod[0]
# test #
cod = img_scan(rgb,color)
print(cod)
img_c = rgb.crop((cod[0]-25,cod[1]-21,1229,516))
img_c.convert("I").show()

