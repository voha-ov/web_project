from PageObjects.Locators import SignInPageLocators


class SignInPageItems:
    def __init__(self, driver):
        self.driver = driver

        # Available options
        self.email_textbox_name = SignInPageLocators.Email
        self.password_textbox_name = SignInPageLocators.Password
        self.captcha_checkbox_xpath = SignInPageLocators.Captcha
        self.sign_in_button_xpath = SignInPageLocators.Sign_in_button
        self.password_reset_button_xpath = SignInPageLocators.Password_reset
        self.create_account_button_xpath = SignInPageLocators.Create_account

        # Errors and messages
        self.unchecked_captcha_message = SignInPageLocators.Unchecked_captcha
        self.popup_txt1 = SignInPageLocators.Correct_highlighted_fields_popup_txt1
        self.popup_txt2 = SignInPageLocators.Correct_highlighted_fields_popup_txt2
        self.popup_ok_btn = SignInPageLocators.Correct_highlighted_fields_popup_ok_btn
        self.popup_x_btn = SignInPageLocators.Correct_highlighted_fields_popup_x_btn

    def enter_email(self, user_email):
        self.driver.find_element_by_name(self.email_textbox_name).clear()
        self.driver.find_element_by_name(self.email_textbox_name).send_keys(user_email)

    def enter_user_password(self, user_password):
        self.driver.find_element_by_name(self.password_textbox_name).clear()
        self.driver.find_element_by_name(self.password_textbox_name).send_keys(user_password)

    def click_on_captcha(self):
        #self.driver.find_element_by_xpath(self.captcha_checkbox_xpath).click()
        pass

    def click_on_sign_in_button(self):
        self.driver.find_element_by_xpath(self.sign_in_button_xpath).click()


    # Invalid cases
    def popuptxt_01(self):
        msg_sorry = self.driver.find_element_by_xpath(self.popup_txt1).text
        return msg_sorry
    def popuptxt_02(self):
        msg_an_error_was = self.driver.find_element_by_xpath(self.popup_txt2).text
        return msg_an_error_was
    def click_pop_up_ok_btn(self):
        self.driver.find_element_by_xpath(self.popup_ok_btn).click()

    def check_of_unchecked_captcha(self):
        msg = self.driver.find_element_by_xpath(self.unchecked_captcha_message).text
        return msg
