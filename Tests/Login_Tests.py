import unittest
import datetime
from selenium import webdriver
from PageObjects.Pages.SignInPage import SignInPageItems
from PageObjects.Pages.HomePage import HomePageItems
import HtmlTestRunner
import time


class LoginTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="D:/Каспер/QA/Python/Roku_web/Drivers/chromedriver.exe")
        print("Run started at :" + str(datetime.datetime.now()))
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        cls.driver.get("https://roku.com")

    # Invalid Cases
    def test_01_login_with_empty_fields(self):
        # Action on HomePage
        homepage = HomePageItems(self.driver)
        homepage.click_on_sign_in()

        # Action on SignPage
        sign_in_page = SignInPageItems(self.driver)
        time.sleep(2)
        sign_in_page.click_on_sign_in_button()

        # Comparing Actual and Expected result
        self.assertEqual(sign_in_page.popuptxt_01(), "Sorry")
        self.assertEqual(sign_in_page.popuptxt_02(),
                         "An error was encountered with the form. Please correct the highlighted fields.")
        sign_in_page.click_pop_up_ok_btn()

    def test_02_login_with_unchecked_captcha(self):
        # Action on HomePage
        homepage = HomePageItems(self.driver)
        homepage.click_on_logo()
        homepage.click_on_sign_in()

        # Action for log in on Sign in Page
        sign_in_page = SignInPageItems(self.driver)
        sign_in_page.enter_email("rokucert14@gmail.com")
        sign_in_page.enter_user_password("roku1234")
        time.sleep(1)
        sign_in_page.click_on_sign_in_button()

        # Comparing Actual and Expected result
        self.assertEqual(sign_in_page.check_of_unchecked_captcha(), "Required")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Finished at :" + str(datetime.datetime.now()))


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="D:/Каспер/QA/Python/Roku_web/Reports"))
