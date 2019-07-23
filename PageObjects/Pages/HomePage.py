from PageObjects.Locators import HomePageLocators
from selenium import webdriver


class HomePageItems:
    def __init__(self, driver):
        self.driver = driver

        # Available options
        self.url = HomePageLocators.Url
        self.logo = HomePageLocators.Logo
        self.how_it_works = HomePageLocators.HowItWorks
        self.activate_device = HomePageLocators.ActivateADevice
        self.sign_in = HomePageLocators.Sign_In
        self.what_to_watch_channel_store = HomePageLocators.WhatToWatch_ChannelStore

    def check_logo_presence(self):
        return self.driver.find_element_by_xpath(self.logo)

    def click_on_logo(self):
        self.driver.find_element_by_xpath(self.logo).click()

    def click_on_how_it_works(self):
        self.driver.find_element_by_xpath(self.how_it_works).click()

    def click_on_activate_device(self):
        self.driver.find_element_by_xpath(self.activate_device).click()

    def click_on_sign_in(self):
        self.driver.find_element_by_xpath(self.sign_in).click()

    def click_on_channel_store(self):
        self.driver.find_element_by_xpath(self.what_to_watch_channel_store).click()


