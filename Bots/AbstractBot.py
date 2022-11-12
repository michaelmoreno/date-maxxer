from abc import ABC, abstractmethod
from deepface import DeepFace
import cv2
from pprint import pprint
from colorama import Fore

from Drivers.AbstractDriver import AbstractDriver

class AbstractBot(ABC):
    driver: AbstractDriver
    preferences: dict
    temp_path: str

    def __init__(self, driver: AbstractDriver, preferences: dict, temp_path: str):
        self.driver = driver
        self.preferences = preferences
        self.temp_path = temp_path

    @abstractmethod
    def _meets_preferences(self, analysis: dict):
        ...

    def analyze(self, image: bytes): # find better way to orchestrate UI outputting
        with open(self.temp_path, "wb") as f:
            f.write(image)
            cv2.imshow('Bumble', cv2.imread(self.temp_path))
            cv2.waitKey(1)
            print("Scanning photo..." + Fore.RESET)
            try:
                analysis = DeepFace.analyze(self.temp_path, actions = ['race', 'gender'])
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

    def run(self):
        self.driver.check_for_login()
        while True:
            self.driver.handle_popup()
            analysis = self.attempt_analysis()
            if analysis and self._meets_preferences(analysis):
                self.driver.like()
            else:
                self.driver.dislike()