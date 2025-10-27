from behave import given, when, then
from selenium import webdriver
from pages.lastfm_home_page import LastfmHomePage
from pages.lastfm_results_page import LastfmResultPage
from pages.lastfm_artist_page import LastfmArtistPage

@given('I am on the Last.fm homepage')
def step_home_page(context):
    context.driver.maximize_window()
    context.driver.get("https://www.last.fm/")
    context.lastfm_home = LastfmHomePage(context.driver)

@when('I search for the artist "{artist_name}"')
def step_search_page(context, artist_name):
    context.lastfm_home.search_artist(artist_name)
    context.lastfm_results = LastfmResultPage(context.driver)

@when('I open the first result')
def step_press_link(context):
    context.lastfm_results.press_link()
    context.lastfm_artist = LastfmArtistPage(context.driver)

@then('I should see the release date of the artist\'s last album')
def step_validate_release_date(context):
    actual_date = context.lastfm_artist.get_latest_release_date()
    print("Latest release date:", actual_date)
