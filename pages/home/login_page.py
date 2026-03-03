import logging
import utilities.custom_logger as cl
from base.basepage import BasePage
from pages.home.navigation_page import NavigationPage

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _login_link = "//a[normalize-space()='Sign In']"
    _email_field = "//form[@name='loginform']//input[@id='email']"
    _password_field = "(//input[@id='login-password'])[1]"
    _login_button = "//button[@id='login']"

    def clickLoginLink(self):
        self.elementClick(locator = self._login_link, locatorType = "xpath")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(locator = self._login_button, locatorType = "xpath")

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent(locator="//h1[normalize-space()='My Courses']", locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent(locator= "//span[contains(text(), 'Incorrect login details')]", locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Login")

    def logout(self):
        self.nav.navigateToLoginIcon()
        self.elementClick(locator="//a[normalize-space()='Logout']", locatorType = "xpath")


