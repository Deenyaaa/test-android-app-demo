from appium.webdriver.common.appiumby import AppiumBy
from utils.gestures import tap_element_center

class VpnMainPage:
    def __init__(self, driver):
        self.driver = driver

    connect_button_locator = 'app.vpn_app_name:id/onOffVpn'
    servers_list_button_locator = 'app.vpn_app_name:id/tvSelectServer'
    connected_server_name_locator = 'app.vpn_app_name:id/tvServerCountyName'

    def show_servers_list(self):
        element = self.driver.find_element(AppiumBy.ID, self.servers_list_button_locator)
        tap_element_center(self.driver, element)

    def connect(self):
        element = self.driver.find_element(AppiumBy.ID, self.connect_button_locator)
        element.click()

    def get_name_connected_server(self):
        element = self.driver.find_element(AppiumBy.ID, self.connected_server_name_locator)
        return element.text