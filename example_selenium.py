# unit test case
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import string
from selenium.webdriver.common.alert import Alert

class TestaddCart(unittest.TestCase):

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
        
    def test_success_add_cart(self): 
        driver = self.driver
        driver.get("https://www.demoblaze.com/index.html#")
        driver.maximize_window()
        time.sleep(1)
        
        #Login
        
        driver.find_element(By.ID, 'login2').click()
        time.sleep(1)
        driver.find_element(By.ID, "loginusername").send_keys('annisarahmaniardp')
        time.sleep(1)
        driver.find_element(By.ID, "loginpassword").send_keys('123')
        time.sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]').click()
        time.sleep(4)
        respon_welcome = driver.find_element(By.ID, 'nameofuser').text
        self.assertEqual(respon_welcome, 'Welcome annisarahmaniardp')
        
        #Add Cart
        
        product_name = driver.find_element(By.LINK_TEXT, "Samsung galaxy s6").text
        product_price = driver.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/div/div[1]/div/div/h5").text
        product_description = driver.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/div/div[1]/div/div/p").text
        
        driver.find_element(By.LINK_TEXT, "Samsung galaxy s6").click()
        time.sleep(2)
        
        response_product_name = driver.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/h2").text
        response_product_price = driver.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/h3").text
        response_product_price_rep = response_product_price.replace(" *includes tax", "")
        response_product_description = driver.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/div[1]/div/div/p").text
        
        self.assertEqual(response_product_name, product_name)
        self.assertEqual(response_product_price_rep, product_price)
        self.assertEqual(response_product_description, product_description)
        
        driver.find_element(By.XPATH, "// a[contains(text(), 'Add to cart')]").click()
        time.sleep(3)
        
        # create alert object
        alert = Alert(driver)
        alert.accept()
        
        driver.find_element(By.XPATH, "/html/body/nav/div/div/ul/li[4]/a").click()
        time.sleep(2)
        
        title = driver.find_element(By.XPATH, "/html/body/div[6]/div/div[1]/div/table/tbody/tr/td[2]").text 
        self.assertEqual(title, response_product_name)
        
        response_product_price_rep2 = response_product_price_rep.replace('$', '')
        price = driver.find_element(By.XPATH, "/html/body/div[6]/div/div[1]/div/table/tbody/tr/td[3]").text 
        
        self.assertEqual(price, response_product_price_rep2)
        
           
    def tearDown(self): 
        self.driver.close() 
        
if __name__ == '__main__':
    unittest.main()