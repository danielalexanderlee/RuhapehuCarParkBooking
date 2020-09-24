###################################################################
#
# Ruapehu Car Booking
#
# depedents:
#		-selenium       "https://pypi.org/project/selenium/"
#               -geckodriver    "https://github.com/mozilla/geckodriver/releases"
#		-chrome driver  "https://chromedriver.chromium.org/"
#
#
###################################################################
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
import threading
from time import sleep
from datetime import datetime, time

# If starting the script prior to the desired start time, the browsers for each booking
# will be initiated to the first booking page and wait until the start time to proceed
startTime = '08:30' 

# Tracking script run time
start_time = datetime.now()

BookingList = []

confirmed = False

class Booking:
    def __init__(self, desiredField, firstName, lastName, phoneNumber, email, regoPlate, partySize, daysList):
        self.desiredField = desiredField
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phoneNumber
        self.email = email
        self.regoPlate = regoPlate
        self.partySize = partySize
        self.daysList = daysList

BookingList.append(Booking(1,"Daniel","Lee","0223185027","d.lee@rocketlab.co.nz","KDK177","2",[False,False,False,True,True,False,False]))
BookingList.append(Booking(1,"Mike","Mason","0212351729","m.mason@rocketlab.co.nz","LCW804","4",[False,False,False,True,True,False,False]))
BookingList.append(Booking(1,"Adrien","Michaud","021396568","adrimichaud@gmail.com","MGL732","2",[False,False,False,True,False,False,False]))
BookingList.append(Booking(1,"Sean","Brennan","0274729712","sean.brennan.nz@gmail.com","MDL583","2",[False,False,False,True,True,False,False]))
BookingList.append(Booking(1,"Daniel","Sinclair","0272481021","danielsinclair2008@gmail.com","GHP113","5",[False,False,False,True,True,False,False]))
BookingList.append(Booking(1,"Dane","Lander","0224088016","d.lander@rocketlab.co.nz","KEP421","4",[False,False,False,True,True,False,False]))
BookingList.append(Booking(1,"Derek","McElwee","0226151256","fernskibikes@gmail.co.nz","RENTAL","6",[False,True,True,True,True,False,False]))
BookingList.append(Booking(1,"Keith","Brock","0212346372","k.brock@rocketlab.co.nz","JJD949","2",[False,False,False,True,False,False,False]))
BookingList.append(Booking(1,"Dorrin","Asefi","0211676746","dorrin_asefi@hotmail.com","KQT502","4",[False,False,True,True,True,False,False]))
BookingList.append(Booking(1,"Chris","Scott","0273372971","c.g.scott@outlook.com","BHM235","4",[False,False,False,True,True,False,False]))
BookingList.append(Booking(1,"Phillip","Drinkwater","0210342558","p.drinkwater@rocketlab.co.nz","KJY470","4",[False,False,False,True,True,False,False]))
BookingList.append(Booking(1,"Chad","Watson","02041641752","c.watson@rocketlab.co.nz","DLW413","1",[False,False,False,True,True,False,False]))
BookingList.append(Booking(1,"Ida","De Smet","0211079785","i.desmet@rocketlab.co.nz","RENTAL","4",[False,False,False,True,True,False,False]))

# don't change anything below
def waitThenClick(browser, elementXPath):
    delay = 0.5
    element = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, elementXPath)))
    ActionChains(browser).click(element).perform()

def waitThenClickisEnabled(browser, elementXPath):
    delay = 0.5
    element = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, elementXPath)))
    isEnabled = element.is_enabled()
    if isEnabled:
        ActionChains(browser).click(element).perform()
    return isEnabled         

def two(browser):
    # Check page URL else reload
    #if browser.current_url != Page2URL:
        #return 1
    
    # Select Field
    waitThenClick(browser, '//*[@id="root"]/div/div[2]/div[1]/div[3]/div[2]/button['+str(currentBooking.desiredField)+']')

        
    wait_start(startTime)
    
    # Clicks next
    waitThenClick(browser, '//*[@id="root"]/div/div[2]/div[1]/div[3]/div[2]/div/div[2]/button')


    return 3
    
