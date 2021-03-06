from selenium.webdriver.chrome.webdriver import WebDriver

from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.session = GroupHelper(self)


    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost:81/addressbook/")

    def destroy(self):
        self.wd.quit()
