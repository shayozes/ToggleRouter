# imports
from selenium import webdriver
from selenium.webdriver.support import wait, expected_conditions
from selenium.webdriver.common.by import By
import sys

# globals
__author__ = 'Omri Shayo'
_router_address = r''
_user_name = ''
_password = ''
_driver = webdriver.Chrome(r'E:\ChromeDriver\chromedriver.exe')
_on_off_codes = {'on': 'Enabled', 'off': 'Disabled'}
_wanted_router_status = ''
_apply_button_selector = 'input[value=Apply]'


def main():
    init_driver()
    login_into_router()

    # go to wireless tab
    _driver.get(r'http://x.x.x.x/wlanBasicSecurity.asp')

    toggle_wireless()
    _driver.find_element_by_css_selector(_apply_button_selector).click()

    wait = wait.WebDriverWait(_driver, 15)

    if _wanted_router_status == _on_off_codes['off']:
        wait.until(expected_conditions.alert_is_present())
        _driver.switch_to.alert.accept()

    wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, _apply_button_selector)))
    _driver.quit()


def init_driver():
    global _driver
    _driver.get(_router_address)


def login_into_router():
    _driver.find_element_by_name('loginUsername').send_keys(_user_name)
    pass_input = _driver.find_element_by_name('loginPassword')
    pass_input.send_keys(_password)
    pass_input.submit()


def toggle_wireless():
    _driver.find_element_by_name('WirelessEnable1').send_keys(_wanted_router_status)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        _wanted_router_status = _on_off_codes[raw_input('on/off?')]
    else:
        _wanted_router_status = _on_off_codes[sys.argv[1]]
    main()



