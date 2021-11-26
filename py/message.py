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
with open('src/message/message.csv', 'w+', newline='') as file:
    writer = csv.writer(file, dialect='myDialect')
    writer.writerow(['Name','Link'])


# csv.register_dialect('myDialect', delimiter=',', quoting=csv.QUOTE_ALL)
# with open('src/message/message.csv', 'w+', newline='') as file:
#     writer = csv.writer(file, dialect='myDialect')
#     writer.writerow(['Name','Email'])


username = sys.argv[1]
password = sys.argv[2]
locList = json.loads(sys.argv[3])
compList = json.loads(sys.argv[4])
mess = sys.argv[5]
filePath = sys.argv[6]
cnt = 10



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

sleep(7)
userid = browser.find_element_by_xpath("(//input[@id='session_key'])[1]")
userid.send_keys(username)
sleep(2)
userpass = browser.find_element_by_xpath("(//input[@id='session_password'])[1]")
userpass.send_keys(password)
sleep(2)
signIn = browser.find_element_by_xpath("(//button[normalize-space()='Sign in'])[1]")

signIn.click()

sleep(7)
browser.maximize_window()



def addToSheet(person):
    csv.register_dialect('myDialect', delimiter=',', quoting=csv.QUOTE_ALL)
    with open('src/message/message.csv','a', newline='') as file:
        writer = csv.writer(file, dialect='myDialect')
        writer.writerow(person)




while browser.current_url !="https://www.linkedin.com/feed/":
    print('wait')

# print(start)

sleep(3)
browser.refresh()
sleep(3)

browser.get("https://www.linkedin.com/search/results/people/?")
sleep(3)
browser.refresh()
sleep(3)


connections = browser.find_element_by_xpath("(//button[normalize-space()='Connections'])[1]").click()
sleep(4)
selConn = browser.find_element_by_xpath("(//label[@for='network-F'])[1]").click()
sleep(4)
filterConn = browser.find_element_by_xpath("(//button[@aria-label='Apply current filter to show results'])[1]").click()
sleep(8)


locations = browser.find_element_by_xpath("(//button[normalize-space()='Locations'])[1]").click()
sleep(5)    
for i in locList:
    # print(f"{i}")
    sleep(3)
    searchLoc = browser.find_element_by_xpath("(//input[@placeholder='Add a location'])[1]")
    searchLoc.send_keys(i)
    sleep(5)
    searchLoc.send_keys(Keys.DOWN)
    sleep(5)
    searchLoc.send_keys(Keys.ENTER)
    sleep(5)

filterLoc = browser.find_element_by_xpath("(//button[@aria-label='Apply current filter to show results'])[2]").click()
sleep(4)
# browser.refresh()
sleep(4)



company = browser.find_element_by_xpath("(//button[normalize-space()='Current company'])[1]").click()
sleep(2)

for i in compList:
    # print(f"{i}")
    sleep(3)
    searchComp = browser.find_element_by_xpath("(//input[@placeholder='Add a company'])[1]")
    searchComp.send_keys(i)
    sleep(5)
    searchComp.send_keys(Keys.DOWN)
    sleep(5)
    searchComp.send_keys(Keys.ENTER)
    sleep(5)

filterComp = browser.find_element_by_xpath("(//button[@aria-label='Apply current filter to show results'])[3]").click()
sleep(4)
# browser.refresh()
sleep(4)


for ind in range(1,cnt):
    print(ind)
    sleep(3)
    btn = browser.find_element_by_xpath(f"(//div[@class='entity-result__actions entity-result__divider'])[{ind}]")
    print("button")
    print(btn.text)
    sleep(3)
    link = browser.find_element_by_xpath(f"(//span[contains(@class,'entity-result__title-line flex-shrink-1 entity-result__title-text--black')])[{ind}]/span/a")
    sleep(3)
    prf = browser.find_element_by_xpath(f"(//span[contains(@class,'entity-result__title-line flex-shrink-1 entity-result__title-text--black')])[{ind}]")
    sleep(3)
    profile = [prf.text.split('\n')[0],link.get_attribute('href')]
    print(profile)
    addToSheet(profile)
    sleep(3)
    connectBtn = browser.find_element_by_xpath(f"(//span[normalize-space()='Message'])[{ind}]")
    connectBtn.click()
    sleep(3)
    browser.find_element_by_xpath("(//div[@aria-label='Write a message…'])[1]").send_keys(mess)   
    sleep(3)

    if(len(filePath)>0):
        textbox= browser.find_element_by_xpath("(//input[@type='file'])[2]")
        sleep(2)
        textbox.send_keys(f"{filePath}")
        sleep(7)
    sleep(3)
    sendBtn = browser.find_element_by_xpath("(//button[normalize-space()='Send'])[1]")
    while(sendBtn.is_enabled() == False):
        print('button is disabled')
        sleep(2)

    print('button is enabled')
    sendBtn.click()
    sleep(3)
    close= browser.find_element_by_xpath("(//button[@class='msg-overlay-bubble-header__control artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--1 artdeco-button--tertiary ember-view'])[1]")
    close.click()
    sleep(3)
    sleep(5)
    

sleep(2)    
browser.close()


