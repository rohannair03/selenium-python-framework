import logging
import utilities.custom_logger as cl
from base.basepage import BasePage

class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _home = "//a[normalize-space()='HOME']"
    _all_courses = "//a[normalize-space()='ALL COURSES']"
    _interview = "//a[normalize-space()='INTERVIEW']"
    _support = "//a[normalize-space()='SUPPORT']"
    _blog = "//a[normalize-space()='BLOG']"
    _user_icon = "//img[@alt='letskodeit']"
    _login_icon = "//img[@class='zl-navbar-rhs-img ']"

    def navigateToHome(self):
        self.elementClick(locator = self._home, locatorType = "xpath")

    def navigateToAllCourses(self):
        self.elementClick(locator = self._all_courses, locatorType = "xpath")

    def navigateToInterview(self):
        self.elementClick(locator = self._interview, locatorType = "xpath")

    def navigateToSupport(self):
        self.elementClick(locator = self._support, locatorType = "xpath")

    def navigateToBlog(self):
        self.elementClick(locator = self._blog, locatorType = "xpath")

    def navigateToUserIcon(self):
        self.elementClick(locator = self._user_icon, locatorType = "xpath")

    def navigateToLoginIcon(self):
        self.elementClick(locator = self._login_icon, locatorType = "xpath")
