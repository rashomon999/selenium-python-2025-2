from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class movieInceptionPage(BasePage):
    MOVIE_TITLE = (By.XPATH, "//*[contains(text(), 'Título original: ')]")
    MOVIE_RATING = (By.CSS_SELECTOR, 'div[data-testid="hero-rating-bar__aggregate-rating__score"] span')   

    def get_title(self):
        return self.find_element(self.MOVIE_TITLE).text
    
    def get_rating(self):
        return self.find_element(self.MOVIE_RATING).text 
        
