from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


def tap_element_center(driver, element):
    location = element.location
    size = element.size
    center_x = location["x"] + size["width"] // 2
    center_y = location["y"] + size["height"] // 2

    finger = PointerInput(interaction.POINTER_TOUCH, "finger1")
    actions = ActionBuilder(driver, mouse=finger)
    actions.pointer_action.move_to_location(center_x, center_y)
    actions.pointer_action.pointer_down()
    actions.pointer_action.pause(0.1)
    actions.pointer_action.pointer_up()
    actions.perform()
