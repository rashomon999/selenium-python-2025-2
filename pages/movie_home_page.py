from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class moviemHomePage(BasePage):
    SEARCH_BOX = (By.ID, "suggestion-search")
    SEARCH_BUTTON = (By.ID, "suggestion-search-button")

    def search_artist(self, movie_name):
        self.click(self.SEARCH_BOX)
        self.enter_text(self.SEARCH_BOX, movie_name)
        self.click(self.SEARCH_BUTTON)
