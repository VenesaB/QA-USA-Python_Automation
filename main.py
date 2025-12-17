import data
import helpers
from selenium import webdriver
from pages import UrbanRoutesPage

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
           from selenium.webdriver import DesiredCapabilities
           capabilities = DesiredCapabilities.CHROME
           capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
           cls.driver = webdriver.Chrome()
           cls.driver.implicitly_wait(5)
    if     helpers.is_url_reachable(data.URBAN_ROUTES_URL):
           print("Connected to the Urban Routes server")
    else:
           print("Cannot connect to Urban Routes. Check the server is on and still running")

    def    test_set_route(self):
           self.driver.get(data.URBAN_ROUTES_URL)
           routes_page = UrbanRoutesPage(self.driver)
           routes_page.enter_from_location(data.ADDRESS_FROM)
           routes_page.enter_to_location(data.ADDRESS_TO)
           assert routes_page.get_from() == data.ADDRESS_FROM
           assert routes_page.get_to() == data.ADDRESS_TO

    def    test_select_plan(self):
           self.driver.get(data.URBAN_ROUTES_URL)
           routes_page = UrbanRoutesPage(self.driver)
           routes_page.enter_from_location(data.ADDRESS_FROM)
           routes_page.enter_to_location(data.ADDRESS_TO)
           routes_page.click_call_taxi()
           routes_page.click_supportive_tariff()
           assert routes_page.get_supportive_status() == 'Supportive'

    def    test_fill_phone_number(self):
           self.driver.get(data.URBAN_ROUTES_URL)
           routes_page = UrbanRoutesPage(self.driver)
           routes_page.enter_from_location(data.ADDRESS_FROM)
           routes_page.enter_to_location(data.ADDRESS_TO)
           routes_page.click_call_taxi()
           routes_page.click_supportive_tariff()
           routes_page.click_phone_number(data.PHONE_NUMBER)
           routes_page.click_next_button()
           routes_page.send_code()
           routes_page.click_confirm_button()
           assert routes_page.get_saved_phone_number() == data.PHONE_NUMBER


    def    test_fill_card(self):
           self.driver.get(data.URBAN_ROUTES_URL)
           routes_page = UrbanRoutesPage(self.driver)
           routes_page.enter_from_location(data.ADDRESS_FROM)
           routes_page.enter_to_location(data.ADDRESS_TO)
           routes_page.click_call_taxi()
           routes_page.click_supportive_tariff()
           routes_page.click_add_payment_method()
           routes_page.enter_card_number(data.CARD_NUMBER)
           routes_page.type_card_code(data.CARD_CODE)
           routes_page.click_link_button()
           assert routes_page.get_card_number() == data.CARD_NUMBER


    def    test_message_for_driver(self):
           self.driver.get(data.URBAN_ROUTES_URL)
           routes_page = UrbanRoutesPage(self.driver)
           routes_page.enter_from_location(data.ADDRESS_FROM)
           routes_page.enter_to_location(data.ADDRESS_TO)
           routes_page.click_call_taxi()
           routes_page.click_supportive_tariff()
           routes_page.enter_message_to_the_driver(data.MESSAGE_FOR_DRIVER)
           assert routes_page.get_message_to_the_driver() == data.MESSAGE_FOR_DRIVER


    def    test_order_blanket_and_handkerchiefs(self):
           self.driver.get(data.URBAN_ROUTES_URL)
           routes_page = UrbanRoutesPage(self.driver)
           routes_page.enter_from_location(data.ADDRESS_FROM)
           routes_page.enter_to_location(data.ADDRESS_TO)
           routes_page.click_call_taxi()
           routes_page.click_supportive_tariff()

    def    test_order_2_ice_creams(self):
           self.driver.get(data.URBAN_ROUTES_URL)
           routes_page = UrbanRoutesPage(self.driver)
           routes_page.enter_from_location(data.ADDRESS_FROM)
           routes_page.enter_to_location(data.ADDRESS_TO)
           routes_page.click_call_taxi()
           routes_page.click_supportive_tariff()
           routes_page.add_ice_cream_button()
           routes_page.add_ice_cream_button()
           assert routes_page.get_ice_cream_count() == 2

    def    test_car_search_model(self):
           self.driver.get(data.URBAN_ROUTES_URL)
           routes_page: UrbanRoutesPage = UrbanRoutesPage(self.driver)
           routes_page.enter_from_location(data.ADDRESS_FROM)
           routes_page.enter_to_location(data.ADDRESS_TO)
           routes_page.click_call_taxi()
           routes_page.click_supportive_tariff()
           routes_page.enter_message_to_the_driver(data.MESSAGE_FOR_DRIVER)
           routes_page.click_car_search_button()
           assert "Car search" in routes_page.get_car_search()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
