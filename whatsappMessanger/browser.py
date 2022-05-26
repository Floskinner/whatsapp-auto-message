import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager

from whatsappMessanger.tools import load_storage
from whatsappMessanger.tools import print_qr_to_terminal_from_image
from whatsappMessanger.tools import save_storage


class Browser:
    """This is the chrome browser to interact with whatsapp"""

    def __init__(self):
        options = self._get_options()
        self.__driver = webdriver.Firefox(
            executable_path=GeckoDriverManager().install(), options=options
        )
        self.__phone_connected = False

    def send_message(self, target: str, msg: str):
        """Send the message to the given name. You need to be connected with whatsapp in the brwoser and your phone.

        Args:
            target (str): Name of the target person
            msg (str): message to send

        Raises:
            Exception: If you are not connected with your phone
        """
        if self.__phone_connected:
            self._open_whatsapp()
            self._open_target(target)
            input_field = self._write_message(msg)
            input_field.send_keys(Keys.ENTER)
            time.sleep(10)
            self._close_whatsapp()
        else:
            raise Exception("First connect the Phone with `connect_phone()`!")

    def connect_phone(self) -> bool:
        """Create "QR_Code.png" to scan OR you just go to the browser. The image is only 20sec valid.

        Returns:
            bool: If the "Scan me" is no longer on the screen return True. Otherwise False
        """
        self._open_whatsapp()
        try:
            qr_code = self._check_if_available('//canvas[@aria-label="Scan me!"]')
        except TimeoutException:
            return False

        if qr_code.screenshot("QR_Code.png"):
            print_qr_to_terminal_from_image("QR_Code.png")
            self._check_if_no_longer_available('//canvas[@aria-label="Scan me!"]')
            self._save_local_storage()
            self.__phone_connected = True
            return True
        return False

    def _open_whatsapp(self):
        self.__driver.get("https://web.whatsapp.com/")
        # self._load_local_storage()

    def _close_whatsapp(self):
        self._save_local_storage()
        self.__driver.get("https://www.google.com/")
        time.sleep(10)

    def _open_target(self, target: str):
        person = self._check_if_available(f'//span[contains(@title, "{target}")]')
        person.click()

    def _write_message(self, msg) -> WebElement:
        input_field = self._check_if_available('//div[@title="Schreib eine Nachricht"]')
        input_field.send_keys(msg)
        return input_field

    def _check_if_available(self, xpath: str) -> WebElement:
        return WebDriverWait(self.__driver, timeout=120).until(
            lambda driver: driver.find_element_by_xpath(xpath)
        )

    def _check_if_no_longer_available(self, xpath: str):
        WebDriverWait(self.__driver, timeout=120).until_not(
            lambda driver: driver.find_element_by_xpath(xpath)
        )

    def _save_local_storage(self):
        storage: dict = self.__driver.execute_script("return window.localStorage;")
        save_storage(storage)

    def _load_local_storage(self):
        # BUG: After closing the application it does not work
        storage = load_storage()
        if storage is not None:
            for key, value in storage.items():
                self.__driver.execute_script(
                    f"window.localStorage.setItem('{key}','{value}');"
                )
            self.__driver.refresh()

        else:
            self.connect_phone()

    def _get_options(self) -> Options:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        return options

    def __del__(self):
        self.__driver.close()
