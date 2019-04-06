from selenium import webdriver
import unittest


class ThorinAndCompanyTest(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome('.\\drivers\\chromedriver.exe', options=chrome_options)
        self.driver.maximize_window()
        self.driver.get('https://thorin-and-company100.herokuapp.com/')

    def test_blog_main_page(self):
        driver = self.driver
        self.driver.implicitly_wait(1)
        try:
            print(">> Running Tests on main page <<")
            self.assertTrue(driver.current_url == "https://thorin-and-company100.herokuapp.com/")
            self.assertEqual(driver.title, "Hello Flask")
            assert driver.find_element_by_css_selector('.navbar-brand').text == "Thorin & Company"
            assert driver.find_element_by_css_selector('.subheading').text == "Thorin and his company of dwares"
        except AssertionError:
            print(">> There was an assert error <<")
            raise

    def test_about(self):
        driver = self.driver
        self.driver.find_elements_by_css_selector('.nav-link')[1].click()
        self.driver.implicitly_wait(1)
        try:
            print(">> Running Tests on About page <<")
            assert driver.current_url == "https://thorin-and-company100.herokuapp.com/about"
            assert driver.find_element_by_link_text('1. Thorin Oakenshield').tag_name == "a"
        except AssertionError:
            raise

    def test_contact_us(self):
        driver = self.driver
        self.driver.find_elements_by_css_selector('.nav-link')[3].click()
        self.driver.implicitly_wait(1)
        try:
            print(">> Running Tests on Contact page <<")
            if driver.find_element_by_id('contactForm'):
                print("Contact Form Exists")
        except AssertionError:
            raise

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
