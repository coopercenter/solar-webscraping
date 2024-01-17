from webscraping_packages import *
"""Driver Setup"""
#download geckodriver https://stackoverflow.com/questions/41190989/how-do-i-install-geckodriver
#download Mozilla Firefox https://www.mozilla.org/en-US/firefox/new/
"""Firefox Version"""  
options = webdriver.FirefoxOptions()
options.headless = True #it's more scalable to work in headless mode (this means a simulation window won't appear) 
options.page_load_strategy = 'none' 
firefox_path = GeckoDriverManager().install() 
firefox_service = Service(firefox_path)
driver = Firefox(options=options, service=firefox_service)
driver.implicitly_wait(5)