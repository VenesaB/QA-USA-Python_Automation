import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from trio import sleep

from data import PHONE_NUMBER
from helpers import retrieve_phone_code


class UrbanRoutesPage:

    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    CALL_TAXI_LOCATOR = (By.XPATH, '//button[text()="Call a taxi"]')
    SUPPORTIVE_ICON_LOCATOR = (By.XPATH, '(//div[text()="Supportive"][1])')
    SUPPORTIVE_ACTIVE_LOCATOR = (By.CSS_SELECTOR, '.tcard.active .tcard-title')
    PHONE_NUMBER_LOCATOR = (By.XPATH,'//div[@class="np-text"]')
    PHONE_NUMBER_FIELD_LOCATOR = (By.CSS_SELECTOR, '.np-button .np-text')
    PHONE_NUMBER_FIELD = (By.XPATH, '<label for="phone" class="label">Phone number</label>')
    PHONE_KEYS_FIELD = (By.ID, 'phone')
    NEXT_BUTTON = (By.XPATH, '//button[@class="button full" and text()="Next"]')
    PHONE_CODE_LOCATOR = (By.CSS_SELECTOR, '.input-container > #code')
    PHONE_CODE_FIELD = (By.XPATH, '<label for="code" class="label">Enter the code</label>')
    CONFIRM_BUTTON = (By.XPATH, '//button[text()="Confirm"]')
    PAYMENT_LOCATOR = (By.CLASS_NAME, 'pp-value-text')
    ADD_CARD_LOCATOR = (By.CLASS_NAME, 'pp-plus')
    CARD_NUMBER_LOCATOR = (By.ID, 'number')
    CARD_NUMBER_INPUT = (By.XPATH, '//div[@class="card-number"]//div//input')
    CARD_CODE_INPUT = (By.CSS_SELECTOR, '#code.card-input')
    CARD_CODE_LOCATOR = (By.CSS_SELECTOR, '#code.card-input')
    CLICK_OUT_OF_BOX = (By.XPATH, '//div[text()="Adding a card"]')
    LINK_BUTTON_LOCATOR = (By.CSS_SELECTOR, "button.button.full.disabled")
    PAYMENT_CLOSE_BUTTON = (By.XPATH, '//div[text()="Payment method"]/preceding-sibling::button[@class="close-button section-close"]')
    MESSAGE_TO_THE_DRIVER_LOCATOR = (By.ID, "comment")
    MESSAGE_TO_THE_DRIVER_BOX = (By.XPATH, '<input id="comment" class="input" type="text" name="comment" placeholder="Message to driver value="message">')
    BLANKET_SLIDER_LOCATOR = (By.XPATH, '//div[text()="Blanket and handkerchiefs"]/following-sibling::div//input')
    BLANKET_SLIDER_STATUS = (By.XPATH, '<span class="slider round"></span>')
    ADD_ICE_CREAM_BUTTON_LOCATOR = (By.CSS_SELECTOR, "div.counter-plus")
    ICE_CREAM_COUNTER_LOCATOR = (By.XPATH, "//div[contains(@class,'counter-value')]")
    ORDER_TAXI_LOCATOR = (By.XPATH, '<button type="button" class="smart-button"><span class="smart-button-main">Order</span><span class="smart-button-secondary">The route will be 1 km. and will take 1 min.</span></button>')
    CAR_SEARCH_BUTTON_LOCATOR = (By.CSS_SELECTOR, "button.smart-button")
    CAR_SEARCH_BUTTON_STATUS = (By.XPATH, '//div[@class="oder-body"]')
    CAR_SEARCH_HEADER = (By.CSS_SELECTOR, "div.order-header-content")

    def     __init__(self, driver):
            self.driver = driver  # Initialize the driver
            self.wait = WebDriverWait(driver, 10)  # wait up to 10 seconds

    def     enter_from_location(self, from_text):
            self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)

    def     get_from(self):
            return self.driver.find_element(*self.FROM_LOCATOR).get_attribute("value")

    def     enter_to_location(self, to_text):
            self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)

    def     get_to(self):
            return self.driver.find_element(*self.TO_LOCATOR).get_attribute("value")

    def     click_call_taxi(self):
            self.driver.find_element(*self.CALL_TAXI_LOCATOR).click()

    def     click_supportive_tariff(self):
            self.driver.find_element(*self.SUPPORTIVE_ICON_LOCATOR).click()

    def     get_supportive_status(self):
            return self.driver.find_element(*self.SUPPORTIVE_ACTIVE_LOCATOR).text

    def     click_phone_number(self, number):
            self.driver.find_element(*self.PHONE_NUMBER_LOCATOR).click()
            self.driver.find_element(*self.PHONE_KEYS_FIELD).send_keys(number)


    def     add_phone_number(self):
            self.driver.find_element(*self.PHONE_NUMBER_LOCATOR).click()
            self.driver.find_element(*self.PHONE_NUMBER_LOCATOR).send_keys(PHONE_NUMBER)

    def     get_phone_number(self):
            return self.driver.find_element(*self.PHONE_NUMBER_LOCATOR).get_attribute("value")

    def     enter_phone_number(self,number):
            self.driver.find_element(*self.PHONE_NUMBER_FIELD).send_keys(number)

    def     click_phone_code(self):
            self.driver.find_element(*self.PHONE_CODE_LOCATOR).click()

    def     enter_phone_code(self, code):
            self.driver.find_element(*self.PHONE_CODE_LOCATOR).send_keys(code)

    def     click_phone_confirm(self):
            code = retrieve_phone_code(self.driver)
            self.driver.find_element(*self.PHONE_CODE_LOCATOR).send_keys(code)
            print(code)
            return code

    def     enter_phone_confirm(self, code):
            self.driver.find_element(*self.PHONE_CODE_LOCATOR).send_keys(code)

    def     click_confirm_button(self):
            self.driver.find_element(*self.CONFIRM_BUTTON).click()

    def     click_next_button(self):
            self.driver.find_element(*self.NEXT_BUTTON).click()

    def     get_saved_phone_number(self):
            return self.driver.find_element(*self.PHONE_NUMBER_LOCATOR).text

    def     get_payment_method(self):
            return self.driver.find_element(*self.PAYMENT_LOCATOR).click

    def     click_add_payment_method(self):
            self.driver.find_element(*self.PAYMENT_LOCATOR).click()
            time.sleep(2)
            self.driver.find_element(*self.ADD_CARD_LOCATOR).click()

    def     click_card_number(self):
            self.driver.find_element(*self.ADD_CARD_LOCATOR).click()

    def     type_card_number(self, number):
            self.driver.find_element(*self.ADD_CARD_LOCATOR).send_keys(number)

    def     enter_card_number(self, number):
            self.driver.find_element(*self.CARD_NUMBER_INPUT).send_keys(number)

    def     get_card_number(self):
            return self.driver.find_element(*self.CARD_NUMBER_LOCATOR).get_attribute("value")

    def     click_card_code(self):
            self.driver.find_element(*self.CARD_NUMBER_INPUT).click()

    def     type_card_code(self, code):
            self.driver.find_element(*self.CARD_CODE_INPUT).send_keys(code)
            self.driver.find_element(*self.CARD_CODE_INPUT).send_keys(Keys.TAB)

    def     click_enter_card_code(self):
            self.driver.find_element(*self.CARD_CODE_LOCATOR).click()

    def     send_code(self):
            code = retrieve_phone_code(self.driver)
            self.driver.find_element(*self.PHONE_CODE_LOCATOR).send_keys(code)
            print(code)
            return code


    def     click_link_button(self):
            self.driver.find_element(*self.LINK_BUTTON_LOCATOR).click()

    def     click_message_to_the_driver_box(self):
            self.driver.find_element(*self.MESSAGE_TO_THE_DRIVER_BOX).click()

    def     enter_message_to_the_driver(self,message):
            self.driver.find_element(*self.MESSAGE_TO_THE_DRIVER_LOCATOR).send_keys(message)

    def     get_message_to_the_driver(self):
            return self.driver.find_element(*self.MESSAGE_TO_THE_DRIVER_LOCATOR).get_attribute("value")


    def     click_blanket_button(self):
            self.driver.find_element(*self.BLANKET_SLIDER_LOCATOR).click()

    def     add_ice_cream_button(self):
            self.driver.find_element(*self.ADD_ICE_CREAM_BUTTON_LOCATOR).click()

    def     get_ice_cream_count(self):
            return int(self.driver.find_element(*self.ICE_CREAM_COUNTER_LOCATOR).text)

    def     click_order_taxi_button(self):
            self.driver.find_element(*self.ORDER_TAXI_LOCATOR).click()

    def     click_car_search_button(self):
            self.driver.find_element(*self.CAR_SEARCH_BUTTON_LOCATOR).click()

    def     click_car_search(self):
            self.driver.find_element(*self.CAR_SEARCH_BUTTON_STATUS).click()

    def     get_car_search(self):
            return self.driver.find_element(*self.CAR_SEARCH_HEADER).text












