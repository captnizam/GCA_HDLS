import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common import keys
import progressPrint as p
import userDetails as u


driver = webdriver.Chrome(executable_path='/Users/capt.nizam/Desktop/EGCA/chromedriver')



def openChrome():
    p.progressPrint("1.Opening Chrome")
    driver.maximize_window()
    driver.implicitly_wait(60)
    driver.get('https://www.dgca.gov.in/digigov-portal/jsp/dgca/common/login.jsp')
    p.progressPrint("2.Chrome & Egca Website opened Successfully")


def login_egca():
    user_input = driver.find_element_by_id('username')
    user_input.send_keys(u.username)
    p.progressPrint("3.Username Passed")
    password_input = driver.find_element_by_id('password')
    password_input.send_keys(u.password)
    print("4.Password Passed")
    captcha_input = driver.find_element_by_id('txt_Captcha')
    CAPTCHA = input("Enter captcha- ")
    captcha_input.send_keys(CAPTCHA)
    print("5.captcha passed")
    login_button = driver.find_element_by_css_selector('#login-tab > button')
    print("logging wait ...")
    login_button.click()


def home_button():
    time.sleep(10) # remove later
    press_home = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/div/div/nav/div/div/ul/li[1]/a')
    driver.implicitly_wait(10)
    press_home.click()
    p.progressPrint("Home Pressed")
    time.sleep(10) #Change to 5 sec later
    driver.implicitly_wait(10)
    dropdown = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/aside/section/div/div/div[2]/div[1]/a')
    dropdown.click()
    fill_elogbook = driver.find_element_by_css_selector('#\\39 0000524 > a')
    driver.implicitly_wait(10)
    fill_elogbook.click()
    p.progressPrint("Fill Elogbook Pressed")
    time.sleep(10) #change to 5 sec later
    driver.implicitly_wait(10)
    sched_logbook = driver.find_element_by_css_selector('#elbScheduledNonScheduled')
    driver.implicitly_wait(10)
    sched_logbook.click()
    driver.implicitly_wait(10)
    current_entry = driver.find_element_by_css_selector('#elbCurrentEntry')
    driver.implicitly_wait(10)
    current_entry.click()
    driver.implicitly_wait(10)
    next_btn = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div/div/div/section[2]/div[1]/form/section/div/div/div[2]/div/div[1]/div[2]/button")
    driver.implicitly_wait(10)
    next_btn.click()
    p.progressPrint("7.Logbook entry page opened")


def fillLogbook_button():
    try:
        time.sleep(10) # remove later
        dropdown = driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div/div/aside/section/div/div/div[2]/div[1]/a')
        dropdown.click()
        driver.implicitly_wait(10)
        fill_elogbook = driver.find_element_by_css_selector('#\\39 0000524 > a')
        driver.implicitly_wait(10)
        fill_elogbook.click()
        p.progressPrint("Fill Elogbook Pressed")
        time.sleep(10) #change to 5 second later
        driver.implicitly_wait(10)
        sched_logbook = driver.find_element_by_css_selector('#elbScheduledNonScheduled')
        driver.implicitly_wait(10)
        sched_logbook.click()
        driver.implicitly_wait(10)
        current_entry = driver.find_element_by_css_selector('#elbCurrentEntry')
        driver.implicitly_wait(10)
        current_entry.click()
        driver.implicitly_wait(10)
        next_btn = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div/div/div/section[2]/div[1]/form/section/div/div/div[2]/div/div[1]/div[2]/button")
        driver.implicitly_wait(10)
        next_btn.click()
        p.progressPrint("7.Logbook entry page opened")
    except:
        home_button()


def airline_selection():
    fto_selection = driver.find_element_by_xpath('//*[@id="ftoId"]')
    driver.implicitly_wait(10)
    fto_selection.click()

    fto_selection.send_keys(u.airline)
    time.sleep(1)

    fto_selection.send_keys(keys.Keys.ENTER)
    p.progressPrint("1.Airline Selected")


def aircraft_reg(vt):
    aircraft_registration1 = driver.find_element_by_xpath('//*[@id="pilotInCmdStyle"]/div/b')
    aircraft_registration1.click()
    aircraft_registration2 = driver.find_element_by_class_name('chosen-search-input')
    aircraft_registration2.send_keys(vt)
    time.sleep(1)
    aircraft_registration2.send_keys(keys.Keys.ENTER)
    p.progressPrint("2.Aircraft Registration selected")


