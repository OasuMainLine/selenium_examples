import time

from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
def main():
    driver = Edge()

    driver.get("https://www.google.com/?hl=es")
    search_input = driver.find_element(By.CSS_SELECTOR, "textarea.gLFyf")

    search_input.send_keys("Selenium")
    ActionChains(driver).key_down(Keys.ENTER).perform()

    link = driver.find_element(By.PARTIAL_LINK_TEXT, "selenium")
    link.click()

    heading = driver.find_element(By.CSS_SELECTOR, "h4.selenium-ide")

    ActionChains(driver).\
        scroll_to_element(heading).\
        pause(3000).move_by_offset(0, -200).\
        pause(1000).move_by_offset(0, 200).\
        perform()

    time.sleep(10000)


if __name__ == '__main__':
    main()
