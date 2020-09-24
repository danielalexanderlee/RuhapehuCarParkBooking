###################################################################
#
# Ruapehu Car Booking
#
# deps:
#		-selenium       "https://pypi.org/project/selenium/"
#       -geckodriver    "https://github.com/mozilla/geckodriver/releases"
#		-firefox
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

class Booking:
    def __init__(self, desiredField, firstName, lastName, phoneNumber, email, regoPlate, partySize, daysList, confirmed):
        self.desiredField = desiredField
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phoneNumber
        self.email = email
        self.regoPlate = regoPlate
        self.partySize = partySize
        self.daysList = daysList
        self.confirmed = confirmed

startTime = '18:00'

BookingList = []

desiredField = 1 # 1: Turoa, 2: Whakapapa
firstName = "Daniel"
lastName = "Lee"
phoneNumber = "0223185027"
email = "d.lee@rocketlab.co.nz"
regoPlate = "KDK177"
partySize = "2"
#           [Wed    Thu     Fri     Sat     Sun     Mon     Tue]
daysList =  [False,  False,  False,  True,  True,  False,  False]
confirmed = True

BookingList.append( Booking(desiredField, firstName, lastName, phoneNumber, email, regoPlate, partySize, daysList, confirmed) )

desiredField = 1 # 1: Turoa, 2: Whakapapa
firstName = "Mike"
lastName = "Mason"
phoneNumber = "0212351729"
email = "m.mason@rocketlab.co.nz"
regoPlate = "KBM366"
partySize = "3"
#           [Wed    Thu     Fri      Sat    Sun    Mon     Tue]
daysList =  [False,  False,  False,  True,  True,  False,  False]

BookingList.append( Booking(desiredField, firstName, lastName, phoneNumber, email, regoPlate, partySize, daysList, confirmed) )

desiredField = 1 # 1: Turoa, 2: Whakapapa 
firstName = "Adrien"
lastName = "Michaud"
phoneNumber = "021396568"
email = "a.michaud@rocketlab.co.nz"
regoPlate = "MGL732"
partySize = "2"
#           [Wed    Thu     Fri     Sat     Sun     Mon     Tue]
daysList =  [False,  False,  False,  True, True,  False,  False]

BookingList.append( Booking(desiredField, firstName, lastName, phoneNumber, email, regoPlate, partySize, daysList, confirmed) )

desiredField = 1 # 1: Turoa, 2: Whakapapa
firstName = "Sean"
lastName = "Brennan"
phoneNumber = "0274729712"
email = "sean.brennan.nz@gmail.com"
regoPlate = "MDL583"
partySize = "2"
#           [Wed    Thu     Fri     Sat     Sun     Mon     Tue]
daysList =  [False,  False,  False,  True,  True,  False,  False]

BookingList.append( Booking(desiredField, firstName, lastName, phoneNumber, email, regoPlate, partySize, daysList, confirmed) )

desiredField = 1 # 1: Turoa, 2: Whakapapa 
firstName = "Daniel"
lastName = "Sinclair"
phoneNumber = "0272481021"
email = "danielsinclair2008@gmail.com"
regoPlate = "GHP113"
partySize = "5"
#           [Wed    Thu     Fri     Sat     Sun     Mon     Tue]
daysList =  [False,  False,  False,  False,  False,  False,  False]

BookingList.append( Booking(desiredField, firstName, lastName, phoneNumber, email, regoPlate, partySize, daysList, confirmed) )

desiredField = 2 # 1: Turoa, 2: Whakapapa
firstName = "Dane"
lastName = "Lander"
phoneNumber = "0224088016"
email = "d.lander@rocketlab.co.nz"
regoPlate = "KEP421"
partySize = "2"
#           [Wed    Thu     Fri     Sat     Sun     Mon     Tue]
daysList =  [False,  False,  False,  True,  True,  False,  False]

BookingList.append( Booking(desiredField, firstName, lastName, phoneNumber, email, regoPlate, partySize, daysList, confirmed) )

desiredField = 1 # 1: Turoa
firstName = "Derek"
lastName = "McElwee"
phoneNumber = "0226151256"
email = "d.mcelwee@rocketlab.co.nz"
regoPlate = "AZK781"
partySize = "4"
#           [Wed    Thu     Fri     Sat     Sun     Mon     Tue]
daysList =  [False,  True,  True,  False,  False,  False,  False]

BookingList.append( Booking(desiredField, firstName, lastName, phoneNumber, email, regoPlate, partySize, daysList, confirmed) )

# don't change anything below
def makeBooking(currentBooking):
    browser = webdriver.Firefox()
    browser.get('https://parking.evacheckin.com/car_park_booking/select_dates?siteId=2');

    wait_start(startTime)

    browser.get('https://parking.evacheckin.com/car_park_booking/select_dates?siteId=2');
                
    # Select Field
    delay = 10
    element = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div[3]/div[2]/button['+str(currentBooking.desiredField)+']')))
    ActionChains(browser).click(element).perform()
    
    # Clicks next
    ActionChains(browser).click(browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[3]/div[2]/button[3]')).perform()

    # Wait for 1 seconds
    sleep(1)

    for idx, day in enumerate(currentBooking.daysList):
        element = browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[3]/div[2]/div[2]/div/div['+str(idx+1)+']/button')
        if (day & element.is_enabled()):
            ActionChains(browser).click(element).perform()
        elif day:
            print(currentBooking.firstName+" "+currentBooking.lastName+", Day "+str(idx+1)+" Already Booked")
                

    # Clicks next
    element = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div[3]/div[2]/div[4]/div[2]/button')))
    if (element.is_enabled()):
        ActionChains(browser).click(element).perform()
    else:
        print(currentBooking.firstName+" "+currentBooking.lastName+", No days were available")
        return

    # Wait for 1 seconds
    sleep(1)

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

    # Wait for 1 seconds
    sleep(1)

    # Uncomment if you don't want to sanity check the booking
    if currentBooking.confirmed:
        print(currentBooking.firstName+" "+currentBooking.lastName+", Booking confirmed!")
        ActionChains(browser).click(browser.find_element_by_xpath('//*[@id="ButtonSubmitPreRegistrations"]')).perform() # Confirms
    else:
        print(currentBooking.firstName+" "+currentBooking.lastName+", Please confirm")


def wait_start(runTime):
    startTime = time(*(map(int, runTime.split(':'))))
    while startTime > datetime.today().time(): # you can add here any additional variable to break loop if necessary
        sleep(1)# you can change 1 sec interval to any other


thread_list = list()

for i, currentBooking in enumerate(BookingList):
    t = threading.Thread(name='Test {}'.format(i), target=makeBooking, args=(currentBooking,))
    t.start()
    sleep(0.1)
    #print t.name + ' started!'
    thread_list.append(t)

# Wait for all thre<ads to complete
for thread in thread_list:
    thread.join()