def copilot(fo_name):
    if u.pilot_type == "p1":
        p1 = driver.find_element_by_id('pilotFuncPic')
        p1.click()
    elif u.pilot_type == "p2":
        p2 = driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div/div/div/div/section[2]/div[1]/form/section/div/div/div[2]/div/div[2]/div[3]/div[2]/div/div[2]/div[1]/div/input[2]')
        p2.click()
    print(u.pilot_type + "- Pilot Function Selected")
    fo_dropdown1 = driver.find_element_by_id('pilotInCommandIdCurrentEntry_chosen')
    fo_dropdown1.click()
    fo_dropdown2 = driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div/div/div/div/div/section[2]/div[1]/form/section/div/div/div[2]/div/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[1]/div[3]/div/div/input')
    fo_dropdown2.send_keys(fo_name)
    time.sleep(1)
    fo_selection = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div/div/div/section[2]/div[1]/form/section/div/div/div[2]/div/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[1]/div[3]/div/ul/li[2]")
    fo_selection.click()
    driver.implicitly_wait(10)
    p.progressPrint("Co-Pilot/Pic Name Selected")


def type_of_flight(shift):
    type_of_flight = driver.find_element_by_id('flyCommercialId')
    type_of_flight.click()
    p.progressPrint("Type of Flight Selected")
    excercise = Select(driver.find_element_by_id('exerciseTypeId'))
    excercise.select_by_visible_text('General/Line Flying')
    if shift == 'DAY':
        excercise.select_by_visible_text("Cross-country flight (day)")
    elif shift == 'NIGHT':
        excercise.select_by_visible_text("Cross-country flight (night)")
    elif shift == "BOTH":
        excercise.select_by_visible_text("Cross-country flight (day)")
        excercise.select_by_visible_text("Cross-country flight (night)")
    p.progressPrint("Excerice type selected")


def from_details(dep, dep_date, dep_time):
    depature1 = driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div/div/div/div/div/section[2]/div[1]/form/section/div/div/div[2]/div/div[2]/div[3]/div[4]/div/div[2]/div[1]/div/div[2]/div[1]/div[1]/div/a/div')
    depature1.click()
    depature2 = driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div/div/div/div/div/section[2]/div[1]/form/section/div/div/div[2]/div/div[2]/div[3]/div[4]/div/div[2]/div[1]/div/div[2]/div[1]/div[1]/div/div/div/input')

    #depature2.send_keys('others')
    #time.sleep(2)
    #depature2.send_keys(keys.Keys.ENTER)
    #otherAirport = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/div/div/section[2]/div[1]/form/section/div/div/div[2]/div/div[2]/div[3]/div[4]/div/div[2]/div[1]/div/div[2]/div[1]/div[2]/input')
    #otherAirport.send_keys(dep)
    #time.sleep(2)

    depature2.send_keys(dep)
    time.sleep(2)
    depature2.send_keys(keys.Keys.ENTER)

    p.progressPrint('Depature aerodrome selected')

    # INPUT 5 DEPATURE DATE
    depature_date = driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div/div/div/div/div/section[2]/div[1]/form/section/div/div/div[2]/div/div[2]/div[3]/div[4]/div/div[2]/div[1]/div/div[2]/div[2]/div[1]/div/input')
    depature_date.click()
    depature_date.send_keys(dep_date)
    time.sleep(2)
    depature_date.send_keys(keys.Keys.ENTER)

    print("Depature date entered")

    # INPUT 6 CHOCKS OFF
    depature_time = driver.find_element_by_id('departuretime')
    depature_time.send_keys(dep_time)

    print("Depature time entered")


