import os
import pytest
import logging
from appium import webdriver
from appium.options.android import UiAutomator2Options

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    filename='logs/test.log',
    filemode='a'
)

@pytest.fixture(scope="session")
def appium_driver():
    """
    Создаёт сессию Appium для Android-устройства
    """
    desired_capabilities = {
        "platformName": os.getenv('ANDROID_PLATFORM_NAME'),
        "platformVersion": os.getenv("ANDROID_PLATFORM_VERSION"),
        "deviceName": os.getenv("ANDROID_DEVICE_NAME"),
        "automationName": "UiAutomator2",
        "noReset": True,
        "forceAppLaunch": True
    }

    options = UiAutomator2Options().load_capabilities(desired_capabilities)
    appium_server_url = os.getenv("APPIUM_SERVER_URL")

    logging.info(f"Создаём сессию Appium: сервер={appium_server_url}, устройство={desired_capabilities['deviceName']}")

    try:
        driver = webdriver.Remote(appium_server_url, options=options)
        logger.info("Сессия Appium успешно создана")
    except Exception as e:
        logger.error(f"Не удалось подключиться к Appium: {e}")
        pytest.exit(f"Не удалось подключиться к Appium: {e}")

    yield driver

    logging.info("Завершаем сессию Appium")
    driver.quit()

@pytest.fixture
def start_app(appium_driver):
    """
    Фикстура для активации приложений по package name
    """
    def _start_app(package_name: str):
        logging.info(f"Запуск приложения: {package_name}")
        appium_driver.activate_app(package_name)
    return _start_app

@pytest.fixture
def close_app(appium_driver):
    """
    Фикстура для закрытия приложений по package name
    """
    def _close_app(package_name: str):
        logging.info(f"Закрываем приложение: {package_name}")
        appium_driver.terminate_app(package_name)
    return _close_app
