import time
from typing import List

from undetected_chromedriver import Chrome
from Drivers.AbstractDriver import AbstractDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
    

class BumbleDriver(AbstractDriver):
    url: str = "https://bumble.com/app"
    driver: Chrome
    _profile_container: WebElement
    _current_images: List[WebElement]

    def __init__(self, driver: Chrome):
        super().__init__(driver)

    @property
    def profile_container(self):
        if hasattr(self, "_profile_container"):
            return self._profile_container
        return self.get_profile_container()
        
    @property
    def current_images(self):
        if hasattr(self, "_current_images"):
            return self._current_images
        return self.get_images()

    def get_profile_container(self):
        try:
            WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located((By.CLASS_NAME, "encounters-album"))) 
                
            self._profile_container = self.driver.find_element(By.CLASS_NAME, "encounters-album")
            return self._profile_container

        except TimeoutException:
            raise TimeoutException("Could not find profile container")

    def get_images(self):
        self._current_images = self.profile_container.find_elements(By.CLASS_NAME, "media-box__picture-image")
        return self._current_images

    def check_for_login(self):
        self.driver.get(self.url)

    def scrape_badges(self) -> dict:
        about = {}
        try:
            WebDriverWait(self.driver, 0.5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "pill__image")))

        except TimeoutException:
            return {}

        badges = self.driver.find_elements(By.CLASS_NAME, "pill__image")
        for badge in badges:
            key = badge.get_attribute("src").split('_')[-1].split('v2')[0]
            value = badge.get_attribute("alt")
            about[key] = value
        return about

    def in_view(self, element: WebElement) -> bool:
        element_midpoint = element.location['y'] + (element.size['height'] / 2)
        container_top = self.profile_container.location['y']
        container_bottom = self.profile_container.location['y'] + self.profile_container.size['height']

        return container_top < element_midpoint < container_bottom

    def get_image(self) -> bytes:
        for image in self.current_images:
            if self.in_view(image):
                return image.screenshot_as_png
        raise Exception("Could not find image")
        
    def like(self):
        self.simulate_reaction_time()
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.RIGHT)
        self._profile_container = self.get_profile_container()
        self._current_images = self.get_images()
        time.sleep(0.4)
    
    def dislike(self):
        self.simulate_reaction_time()
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.LEFT)
        self._profile_container = self.get_profile_container()
        self._current_images = self.get_images()
        time.sleep(0.5)

    def next_picture(self):
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.DOWN)
        time.sleep(.5)
        if not any([self.in_view(image) for image in self.current_images]):
            self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.DOWN)
            time.sleep(0.5)

    def detect_match(self):
        try: 
            self.driver.find_element(By.XPATH, '//*[@id="main"]/div/div[1]/main/div[2]/article/div')
        except: 
            return False

    # def handle_match(self): 
    #     if self.detect_match():
    #         print('-----------------MATCH-----------------')
    #         xpath = input('Enter xpath: ')
    #         while xpath != 'q':
    #             try:
    #                 escape = self.driver.find_element(By.XPATH, xpath)
    #         # escape = self.driver.find_element(By.XPATH, '//*[@id="main"]/div/div[1]/main/div[2]/article/div/footer/div[2]/div[2]/div')
    #                 self.simulate_reaction_time()
    #                 escape.click()
    #             except:
    #                 print('Invalid xpath')
    #             xpath = input('Enter xpath: ')

    def handle_popup(self):
        ...
        # self.handle_match()
