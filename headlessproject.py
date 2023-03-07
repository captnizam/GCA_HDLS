from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
import userDetails as u
import pandas as pd
import time
from selenium.webdriver.common.alert import Alert
import progressPrint as p
from selenium.webdriver.support.ui import Select

options = Options()
options.add_argument("--headless")
options.add_argument('--no-sandbox')
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-extensions")
options.add_argument("--start-maximized")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--disable-dev-shm-usage")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.binary_location = "/Applications/Chromium.app/Contents/MacOS/Chromium"

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
options.add_argument(f'user-agent={user_agent}')
options.headless = True

driver = webdriver.Chrome(executable_path='/Users/capt.nizam/Desktop/EGCA/chromedriver', options=options)
driver.get("https://www.dgca.gov.in/digigov-portal/jsp/dgca/common/login.jsp")
driver.set_window_size(1000, 600)
print(driver.title)

capcha = driver.find_element_by_xpath('/html/body/form[2]/div/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/img[1]')
screenshot_as_bytes = capcha.screenshot_as_png
with open('capcha.png', 'wb') as f:
    f.write(screenshot_as_bytes)
user_capcha = input()
driver.find_element_by_id('username').send_keys(u.username)
driver.find_element_by_id('password').send_keys(u.password)
driver.find_element_by_id('txt_Captcha').send_keys(user_capcha)
login_button = driver.find_element_by_css_selector('#login-tab > button')
login_button.click()


def home_button():
    time.sleep(10)  # remove later
    press_home = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/div/div/nav/div/div/ul/li[1]/a')
    driver.implicitly_wait(10)
    press_home.click()
    p.progressPrint("Home Pressed")
    time.sleep(10)  # Change to 5 sec later
    driver.implicitly_wait(10)
    dropdown = driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div/div/div/aside/section/div/div/div[2]/div[1]/a')
    dropdown.click()
    fill_elogbook = driver.find_element_by_css_selector('#\\39 0000524 > a')
    driver.implicitly_wait(10)
    fill_elogbook.click()
    p.progressPrint("Fill Elogbook Pressed")
    time.sleep(10)  # change to 5 sec later
    driver.implicitly_wait(10)
    sched_logbook = driver.find_element_by_css_selector('#elbScheduledNonScheduled')
    driver.implicitly_wait(10)
    sched_logbook.click()
    driver.implicitly_wait(10)
    current_entry = driver.find_element_by_css_selector('#elbCurrentEntry')
    driver.implicitly_wait(10)
    current_entry.click()
    driver.implicitly_wait(10)
    next_btn = driver.find_element_by_xpath(
        "/html/body/div[1]/div[1]/div/div/div/div/div/section[2]/div[1]/form/section/div/div/div[2]/div/div[1]/div[2]/button")
    driver.implicitly_wait(10)
    next_btn.click()
    p.progressPrint("7.Logbook entry page opened")


def fillLogbook_button():
    try:
        time.sleep(10)  # remove later
        dropdown = driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div/div/aside/section/div/div/div[2]/div[1]/a')
        dropdown.click()
        driver.implicitly_wait(10)
        fill_elogbook = driver.find_element_by_css_selector('#\\39 0000524 > a')
        driver.implicitly_wait(10)
        fill_elogbook.click()
        p.progressPrint("Fill Elogbook Pressed")
        time.sleep(10)  # change to 5 second later
        driver.implicitly_wait(10)
        sched_logbook = driver.find_element_by_css_selector('#elbScheduledNonScheduled')
        driver.implicitly_wait(10)
        sched_logbook.click()
        driver.implicitly_wait(10)
        current_entry = driver.find_element_by_css_selector('#elbCurrentEntry')
        driver.implicitly_wait(10)
        current_entry.click()
        driver.implicitly_wait(10)
        next_btn = driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div/div/div/div/div/section[2]/div[1]/form/section/div/div/div[2]/div/div[1]/div[2]/button")
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


def copilot(fo_name, training):
    if u.pilot_type == "p1" and training != "RC":
        if training !="SLF" or "LTC":
            p1 = driver.find_element_by_id('pilotFuncPic')
            p1.click()
            print("p1111111111")
    elif u.pilot_type == "p2" and training != "RC":
        p2 = driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div/div/div/div/section[2]/div[1]/form/section/div/div/div[2]/div/div[2]/div[3]/div[2]/div/div[2]/div[1]/div/input[2]')
        p2.click()
    if training == "LTC":
        instructor = driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div/div/div/div/section[2]/div[1]/form/section/div/div/div[2]/div/div[2]/div[3]/div[2]/div/div[2]/div[1]/div/input[3]')
        instructor.click()
    if training == "RC" or "SLF" or "STOL":
        rcclick = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/div/div/section[2]/div[1]/form/section/div/div/div[2]/div/div[2]/div[3]/div[2]/div/div[2]/div[1]/div/input[5]')
        rcclick.click()
        print("P1 US Selected")

    print(u.pilot_type + "- Pilot Function Selected")
    fo_dropdown1 = driver.find_element_by_id('pilotInCommandIdCurrentEntry_chosen')
    fo_dropdown1.click()
    fo_dropdown2 = driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div/div/div/div/div/section[2]/div[1]/form/section/div/div/div[2]/div/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[1]/div[3]/div/div/input')
    fo_dropdown2.send_keys(fo_name)
    time.sleep(1)
    fo_selection = driver.find_element_by_xpath(
        "/html/body/div[1]/div[1]/div/div/div/div/div/section[2]/div[1]/form/section/div/div/div[2]/div/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[1]/div[3]/div/ul/li[2]")
    fo_selection.click()
    driver.implicitly_wait(10)
    p.progressPrint("Co-Pilot/Pic Name Selected")


