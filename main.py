import time
from selenium.webdriver.common.devtools.v127 import page
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
    if   helpers.is_url_reachable(data.URBAN_ROUTES_URL):
         print("Connected to the Urban Routes server")
    else:
         print("Cannot connect to Urban Routes. Check the server is on and still running")

    def  test_set_route(self):
         self.driver.get(data.URBAN_ROUTES_URL)
         routes_page = UrbanRoutesPage(self.driver)
         routes_page.enter_from_location('data.ADDRESS_FROM, data.ADDRESS_TO')
         assert routes_page.get_from() == data.ADDRESS_FROM
         assert routes_page.get_to() == data.ADDRESS_TO


    def  test_select_plan(self):
         self.driver.get(data.URBAN_ROUTES_URL)
         routes_page = UrbanRoutesPage(self.driver)
         routes_page.enter_to_location('data.ADDRESS_FROM, data.ADDRESS_TO')
         routes_page.click_call_taxi()
         routes_page.click_supportive_tariff()
         assert routes_page.get_supportive_status() == 'Supportive'

    def  test_fill_phone_number(self):
         self.driver.get(data.URBAN_ROUTES_URL)
         routes_page = UrbanRoutesPage(self.driver)
         routes_page.enter_to_location('data.ADDRESS_FROM, data.ADDRESS_TO')
         routes_page.click_call_taxi()
         routes_page.click_supportive_tariff()
         routes_page.add_phone_number()
         code = retrieve_phone_code(self.driver)
         print(f"Received code: {code}")
         assert routes_page.add_phone_number() == data.PHONE_NUMBER


    def  test_fill_card(self):
         self.driver.get(data.URBAN_ROUTES_URL)
         routes_page = UrbanRoutesPage(self.driver)
         routes_page.enter_to_location('data.ADDRESS_FROM, data.ADDRESS_TO')
         routes_page.click_call_taxi()
         routes_page.click_supportive_tariff()
         routes_page.click_add_payment_method()
         card_number_value = self.driver.find_element('*routes_page.card_number').get_attribute("value")
         card_cvv_value = self.driver.find_element('*routes_page.card_CVV').get_attribute("value")
         assert card_cvv_value == data.CARD_CODE


    def  test_car_search_model(self):
         self.driver.get(data.URBAN_ROUTES_URL)
         routes_page: UrbanRoutesPage = UrbanRoutesPage(self.driver)
         routes_page.enter_to_location('data.ADDRESS_FROM, data.ADDRESS_TO')
         routes_page.click_call_taxi()
         routes_page.click_supportive_tariff()
         routes_page.click_car_search_button()
         comment_text = data.MESSAGE_FOR_DRIVER
         routes_page.click_car_search_button()
         assert routes_page.get_comment_value() == comment_text


    def  test_order_blanket_and_handkerchiefs(self):
         self.driver.get(data.URBAN_ROUTES_URL)
         routes_page = UrbanRoutesPage(self.driver)
         routes_page.enter_from_location('data.ADDRESS_FROM, data.ADDRESS_TO')
         routes_page.click_call_taxi()
         routes_page.click_supportive_tariff()
         routes_page.order_blanket_and_handkerchiefs()
         assert routes_page.check_blanket_and_handkerchiefs(), "The blanket and handkerchiefs switch is not checked"

    def  test_order_2_ice_creams(self):
         self.driver.get(data.URBAN_ROUTES_URL)
         routes_page = UrbanRoutesPage(self.driver)
         routes_page.enter_from_location('data.ADDRESS_FROM, data.ADDRESS_TO')
         routes_page.click_call_taxi()
         routes_page.click_supportive_tariff()
         routes_page.click_order_requirement()
         routes_page.add_ice_cream(count=2)
         assert routes_page.get_ice_cream_count() == 2
         number_of_ice_creams = 2  # Define a variable for the number of iterations
    for  ice_cream in range('number_of_ice_cream'):


    def  test_car_search_model_appears(self):
         self.driver.get(data.URBAN_ROUTES_URL)
         routes_page = UrbanRoutesPage(self.driver)
         routes_page.enter_from_location('data.ADDRESS_FROM, data.ADDRESS_TO')
         routes_page.click_call_taxi()
         routes_page.click_supportive_tariff()
         routes_page.click_car_search_button()

        @classmethod
    def  teardown_class(cls):
         cls.driver.quit()