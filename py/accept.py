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


csv.register_dialect('myDialect', delimiter=',', quoting=csv.QUOTE_ALL)
with open('src/accept/accept.csv', 'w+', newline='') as file:
    writer = csv.writer(file, dialect='myDialect')
    writer.writerow(['Link'])


username = sys.argv[1]
password = sys.argv[2]
noOfUserTOAccept= int(float(sys.argv[3]))


# username = "vishal.borse898@gmail.com"
# password = "azlinkedin123"
# noOfUserTOAccept=2; 



browser =""
try:
    browser = webdriver.Chrome(ChromeDriverManager().install()) 
except:
    try: 
        browser =  webdriver.Edge(EdgeChromiumDriverManager().install())
    except:
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())





 
browser.get('https://www.linkedin.com/login')
sleep(3)
browser.refresh()
sleep(3)

sleep(5)
browser.maximize_window()
sleep(10)
userid = browser.find_element_by_xpath(".//*[@id='session_key']")
userid.send_keys(username)
sleep(2)
userpass = browser.find_element_by_xpath(".//*[@id='session_password']")
userpass.send_keys(password)
sleep(2)
signIn = browser.find_element_by_xpath("(//button[normalize-space()='Sign in'])[1]")
signIn.click()

sleep(3)
browser.refresh()
sleep(3)

while browser.current_url !="https://www.linkedin.com/feed/?trk=homepage-basic_signin-form_submit":
    print('wait')

sleep(5)    
try:
	downButton= browser.find_element_by_xpath("(//li-icon[@type='chevron-down-icon'])[4]")
	downButton.click()
except:
	print('no down button')


sleep(5)
networkButton= browser.find_element_by_xpath("(//*[name()='svg'][@class='global-nav__icon '])[2]")
networkButton.click()
# networkButton= browser.find_element_by_xpath("(//a[@data-test-global-nav-link='mynetwork'])[1]")
# networkButton.click()




def addToSheet(person):
    csv.register_dialect('myDialect', delimiter=',', quoting=csv.QUOTE_ALL)
    with open('src/accept/accept.csv', 'a', newline='') as file:
        writer = csv.writer(file, dialect='myDialect')
        writer.writerow(person)





cntConnected=0

while cntConnected < noOfUserTOAccept :
    sleep(5)
    cntConnected=cntConnected+1
    try:
        
        sleep(5)
        profile= browser.find_element_by_xpath("(//a[@class='ember-view invitation-card__picture'])[1]");
        #print(profile)
        #print( profile.is_enabled() and profile.is_displayed())
        sleep(5)
        profile.click()
        sleep(5)
        print(browser.current_url)
        sleep(2)
        link=browser.current_url
        profile=[link]
        addToSheet(profile)
        sleep(5)
        browser.back()
        sleep(5)
        connectButton= browser.find_element_by_xpath("(//span[@class='artdeco-button__text'][normalize-space()='Accept'])[1]")       
        sleep(15)
        connectButton.click()
    except:
        print("no more connection to accept")
        break

    
print("code ended")

browser.close()






