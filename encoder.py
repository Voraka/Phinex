import sys, os
import math
from PIL import Image

def encode(inpath, key):
	size = os.path.getsize(inpath)
	pixsize = int(size/3)
	length = int(math.sqrt(pixsize)+1)
	f = open(inpath, "rb")
	buffer = f.read()
	f.close()
	array_list = []
	array = bytearray(buffer)
	for b in array:	
		array_list.append(b)		
	index = 0
	im = Image.new("RGB", (length, length))	
	result = ""	
	key_array = bytearray(key)
	for i in xrange(length):
		for j in xrange(length):
			R = 0
			G = 0
			B = 0
			try:
				R = array_list.pop(0)
				G = array_list.pop(0)
				B = array_list.pop(0)
			except:
				pass
			R = R ^ (key_array[(index*3) % len(key)])
			G = G ^ (key_array[(index*3+1) % len(key)])
			B = B ^ (key_array[(index*3+2) % len(key)])
			result += "(%d, %d)  (%d, %d, %d)\n" %(i, j , R, G, B)
			index +=1		
			if index <size:						
				im.putpixel((i, j), (R, G, B))

	im.save(inpath+'.bmp')
	with open(inpath+'_enc.log', "w")as flog:
		flog.write(result)
		flog.close()


def main():
	inpath = r"C:\Users\Adminuser\Desktop\073a97a88e7a1512e1a7bbadcab962f4dcedd3f5.exe"		#payload here
	key = "RZ8DGTE2Cmb1qngtwdMkF5Lx9yJSjYriX0H46KfBQs"		#encrypt key here
	encode(inpath, key)
	
main()
