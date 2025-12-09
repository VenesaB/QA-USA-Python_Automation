from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from data import PHONE_NUMBER
from helpers import retrieve_phone_code


class UrbanRoutesPage:
    FROM_LOCATION = (By.ID,"from")
    TO_LOCATION = (By.ID,"to")
    CALL_TAXI_BUTTON = (By.XPATH, '//button[text()="Call a taxi"]')
    SUPPORTIVE_ICON_LOCATOR = (By.XPATH, '(//div[text()="Supportive"][1])')
    SUPPORTIVE_ACTIVE_LOCATOR = (By.CSS_SELECTOR, '.tcard.active .tcard-title')
    PHONE_NUMBER_LOCATOR = (By.XPATH,'<div class="np-text">Phone number</div>')
    PHONE_NUMBER_FIELD_LOCATOR = (By.CSS_SELECTOR, '.np-button .np-text')
    NEXT_BUTTON = (By.XPATH, '//button[@class="button full" and text()="Next"]')
    PHONE_CODE_LOCATOR = (By.CSS_SELECTOR, '.input-container > #code')
    PHONE_CODE_FIELD = (By.XPATH, '<label for="code" class="label">Enter the code</label>')
    CONFIRM_BUTTON = (By.XPATH, '//button[text()="Confirm"]')
    PAYMENT_LOCATOR = (By.XPATH, '<div class="pp-title">Add card</div>')
    ADD_CARD_LOCATOR = (By.XPATH, '<div class="pp-separator"></div>')
    CARD_NUMBER_LOCATOR = (By.XPATH, '<input type="text" id="number" name="number" placeholder="1234 0000 4321" class="card-input" value="">')
    CARD_CODE_LOCATOR = (By.XPATH, '<input type="text" id="code" name="code" placeholder="12" class="card-input" value="12">')
    LINK_BUTTON_LOCATOR = (By.XPATH, '<button type="submit" class="button full">Link</button>')
    MESSAGE_TO_THE_DRIVER_LOCATOR = (By.XPATH, '<label for="comment" class="label">Message to the driver...</label>')
    MESSAGE_TO_THE_DRIVER_BOX = (By.XPATH, '<input id="comment" class="input" type="text" name="comment" placeholder="Get some whiskey" value="message">')
    BLANKET_SLIDER_LOCATOR = (By.XPATH, '<span class="slider round"></span>')
    ADD_ICE_CREAM_BUTTON_LOCATOR = (By.XPATH, '<div class="counter-plus disabled">+</div>')
    ICE_CREAM_COUNTER_LOCATOR = (By.XPATH, '<div class="counter-value">2</div>')
    ORDER_TAXI_LOCATOR = (By.XPATH, '<button type="button" class="smart-button"><span class="smart-button-main">Order</span><span class="smart-button-secondary">The route will be 1 km. and will take 1 min.</span></button>')
    CAR_SEARCH_BUTTON_LOCATOR = (By.XPATH, 'div class="order-header"><div class="order-header-content"><div class="order-header-title">Car search</div><div class="order-header-time">00:17</div><div class="order-progress visible" style="width: 45.1613%;"></div></div></div>')
    CAR_SEARCH_BUTTON_STATUS = (By.XPATH, '//div[@class="oder-body"]')




    def __init__(self, driver):
          self.driver = driver #Initialize the driver
          self.wait = WebDriverWait(driver, 10) # wait up to 10 seconds

    def   enter_from_location(self, from_text):
          self.driver.find_element(*self.FROM_LOCATION).send_keys(from_text)


    def   get_from(self):
          return self.driver.find_element(*self.FROM_LOCATION).get_attribute("value")

    def   enter_to_location(self, to_text):
          self.driver.find_element(*self.TO_LOCATION).send_keys(to_text)


    def   get_to(self):
          return self.driver.find_element(*self.TO_LOCATION).get_attribute("value")

    def   click_call_taxi_button(self):
          WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.CALL_TAXI_BUTTON)).click()

    def   click_supportive_tariff(self):
          self.driver.find_element(*self.SUPPORTIVE_ICON_LOCATOR).click()

    def   get_supportive_status(self):
          return self.driver.find_element(*self.SUPPORTIVE_ACTIVE_LOCATOR).text

    def   add_phone_number(self):
          self.driver.find_element(*self.PHONE_NUMBER_LOCATOR).click()
          self.driver.find_element(*self.PHONE_NUMBER_LOCATOR).send_keys(PHONE_NUMBER)

    def   send_code(self):
          code = retrieve_phone_code(self.driver)
          self.driver.find_element(*self.PHONE_CODE_LOCATOR).send_keys(code)
          print(code)
          return code

    def   click_confirm_button(self):
          self.driver.find_element(*self.CONFIRM_BUTTON).click()

    def   get_payment_method(self):
          return self.driver.find_element(*self.PAYMENT_LOCATOR).text_attribute("value")

    def   click_add_payment_method(self):
          self.driver.find_element(*self.ADD_CARD_LOCATOR).click()

    def   click_card_number(self):
          self.driver.find_element(*self.CARD_NUMBER_LOCATOR).click()

    def   type_in_card_number(self, number):
          self.driver.find_element(*self.ADD_CARD_LOCATOR).send_keys(number)

    def   click_card_code(self):
          self.driver.find_element(*self.CARD_CODE_LOCATOR).click()

    def   click_link_button(self):
          self.driver.find_element(*self.LINK_BUTTON_LOCATOR).click()

    def   click_message_to_the_driver(self):
          self.driver.find_element(*self.MESSAGE_TO_THE_DRIVER_LOCATOR).click()

    def   click_message_to_the_driver_box(self):
          self.driver.find_element(*self.MESSAGE_TO_THE_DRIVER_BOX).click()

    def   click_blanket_button(self):
          self.driver.find_element(*self.BLANKET_SLIDER_LOCATOR).click()

    def   add_ice_button(self):
          number_of_ice_creams = 2
          for i in range(number_of_ice_creams):
              self.driver.find_element(*self.ADD_ICE_CREAM_BUTTON_LOCATOR).click()

    def   get_ice_cream_count(self):
          return int(self.driver.find_element(*self.ICE_CREAM_COUNTER_LOCATOR).text)

    def   click_order_taxi_button(self):
          self.driver.find_element(*self.ORDER_TAXI_LOCATOR).click()

    def   click_car_search_button(self):
          self.driver.find_element(*self.CAR_SEARCH_BUTTON_LOCATOR).click()

    def   click_car_search(self):
          self.driver.find_element(*self.CAR_SEARCH_BUTTON_STATUS).click()






