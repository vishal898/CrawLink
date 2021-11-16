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

f = open("message.txt","w")
f.write('started message.py\n')


csv.register_dialect('myDialect', delimiter=',', quoting=csv.QUOTE_ALL)
with open('src/message/message.csv', 'w+', newline='') as file:
    writer = csv.writer(file, dialect='myDialect')
    writer.writerow(['Name','Email'])


# csv.register_dialect('myDialect', delimiter=',', quoting=csv.QUOTE_ALL)
# with open('message.csv', 'w+', newline='') as file:
#     writer = csv.writer(file, dialect='myDialect')
#     writer.writerow(['Name','Email'])


username = sys.argv[1]
password = sys.argv[2]
# locList = ['india']
locList = json.loads(sys.argv[3])
# compList = ['Contrivers Edge','amazon']
# compList = []
compList = json.loads(sys.argv[4])
mess = "Hello"
mess = sys.argv[5]

f.writelines([str(username),'\n',str(password),'\n',str(locList),'\n',str(compList),'\n',str(mess),'\n'])

def addToSheet(person):
    csv.register_dialect('myDialect', delimiter=',', quoting=csv.QUOTE_ALL)
    with open('src/message/message.csv', 'a', newline='') as file:
        writer = csv.writer(file, dialect='myDialect')
        writer.writerow(person)
    f.write('adding to csv done\n')


# def addToSheet(person):
#     csv.register_dialect('myDialect', delimiter=',', quoting=csv.QUOTE_ALL)
#     with open('message.csv', 'a', newline='') as file:
#         writer = csv.writer(file, dialect='myDialect')
#         writer.writerow(person)
#     f.write('adding to csv done\n')

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
userid = browser.find_element_by_xpath("(//input[@id='session_key'])[1]")
userid.send_keys(username)
sleep(2)
userpass = browser.find_element_by_xpath("(//input[@id='session_password'])[1]")
userpass.send_keys(password)
sleep(2)
signIn = browser.find_element_by_xpath("(//button[normalize-space()='Sign in'])[1]")
signIn.click()
sleep(5)
browser.maximize_window()

f.write('login done\n')


while browser.current_url !="https://www.linkedin.com/feed/?trk=homepage-basic_signin-form_submit":
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


for ind in range(1,11):
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
    sleep(3)
    connectBtn = browser.find_element_by_xpath(f"(//span[normalize-space()='Message'])[{ind}]")
    connectBtn.click()
    sleep(3)
    browser.find_element_by_xpath("(//div[@aria-label='Write a message…'])[1]").send_keys(mess)   
    sleep(3)
    browser.find_element_by_xpath("(//button[normalize-space()='Send'])[1]").click()
    sleep(3)
    close= browser.find_element_by_xpath("(//button[@class='msg-overlay-bubble-header__control artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--1 artdeco-button--tertiary ember-view'])[1]")
    close.click()
    sleep(3)
    addToSheet(profile)
    sleep(5)
    
f.close() 
sleep(2)    
browser.close()


