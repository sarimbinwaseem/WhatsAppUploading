import os
def Rename():	
	print("Renamer started..")
	path = 'D:\\FikreAkhirat WhatsApp Posts\\Posts'
	os.chdir(path)
	files = os.listdir()
	x = str(200)
	for file in files:
		y =str(x) + ".jpg"
		os.rename(file, y)
		x = int(x)
		print("Done:", x)
		x += 1
	print("Total files renamed:", x)

	print("Renamed from 200...")


	files = os.listdir()
	x = str(0)
	for file in files:
		y =str(x) + ".jpg"
		os.rename(file, y)
		x = int(x)
		print("Done:", x)
		x += 1
	print("Total files renamed:", x)

	print("Renamed...")
	print("Renamer Ended...")

# if __name__ == "__main__":
# 	Rename()

	
