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
with open('src/job/job.csv', 'w+', newline='') as file:
    writer = csv.writer(file, dialect='myDialect')
    writer.writerow(['Link'])



username = sys.argv[1]
password = sys.argv[2]
jobTypeList = json.loads(sys.argv[3])
noOfComp=int(float(sys.argv[4]))
compList = json.loads(sys.argv[5])



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



sleep(5)
try:
	downButton= browser.find_element_by_xpath("(//li-icon[@type='chevron-down-icon'])[4]")
	downButton.click()
except:
	print('no down button')




def addToSheet(person):
    csv.register_dialect('myDialect', delimiter=',', quoting=csv.QUOTE_ALL)
    with open('src/job/job.csv', 'a', newline='') as file:
        writer = csv.writer(file, dialect='myDialect')
        writer.writerow(person)



browser.get("https://www.linkedin.com/jobs/search/?")
sleep(4)
browser.refresh
sleep(4)



sleep(2)
jobType = browser.find_element_by_xpath("(//button[normalize-space()='Job Type'])[1]").click()

sleep(5)
for i in jobTypeList:
    sleep(5)
    selJobType = browser.find_element_by_xpath(f"//label[contains(@for,'jobType-{i}')]")
    sleep(2)
    selJobType.click()

sleep(2)
filterJobType = browser.find_element_by_xpath("(//span[@class='artdeco-button__text'])[12]").click()
sleep(4)
browser.refresh
sleep(4)


company = browser.find_element_by_xpath("(//button[normalize-space()='Company'])[1]").click()
sleep(2)

for i in compList:
    
    sleep(7)
    searchComp = browser.find_element_by_xpath(f"//input[@placeholder='Add a company']")
    sleep(7)
    searchComp.send_keys(i)
    sleep(7)
    searchComp.send_keys(Keys.DOWN)
    sleep(7)
    searchComp.send_keys(Keys.ENTER)
    sleep(5)

sleep(7)
filterComp = browser.find_element_by_xpath("(//span[@class='artdeco-button__text'])[12]")
sleep(7)
filterComp.click()
sleep(4)






cnt=0



def funForClick():
		sleep(5)
		print(browser.current_url)
		link=browser.current_url
		profile=[link]
		addToSheet(profile)
		browser.back()
		return


while cnt < noOfComp:
    sleep(4)
    try:
        filterComp = browser.find_element_by_xpath(f"(//div[@class='job-card-list__entity-lockup artdeco-entity-lockup artdeco-entity-lockup--size-4 ember-view'])[{cnt+1}]")
    except:
        print("no more job")
        break

    filterComp.click()
    funForClick()
    cnt = cnt + 1



browser.close();




