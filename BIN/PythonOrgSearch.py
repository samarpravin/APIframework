import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



from selenium.webdriver.support.ui import WebDriverWait

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        timeout = 10
        driver.get("https://www.amazon.in")
        driver.maximize_window()
        signIn=driver.find_element_by_xpath("//span[contains(text(),'Hello. Sign in')]")
        signIn.click()
        element_present = EC.presence_of_element_located((By.XPATH, "//input[@type='email']"))
        WebDriverWait(driver, timeout).until(element_present)
        email=driver.find_element_by_xpath("//input[@type='email']")
        email.send_keys("pravin.kusin@gmail.com")

        continuebutton=driver.find_element_by_xpath("//input[@id='continue']")
        continuebutton.click()

        element_present = EC.presence_of_element_located((By.XPATH, "//input[@id='ap_password']"))
        WebDriverWait(driver, timeout).until(element_present)
        password = driver.find_element_by_xpath("//input[@id='ap_password']")
        password.send_keys("Hari&sadu11")
        login = driver.find_element_by_xpath("//input[@id='signInSubmit']")
        login.click()
        element_present = EC.presence_of_element_located((By.XPATH, "//div[@id='nav-tools']/a[1]/span[@class='nav-line-1']"))
        WebDriverWait(driver, timeout).until(element_present)
        landingpage = driver.find_element_by_xpath("//div[@id='nav-tools']/a[1]/span[@class='nav-line-1']")
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