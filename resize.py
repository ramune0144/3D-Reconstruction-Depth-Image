from PIL import Image
from scr import mat_con,data
import concurrent.futures
import os
def resize(image):
    img = Image.open(image)
    new_width  = 200
    new_height = 300
    img = img.resize((new_width, new_height), Image.ANTIALIAS)
    img.save(f"./img/{os.path.basename(image)}.jpg")
    

dat = data.json_read("setting.json")
img_color = dat["color"]
img_depth = dat["depth"]       

for i in img_color:
    resize(i)
for i in img_depth:
    resize(i)    