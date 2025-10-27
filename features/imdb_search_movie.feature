Feature: Search for a movie on IMDb
  Scenario: Search for Inception and check title and rating
    Given I am on the IMDb homepage
    When I search for the movie "Inception"
    And I open the first movie result
    Then I should see the movie title and rating
