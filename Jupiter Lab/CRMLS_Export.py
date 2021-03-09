from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from math import ceil
from selenium.common.exceptions import NoSuchElementException
import os
from datetime import date

PATH = 'C:\Program Files (x86)\chromedriver.exe'
USER = 'ocnguthan'
PWD = 'thuunguy1129'


try:
    # Chrome as access to web with devtools open
    driver_options = Options()
    driver_options.add_argument("--window-size=1600,1000")
    driver_options.add_argument('auto-open-devtools-for-tabs')
    driver_options.add_argument("--incognito")
    driver = webdriver.Chrome(PATH, options=driver_options)
    # Open the website
    driver.get('https://go.crmls.org/')
    time.sleep(0.5)
    # Navigate to login screen
    mls_dashboard_login = driver.find_element_by_link_text('MLS Dashboard Login').click()
    driver.close()
    time.sleep(0.5)
    driver.switch_to.window(driver.window_handles[0])
    # Login to CRMLS
    ## Enter USER
    mls_userid = driver.find_element_by_id("clareity")
    mls_userid.send_keys(USER)
    time.sleep(1)
    ## Enter PWD
    mls_pwd = driver.find_element_by_id("security")
    mls_pwd.clear()
    mls_pwd.send_keys('a')
    for letter in PWD:
        mls_pwd.send_keys(letter)
    mls_pwd.send_keys(Keys.RETURN)
    # Navigate to CRMLS Matrix
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,'logoimage')))
    driver.get('https://matrix.crmls.org/Matrix/Search/Residential/Detail')
    # Confirm Multiple Login Screen
    if driver.find_element_by_id('btnContinue'):
        driver.find_element_by_id('btnContinue').click()
    # Define search criteria
    ## Search for active and closed listing
    status_active = driver.find_elements_by_name('Fm2_Ctrl3_LB')[1].click()
    status_closed = driver.find_elements_by_name('Fm2_Ctrl3_LB')[4].click()
    ## For closed listing, search for the past year (365 days)
    status_closed_textbox = driver.find_element_by_id('FmFm2_Ctrl3_6145_Ctrl3_TB')
    status_closed_textbox.clear()
    days_range = '731-1095'
    status_closed_textbox.send_keys(days_range)
    ## Search for single family residence only
    sfr_only = driver.find_element_by_xpath("//*[@title='Single Family Residence']").click()
    ## Search for county
    county = driver.find_element_by_xpath("//*[@title='Orange']").click()
    ## Create a list of cities to interate through
    city_list = Select(driver.find_element_by_id('Fm2_Ctrl10_LB'))
    cities = []
    for city in city_list.options:
        name = city.get_attribute('title')
        cities.append(name)
    # Reset search criteria
    driver.get('https://matrix.crmls.org/Matrix/Search/Residential/Detail')
    #Loop through list of cities
    for city in cities:
        ## Search for active and closed listing
        time.sleep(.5)
        status_active = driver.find_elements_by_name('Fm2_Ctrl3_LB')[1].click()
        time.sleep(.5)
        status_closed = driver.find_elements_by_name('Fm2_Ctrl3_LB')[4].click()
        ## For closed listing, search for the past year (365 days)
        status_closed_textbox = driver.find_element_by_id('FmFm2_Ctrl3_6145_Ctrl3_TB')
        time.sleep(.5)
        status_closed_textbox.clear()
        time.sleep(.5)
        status_closed_textbox.send_keys(days_range)
        ## Search for single family residence only
        time.sleep(.5)
        sfr_only = driver.find_element_by_xpath("//*[@title='Single Family Residence']").click()
        ## Search for county
        time.sleep(.5)
        county = driver.find_element_by_xpath("//*[@title='Orange']").click()
        ## Search for city
        time.sleep(.5)
        city_list = Select(driver.find_element_by_id('Fm2_Ctrl10_LB'))
        time.sleep(.5)
        city_list.select_by_visible_text(city)
        # Perform search
        driver.find_element_by_id('m_ucSearchButtons_m_lbSearch').click()
        # Change result page layout to 100
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,'m_ucDisplayPicker_m_ddlPageSize')))
        driver.find_element_by_id('m_ucDisplayPicker_m_ddlPageSize').click()
        num_per_page = Select(driver.find_element_by_id('m_ucDisplayPicker_m_ddlPageSize'))
        num_per_page.select_by_value('100')
        # Determine the total num of results and page
        time.sleep(1)
        results = driver.find_elements_by_tag_name('b')
        result_list = []
        for x in results:
            current = x.get_attribute('innerHTML')
            result_list.append(current)
        print(result_list)
        result_total = max(result_list[1:])
        if int(result_total) == 0:
            print('No results')
            driver.get('https://matrix.crmls.org/Matrix/Search/Residential/Detail')
            continue
    ##    result_total = driver.find_elements_by_tag_name('b')[2].get_attribute('innerHTML')
        print('Result: ' + result_total)
        page_total = ceil(int(result_total)/100)
        print('Pages: ' + str(page_total))
        file_num = 0
        # If total result is 500 or less, perform below
        for i in range(ceil(int(result_total)/500)):
            # Logic to determine how many times to click next page
            current_page = i * 5
            page_count = page_total - current_page
            interation = min(4, page_count - 1)
            time.sleep(.7)
            driver.find_element_by_id('m_lnkCheckPageLink').click()
            # Click through and select all result of page
            for i in range(interation):
                time.sleep(.7)
                driver.find_element_by_id('m_DisplayCore_dpy2').click()
                time.sleep(.7)
                driver.find_element_by_id('m_lnkCheckPageLink').click()
            # Export results
            driver.find_element_by_xpath("//*[@class='linkIcon icon_export']").click()
            time.sleep(.5)
            driver.find_element_by_id('m_ddExport').click()
            export_type = Select(driver.find_element_by_id('m_ddExport'))
            export_type.select_by_visible_text('Full')
            driver.find_element_by_id('m_btnExport').click()
            driver.find_element_by_id('m_btnBack').click()
            file_num = file_num + 1
            # Print Log for Tracking
            msg = "City: {}\nResults: {}\nFile: {}\n".format(city, result_total, file_num)
            print(msg)
            # Change File Name in Downloads
            time.sleep(2)
            old_file = 'Full.csv'
            new_file = 'C-{}_RE-{}_F-{}_D-{}_DR-{}.csv'.format(city, result_total, file_num, date.today(),days_range)
            PATH_DOWNLOAD = "/Users/Thang Nguyen/Downloads"
            os.chdir(PATH_DOWNLOAD)
            os.rename(old_file, new_file)
            # Logic to deselect or reset to search criteria page
            try:
                driver.find_element_by_id('m_lnkCheckNoneLink').click()
                time.sleep(.5)
                driver.find_element_by_id('m_DisplayCore_dpy2').click()
            except NoSuchElementException:
                driver.get('https://matrix.crmls.org/Matrix/Search/Residential/Detail')
finally:
    input('Press return to quit')
    driver.quit()










##driver.quit()