def type_of_flight(shift, training):
    type_of_flight = driver.find_element_by_id('flyCommercialId')
    type_of_flight.click()
    p.progressPrint("Type of Flight Selected")
    excercise = Select(driver.find_element_by_id('exerciseTypeId'))
    if training == "SLF":
        excercise.select_by_visible_text('Supervised line flying')
    elif training == "RC":
        excercise.select_by_visible_text('Route check')
    elif training == "STOL":
        excercise.select_by_visible_text('Supervised take-off and landing')

    else:
        excercise.select_by_visible_text('General/Line Flying')


    if u.airline == "SPICE JET":
        if shift == 'DAY':
            excercise.select_by_visible_text("Cross-country flight (day)")
        elif shift == 'NIGHT':
            excercise.select_by_visible_text("Cross-country flight (night)")
        elif shift == "BOTH":
            excercise.select_by_visible_text("Cross-country flight (day)")
            excercise.select_by_visible_text("Cross-country flight (night)")
    p.progressPrint("Excerice type selected")


def from_details(dep, dep_date, dep_time, intr):
    depature1 = driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div/div/div/div/div/section[2]/div[1]/form/section/div/div/div[2]/div/div[2]/div[3]/div[4]/div/div[2]/div[1]/div/div[2]/div[1]/div[1]/div/a/div')
    depature1.click()
    depature2 = driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div/div/div/div/div/section[2]/div[1]/form/section/div/div/div[2]/div/div[2]/div[3]/div[4]/div/div[2]/div[1]/div/div[2]/div[1]/div[1]/div/div/div/input')
    if intr == "ID":
        depature2.send_keys('others')
        time.sleep(2)
        depature2.send_keys(keys.Keys.ENTER)
        otherAirport = driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div/div/div/div/section[2]/div[1]/form/section/div/div/div[2]/div/div[2]/div[3]/div[4]/div/div[2]/div[1]/div/div[2]/div[1]/div[2]/input')
        otherAirport.send_keys(dep)
        time.sleep(2)
    elif intr == "DA":
        depature2.send_keys('others')
        time.sleep(2)
        depature2.send_keys(keys.Keys.ENTER)
        otherAirport = driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div/div/div/div/section[2]/div[1]/form/section/div/div/div[2]/div/div[2]/div[3]/div[4]/div/div[2]/div[1]/div/div[2]/div[1]/div[2]/input')
        otherAirport.send_keys(dep)
        time.sleep(2)
    else:
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


def arrival_entry(arr, arr_date, arr_time, dist, intr):
    arrival1 = driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div/div/div/div/div/section[2]/div[1]/form/section/div/div/div[2]/div/div[2]/div[3]/div[4]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/a/span')
    arrival1.click()
    arrival2 = driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div/div/div/div/div/section[2]/div[1]/form/section/div/div/div[2]/div/div[2]/div[3]/div[4]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/input')

    if intr == "IA":
        arrival2.send_keys('others')
        arrival2.send_keys(keys.Keys.ENTER)
        otherAirport = driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div/div/div/div/section[2]/div[1]/form/section/div/div/div[2]/div/div[2]/div[3]/div[4]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/input')
        otherAirport.send_keys(arr)
    elif intr == "DA":
        arrival2.send_keys('others')
        arrival2.send_keys(keys.Keys.ENTER)
        otherAirport = driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div/div/div/div/section[2]/div[1]/form/section/div/div/div[2]/div/div[2]/div[3]/div[4]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/input')
        otherAirport.send_keys(arr)
    else:
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


df = pd.read_csv('GULZAR 2023 - Sheet3.csv')

entrty_count = 1
driver.get_screenshot_as_file("screenshot.png")
for row in df.values.tolist():
    try:
        entrty_count += 1
        try:
            fillLogbook_button()
        except:
            home_button()

        airline_selection()
        vt = row[7]

        aircraft_reg(vt)

        fo_name = row[8]
        training = row[16]
        copilot(fo_name, training)

        dep = row[2]
        dep_date = row[1]
        dep_time = row[3]
        intr = row[15]

        shift = row[10]
        type_of_flight(shift,training)
        from_details(dep, dep_date, dep_time, intr)

        arr = row[5]
        arr_date = row[4]
        arr_time = row[6]
        dist = row[13]
        arrival_entry(arr, arr_date, arr_time, dist, intr)

        ir_time1 = row[9]
        instrument_time(ir_time1)

        d_time = row[11]
        n_time = row[12]

        day_or_night(shift, d_time, n_time)

        final_submission()

        print(entrty_count, " ENTRY SUBMITTEDddddddddddddddddddddddddddddddddddddddd                     SUBMITTED")
        print(dep_date, dep, fo_name, "Submitted")

    except:
        driver.get_screenshot_as_file("Fail screenshot.png")
        print(entrty_count,
              " Entry Failedddddddddddddddddddddddddddddddddddddddddddd                         FAILED     ", )
        pass
