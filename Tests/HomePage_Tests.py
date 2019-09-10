import unittest
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from PageObjects.Pages.HomePage import HomePageItems
from PageObjects.Pages.ChannelStorePage import ChannelStoreItems
import HtmlTestRunner
import time


class HomePageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="D:/Каспер/QA/Python/Roku_web/Drivers/chromedriver.exe")
        print("Run started at :" + str(datetime.datetime.now()))
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        cls.driver.get("https://roku.com")

    # Invalid Cases
    # def test_01_presence_of_logo(self):
    #     # Action on HomePage
    #     homepage = HomePageItems(self.driver)
    #     self.assertTrue(homepage.check_logo_presence())
    #
    # def test_02_logo_redirects_to_homepage(self):
    #     homepage = HomePageItems(self.driver)
    #     homepage.click_on_logo()
    #     self.assertEqual(homepage.url, "https://www.roku.com/en-gb/")

    def test_03_add_the_channel(self):
        homepage = HomePageItems(self.driver)
        homepage.click_on_channel_store()

        channelstorepage = ChannelStoreItems(self.driver)
        #self.assertEqual(channelstorepage.verify_channel_store_page_url(),
                         #"https://channelstore.roku.com/en-gb/browse")
        channelstorepage.enter_txt_to_the_search_field("Netflix")
        time.sleep(2)
        channelstorepage.pressing_enter_for_searching()
        time.sleep(2)
        channelstorepage.pressing_on_netflix_details_btn()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Finished at :" + str(datetime.datetime.now()))


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="D:\Каспер\QA\Python\Roku_web\Reports"))
