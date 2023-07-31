from webscraping_packages import *
"""Driver Setup"""

"""Firefox Version"""  
options = webdriver.FirefoxOptions()
options.headless = True # it's more scalable to work in headless mode  
options.page_load_strategy = 'none' 
firefox_path = GeckoDriverManager().install() 
firefox_service = Service(firefox_path)
driver = Firefox(options=options, service=firefox_service)
driver.implicitly_wait(5)