def arrival_entry(arr, arr_date, arr_time, dist):
    arrival1 = driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div/div/div/div/div/section[2]/div[1]/form/section/div/div/div[2]/div/div[2]/div[3]/div[4]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/a/span')
    arrival1.click()
    arrival2 = driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div/div/div/div/div/section[2]/div[1]/form/section/div/div/div[2]/div/div[2]/div[3]/div[4]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/input')

    #arrival2.send_keys('others')
    #arrival2.send_keys(keys.Keys.ENTER)
    #otherAirport = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/div/div/section[2]/div[1]/form/section/div/div/div[2]/div/div[2]/div[3]/div[4]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/input')
    #otherAirport.send_keys(arr)

    arrival2.send_keys(arr)
    arrival2.send_keys(keys.Keys.ENTER)
    print('Arrival aerodrome  selected')

    arrival_date = driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div/div/div/div/div/section[2]/div[1]/form/section/div/div/div[2]/div/div[2]/div[3]/div[4]/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/input')
    arrival_date.click()
    arrival_date.send_keys(arr_date)
    arrival_date.send_keys(keys.Keys.ENTER)

    arrival_time = driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div/div/div/div/div/section[2]/div[1]/form/section/div/div/div[2]/div/div[2]/div[3]/div[4]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/input')
    arrival_time.send_keys(arr_time)  # No 8
    print("Arrival time entered")

    if u.airline == "SPICE JET":
        distance = driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div/div/div/div/div/section[2]/div[1]/form/section/div/div/div[2]/div/div[2]/div[3]/div[4]/div/div[2]/div[2]/div/div[2]/div[3]/div[1]/input")
        distance.click()
        time.sleep(1)
        distance.send_keys(int(dist))
        p.progressPrint("Distance entered")


def instrument_time(ir_time1):
    for_instrument = driver.find_element_by_id('farInstrumentActual')
    for_instrument.click()
    ir_time = driver.find_element_by_id('farInstrumentActualTime')
    ir_time.send_keys(ir_time1)  # No 9
    print("Instrument time entered")


def day_or_night(shift, d_time, n_time):
    if shift == "DAY":
        daytime = driver.find_element_by_id('flyTimeIdDay')
        daytime.click()

    elif shift == "NIGHT":
        night_time = driver.find_element_by_id('flyTimeIdNight')
        night_time.click()

    elif shift == "BOTH":
        both_time = driver.find_element_by_id('flyTimeIdBoth')
        both_time.click()

        day_time = driver.find_element_by_id('flightTimeDay')
        driver.implicitly_wait(10)
        day_time.send_keys("0" + d_time)
        night_time = driver.find_element_by_id('flightTimeNight')
        driver.implicitly_wait(10)
        night_time.send_keys(n_time)

    p.progressPrint("Shift Selected (Day/Night")


def final_submission():
    add_entry = driver.find_element_by_id('btnAddAppTrnElbLndgTkOffDtl')
    add_entry.click()
    print("Add button pressed")

    elogverifier = driver.find_element_by_xpath('//*[@id="verifiedById"]')
    driver.implicitly_wait(10)
    elogverifier.click()
    elogverifier = Select(driver.find_element_by_xpath('//*[@id="verifiedById"]'))
    elogverifier.select_by_visible_text('eLog Book Verifier')
    print("elogbook verifier seleceted")
    verifiername = driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div/div/div/div/div/section[2]/div[1]/form/section/div/div/div[2]/div/div[2]/div[3]/div[5]/div/div[2]/div/div[2]/select')
    driver.implicitly_wait(10)
    verifiername.click()
    verifiername.send_keys(u.egcaVerifier)
    verifiername.send_keys(keys.Keys.ENTER)
    print(u.egcaVerifier, "Selected")
    toc = driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div/div/div/div/div/section[2]/div[1]/form/section/div/div/div[2]/div/div[2]/div[3]/div[6]/div/div[2]/div[1]/div/input')
    toc.click()
    submit_button = driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div/div/div/div/div/section[2]/div[1]/form/section/div/div/div[2]/div/div[2]/div[3]/div[6]/div/div[2]/div[3]/div/input[1]')
    time.sleep(1)
    submit_button.click()
    print("submit button pressed")

    driver.implicitly_wait(10)
    alert = Alert(driver)
    driver.implicitly_wait(10)
    time.sleep(1)
    print(alert.text)
    alert.accept()
    print("Alert Accepted")
    driver.implicitly_wait(10)
    press_ok = driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div/div/div/div/div/section[2]/div[1]/center/div/div/input')
    driver.implicitly_wait(10)
    press_ok.click()
    time.sleep(5)

def takeScreenShot(row):
        driver.get_screenshot_as_file(row)
        time.sleep(1)

