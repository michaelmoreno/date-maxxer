import cv2
from pprint import pprint
from colorama import Fore
from deepface import DeepFace
from Drivers.BumbleDriver import BumbleDriver


class BumbleBot:
    driver: BumbleDriver
    preferences: dict

    def __init__(self, driver: BumbleDriver, preferences: dict):
        self.driver = driver
        self.preferences = preferences

    def analyze(self, image: bytes): # find better way to orchestrate UI outputting
        with open("temp/bumble.png", "wb") as f:
            f.write(image)
        cv2.imshow('Bumble', cv2.imread('temp/bumble.png'))
        cv2.waitKey(1)
        print("Scanning photo..." + Fore.RESET)
        try:
            analysis = DeepFace.analyze("temp/bumble.png", actions = ['race', 'gender'])
            print(Fore.GREEN + 'Analysis:')
            pprint(analysis)
            print(Fore.RESET)
            return analysis
        except:
            print(Fore.YELLOW + "No face detected, trying next photo..." + Fore.RESET)
            return None

    def attempt_analysis(self, attempts: int = 4):
        for _ in range(attempts):
            image = self.driver.get_image()
            analysis = self.analyze(image)
            if analysis:
                return analysis
            self.driver.next_picture()

    def _meets_preferences(self, analysis: dict):
        if analysis['dominant_race'] not in self.preferences['races']:
            return False
        if analysis['gender'] not in self.preferences['genders']:
            return False
        return True

    def run(self):
        self.driver.check_for_login()
        while True:
            self.driver.handle_popup()
            analysis = self.attempt_analysis()
            self.driver.like()
            if analysis and self._meets_preferences(analysis):
                self.driver.like()
            else:
                self.driver.dislike()
        