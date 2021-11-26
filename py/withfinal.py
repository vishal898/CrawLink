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
with open('src/withdraw/withdraw.csv', 'w+', newline='') as file:
    writer = csv.writer(file, dialect='myDialect')
    writer.writerow(['link'])

#username = input("Enter Email of Linkedin : ")
#password = input("Enter Password of Linkedin : ")

#username="sweetyjiji11@gmail.com"
#password="Kshitij5"

#username="kshitijsabale14@gmail.com"
#password="Mumbai#123"
username = sys.argv[1]
password = sys.argv[2]
noOfPeople=int(float(sys.argv[3]))

def addToSheet(person):
    csv.register_dialect('myDialect', delimiter=',', quoting=csv.QUOTE_ALL)
    with open('src/withdraw/withdraw.csv', 'a', newline='') as file:
        writer = csv.writer(file,  dialect='myDialect')
        writer.writerow(person)

#noOfPeople=int(input("Enter no.of people to withdraw between 1 to 25: "))

if noOfPeople<=25 and noOfPeople>0:
    # browser= webdriver.Edge(executable_path=r'C:/Users/Kshitij/Downloads/edgedriver_win64/msedgedriver.exe')
    browser =""
    try:
        browser = webdriver.Chrome(ChromeDriverManager().install())
        
    except:
        try: 
            browser = webdriver.Edge(EdgeChromiumDriverManager().install())
            
        except:
            browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            
    browser.get('https://www.linkedin.com/login')

    sleep(2)
    browser.maximize_window()
    sleep(25)
    userid = browser.find_element_by_xpath("(//input[@name='session_key'])[1]")
    userid.send_keys(username)
    sleep(2)
    userpass = browser.find_element_by_xpath("(//input[@name='session_password'])[1]")
    userpass.send_keys(password)
    sleep(2)
    signIn = browser.find_element_by_xpath("(//button[normalize-space()='Sign in'])[1]")
    signIn.click()
    print('wait')

    # print(start)

    sleep(3)
    while browser.current_url !="https://www.linkedin.com/feed":
        print('wait')
    sleep(3)
        


   
    
    
    
    browser.get("https://www.linkedin.com/mynetwork/invitation-manager/sent/")
    sleep(4)
    browser.refresh
    sleep(4)
    
    
    
    
    
    #finding no. of people
    
    p=browser.find_element_by_xpath("(//button[@id='mn-invitation-manager__invitation-facet-pills--CONNECTION'])[1]").text
    k=int(p.index(')'))
    s=int(p[8:k])
    print(s)
    pageNo=int((s/100))+2
    print(pageNo)
    
    #navigating to last page by clicking next button
    try:
        for i in range(s):
            print("\n")
            print(i)
            next=browser.find_element_by_xpath("(//span[normalize-space()='Next'])[1]").click()
    
    except:
        print('except')
          
    finally:
        
        sleep(2)
        time=[]
        time=browser.find_elements_by_xpath("(//time[@class='time-badge t-12 t-black--light t-normal'])")
        """  
        #len=int(len(time3))
        timestr=[]
            
        for i in time:
            print("\n")
            print(i.text)     
            timestr.append(i.text)
        """    
        withdraw=[]    
        withdraw=browser.find_elements_by_xpath("(//span[@class='artdeco-button__text'][normalize-space()='Withdraw'])")    
        print("\n\n selecting withdraw button")
        
        sleep(2)
         
        list=['mon','yea'] 
        cnt=0; 
        link=browser.find_elements_by_xpath("(//a[@class='ember-view invitation-card__picture'])")
        sleep(2)
        linkList=[];
        
        
        for a in range(noOfPeople+1):
            try:
                    for i in time:
                        for j in list:
                            if j in i.text:
                                print(i)
                                print(i.text)
                                linkList.append(link[a].get_attribute("href"))
                                withdraw[a].click()
                                sleep(4)
                                browser.find_element_by_xpath("(//span[@class='artdeco-button__text'][normalize-space()='Withdraw'])[1]").click()
                                sleep(3)
            except:
                        print("{} invitations succcesfully withdrawn".format(noOfPeople))    
                        print('except')  
        for k in range(1,noOfPeople+1):
                print(linkList[k]);
                profile = [linkList[k]]
                # print(profile)
                addToSheet(profile)
                print("\n")                  
else:
    print("no of people is not between 1 & 25")

browser.close()
    