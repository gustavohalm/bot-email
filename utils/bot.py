from selenium import webdriver
from selenium.webdriver.firefox.webelement import  FirefoxWebElement
import os


class Bot:

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox()
        self.driver.get(url)

    def insert_input(self, xpath, value):
        element = self.driver.find_element_by_xpath(xpath)
        element.send_keys(value)

    def click(self, xpath):
        element = self.driver.find_element_by_xpath(xpath)
        element.click()

    def upload_file(self, xpath, file_path):
        element = self.driver.find_element_by_xpath(xpath)
        element.send_keys(file_path)

    def capture_table(self, xpath):
        return self.driver.find_element_by_xpath(xpath).find_element_by_tag_name('tbody')

    def list_itens(self, element: FirefoxWebElement):
        return element.find_elements_by_tag_name('tr')

    def change_page(self, url):
        self.driver.get(url)

    def elements_by_class(self, class_name):
        return self.driver.find_elements_by_class_name(class_name)

    def click_js(self, id):
        self.driver.execute_script(f'document.getElementById(\"{id}\").click()')
