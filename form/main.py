from selenium import  webdriver
from selenium.webdriver.common.by import By
from time import sleep
url = "http://localhost:5173/"

user = {
    "name": "Ricardo",
    "email": "rickard@gmail.com",
    "password": "Richard2341",
    "username": "Rich",
}
def main():
    driver = webdriver.Edge()

    driver.get(url)
    driver.implicitly_wait(3)
    next_btn = driver.find_element(By.ID, "nextButton")
    # Step One
    name_input = driver.find_element(By.ID, "name-input")
    name_input.send_keys(user["name"])

    email_input = driver.find_element(By.CSS_SELECTOR, 'input[type="email"]')
    email_input.send_keys(user["email"])

    next_btn.click()

    #Step two
    user_input = driver.find_element(By.CSS_SELECTOR, 'input#username-input')
    user_input.send_keys(user["username"])

    password_input = driver.find_element(By.XPATH, "/html/body/div/form/div[3]/div[2]/input")
    password_input.send_keys(user["password"])

    next_btn.click()

    #Step three
    checkbox_input = driver.find_element(By.CLASS_NAME, "checkbox")
    checkbox_input.click()

    submit_btn = driver.find_element(By.ID, "submitButton")
    submit_btn.click()

    sleep(5)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
