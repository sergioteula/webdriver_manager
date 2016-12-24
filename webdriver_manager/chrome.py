import os

from webdriver_manager.driver import ChromeDriver
from webdriver_manager.manager import DriverManager


class ChromeDriverManager(DriverManager):
    def __init__(self, version="latest",
                 name="chromedriver",
                 url="http://chromedriver.storage.googleapis.com"):
        DriverManager.__init__(self)
        self.driver = ChromeDriver(driver_url=url, name=name, version=version)

    def install(self, to_folder=".drivers"):
        path = self._file_manager.download_driver(self.driver, to_folder)
        os.chmod(path, 0755)
        return path