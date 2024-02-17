import unittest
from selenium import webdriver
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from time import sleep

class SeleniumTestCase(unittest.TestCase):
    driver: WebDriver = None
    base_url: str = "http://localhost:5173/"

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = WebDriver()
    @classmethod

    def setUp(self) -> None:
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(10)

    @classmethod
    def containsText(cls, query: str) -> str:
        return f"//*[contains(text(), '{query}')]"


class TestAddTodos(SeleniumTestCase):
    "Los todos se pueden añadir"

    def addTodo(self, todo: str):
        text_input = self.driver.find_element(By.CSS_SELECTOR, 'input[type="text"][placeholder="WRITE SOMETHING"]')
        text_input.send_keys(todo)
        add_btn = self.driver.find_element(By.NAME, "addBtn")
        add_btn.click()

    def test_add_todos_by_button(self):
        """Se puede añadir un todo por el botón"""
        todo = "Lavar la casa"
        self.addTodo(todo)
        elements = self.driver.find_elements(By.XPATH, self.containsText(todo))
        self.assertEqual(len(elements), 1, "Debe de haber solo un todo")
    def test_add_todos_by_enter(self):
        """Se pueden añadir un todo por enter"""
        todo = "Limpiar el carro"
        text_input = self.driver.find_element(By.CSS_SELECTOR, 'input[type="text"][placeholder="WRITE SOMETHING"]')
        text_input.send_keys(todo)
        ActionChains(self.driver).key_down(Keys.ENTER).perform()

        elements = self.driver.find_elements(By.XPATH, self.containsText(todo))
        self.assertEqual(len(elements), 1, "Debe de haber solo un todo")
    def test_add_multiple_todos(self):
        """Se pueden añadir varios todos"""
        todos = ["Lavar la casa", "Pasear al perro", "Hacer la tarea"]

        for todo in todos:
            self.addTodo(todo)
            elements = self.driver.find_elements(By.XPATH, self.containsText(todo))
            self.assertEqual(len(elements), 1, f"Debe de haber un todo con el texto {todo}")
    def test_not_add_blank_todo(self):
        """No se puede agregar un todo en blanco"""
        self.addTodo("")
        todos = self.driver.find_elements(By.CLASS_NAME, "todo-item")
        self.assertEqual(len(todos), 0, "No deberia de haber ningún todo")


if __name__ == "__main__":
    unittest.main()
