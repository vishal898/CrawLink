from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import json
import sys 
import csv


f = open("notifLike.txt","w")
f.write('started notifLike.py\n')

csv.register_dialect('myDialect', delimiter=',', quoting=csv.QUOTE_ALL)
with open('src/notification/notifLike.csv', 'w+', newline='') as file:
    writer = csv.writer(file, dialect='myDialect')
    writer.writerow(['Link'])



username = sys.argv[1]
password = sys.argv[2]
cntreq =int(float(sys.argv[3]))


f.writelines([str(username),'\n',str(password),'\n',str(cntreq),'\n'])

# username = "vishal.borse898@gmail.com"
# password = "azlinkedin123"
# cntreq=3; 



browser =""
try:
    browser = webdriver.Chrome(ChromeDriverManager().install()) 
except:
    try: 
        browser =  webdriver.Edge(EdgeChromiumDriverManager().install())
    except:
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())



browser.get('https://www.linkedin.com')
sleep(3)
browser.refresh()
sleep(3)

sleep(7)

userid = browser.find_element_by_xpath(".//*[@id='session_key']")
userid.send_keys(username)
sleep(2)
userpass = browser.find_element_by_xpath(".//*[@id='session_password']")
userpass.send_keys(password)
sleep(2)
signIn = browser.find_element_by_xpath("(//button[normalize-space()='Sign in'])[1]")
signIn.click()
sleep(5)
browser.maximize_window()

f.write('login done\n')

while browser.current_url !="https://www.linkedin.com/feed/?trk=homepage-basic_signin-form_submit":
    print('wait')

sleep(3)
browser.refresh()
sleep(3)


sleep(3)
try:
	downButton= browser.find_element_by_xpath("(//li-icon[@type='chevron-down-icon'])[4]")
	downButton.click()
except:
	print('no down button')

sleep(3)
notfButton= browser.find_element_by_xpath("(//a[@data-test-global-nav-link='notifications'])[1]")
notfButton.click()


buttonNo=1
tileNo=1
cnt=0


def addToSheet(person):
    csv.register_dialect('myDialect', delimiter=',', quoting=csv.QUOTE_ALL)
    with open('src/notification/notifLike.csv','a', newline='') as file:
        writer = csv.writer(file, dialect='myDialect')
        writer.writerow(person)



def funForLikeClick():
	sleep(5)
	try :
		like= browser.find_element_by_xpath("(//span[@aria-hidden='true'][normalize-space()='Like'])[1]")
		sleep(2)
	except :
		try:
			send= browser.find_element_by_xpath("(//button[normalize-space()='Send'])[1]")
			sleep(3)
		except:
			browser.back()
			return
		sleep(2)
		
		try:		
			send.click()
			sleep(3)
		except:
			print("not clickable")

		close= browser.find_element_by_xpath("(//button[@class='msg-overlay-bubble-header__control artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--1 artdeco-button--tertiary ember-view'])[1]")
		sleep(2)
		close.click()
		sleep(3)
		return
	isClassPresent = like.get_attribute("class").split(' ')
	for i in isClassPresent:
		print(i)
		if(i == 'react-button__text--like'):
			browser.back()
			return

	like.click()
	print(browser.current_url)
	link=browser.current_url
	profile=[link]
	addToSheet(profile)
	browser.back()
	return



def funForTile():
	global tileNo
	global cnt
	while 1 :
		print("in1")
		try :
			if cnt >= cntreq :
				return
			print(tileNo)
			sleep(5)
			tile= browser.find_element_by_xpath(f"(//span[@class='nt-card__text--3-line'])[{tileNo}]")
			sleep(5)
			tile.click()
			cnt=cnt+1
		except :
			print("not found")
			break

		tileNo=tileNo+1
		
		funForLikeClick()
		sleep(10)
		


 

while 1:
	sleep(5)
	funForTile()
	sleep(4)
	if cnt > cntreq :
		 break
	try:
		showMoreButton= browser.find_element_by_xpath("(//span[@class='artdeco-button__text'][normalize-space()='Show more results'])[1]")
		showMoreButton.click();
	except:
		print("all finised")
		break;

browser.close()