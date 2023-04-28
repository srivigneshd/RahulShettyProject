from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class rahul_flight_booking:
    url="https://rahulshettyacademy.com/dropdownsPractise/"
    driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    departure_id="ctl00_mainContent_ddl_originStation1_CTXT"
    capture_all_departure_xpath="//div[@id='dropdownGroup1']/div/descendant::li"
    capture_all_arrival_xpath="//*[@id='ctl00_mainContent_ddl_destinationStation1_CTNR']//descendant::a"

    date_css_selector='#ctl00_mainContent_view_date1'
    year_xpath="(//span[@class='ui-datepicker-year'])[1]"
    month_xpath="(//span[@class='ui-datepicker-month'])[1]"
    next_xpath="//span[@class='ui-icon ui-icon-circle-triangle-e']"
    date_xpath="(//table[@class='ui-datepicker-calendar'])[1]//tbody/tr/td/a"

    year="2023"
    month="August"
    date="23"

    return_year='2013'
    return_mon='September'
    return_date='10'

    passengers_css_selector='#divpaxinfo'
    passengers_adult_css_selector='#hrefIncAdt'
    passengers_child_css_selector='#hrefIncChd'
    passenger_done_css_selector='#btnclosepaxoption'

    #currency_css_selector='ctl00_mainContent_DropDownListCurrency'
    currency_css_selector="//select[@id='ctl00_mainContent_DropDownListCurrency']"

    search_xpath="//input[contains(@id,'ctl00_mainContent_btn_FindFlights')]"

    #test case 2 
    roundTrip_css_selector='#ctl00_mainContent_rbtnl_Trip_1'
    return_date_css_selector='#ctl00_mainContent_view_date2'
    return_mon_css_selector="(//div[@class='ui-datepicker-title']/span[@class='ui-datepicker-month'])[1]"
    return_year_css_selector="(//div[@class='ui-datepicker-title']/span[@class='ui-datepicker-year'])[1]"
    return_dates_xpath="(//table[@class='ui-datepicker-calendar'])[1]//tbody/tr/td/a"
    return_next_xpath="(//*[text()='Next'])[1]"

    def __init__(self):
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.url)

    def testcase1_onetrip(self):
        #Departure selection
        self.driver.find_element(by=By.ID,value=self.departure_id).click()
        depature_cities=self.driver.find_elements(by=By.XPATH,value=self.capture_all_departure_xpath)
        for city in depature_cities:
            if city.text=="Amritsar (ATQ)":
                city.click()
                print("selected",city.text)
                break
        print("departure city is selected")
        #selection selection
        arrival_cities=self.driver.find_elements(by=By.XPATH,value=self.capture_all_arrival_xpath)
        print(len(arrival_cities))
        for city in arrival_cities:
            if city.text=="Kabul (KBL)":
                city.click()
                print("selected",city.text)
                break
        print("arrival city is selected")
        #data selection
        self.driver.find_element(by=By.CSS_SELECTOR,value=self.date_css_selector).click()
        while True:
            yr=self.driver.find_element(by=By.XPATH,value=self.year_xpath).text
            mon=self.driver.find_element(by=By.XPATH,value=self.month_xpath).text
            if mon==self.month and yr==self.year:
                print(mon,yr)
                break
            else:
                self.driver.find_element(by=By.XPATH,value=self.next_xpath).click()

        dates=self.driver.find_elements(by=By.XPATH,value=self.date_xpath)
        for i in dates:
            if i.text==self.date:
                i.click()
                break
        #passengers selection
        self.driver.find_element(by=By.CSS_SELECTOR,value=self.passengers_css_selector).click()
        self.driver.find_element(by=By.CSS_SELECTOR,value=self.passengers_adult_css_selector).click()
        self.driver.find_element(by=By.CSS_SELECTOR,value=self.passengers_child_css_selector).click()
        self.driver.find_element(by=By.CSS_SELECTOR,value=self.passenger_done_css_selector).click()

        #currency selection
        drp_currency_ele=self.driver.find_element(by=By.XPATH,value=self.currency_css_selector)
        drp_currency=Select(drp_currency_ele)
        all_options=drp_currency.options
        for i in all_options:
            if i.text=="AED":
                i.click()
                break
        self.driver.find_element(by=By.XPATH,value=self.search_xpath).click()

    #testcase : 2 for round trip
    def testcase02_roundtrip(self):
        self.driver.find_element(by=By.CSS_SELECTOR,value=self.roundTrip_css_selector).click()
        self.driver.find_element(by=By.ID,value=self.departure_id).click()
        depature_cities=self.driver.find_elements(by=By.XPATH,value=self.capture_all_departure_xpath)
        for city in depature_cities:
            if city.text=="Amritsar (ATQ)":
                city.click()
                print("selected",city.text)
                break
        print("departure city is selected")
        #selection selection
        arrival_cities=self.driver.find_elements(by=By.XPATH,value=self.capture_all_arrival_xpath)
        print(len(arrival_cities))
        for city in arrival_cities:
            if city.text=="Kabul (KBL)":
                city.click()
                print("selected",city.text)
                break
        print("arrival city is selected")
        #departure data selection
        self.driver.find_element(by=By.CSS_SELECTOR,value=self.date_css_selector).click()
        while True:
            yr=self.driver.find_element(by=By.XPATH,value=self.year_xpath).text
            mon=self.driver.find_element(by=By.XPATH,value=self.month_xpath).text
            if mon==self.month and yr==self.year:
                print(mon,yr)
                break
            else:
                self.driver.find_element(by=By.XPATH,value=self.next_xpath).click()

        dates=self.driver.find_elements(by=By.XPATH,value=self.date_xpath)
        for i in dates:
            if i.text==self.date:
                i.click()
                break

        
        #return date selection
        self.driver.find_element(by=By.CSS_SELECTOR,value=self.return_date_css_selector).click()
        while True:
            yr=self.driver.find_element(by=By.XPATH,value=self.return_year_css_selector).text
            mon=self.driver.find_element(by=By.XPATH,value=self.return_mon_css_selector).text
            if mon==self.return_mon and yr==self.return_year:
                print(mon,yr)
                print("return month and year")
                break
            else:
                self.driver.find_element(by=By.XPATH,value=self.return_next_xpath).click()

        dates=self.driver.find_elements(by=By.XPATH,value=self.return_dates_xpath)
        for i in dates:
            if i.text==self.return_date:
                i.click()
                break


exp=rahul_flight_booking()
exp.testcase1_onetrip()
exp.testcase02_roundtrip()
