import os
import logging
from pages.speedtest_app_main_page import SpeedtestMainPage
from pages.vpn_app_main_page import VpnMainPage
from pages.vpn_app_servers_list_page import ServersListPage
from models.report import Report
from utils.reporter import save_report_to_file
from utils.wait_helpers import wait_for_visibility, wait_for_clickable

def test_all_servers(appium_driver, start_app, close_app):
    """Проверяет скорость соединения на всех доступных VPN серверах."""

    vpn_main_page = VpnMainPage(appium_driver)
    servers_list_page = ServersListPage(appium_driver)
    speedtest_main_page = SpeedtestMainPage(appium_driver)
    reports = []

    vpn_package_name = os.getenv("APP_PACKAGE_NAME_VPN")
    speedtest_package_name = os.getenv("APP_PACKAGE_NAME_SPEEDTEST")

    start_app(vpn_package_name)
    vpn_main_page.show_servers_list()
    servers_count = servers_list_page.get_count_servers()
    logging.info(f"Обнаружено {servers_count} серверов для тестирования")

    for index in range(servers_count):
        try:
            # === Подключение к серверу по index ===
            start_app(vpn_package_name)
            current_server = servers_list_page.get_current_server(index)
            current_server.click()
            servers_list_page.connect_to_server()
            wait_for_visibility(appium_driver, vpn_main_page.connected_server_name_locator)
            name = vpn_main_page.get_name_connected_server()
            logging.info(f"Подключено к серверу: {name}")

            # === Запуск Speedtest ===
            start_app(speedtest_package_name)
            wait_for_visibility(appium_driver, speedtest_main_page.start_button_locator)
            speedtest_main_page.start_checking()
            wait_for_clickable(appium_driver, speedtest_main_page.id_test_locator, 50)
            speed = speedtest_main_page.get_speed()
            ping = speedtest_main_page.get_ping()
            logging.info(f"Результаты проверки скорости: Имя сервера = {name}, скорость = {speed}, пинг = {ping}")

            # === Формирование отчёта ===
            report = Report(server_name=name, server_speed=speed, server_ping=ping)
            reports.append(report)

        except Exception as e:
            logging.error(f"Ошибка при тестировании сервера №{index}: {e}")
            continue
        finally:
            # === Возвращаемся в VPN-приложение ===
            close_app(speedtest_package_name)
            start_app(vpn_package_name)
            wait_for_visibility(appium_driver, vpn_main_page.connected_server_name_locator)

    report_path = save_report_to_file(reports)
    logging.info(f"Отчёт о тестировании сохранён в: {report_path}")
    close_app(vpn_package_name)
    close_app(speedtest_package_name)