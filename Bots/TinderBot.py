from deepface import DeepFace
from pprint import pprint
from colorama import Fore
import cv2

from Drivers.TinderDriver import TinderDriver
from Bots.AbstractBot import AbstractBot

class TinderBot(AbstractBot):
    driver: TinderDriver
    # analyzer: Analyzer 
    preferences: dict 

    def __init__(self, driver: TinderDriver, preferences: dict, temp_path: str):
        self.driver = driver
        self.preferences = preferences
        self.temp_path = temp_path

    def _meets_preferences(self, analysis: dict):
        if analysis['dominant_race'] not in self.preferences['races']:
            return False
        if analysis['gender'] not in self.preferences['genders']:
            return False
        return True