def three(browser):
    # Check page URL else reset to page 1
    #if browser.current_url != Page3URL:
        #return 1
    
    # Wait for page to load (2 second delay)
    WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div[3]/div[2]/div[4]/div[1]/button')))

    freeDay = False
    for idx, day in enumerate(currentBooking.daysList):
        if day:
            if waitThenClickisEnabled(browser, '//*[@id="booking-slots-slider"]/div['+str(idx+1)+']/button'):
                freeDay = True
                print(currentBooking.firstName+" "+currentBooking.lastName+", Day "+str(idx+1)+" was added")
            else:
                print(currentBooking.firstName+" "+currentBooking.lastName+", Day "+str(idx+1)+" was not available")

    # If none of the desired days were available
    if not freeDay:
        print('no free day')
        # Clicks back to return to page 1
        waitThenClick(browser, '//*[@id="root"]/div/div[2]/div[1]/div[3]/div[2]/div[4]/div[1]/button')                                 
        return 1

    print('clicking next on page 2')            
    # Clicks next proceeding to page 3 //*[@id="root"]/div/div[2]/div[1]/div[3]/div[2]/div[4]/div[2]/button
    waitThenClick(browser, '//*[@id="root"]/div/div[2]/div[1]/div[3]/div[2]/div[4]/div[2]/button')
    return 4

def one(browser):
    # Check page URL else reset to page 1
    if browser.current_url != Page1URL:
        browser.get(Page1URL)
    
    # Wait for page to load
    WebDriverWait(browser, 1).until(EC.presence_of_element_located((By.XPATH, '//*[@id="FirstName"]')))
    Page3PerformList = [['//*[@id="FirstName"]', currentBooking.firstName],
                        ['//*[@id="LastName"]', currentBooking.lastName],
                        ['//*[@id="Phone"]', currentBooking.phoneNumber],
                        ['//*[@id="Email"]', currentBooking.email],
                        ['//*[@id="Rego"]', currentBooking.regoPlate],
                        ['//*[@id="PartySize"]', currentBooking.partySize]]

    for [element,value] in Page3PerformList:
        browser.find_element_by_xpath(element).clear()
        browser.find_element_by_xpath(element).send_keys(value)
    ActionChains(browser).click(browser.find_element_by_xpath('//*[@id="ButtonEnterDetails"]')).perform() # Clicks next
    
    return 2

def four(browser):
    if confirmed:
        # Wait for confirmation page to load
        waitThenClick(browser, 'Confirmation Button', '//*[@id="ButtonSubmitPreRegistrations"]') # Confirms
        print(currentBooking.firstName+" "+currentBooking.lastName+", Booking confirmed!")
    else:
        WebDriverWait(browser, 1000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ButtonSubmitPreRegistrations"]')))
        print(currentBooking.firstName+" "+currentBooking.lastName+", Please confirm")
    return 5



# Defining CONSTANTS
Page2URL = 'https://parking.evacheckin.com/car_park_booking/select_car_park?siteId=2'
Page3URL = 'https://parking.evacheckin.com/car_park_booking/select_dates?siteId=2'
Page1URL = 'https://parking.evacheckin.com/car_park_booking/enter_details?siteId=2'
        
def makeBooking(currentBooking):
    browser = webdriver.Chrome()
    browser.get(Page1URL)
    
    page = 1
    pages = {1: one,
             2: two,
             3: three,
             4: four}

    WebDriverWait(browser, 1000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="FirstName"]')))

    

    while page != 5:
        print(str(page))
        try:
            page = pages[page](browser)
        except:
            print('Failed on page '+str(page))
            # if error encountered, reset to page 1
            page = 1


def wait_start(runTime):
    startTime = time(*(map(int, runTime.split(':'))))
    while startTime > datetime.today().time(): # you can add here any additional variable to break loop if necessary
        sleep(1)# you can change 1 sec interval to any other


thread_list = list()

for i, currentBooking in enumerate(BookingList):
    t = threading.Thread(name='Test {}'.format(i), target=makeBooking, args=(currentBooking,))
    t.start()
    sleep(0.2)
    #print t.name + ' started!'
    thread_list.append(t)

# Wait for all threads to complete
for thread in thread_list:
    thread.join()

print("--- %s seconds ---" % (datetime.now() - start_time))
