from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class LoginPage01(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # # <Locators>
    _login_link = "//a[@class='uk-float-left js_ga-event']"
    _email_field = "//input[@id='username_header']"
    _password_field = "//input[@id='password_header']"
    _login_button = "//button[@name='login']"
    # <Additional locators>(if there is a middle step)
    _btn_One = "//button[@id='next-step']"
    _btn_Two = "/html/body/div[14]/div/div/div[1]/div[1]/button"
    # <Checkups>
    _check_One = "//div[@class='uk-float-left']//span[contains(text(),'dusanpet.94@gmail.com')]"
    # <iFrames>
    _iFrame_name = "lsgetframe"
    # </Locators>

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="xpath")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field, locatorType='xpath')

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, locatorType="xpath")

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    # Multiplied as many as times as needed
    def justClick(self):
        self.elementClick(self._btn_One, locatorType="xpath")

    def justClick_2(self):
        self.elementClick(self._btn_Two, locatorType="xpath")

    # <click fillers>
    def login(self, email="", password=""):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
    # </click fillers>

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//*[@id='navbar']//span[text()='User Settings']",
                                       locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[contains(text(),'Invalid email or password')]",
                                       locatorType="xpath")
        return result

    def verifyTitle(self):
        if "Google" in self.getTitle():
            return True
        else:
            return False

    def verifyContains(self):
        check = self.getElement(self._check_One, locatorType="xpath")
        check_text = check.text

        if "dusanpet.94@gmail.com" in check_text:
            return True
        else:
            return False

    def elementPresent(self):
        self.isElementPresent(self._btn_Two, "xpath")
