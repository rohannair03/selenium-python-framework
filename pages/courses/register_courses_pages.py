import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _all_courses_link = "//a[normalize-space()='ALL COURSES']"
    _search_box = "//input[@id='search'][1]"
    _search = "//button[@type='submit']"
    _found_course = "//h4[contains(@class, 'dynamic-heading') and contains(text(), '{0}')]"
    _all_courses = ""
    _enroll_button = "//button[normalize-space()='Enroll in Course']"
    _cc_num = "//input[@aria-label='Credit or debit card number']"
    _cc_exp = "//input[@aria-label='Credit or debit card expiry date']"
    _cc_cvv = "//input[@aria-label='Credit or debit card CVC/CVV']"
    _submit_enroll = "//button[@class='zen-subscribe sp-buy btn btn-default btn-lg btn-block btn-gtw btn-submit checkout-button dynamic-button']"
    _enroll_error_message = "//span[normalize-space()='Your card number is invalid.']"

    def clickCoursesLink(self):
        self.elementClick(locator=self._all_courses_link, locatorType="xpath")

    def clickSearch(self, courses):
        self.sendKeys(courses, locator=self._search_box, locatorType="xpath")

    def clickSearchCourses(self):
        self.elementClick(locator=self._search, locatorType="xpath")

    def clickCourse(self, course):
        self.elementClick(locator=self._found_course.format(course), locatorType="xpath")

    def clickEnroll(self):
        self.elementClick(locator=self._enroll_button, locatorType="xpath")

    def scrollDown(self):
        self.webScroll("down")

    def enterCardNum(self, cc_num):
        self.SwitchFrameByIndex(self._cc_num, locatorType="xpath")
        self.sendKeys(cc_num, locator=self._cc_num, locatorType="xpath")
        self.switchToDefaultContent()

    def enterCardExp(self, cc_exp):
        self.SwitchFrameByIndex(self._cc_exp, locatorType="xpath")
        self.sendKeys(cc_exp, locator=self._cc_exp, locatorType="xpath")
        self.switchToDefaultContent()

    def enterCardCVV(self, cc_cvv):
        self.SwitchFrameByIndex(self._cc_cvv, locatorType="xpath")
        self.sendKeys(cc_cvv, locator=self._cc_cvv, locatorType="xpath")
        self.switchToDefaultContent()

    def clickEnrollSubmitButton(self):
        self.elementClick(locator=self._submit_enroll, locatorType="xpath")

    def enrollCourse(self, courses=""):
        self.clickCoursesLink()
        self.clickSearch(courses)
        self.clickSearchCourses()
        self.clickCourse(courses)
        self.clickEnroll()
        self.scrollDown()

    def enterCardDetails(self, cc_num="", cc_exp="", cc_cvv=""):
        self.enterCardNum(cc_num=cc_num)
        self.enterCardExp(cc_exp=cc_exp)
        self.enterCardCVV(cc_cvv=cc_cvv)

    def verifyEnrollFailed(self):
        result = self.isElementPresent(locator=self._enroll_error_message, locatorType="xpath")
        return result
