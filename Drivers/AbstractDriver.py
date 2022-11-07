from abc import ABC, abstractmethod
from undetected_chromedriver import Chrome
import random
import time

class AbstractDriver(ABC):
    url: str
    driver: Chrome

    def __init__(self, driver: Chrome):
        self.driver = driver

    @abstractmethod
    def check_for_login(self):
        pass

    def simulate_reaction_time(self):
        r = random.random()
        if r < 0.7:
            time.sleep(random.uniform(0.5374, 0.843))
        else:
            time.sleep(random.uniform(0.8059, 2.9005))
