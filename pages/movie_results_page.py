from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class movieResultsPage(BasePage):
    #ARTIST_LINK = (By.CLASS_NAME, "link-block-target")
    FIRST_RESULT = (By.XPATH, "//ul[@role='presentation']/li")

    def press_link(self):
        self.click(self.FIRST_RESULT)
