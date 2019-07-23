# import unittest
# import datetime
# from selenium import webdriver
# from PageObjects.Pages.LoginPage import LoginPage
#
#
# class LoginTests(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         cls.driver = webdriver.Chrome(executable_path="D:\Каспер\QA\Python\Roku_web\Drivers\chromedriver.exe")
#         print("Run started at :" + str(datetime.datetime.now()))
#         cls.driver.implicitly_wait(5)
#         cls.driver.maximize_window()
#
#
#
#     @classmethod
#     def tearDownClass(cls):
#         print("Finished at :" + str(datetime.datetime.now()))
#         cls.driver.close()
#         cls.driver.quit()
#
#
# if __name__ == "__main__":
#     unittest.main()
