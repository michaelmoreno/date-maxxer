from abc import ABC, abstractmethod
from undetected_chromedriver import Chrome

class AbstractDriver(ABC):
    url: str
    driver: Chrome

    def __init__(self, driver: Chrome):
        self.driver = driver

    @abstractmethod
    def check_for_login(self):
        pass