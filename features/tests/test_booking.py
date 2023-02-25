"""Verify booking.com website feature tests."""
import pytest
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
    parsers
)

from support.common_methods import CommonMethods

obj_common = CommonMethods()

@scenario('bdd_files/booking.feature', ':Problem statement')
def test_problem_statement():
    """:Problem statement."""


@given('user clicks on "flights" tab')
def user_clicks_on_flights_tab():
    """user clicks on "flights" tab."""
    obj_common.get_clickable_web_element(pytest.locators.str_flight_button).click()


@given('user clicks on one way radio button')
def user_clicks_on_one_way_radio_button():
    """user clicks on one way radio button."""
    obj_common.get_clickable_web_element(pytest.locators.str_one_way_button).click()


@given('user clicks on the search button')
def user_clicks_on_the_serch_button():
    """user clicks on the serch button."""
    obj_common.get_clickable_web_element(pytest.locators.str_search_button).click()




@given('user enters Bangalore in to')
def user_enters_bangalore_in_to():
    """user enters Bangalore in to."""
    obj_common.get_clickable_web_element(pytest.locators.str_to_field_click).click()
    obj_common.get_clickable_web_element(pytest.locators.str_airport_city_field,10).send_keys("Bangalore")
    obj_common.get_clickable_web_element(pytest.locators.str_bangalore_airport_select,10).click()



@given('user enters Delhi in from')
def user_enters_delhi_in_from():
    """user enters Delhi in from."""
    obj_common.get_clickable_web_element(pytest.locators.str_from_field_click).click()
    obj_common.get_clickable_web_element(pytest.locators.str_remove_loc).click()
    obj_common.get_clickable_web_element(pytest.locators.str_airport_city_field,10).send_keys("Delhi")
    obj_common.get_clickable_web_element(pytest.locators.str_delhi_airport_select,10).click()

@given(parsers.cfparse('user navigates to "{hyperlink}"'))
def user_navigates_to_httpswwwbookingcom(hyperlink):
    """user navigates to "https://www.booking.com/"."""
    obj_common.navigate_to_webpage(hyperlink)
    obj_common.dismiss_sign_in_notification_if_exists()




@given('user selects cheapest price and click on See Flights button')
def user_selects_cheapest_price_and_click_on_see_flights_button():
    """user selects cheapest price and click on See Flights button."""
    obj_common.wait_for_element_invisiblity(pytest.locators.str_popup,20)
    obj_common.get_clickable_web_element(pytest.locators.str_cheapest_tab,10).click()
    obj_common.get_clickable_web_element(pytest.locators.str_first_chepest_flight,10).click()





@given('user selects the data 5 days from now')
def user_selects_the_data_5_days_from_now():
    """user selects the data 5 days from now."""
    obj_common.get_clickable_web_element(pytest.locators.str_click_departure_date_chooser).click()
    obj_common.get_clickable_web_element(pytest.locators.str_date_picker.replace("<<text_replace>>",obj_common.get_future_date().strip())).click()




@then('user clicks select button in the pop up')
def user_clicks_select_button_in_the_pop_up():
    """user clicks select button in the pop up."""
    obj_common.get_clickable_web_element(pytest.locators.str_final_select,10).click()

