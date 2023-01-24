from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://189.202.211.146:4433")


options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')

browser = webdriver.Chrome(chrome_options=options, desired_capabilities=cap)
cap = DesiredCapabilities.CHROME
cap['acceptInsecureCerts'] = True


# file_input = driver.find_element_by_id("file-input")
# file_input.send_keys("/path/to/file.jpg")