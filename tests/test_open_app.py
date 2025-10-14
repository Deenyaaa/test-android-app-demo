import os
import logging
from pages.vpn_app_main_page import VpnMainPage
from utils.wait_helpers import wait_for_visibility


def test_open_vpn_app(appium_driver, start_app):
    vpn_app_page = VpnMainPage(appium_driver)
    vpn_app_package_name = os.getenv("APP_PACKAGE_NAME_VPN")
    try:
        start_app(vpn_app_package_name)
        wait_for_visibility(appium_driver, vpn_app_page.connect_button_locator)

    except Exception as e:
        logging.error(f"Ошибка при запуске приложения: {e}")

    assert appium_driver.find_element(vpn_app_page.connect_button_locator).is_displayed()