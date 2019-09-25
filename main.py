from selenium import webdriver
import time
import Renamer
import PictureCutPaste as pcp
import os
import winsound



options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=D:\\WebWhatsAppBot")
navegador = webdriver.Chrome(
executable_path="D:\\WebWhatsAppBot\\chromedriver.exe", chrome_options=options)

def playsound():
	winsound.PlaySound("1.wav", winsound.SND_ASYNC)
	time.sleep(5)

def upload():
	linkToPost = 'D:\\FikreAkhirat WhatsApp Posts\\Posts\\0.jpg'
	print("Getting the web page")	
	navegador.get("https://web.whatsapp.com/")
	time.sleep(10)
	print("Got it...!!!")
	
	per = True

	while per:
		
		try:

			grou = '//*[@title="جامعہ علی رضی اللہ عنہ"]'
			
			group = navegador.find_element_by_xpath(grou).click()
		except Exception as e:
			print(e)
			print("Connect your phone to Internet..")
			playsound()
			
			navegador.refresh()
			time.sleep(15)
		else:
			print("Posting to Jamia Ali group")
			time.sleep(1)
			clip_button = navegador.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]').click()
			time.sleep(1)
			photo_icon = navegador.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[1]/button/input')
			time.sleep(1)
			photo_icon.send_keys(linkToPost)

			time.sleep(2)

			submit_button = navegador.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span[2]/div').click()

			time.sleep(8)
			print('Posted...')
			#######################################################
			# print('Posting to Sharing...')
			# grou = '//*[@title="Sharing"]'
			# group = navegador.find_element_by_xpath(grou).click()
			# time.sleep(1)
			# clip_button = navegador.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]').click()
			# time.sleep(1)
			# photo_icon = navegador.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[1]/button/input')
			# time.sleep(1)
			# photo_icon.send_keys(linkToPost)

			# time.sleep(2)

			# submit_button = navegador.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span[2]/div').click()

			# time.sleep(8)
			# print('Posted...')
			##########################################################
			# navegador.close()
			navegador.quit()
			pcp.pcp()
			time.sleep(2)
			Renamer.Rename()
			time.sleep(1)
			per = False
			
if __name__ == '__main__':
	upload()