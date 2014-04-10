from PIL import Image
from math import floor
import os

def generate(w,h):
    pentagram_image = Image.open('./static/images/pentagram_white.png')

    # get size of pentagram image
    pentagram_image_size = pentagram_image.size
    pentagram_image_width = pentagram_image_size[0]
    pentagram_image_height = pentagram_image_size[1]

    # resize pentagram if created image is under a certain size
    if w < 350 or h < 350:
        max_dim=0
        if w < 350 and h < 350:
            # pentagram should scale down to 75% of the shortest dimension of the image
            if w < h:
                max_dim = int(floor(.75*w))
            else:
                max_dim = int(floor(.75*h))

        elif w < 350:
            max_dim = int(floor(.75*w))
        elif h < 350:
            max_dim = int(floor(.75*h))

        pentagram_image_width = max_dim
        pentagram_image_height = max_dim
        print max_dim
        pentagram_image = pentagram_image.resize((pentagram_image_width,pentagram_image_height),Image.ANTIALIAS)

    # calculate x/y origin point for pentagram so it is centered
    # (W/2)-(w/2)
    pentagram_origin_x = (w/2)-(pentagram_image_width/2)
    # (H/2)-(h/2)
    pentagram_origin_y = (h/2)-(pentagram_image_height/2)

    background = Image.new('RGB',(w,h),(0,0,0))
    background.paste(pentagram_image,(pentagram_origin_x,pentagram_origin_y))

    file_path='/tmp/test.png'
    background.save(file_path)
    return file_path
