from behave import given, when, then
from selenium import webdriver
from pages.imdb_search_movie_page import ImdbSearchMoviePage

@given('I am on the IMDb homepage')
def step_open_homepage(context):
    context.driver.maximize_window()
    context.driver.get("https://www.imdb.com/")
    context.imdb_page = ImdbSearchMoviePage(context.driver)

@when('I search for the movie "{movie_name}"')
def step_search_movie(context, movie_name):
    context.imdb_page.search_movie(movie_name)

@when('I open the first movie result')
def step_open_first_result(context):
    context.imdb_page.open_first_result()

@then('I should see the movie title and rating')
def step_check_movie_info(context):
    title, rating = context.imdb_page.get_movie_title_and_rating()
    assert rating is not None, "Rating not found"
    print(f" Found movie: {title}, rating: {rating}")
 