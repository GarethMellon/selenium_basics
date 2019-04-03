from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome('.\\drivers\\chromedriver.exe', options = chrome_options)


## Validate the landing page and check page elements
driver.get('https://thorin-and-company100.herokuapp.com/')
try:
    assert driver.current_url=="https://thorin-and-company100.herokuapp.com/"
    assert driver.title == "Hello Flask"
    assert driver.find_element_by_css_selector('.navbar-brand').text == "Thorin & Company"
    assert driver.find_element_by_css_selector('.subheading').text == "Thorin and his company of dwares"
except AssertionError:
    raise

## Validate About page and check page elements
driver.find_elements_by_css_selector('.nav-link')[1].click()
try:
    assert driver.current_url=="https://thorin-and-company100.herokuapp.com/about"
    assert driver.find_element_by_link_text('1. Thorin Oakenshield').tag_name == "a"
except AssertionError:
    raise

## Validate Contact Us page and check if form exists
driver.find_elements_by_css_selector('.nav-link')[3].click()
try:
    if driver.find_element_by_id('contactForm'):
        print("Contact Form Exists")
except AssertionError:
    raise

driver.close()