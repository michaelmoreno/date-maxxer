from abc import ABC, abstractmethod
from undetected_chromedriver import Chrome
import random
import time

class AbstractDriver(ABC):
    url: str
    driver: Chrome
    preferences: dict

    def __init__(self, driver: Chrome, preferences: dict):
        self.driver = driver
        self.preferences = preferences

    @abstractmethod
    def check_for_login(self):
        pass

    @abstractmethod
    def like(self):
        ...

    @abstractmethod
    def dislike(self):
        ...

    @abstractmethod
    def handle_popup(self):
        ...

    def simulate_reaction_time(self):
        r = random.random()
        if r < 0.7:
            time.sleep(random.uniform(0.5374, 0.843))
        else:
            time.sleep(random.uniform(0.8059, 2.9005))
