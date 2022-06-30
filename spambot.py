# Whatsapp spam bot to troll your friends

# What you need is = What you need is: python, selenium webdriver and chromdriver successfully installed, knowing how to copy an x path

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, random 



browser = webdriver.Chrome('chromedriver') 
name_of_your_contact= 'henning'
messages = ['hi henning','hallo henning'] 


 



def go(name_of_your_contact, messages):          
	try:
		browser.get('https://web.whatsapp.com') #IMPORTANT: The login you have to do yourself at whatsapp web, for that you have to look at settings at whatsapp(on your phone) and scan the qr code. You have to have it ready, because you have only 20 seconds to do it.
		time.sleep(30)
		browser.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div[2]').send_keys(name_of_your_contact)  
		time.sleep(random.randrange(2,4))
		browser.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div[8]/div/div/div[2]/div[1]/div[1]/span').click() #every contact has a different xpath. When you are on whatsapp web, you need to copy the x path of your contact, the full x path where the field of your contact's name is.
		for message in range(500):                
			time.sleep(0.01)
			browser.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').send_keys(random.choice(messages))
			time.sleep(0.01)
			browser.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
			




	except Exception as err: 
		print(err)

go(name_of_your_contact, messages)