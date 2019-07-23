class HomePageLocators:
    # Home page locators

    Url = "https://www.roku.com/en-gb/"
    Logo = "//div[@class='nav-logo']//a"
    HowItWorks = "//a[@class='navListItems'][contains(text(),'How it works')]"
    ActivateADevice = "//a[@class='navListItems'][contains(text(),'Activate a device')]"
    Sign_In = "//a[contains(text(),'Sign in')]"
    WhatToWatch_ChannelStore = "//span[contains(text(),'Channel Store')]"
    WhatToWatch = "//a[contains(text(),'What to watch')]"


class SignInPageLocators:
    # Sign_In Page locators

    Email = "email"
    Password = "password"
    Captcha = "//iframe[@name='a-kmxuov6w5vy3']"
    Sign_in_button = "//button[@class='signin-button']"
    Password_reset = "//a[@class='password-reset']"
    Create_account = "//button[@class='signup-button']"

    # Errors and messages
    Unchecked_captcha = "//div[@class='catpcha_error']"
    Correct_highlighted_fields_popup_txt1 = "//div[@class='modal']//h2[contains(text(),'Sorry')]"
    Correct_highlighted_fields_popup_txt2 = "//div[@class='modal']//div[@class='modal-content'][" \
                               "contains(text(),'An error was encountered with the form. Please cor')]"
    Correct_highlighted_fields_popup_ok_btn = "//div[@class='modal']//button[contains(text(),'OK')]"
    Correct_highlighted_fields_popup_x_btn = "//div[@class='modal']//button[@class='modal-close'][contains(text(),'×')]"



class SignUpPageLocators:
    # Sign_Up Page locators

    First_name = "//input[@id='firstname']"
    Last_name = "//input[@id='lastname']"
    Sign_up_email = "//input[@id='email']"
    Sign_up_password = "//input[@id='password']"
    Display_password = "//span[@class='input-container-eye']"
    Check_box_18_years = "//span[contains(text(),'I am 18 years or older.')]"
    Check_box_tos = "//span[@class='tos']"
    Check_box_email_me = "//span[contains(text(),'Email me product tips, the latest releases, hot ne')]"
    Sign_up_captcha = "recaptcha-anchor"
    Continue = "//button[@class='roku-button']"
    Sign_up_sign_in_button = "//div[@class='signin']//a[contains(text(),'Sign in')]"


class ForgotPasswordPageLocators:
    # Forgot Password Page locators
    Email = "//input[@id='Shell-51-Email']"
    Sign_up_captcha = "recaptcha-anchor"
    Submit_button = "//button[contains(text(),'Submit')]"


class ChannelStorePageLocators:
    # Channel Store Page Locators

    Search_channel = "// input[ @ id = 'Shell-21-Searchbar']"
