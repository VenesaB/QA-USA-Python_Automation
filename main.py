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
         routes_page.enter_from_location(data.ADDRESS_FROM)
         routes_page.enter_to_location(data.ADDRESS_TO)
         assert routes_page.get_from() == data.ADDRESS_FROM
         assert routes_page.get_to() == data.ADDRESS_TO


    def  test_select_plan(self):
         self.driver.get(data.URBAN_ROUTES_URL)
         routes_page = UrbanRoutesPage(self.driver)
         routes_page.enter_to_location(data.ADDRESS_FROM)
         routes_page.enter_to_location(data.ADDRESS_TO)
         routes_page.click_call_taxi_button()
         routes_page.click_supportive_tariff()
         assert routes_page.get_supportive_status() == 'Supportive'

    def  test_fill_phone_number(self):
         self.driver.get(data.URBAN_ROUTES_URL)
         routes_page = UrbanRoutesPage(self.driver)
         routes_page.enter_to_location(data.ADDRESS_FROM)
         routes_page.enter_to_location(data.ADDRESS_TO)
         routes_page.click_call_taxi_button()
         routes_page.click_supportive_tariff()
         routes_page.add_phone_number()
         assert routes_page.add_phone_number() == data.PHONE_NUMBER


    def  test_fill_card(self):
         self.driver.get(data.URBAN_ROUTES_URL)
         routes_page = UrbanRoutesPage(self.driver)
         routes_page.enter_to_location(data.ADDRESS_FROM)
         routes_page.enter_to_location(data.ADDRESS_TO)
         routes_page.click_call_taxi_button()
         routes_page.click_supportive_tariff()
         routes_page.click_add_payment_method()
         card_number_value = self.driver.find_element('*routes_page.card_number').get_attribute("value")
         card_cvv_value = self.driver.find_element('*routes_page.card_CVV').get_attribute("value")
         assert routes_page.get_payment_method() == "Card"


    def  test_car_search_model(self):
         self.driver.get(data.URBAN_ROUTES_URL)
         routes_page: UrbanRoutesPage = UrbanRoutesPage(self.driver)
         routes_page.enter_to_location(data.ADDRESS_FROM)
         routes_page.enter_to_location(data.ADDRESS_TO)
         routes_page.click_call_taxi_button()
         routes_page.click_supportive_tariff()
         routes_page.click_car_search_button()
         comment_text = data.MESSAGE_FOR_DRIVER
         routes_page.click_car_search_button()



    def  test_order_blanket_and_handkerchiefs(self):
         self.driver.get(data.URBAN_ROUTES_URL)
         routes_page = UrbanRoutesPage(self.driver)
         routes_page.enter_from_location(data.ADDRESS_FROM)
         routes_page.enter_to_location(data.ADDRESS_TO)
         routes_page.click_call_taxi_button()
         routes_page.click_supportive_tariff()
         routes_page.click_car_search_button()


    def  test_order_2_ice_creams(self):
         self.driver.get(data.URBAN_ROUTES_URL)
         routes_page = UrbanRoutesPage(self.driver)
         routes_page.enter_from_location(data.ADDRESS_FROM)
         routes_page.enter_to_location(data.ADDRESS_TO)
         routes_page.click_call_taxi_button()
         routes_page.click_supportive_tariff()
         routes_page.add_ice_button(count=2)
         assert routes_page.get_ice_cream_count() == 2
         number_of_ice_creams = 2  # Define a variable for the number of iterations

    def  test_car_search_model_appears(self):
         self.driver.get(data.URBAN_ROUTES_URL)
         routes_page = UrbanRoutesPage(self.driver)
         routes_page.enter_from_location(data.ADDRESS_FROM)
         routes_page.enter_to_location(data.ADDRESS_TO)
         routes_page.click_call_taxi_button()
         routes_page.click_supportive_tariff()
         routes_page.click_car_search_button()

    @classmethod

    def  teardown_class(cls):
         cls.driver.quit()