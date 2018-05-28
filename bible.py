#!/usr/bin/env python

import inkyphat
from random import randint

def draw_text(position, text, font=None, colour=inkyphat.BLACK):
 x, y = position
 x = x+5
 if font is None:
  font = inkyphat.ImageFont.truetype(inkyphat.fonts.AmaticSC,20) # The font size here must match test_font 
  w, h = font.getsize(text)
  mask = inkyphat.Image.new('1', (w, h))
  draw = inkyphat.ImageDraw.Draw(mask)
  draw.text((0, 0), text, 1, font)
  position = x,y
  inkyphat.paste(colour, position, mask)

# Test font size to determine the maximum number of characters per line and should match the default font used in draw_text
test_font = inkyphat.ImageFont.truetype(inkyphat.fonts.AmaticSC,20)
w, h = test_font.getsize("1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ")
max_char = int((212/(w/36)))

quotes = open("quotes", "r")
lines = quotes.readlines()
quotes.close()
maximum = len(lines)
choice=(randint(1,maximum-1))
test = str(lines[choice])
text = [test[i:i+max_char] for i in range(0,len(test),max_char)]


for i in range(len(text)):
 new_text=text[i]
 if (new_text[max_char-1:max_char])!=" ":
  new_text=new_text+"-"
  if (new_text[-2:-1:])==".":
   new_text=new_text[:-1]
  if (new_text[-2:-1:])==",":
   new_text=new_text[:-1]
  if (new_text[-2:-1:])==";":
   new_text=new_text[:-1]
  if (new_text[-2:-1:])==":":
   new_text=new_text[:-1]
  if (new_text[-2:-1:])==" ":
   new_text=new_text[:-1]
 text[i]=new_text

try:
 draw_text((0,0), str(text[0]), colour=inkyphat.RED)
 draw_text((0,20), str(text[1]), colour=inkyphat.BLACK)
 draw_text((0,40), str(text[2]), colour=inkyphat.BLACK)
 draw_text((0,60), str(text[3]), colour=inkyphat.BLACK)
 draw_text((0,80), str(text[4]), colour=inkyphat.BLACK)
except IndexError:
    pass
inkyphat.show()
