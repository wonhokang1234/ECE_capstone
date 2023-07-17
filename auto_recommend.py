import outfit_func as of
import sys
from urllib.request import HTTPError #py3
from urllib.request import urlopen
import base64
import tkinter as tk
from PIL import Image, ImageTk
import PIL

import io

root = tk.Tk()
root.title("display a website image")
w = 1920
h = 1080
x = 960
y = 540

root.geometry("%dx%d+%d+%d" % (w, h, x, y))
cv = tk.Canvas(bg='black')
cv.pack(side='top', fill='both', expand='yes')

# read output.txt from opencv api
with open('/home/d4/myflection/opencv_color/output.txt', 'r') as f:
    color_line = f.readline()
    rgb_values = color_line[1:-2].split(', ')

# set rgb values from opencv
in_col_r = rgb_values[0]
in_col_g = rgb_values[1]
in_col_b = rgb_values[2]

in_col_r = int(in_col_r)
in_col_g = int(in_col_g)
in_col_b = int(in_col_b)

formality = 'informal'

outfit_recommendation = of.find_outfit_recommend(in_col_r, in_col_g, in_col_b, formality)

print('outfit recommendations: ', outfit_recommendation)

def load_image_to_base64(image_url):
    """ Load an image from a web url and return its data base64 encoded"""
    image_byt = urlopen(image_url).read()
    # image_b64 = base64.encodestring(image_byt)
    return image_byt

# load photos to photos list
urllist = []
for (topurl, boturl) in outfit_recommendation:
	urllist.append(topurl)
	urllist.append(boturl)

photos = []
for i, url in enumerate(urllist):
    try:
        data=load_image_to_base64(url)
        image = Image.open(io.BytesIO(data))
        resize_image = image.resize((400, 400))
        # image.resize((200, 200))
        photo = ImageTk.PhotoImage(resize_image)
        photos.append(photo)
    except HTTPError as err:
        print("image not found, http error code:", err.code)
    except ValueError:
        print("invalid url", url)


# iterate through photos and put them onto the canvas
for j, photo in enumerate(photos[:8]):
    if (j % 2 == 0):
        cv.create_image(70 + 220*j, 100, image=photo, anchor='nw')
    else:
        cv.create_image(70 + 220*(j-1), 550, image=photo, anchor='nw')
    

root.mainloop()
#...

# with open("recommendation0.txt", 'w') as sys.stdout:
# 	print(outfit_recommendation[0])

# with open("recommendation1.txt", 'w') as sys.stdout:
# 	print(outfit_recommendation[1])

# with open("recommendation2.txt", 'w') as sys.stdout:
# 	print(outfit_recommendation[2])

# with open("recommendation3.txt", 'w') as sys.stdout:
# 	print(outfit_recommendation[3])

# with open("recommendation4.txt", 'w') as sys.stdout:
# 	print(outfit_recommendation[4])
