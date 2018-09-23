import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



from selenium.webdriver.support.ui import WebDriverWait

class test_pytestframeClass(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.amazon.in")

    def test_search_in_python_org(self):
        timeout = 10
        self.driver.maximize_window()
        signIn=self.driver.find_element_by_xpath("//span[contains(text(),'Hello. Sign in')]")
        signIn.click()
        element_present = EC.presence_of_element_located((By.XPATH, "//input[@type='email']"))
        WebDriverWait(self.driver, timeout).until(element_present)
        email=self.driver.find_element_by_xpath("//input[@type='email']")
        email.send_keys("pravin.kusin@gmail.com")
        continuebutton=self.driver.find_element_by_xpath("//input[@id='continue']")
        continuebutton.click()
        element_present = EC.presence_of_element_located((By.XPATH, "//input[@id='ap_password']"))
        WebDriverWait(self.driver, timeout).until(element_present)
        password = self.driver.find_element_by_xpath("//input[@id='ap_password']")
        password.send_keys("Hari&sadu11")
        login = self.driver.find_element_by_xpath("//input[@id='signInSubmit']")
        login.click()
        element_present = EC.presence_of_element_located((By.XPATH, "//div[@id='nav-tools']/a[1]/span[@class='nav-line-1']"))
        WebDriverWait(self.driver, timeout).until(element_present)
        landingpage = self.driver.find_element_by_xpath("//div[@id='nav-tools']/a[1]/span[@class='nav-line-1']")
        welcometxt =  landingpage.text
        print welcometxt
        splitvar = welcometxt.split(",")
        if splitvar[0] == "Hello":
            print "login is successfull for the user {}".format(welcometxt)
        else:
            print "login is not successfull for the user {}".format(welcometxt)
            raise Exception


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()