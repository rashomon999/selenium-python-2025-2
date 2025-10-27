from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class ImdbSearchMoviePage(BasePage):
    SEARCH_BOX = (By.ID, "suggestion-search")
    SEARCH_BUTTON = (By.ID, "suggestion-search-button")
    FIRST_RESULT = (By.XPATH, "//ul[@role='presentation']/li")
    MOVIE_TITLE = (By.XPATH, "//*[contains(text(), 'Título original: ')]")
    MOVIE_RATING = (By.CSS_SELECTOR, 'div[data-testid="hero-rating-bar__aggregate-rating__score"] span')   

    def search_movie(self, name):
        self.enter_text(self.SEARCH_BOX, name)
        self.click(self.SEARCH_BUTTON)

    def open_first_result(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.FIRST_RESULT)
        ).click()

    def get_movie_title_and_rating(self):
        try:
            title = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.MOVIE_TITLE)
            ).text
        except:
            title = None

        try:
            rating = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.MOVIE_RATING)
            ).text
        except:
            rating = None

        print(f" Title: {title} |  Rating: {rating}")
        return title, rating
