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


username = sys.argv[1]
password = sys.argv[2]
# lstOfProf = ['Dnyaneshwar Ware','devang kamble','vishal borse']
# lstOfProf = ['https://www.linkedin.com/in/dnyaneshwar2023/','https://www.linkedin.com/in/vishal-borse-76b9a5190/','https://www.linkedin.com/in/devang-kamble/']
lstOfProf = json.loads(sys.argv[3])
# print(lstOfProf)

browser =""
try:
    browser =  webdriver.Edge(EdgeChromiumDriverManager().install())
except:
    try: 
        browser =  webdriver.Chrome(ChromeDriverManager().install())
    except:
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        
browser.get('https://www.linkedin.com')
# browser.get('https://www.browserstack.com/guide/selenium-scroll-tutorial')

sleep(2)
browser.maximize_window()

sleep(2)
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

# print(start)

sleep(15)

for url in lstOfProf :
    print(url)
    browser.get(url)
    # print(browser.page_source)
    # sleep(15)
    # height = browser.execute_script("return document.body.scrollHeight")
    # print(height)
    browser.execute_script(f"window.scrollTo(0,5000);")
    sleep(5)
    i = browser.execute_script("return document.body.scrollHeight")
    while i>=0 :
        browser.execute_script(f"window.scrollTo(0,{i});")
        sleep(5)
        try : 
            sleep(5)
            browser.find_element_by_xpath("//h2[normalize-space()='Skills & endorsements']")
            sleep(5)
            # if len(browser.find_elements_by_xpath("//section[contains(@class, 'pv-profile-section')]"))>0 :
            #     print(len(browser.find_elements_by_xpath("//section[contains(@class, 'pv-profile-section')]")))
            skillBtns = browser.find_elements_by_xpath("(//button[@class='pv-skill-entity__featured-endorse-button-shared  artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--1 artdeco-button--secondary ember-view'])")
            sleep(5)
            print(skillBtns)
            for btn in skillBtns:
                print('btn')
                sleep(5)
                btn.click()
                sleep(5)
                close = browser.find_element_by_xpath("(//button[@aria-label='Dismiss'])[1]")
                close.click()
            break;
        except :
            i-=250
            

        # if len(browser.find_elements_by_xpath("//section[contains(@class, 'pv-profile-section')]"))>0 :
        #     print(len(browser.find_elements_by_xpath("//section[contains(@class, 'pv-profile-section')]")))

    


browser.close()




