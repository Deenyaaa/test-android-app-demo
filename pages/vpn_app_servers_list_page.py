from appium.webdriver.common.appiumby import AppiumBy

class ServersListPage:
    def __init__(self, driver):
        self.driver = driver

    all_servers_list_locator = 'androidx.appcompat.widget.LinearLayoutCompat'
    connect_button_locator = 'app.vpn_app_name:id/cvProgressButton'

    def connect_to_server(self):
        element = self.driver.find_element(AppiumBy.ID, self.connect_button_locator)
        element.click()

    def get_count_servers(self):
        return len(self.driver.find_elements(AppiumBy.CLASS_NAME, self.all_servers_list_locator))

    def get_current_server(self, index):
        list_servers = self.driver.find_elements(AppiumBy.CLASS_NAME, self.all_servers_list_locator)
        return list_servers[index]