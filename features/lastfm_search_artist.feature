# features/lastfm_search_artist.feature
Feature: Search artist on Last.fm

  Scenario: Search for Bruno Mars and check last release
    Given I am on the Last.fm homepage
    When I search for the artist "Bruno Mars"
    And I open the first result
    Then I should see the release date of the artist's last album
