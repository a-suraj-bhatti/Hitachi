
Feature: Verify booking.com website
  As a QA
  I want to test Booking.com
  So that I can verify if the flight with the lowest price can be selected

  Scenario: :Problem statement
    Given user navigates to "https://www.booking.com/"
    And user clicks on "flights" tab
    And user clicks on one way radio button
    And user enters Delhi in from
    And user enters Bangalore in to
    And user selects the data 5 days from now
    And user clicks on the search button
    And user selects cheapest price and click on See Flights button
    Then user clicks select button in the pop up


