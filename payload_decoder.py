import sys, os
import math
from PIL import Image


def decode(inpath, key):
	key_array = bytearray(key)
	im = Image.open(inpath)
	rgb_im = im.convert('RGB')
	byte_buffer = []	
	enc_log = ""
	index = 0
	lengthX, lengthY = im.size
	for i in xrange(lengthX):
		for j in xrange(lengthY):		
			R, G, B = rgb_im.getpixel((i, j))
			R = R ^ (key_array[(index*3) % len(key)])
			G = G ^ (key_array[(index*3+1) % len(key)])
			B = B ^ (key_array[(index*3+2) % len(key)])
			enc_log += "(%d, %d)  (%d, %d, %d)\n" %(i, j , R, G, B)
			index +=1
			byte_buffer.append(R)
			byte_buffer.append(G)
			byte_buffer.append(B)								
			
	# with open(inpath+'_dec.log', "w")as flog:
		# flog.write(enc_log)
		# flog.close()
	
	with open(inpath+'_dec.exe', "wb")as fout:
		fout.write(bytearray(byte_buffer[:lengthX*lengthY]))
		fout.close()
		
		
def main():	
	inpath = r"C:\Users\Adminuser\Desktop\PydbgHook.py.bmp"
	key = "RZ8DGTE2Cmb1qngtwdMkF5Lx9yJSjYriX0H46KfBQs"
	decode(inpath, key)
	
main()
