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
                #v_point =True
                #u_start = True
        #if v_point == False and u_start == True: break #หากหมดเเล้วออกloopเลย
        #v_point = False         
    return cod[0]
#ตัดภาพ

cod = img_scan(rgb,color)
print(cod)
img_c = rgb.crop((cod[0]-25,cod[1]-21,1229,516))
#img_c =image[cod[0][1]:cod[1][1],cod[0][0]:cod[1][0]] #[start_y:end_y, start_x:end_x]
#print(rgb.convert("I").getpixel((94,564)))
##
#เเสดงภาพ
#img = Image.fromarray(img_c,'RGB')#ทำให้ np.arrayเป็นimgเเบบgrayscale
img_c.convert("I").show()
##
