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

# f = open('sendMessToPeopleOld.csv', "w+")
# f.close()
csv.register_dialect('myDialect', delimiter=',', quoting=csv.QUOTE_ALL)
with open('src/connection/sendMessToPeopleOld.csv', 'w+', newline='') as file:
    writer = csv.writer(file, dialect='myDialect')
    writer.writerow(['Name','Link'])




username = sys.argv[1]
password = sys.argv[2]
#connList = ['S','O']
connList = json.loads(sys.argv[3])
# locList = ['india','usa']
#locList = []
locList = json.loads(sys.argv[4])
# compList = ['Amazon']
#compList = []
compList = json.loads(sys.argv[5])
mess = sys.argv[6]
'''

username="sweetyjiji11@gmail.com"
password="Kshitij5"
#username="kshitijsabale14@gmail.com"
#password="Mumbai#123"
connList = ['S','O']
locList = ['india','usa']
compList = ['Amazon']
mess=""
'''


def addToSheet(person):
    csv.register_dialect('myDialect', delimiter=',', quoting=csv.QUOTE_ALL)
    with open('src/connection/sendMessToPeopleOld.csv', 'a', newline='') as file:
        writer = csv.writer(file, dialect='myDialect')
        writer.writerow(person)


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
sleep(15)
userid = browser.find_element_by_xpath(".//*[@id='session_key']")
userid.send_keys(username)
sleep(2)
userpass = browser.find_element_by_xpath(".//*[@id='session_password']")
userpass.send_keys(password)
sleep(2)
signIn = browser.find_element_by_xpath("(//button[normalize-space()='Sign in'])[1]")
signIn.click()

while browser.current_url !="https://www.linkedin.com/feed/?trk=homepage-basic_signin-form_submit":
    print('wait')


sleep(15)

browser.get("https://www.linkedin.com/search/results/people/?")
sleep(4)
browser.refresh()
sleep(4)
# browser.get("https://www.linkedin.com/search/results/people/?network=%5B%22S%22%2C%22O%22%5D&origin=FACETED_SEARCH&sid=D2u")



connections = browser.find_element_by_xpath("(//button[normalize-space()='Connections'])[1]").click()
sleep(3)
for i in connList:
    sleep(2)
    selConn = browser.find_element_by_xpath(f"(//label[@for='network-{i}'])[1]").click()
    sleep(3)

sleep(2)
filterConn = browser.find_element_by_xpath("(//button[@aria-label='Apply current filter to show results'])[1]").click()
sleep(4)
# browser.refresh()
sleep(4)



locations = browser.find_element_by_xpath("(//button[normalize-space()='Locations'])[1]").click()
sleep(3)    
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
sleep(3)
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
con=browser.find_elements_by_xpath("(//span[@class='artdeco-button__text'][normalize-space()='Connect'])")

c=0
for ind in range(1,11):
    sleep(3)
    btn=con[c]

    sleep(3)
    link = browser.find_element_by_xpath(f"(//span[contains(@class,'entity-result__title-line flex-shrink-1 entity-result__title-text--black')])[{ind}]/span/a")
    # print("link")
    print(link.get_attribute('href'))
    sleep(2)
    prf = browser.find_element_by_xpath(f"(//span[contains(@class,'entity-result__title-line flex-shrink-1 entity-result__title-text--black')])[{ind}]")
    # print("profile")
    print(prf.text.split('\n')[0])
    sleep(3)
    profile = [prf.text.split('\n')[0],link.get_attribute('href')]
    # print(profile)
    sleep(3)
   
    print(btn)
    btn.click()
    sleep(3)
    print("mess length")
    print(len(mess))
    if(len(mess)>0):
        print(mess)
        browser.find_element_by_xpath("(//span[normalize-space()='Add a note'])[1]").click()
        sleep(4)
        browser.find_element_by_xpath("(//textarea[@id='custom-message'])[1]").send_keys(mess)   
        sleep(4)
        browser.find_element_by_xpath("(//span[normalize-space()='Send'])[1]").click()
    else:
        browser.find_element_by_xpath("(//*[name()='svg'][@class='mercado-match'])[1]").click()
    # browser.find_element_by_xpath("(//button[@aria-label='Send now'])[1]").click()
    sleep(3)
    addToSheet(profile)
    c=c+1
    sleep(5)
        # browser.find_element_by_xpath("(//button[@aria-label='Dismiss'])[1]").click()

# for buts in browser.find_elements_by_xpath("//button[normalize-space()='Connect']"):
#     sleep(2)

#     sleep(2)
#     buts.click()
#     sleep(2)
#     browser.find_element_by_xpath("(//button[@aria-label='Dismiss'])[1]").click()
#     print(buts)

# cnt =0
# while cnt<10:
#     (//button[@class='artdeco-button artdeco-button--2 artdeco-button--secondary ember-view'])[1] - connect 
#     (//button[@class='artdeco-button artdeco-button--2 artdeco-button--primary ember-view'])[1] - message
#     (//button[@aria-label='Follow'])[3] - follow 

# crawling over pages 
# https://www.linkedin.com/search/results/people/?page=

browser.close()


