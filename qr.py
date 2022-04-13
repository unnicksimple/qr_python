#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 05:27:37 2022

@author: unnick
"""

import sys
import qrcode
from PIL import Image, ImageDraw, ImageFont

# texto
# pie de qr
# version
# dimension

#ejecucion python qr.py "otra cosa"

gpus = sys.argv

qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 10,
    border=4
)

datos = str(sys.argv[1])

qr.add_data(datos)
qr.make(fit=True)

img = qr.make_image()

img.save('/home/unnick/Pictures/codigo.png')

img = Image.open('/path/codigo.png')
ancho, alto = img.size

img = img.resize((330, 330), Image.ANTIALIAS)

draw = ImageDraw.Draw(img)

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf", 20)
draw.text((30, 300), datos, font=font, fill="black")
img.save('/path/codigo_txt.png')
