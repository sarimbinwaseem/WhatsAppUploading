# import os 
import datetime
import time
import urllib.request
import winsound

# Eip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
# print(Eip)
def playsound():
	winsound.PlaySound("1.wav", winsound.SND_ASYNC)
	time.sleep(5)

# print(datetime.datetime.today().hour)
# print(datetime.datetime.today().minute)
# datetime.date.today().day

time1 = 11
time2 = 18

per = True

while per:
	per2 = True
	if 	datetime.datetime.today().hour == time1 or datetime.datetime.today().hour == time2:
		while per2:
			try:
				Eip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
				if Eip:
					# os.system("python main.py")
					print("Main Program Executed") 
					time.sleep(3600)
					per2 = False
				
					
					 
			except:
				# playsound()
				print("Check Your Computer's Connection")
				time.sleep(20)
			
		time.sleep(2)
			