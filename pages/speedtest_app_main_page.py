from appium.webdriver.common.appiumby import AppiumBy

class SpeedtestMainPage:
    def __init__(self, driver):
        self.driver = driver

    start_button_locator = 'org.zwanoo.android.speedtest:id/go_button'
    id_test_locator = 'org.zwanoo.android.speedtest:id/test_result_id_text'
    result_download_speed_locator = '//*[@resource-id="org.zwanoo.android.speedtest:id/download_result_view"]//*[@resource-id="org.zwanoo.android.speedtest:id/txt_test_result_value"]'
    result_ping_locator = '//*[@resource-id="org.zwanoo.android.speedtest:id/resultsIconValueViewContainer"]//*[@resource-id="org.zwanoo.android.speedtest:id/txt_test_result_value"]'

    def start_checking(self):
        self.driver.find_element(AppiumBy.ID, self.start_button_locator).click()

    def get_speed(self):
        return self.driver.find_element(AppiumBy.XPATH, self.result_download_speed_locator).text

    def get_ping(self):
        return self.driver.find_element(AppiumBy.XPATH, self.result_ping_locator).text