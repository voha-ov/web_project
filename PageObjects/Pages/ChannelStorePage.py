from PageObjects.Locators import ChannelStorePageLocators
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class ChannelStoreItems:
    def __init__(self, driver):
        self.driver = driver

        # available options
        self.url = ChannelStorePageLocators.Url
        self.search_filed = ChannelStorePageLocators.Search_field
        self.pressing_on_netflix_details_btn = ChannelStorePageLocators.Netflix_details_btn

    def verify_channel_store_page_url(self):
        self.driver.current_url

    def enter_txt_to_the_search_field(self, txt):
        self.driver.find_element_by_class_name(self.search_filed).send_keys(txt)

    def pressing_enter_for_searching(self):
        self.driver.find_element_by_class_name("form-control").send_keys(Keys.ENTER)

    def netflix_details(self):
        self.driver.find_element_by_partial_link_text(self.pressing_on_netflix_details_btn).click()
