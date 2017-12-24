import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select


class AtomicBoard(unittest.TestCase):

    def setUp(self):
        pass

    def test_1_create_user(self):
        driver = self.driver
        driver.get("http://atomicboard.devman.org/create_test_user/")
        self.assertIn("Создать", driver.title)
        button = driver.find_element_by_css_selector("form button")
        button.click()

    def test_2_display_tasks(self):
        driver = self.driver
        driver.get("http://atomicboard.devman.org/#/")
        self.assertIn("AtomicBoard", driver.title)
        tasks = WebDriverWait(driver, self.timeout).until(
            EC.visibility_of_all_elements_located(
                (By.CSS_SELECTOR, ".js-ticket")))
        self.assertTrue(tasks)

    def test_3_1_edit_task_title(self):
        text_for_editing = 'Тестовый заголовок'
        driver = self.driver
        task = WebDriverWait(driver, self.timeout).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".js-panel-heading_text")))
        task.click()
        input = driver.find_element_by_css_selector(".editable-input")
        input.clear()
        input.send_keys(text_for_editing)
        ok_button = driver.find_element_by_css_selector(
            ".editable-buttons .btn-primary")
        ok_button.click()
        self.assertEqual(task.text, text_for_editing)

    def test_3_2_edit_task_category(self):
        selected_index = 1
        driver = self.driver
        WebDriverWait(driver, self.timeout).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".js-panel-heading_text"))).click()
        task_category = driver.find_element_by_css_selector(
            ".ticket_description span.ng-scope")
        task_category.click()
        select = Select(driver.find_element_by_css_selector(
            "select.editable-input"))
        select.select_by_index(selected_index)
        selected_category = select.options[selected_index].text
        ok_button = driver.find_element_by_css_selector(
            ".editable-buttons .btn-primary")
        ok_button.click()
        self.assertEqual(selected_category, task_category.text)

    def test_3_3_edit_task_importance(self):
        selected_index = 0
        driver = self.driver
        WebDriverWait(driver, self.timeout).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".js-panel-heading_text"))).click()
        task_importance = driver.find_element_by_css_selector(
            ".ticket_description span.importance_edit")
        task_importance.click()
        select = Select(driver.find_element_by_css_selector(
            "select.editable-input"))
        select.select_by_index(selected_index)
        selected_importance = select.options[selected_index].text
        ok_button = driver.find_element_by_css_selector(
            ".editable-buttons .btn-primary")
        ok_button.click()
        self.assertEqual(selected_importance, task_importance.text)

    def test_4_change_task_status(self):
        driver = self.driver
        task_status = WebDriverWait(driver, self.timeout).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".ticket_status")))
        task_status.click()
        driver.switch_to.alert
        closed_button = WebDriverWait(driver, self.timeout).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "button.btn-primary")))
        closed_button.click()
        self.assertEqual(task_status.text, 'closed')

    def test_5_add_new_task(self):
        new_task_title = 'Новое задание'
        driver = self.driver
        WebDriverWait(driver, self.timeout).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".add-ticket-block_button"))).click()
        input = driver.find_element_by_css_selector(".editable-input")
        input.clear()
        input.send_keys(new_task_title)
        ok_button = driver.find_element_by_css_selector(
            ".editable-buttons .btn-primary")
        ok_button.click()
        time.sleep(1)
        task_titles = [task.text for task in driver.find_elements_by_css_selector(
            ".js-panel-heading_text")]
        self.assertTrue(new_task_title in task_titles)

    def test_6_drag_and_drop(self):
        task_number = 0
        target_column_number = 1
        jquery_url = "http://code.jquery.com/jquery-1.11.2.min.js"
        driver = self.driver
        columns = WebDriverWait(driver, self.timeout).until(
            EC.visibility_of_all_elements_located(
                (By.CSS_SELECTOR, ".js-tickets-column")))
        task_title = driver.find_elements_by_css_selector(
            ".js-panel-heading_text")[task_number].text
        driver.set_script_timeout(self.timeout)
        with open("jquery_load_helper.js") as f:
            load_jquery_js = f.read()
        with open("drag_and_drop_helper.js") as f:
            drag_and_drop_js = f.read()
        driver.execute_async_script(load_jquery_js, jquery_url)
        driver.execute_script(drag_and_drop_js +
                              "$('.js-ticket:eq(%d)').simulateDragDrop("
                              "{ dropTarget: '.js-tickets-column:eq(%d)'});"
                              % (task_number, target_column_number))
        target_column = columns[target_column_number]
        target_column_task_titles = [task.text for task in target_column.find_elements_by_css_selector(
            ".js-panel-heading_text")]
        self.assertTrue(task_title in target_column_task_titles)
        driver.quit()

    def tearDown(self):
        pass


if __name__ == "__main__":
    AtomicBoard.driver = webdriver.Chrome()
    AtomicBoard.timeout = 10
    unittest.main()
