import logging
import utilities.custom_logger as cl
from base.basepage import BasePage
from pages.home.navigation_page import NavigationPage
import allure

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

    @allure.step("Click Login Link")
    def clickLoginLink(self):
        self.elementClick(locator = self._login_link, locatorType = "xpath")

    @allure.step("Send Email Entered: {email}")
    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    @allure.step("Send Password Entered")
    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    @allure.step("Click Login Button")
    def clickLoginButton(self):
        self.elementClick(locator = self._login_button, locatorType = "xpath")

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    @allure.step("Verify Login Successful")
    def verifyLoginSuccessful(self):
        result = self.isElementPresent(locator="//h1[normalize-space()='My Courses']", locatorType="xpath")
        return result

    @allure.step("Verify Login Failed")
    def verifyLoginFailed(self):
        result = self.isElementPresent(locator= "//span[contains(text(), 'Incorrect login details')]", locatorType="xpath")
        return result

    @allure.step("Verify Login Title")
    def verifyLoginTitle(self):
        return self.verifyPageTitle("Login")

    @allure.step("Click Logout")
    def logout(self):
        self.nav.navigateToLoginIcon()
        self.elementClick(locator="//a[normalize-space()='Logout']", locatorType = "xpath")


