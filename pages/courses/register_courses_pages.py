import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import allure

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

    @allure.step("Click All Courses Link")
    def clickCoursesLink(self):
        self.elementClick(locator=self._all_courses_link, locatorType="xpath")

    @allure.step("Search for course: {courses}")
    def clickSearch(self, courses):
        self.sendKeys(courses, locator=self._search_box, locatorType="xpath")

    @allure.step("Click Search Button")
    def clickSearchCourses(self):
        self.elementClick(locator=self._search, locatorType="xpath")

    @allure.step("Click course: {course}")
    def clickCourse(self, course):
        self.waitForElement(locator=self._found_course.format(course), locatorType="xpath", timeout=20)
        self.elementClick(locator=self._found_course.format(course), locatorType="xpath")

    @allure.step("Click Enroll Button")
    def clickEnroll(self):
        self.waitForElement(locator=self._enroll_button, locatorType="xpath", timeout=20)
        self.elementClick(locator=self._enroll_button, locatorType="xpath")

    @allure.step("Scroll Down")
    def scrollDown(self):
        self.webScroll("down")

    @allure.step("Enter Card Number")
    def enterCardNum(self, cc_num):
        self.SwitchFrameByIndex(self._cc_num, locatorType="xpath")
        self.sendKeys(cc_num, locator=self._cc_num, locatorType="xpath")
        self.switchToDefaultContent()

    @allure.step("Enter Card Expiry")
    def enterCardExp(self, cc_exp):
        self.SwitchFrameByIndex(self._cc_exp, locatorType="xpath")
        self.sendKeys(cc_exp, locator=self._cc_exp, locatorType="xpath")
        self.switchToDefaultContent()

    @allure.step("Enter Card CVV")
    def enterCardCVV(self, cc_cvv):
        self.SwitchFrameByIndex(self._cc_cvv, locatorType="xpath")
        self.sendKeys(cc_cvv, locator=self._cc_cvv, locatorType="xpath")
        self.switchToDefaultContent()

    @allure.step("Click Enroll Submit Button")
    def clickEnrollSubmitButton(self):
        self.elementClick(locator=self._submit_enroll, locatorType="xpath")

    @allure.step("Enroll in Course: {courses}")
    def enrollCourse(self, courses=""):
        self.clickCoursesLink()
        self.clickSearch(courses)
        self.clickSearchCourses()
        self.clickCourse(courses)
        self.clickEnroll()
        self.scrollDown()

    @allure.step("Enter Card Details")
    def enterCardDetails(self, cc_num="", cc_exp="", cc_cvv=""):
        self.enterCardNum(cc_num=cc_num)
        self.enterCardExp(cc_exp=cc_exp)
        self.enterCardCVV(cc_cvv=cc_cvv)

    @allure.step("Verify Enroll Failed")
    def verifyEnrollFailed(self):
        result = self.isElementPresent(locator=self._enroll_error_message, locatorType="xpath")
        return result
