from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import json
import sys 
import csv






csv.register_dialect('myDialect', delimiter=',', quoting=csv.QUOTE_ALL)
with open('src/project/project.csv', 'w+', newline='') as file:
    writer = csv.writer(file, dialect='myDialect')
    writer.writerow(['Link'])


username = sys.argv[1]
password = sys.argv[2]
noOfProject= int(float(sys.argv[3]))
compList = json.loads(sys.argv[4])







browser =""
try:
    browser = webdriver.Chrome(ChromeDriverManager().install()) 
except:
    try: 
        browser =  webdriver.Edge(EdgeChromiumDriverManager().install())
    except:
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())








 
browser.get('https://www.linkedin.com')

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

while browser.current_url !="https://www.linkedin.com/feed/?trk=homepage-basic_signin-form_submit":
    print('wait')


sleep(15)


sleep(5)    
try:
	downButton= browser.find_element_by_xpath("(//li-icon[@type='chevron-down-icon'])[4]")
	downButton.click()
except:
	print('no down button')

sleep(4)


browser.get("https://www.linkedin.com/search/results/people/?")
sleep(4)
browser.refresh
sleep(4)



def addToSheet(person):
    csv.register_dialect('myDialect', delimiter=',', quoting=csv.QUOTE_ALL)
    with open('src/project/project.csv', 'a', newline='') as file:
        writer = csv.writer(file, dialect='myDialect')
        writer.writerow(person)








company = browser.find_element_by_xpath("(//button[normalize-space()='Current company'])[1]")
sleep(2)
company.click();
sleep(2)

for i in compList:
    # print(f"{i}")
    sleep(2)
    searchComp = browser.find_element_by_xpath("(//input[@placeholder='Add a company'])[1]")
    searchComp.send_keys(i)
    sleep(3)
    searchComp.send_keys(Keys.DOWN)
    sleep(3)
    searchComp.send_keys(Keys.ENTER)

filterComp = browser.find_element_by_xpath("(//button[@aria-label='Apply current filter to show results'])[3]").click()
sleep(4)
browser.refresh
sleep(4)









def funForProject():
        element=browser.find_element_by_xpath("(//button[@aria-label='Expand projects section'])[1]");
        sleep(5)
        element.click();
        no=1
        while 1:
            try : 
                 sleep(5)
                 proj=browser.find_element_by_xpath(f"(//p[contains(@class,'pv-accomplishment-entity__description t-14')])[{no}]")
                 sleep(5)
                 print(proj.text)
                 profile=[proj.text]
                 addToSheet(profile)
                 no=no+1;
            except :
                 return

def funOnProfile():
         sleep(15)
         i = browser.execute_script("return document.body.scrollHeight")
         while i>=0 :
             browser.execute_script(f"window.scrollTo(0,{i});")
             sleep(5)
             try : 
                 sleep(5)
                 proj=browser.find_element_by_xpath("(//h3[normalize-space()='Projects'])[1]")
                 print(proj.text)
                 sleep(5)
                 funForProject();
                 browser.back();  
                 sleep(10)  
                 return
             except:
                 browser.back();  
                 sleep(10)
                 break
         return


i=1;
while i <= noOfProject:
            
         sleep(5)
         j=browser.find_element_by_xpath(f"(//span[@dir='ltr'])[{i}]");
         sleep(2)
         j.click();
         sleep(2);
         funOnProfile(); 
         sleep(5)
         i=i+1
       






















