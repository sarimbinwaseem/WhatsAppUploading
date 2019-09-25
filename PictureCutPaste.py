import os
import string
import random
def pcp():	
	print("Cut Paste Started")
	os.chdir('D:\\FikreAkhirat WhatsApp Posts\\Posts')
	path = 'D:\\FikreAkhirat WhatsApp Posts\\Done\\' + str(random.choice(string.ascii_letters)) + str(random.choice(string.ascii_letters)) + str(random.choice(string.ascii_letters)) + '.jpg'
	os.rename('0.jpg', path)
	print("Cut and Pasted")

# if __name__ == "__main__":
# 	pcp()