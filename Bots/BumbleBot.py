import cv2
from pprint import pprint
from colorama import Fore
from deepface import DeepFace
from Drivers.BumbleDriver import BumbleDriver
from Bots.AbstractBot import AbstractBot

class BumbleBot(AbstractBot):
    driver: BumbleDriver
    preferences: dict

    def __init__(self, driver: BumbleDriver, preferences: dict, temp_path: str):
        self.driver = driver
        self.preferences = preferences
        self.temp_path = temp_path

    def _meets_preferences(self, analysis: dict):
        if analysis['dominant_race'] not in self.preferences['races']:
            return False
        if analysis['gender'] not in self.preferences['genders']:
            return False
        return True
