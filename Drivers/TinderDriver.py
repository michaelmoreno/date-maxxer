import time
import random
import cv2
from undetected_chromedriver import Chrome
from deepface import DeepFace
from colorama import Fore
from pprint import pprint

from Drivers.AbstractDriver import AbstractDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys


class TinderDriver(AbstractDriver):
    url: str = "https://tinder.com"
    driver: Chrome

    def __init__(self, driver: Chrome, preferences: dict):
        super().__init__(driver, preferences)

    def check_for_login(self):
        self.driver.get(self.url)

    def get_image(self):
        xpath = '//*[@id="o-2124353878"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div[1]/div[1]'
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath)))

            time.sleep(0.3)
            element = self.driver.find_element(By.XPATH, xpath)

        except TimeoutException:
            return None
        
        return element.screenshot_as_png

    def like(self):
        self.simulate_reaction_time()
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.RIGHT)

    def dislike(self):
        self.simulate_reaction_time()
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.LEFT)

    def handle_popup(self):
        try:
            self.driver.find_element(By.XPATH, '//*[@id="o442232342"]/main')
            time.sleep(random.uniform(0.4374, 0.943))
            print(Fore.GREEN + "Popup detected, closing..." + Fore.RESET)
            # self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
            close_btn = self.driver.find_element(By.XPATH, '//*[@id="o442232342"]/main/div/div/div[3]/button[2]/span')
            close_btn.click()
        except:
            pass

    def next_picture(self):
        time.sleep(random.uniform(0.1, 0.3))
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.SPACE)
    
    def _meets_preferences(self, analysis: dict) -> bool:
        if analysis['dominant_race'] not in self.preferences['races']:
            return False
        if analysis['gender'] not in self.preferences['genders']:
            return False
        return True

    def analyze_face(self, attempts: int = 4):
        bytes = self.get_image()
        with open("temp/tinder.png", "wb") as f:
            f.write(bytes) # type: ignore
        cv2.imshow('Tinder', cv2.imread('temp/tinder.png'))
        cv2.waitKey(1)
        print("Scanning photo..." + Fore.RESET)
        try:
            
            analysis = DeepFace.analyze("temp/tinder.png", actions = ['race', 'gender'])
            print(Fore.GREEN + 'Analysis:')
            pprint(analysis)
            print(Fore.RESET)
            if self._meets_preferences(analysis):
                self.like()
            else:
                self.dislike()
            return
        except:
            print(Fore.YELLOW + "No face detected, trying next photo..." + Fore.RESET)
            self.next_picture()
            if attempts > 0:
                self.analyze_face(attempts - 1)
            else:
                print(Fore.RED + "No faces detected, skipping profile" + Fore.RESET)
                self.dislike()

    def run(self):
        while True:
            self.handle_popup()
            self.analyze_face()
