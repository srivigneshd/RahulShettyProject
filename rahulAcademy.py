from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class rahulacademy:
    url="https://rahulshettyacademy.com/locatorspractice/"
    driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    user_inpubox_id="inputUsername"
    password_inputbox_name="inputPassword"
    agree_click_id="chkboxTwo"
    submit_button_css_selector="button[type='submit']"
    incorrect_username_xpath='//p[@class="error"]'

    forgot_linktext="Forgot your password?"
    name_css_selector="input[placeholder='Name']"
    email_css_selector="input[placeholder='Email']"
    phone_number_css_selector="input[placeholder='Phone Number']"
    gotolog_xpath="//button[normalize-space()='Go to Login']"

    reset_login_xpath="//button[@class='reset-pwd-btn']"
    temp_password_css_selector='.infoMsg'

    successful_login_xpath="//p[normalize-space()='You are successfully logged in.']"

    logout_xpath="//button[@class='logout-btn']"

    username="srivignesh"
    password="dserfd"

    name="Srivignesh"
    email="sriv1516@gmail.com"
    phone="8754245401"
    #retrived_password="rahulshettyacademy"


    #constructor for rahulacademy  
    def __init__(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
    def login(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.ID,value=self.user_inpubox_id).send_keys(self.username)
        self.driver.find_element(by=By.NAME,value=self.password_inputbox_name).send_keys(self.password)
        self.driver.find_element(by=By.ID,value=self.agree_click_id).click()
        self.driver.find_element(by=By.CSS_SELECTOR,value=self.submit_button_css_selector).click()
        actual_val=self.driver.find_element(by=By.XPATH,value=self.incorrect_username_xpath).text
        expected_val="* Incorrect username or password"
        if actual_val==expected_val:
            print("Success:login functionality is working properly for incorrect input data")
        else:
            print("Failed")
    def forgetPassword(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.LINK_TEXT,value=self.forgot_linktext).click()
        self.driver.find_element(by=By.CSS_SELECTOR,value=self.name_css_selector).send_keys(self.name)
        self.driver.find_element(by=By.CSS_SELECTOR,value=self.email_css_selector).send_keys(self.email)
        self.driver.find_element(by=By.CSS_SELECTOR,value=self.phone_number_css_selector).send_keys(self.phone)
        self.driver.find_element(by=By.XPATH,value=self.reset_login_xpath).click()
        temp_passwords=self.driver.find_element(by=By.CSS_SELECTOR,value=self.temp_password_css_selector).text
        print(temp_passwords[31:49])
        print("succesfully filled the forget password details")
        retrived_password=temp_passwords[31:49]
        self.driver.find_element(by=By.XPATH,value=self.gotolog_xpath).click()
    def successful_login(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.LINK_TEXT,value=self.forgot_linktext).click()
        self.driver.find_element(by=By.CSS_SELECTOR,value=self.name_css_selector).send_keys(self.name)
        self.driver.find_element(by=By.CSS_SELECTOR,value=self.email_css_selector).send_keys(self.email)
        self.driver.find_element(by=By.CSS_SELECTOR,value=self.phone_number_css_selector).send_keys(self.phone)
        self.driver.find_element(by=By.XPATH,value=self.reset_login_xpath).click()
        temp_passwords=self.driver.find_element(by=By.CSS_SELECTOR,value=self.temp_password_css_selector).text
        retrived_password=temp_passwords[31:49]
        self.driver.find_element(by=By.XPATH,value=self.gotolog_xpath).click()
        self.driver.find_element(by=By.ID,value=self.user_inpubox_id).send_keys(self.username)
        self.driver.find_element(by=By.NAME,value=self.password_inputbox_name).send_keys(retrived_password)
        self.driver.find_element(by=By.ID,value=self.agree_click_id).click()
        self.driver.find_element(by=By.CSS_SELECTOR,value=self.submit_button_css_selector).click()
        sleep(5)
        actual_val=self.driver.find_element(by=By.XPATH,value=self.successful_login_xpath).text
        expected_val="You are successfully logged in."
        if actual_val==expected_val:
            print("Success:login functionality is working")
        else:
            print("Failed")
        self.driver.find_element(by=By.XPATH,value=self.logout_xpath).click()
    
exp=rahulacademy()
exp.login()
exp.forgetPassword()
exp.successful_login()