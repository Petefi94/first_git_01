from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class LoginPage02(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # <Locators>
    _login_link = "placeholder"
    _email_field = "placeholder"
    _password_field = "placeholder"
    _login_button = "placeholder"
    # <Additional locators>(if there is a middle step)
    _btn_1 = "placeholder"
    _btn_2 = "placeholder"
    # <Checkups>
    _check_1 = "//h1[@class='home-title uk-text-center-small']"
    # <iFrames>
    _iFrame_name = "placeholder"
    # </Locators>

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="xpath")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field, locatorType='xpath')

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, locatorType="xpath")

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    # <click fillers>
    def justClick_btn1(self):
        self.elementClick(self._btn_1, locatorType="xpath")
    def justClick_btn2(self):
        self.elementClick(self._btn_2, locatorType="xpath")
    # </click fillers>

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//*[@id='navbar']//span[text()='User Settings']",
                                       locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[contains(text(),'Invalid email or password')]",
                                       locatorType="xpath")
        return result

    def verifyTitle(self):
        if "Home" in self.getTitle():
            return True
        else:
            return False

    def verifyContains(self):
        check = self.getElement(self._check_1, locatorType="xpath")
        check_text = self.getText(element=check)

        if "Automobili" in check_text:
            return True
        else:
            return False

    def elementPresent(self):
        self.isElementPresent(self._btn_2, "xpath")





