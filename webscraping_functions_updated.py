from webscraping_packages import *

"""Driver Setup"""
#download geckodriver https://stackoverflow.com/questions/41190989/how-do-i-install-geckodriver
#download Mozilla Firefox https://www.mozilla.org/en-US/firefox/new/
"""Firefox Version"""
#initialize the webdriver  
def get_webdriver():
    options = webdriver.FirefoxOptions()
    options.headless = True #it's more scalable to work in headless mode (this means a simulation window won't appear) 
    options.page_load_strategy = 'none' 
    firefox_path = GeckoDriverManager().install() 
    firefox_service = Service(firefox_path)
    return webdriver.Firefox(options=options, service=firefox_service)

#function to confirm that the internet is functional while we webscrape
def is_internet_active(timeout):
    try:
        requests.head("http://www.google.com/", timeout=timeout)
        return True
    except requests.ConnectionError:
        return False
    
#function to confirm that the stored url for the locality is still reachable   
def verify_url(url):
    try:
        #fetch the URL with a basic request
        get = requests.get(url)
        #check that the status code is 200 (successful)
        if get.status_code == 200:
            return(True)
        else:
             return(f"{url}: is Not reachable, status_code: {get.status_code}")
    except requests.exceptions.RequestException as e:
        # print URL with Errs
        raise SystemExit(f"{url}: is Not reachable \nErr: {e}")

#function to check the date of a posted meeting agenda, if available    
def check_meeting_date(meeting_time_string): 
    #all_meetings[i].text should be set as the meeting title for boarddocs sites
    if datetime.now() < dateutil.parser.parse(meeting_time_string, fuzzy=True) or datetime.now() == dateutil.parser.parse(meeting_time_string, fuzzy=True):
        return True
    else:
        return False

#confirm that a document can be read by extracting information in the HTML tags
def check_pdf_readibility(agenda_content):
    agenda_string = ""
    for item in agenda_content:
        agenda_string = agenda_string + item.text
    if agenda_string == "":
        readibility = False
    else:
        readibility = True
    return readibility

#search the computer-readable agenda text for the keywords we're tracking
def search_agenda_for_keywords(agenda_content):
    search_results = []
    for item in agenda_content:
        if 'Solar'in item.text or 'solar' in item.text:
            search_results.append('Solar')
        if 'Zoning Ordinance' in item.text or 'Zoning ordinance' in item.text or 'zoning ordinance' in item.text:
            search_results.append("Zoning Ordinance")
        if 'Comprehensive Plan' in item.text or 'Comprehensive plan' in item.text or 'comprehensive plan' in item.text:
            search_results.append("Comprehensive Plan")
    return search_results

#email the results of the agenda search
def email_new_alerts(email_message):
    "Outlook Email Development"
    #steps from https://www.makeuseof.com/send-outlook-emails-using-python/
    ol = win32com.client.Dispatch('Outlook.Application')
    # size of the new email
    olmailitem = 0x0
    newmail = ol.CreateItem(olmailitem)
    newmail.Subject = 'New Information for Review'
    newmail.SentOnBehalfOfName = "Solar Alerts"
    newmail.To = "egl6a@virginia.edu; emm2t@virginia.edu"
    newmail.Body= email_message
    newmail.Send()

#set the driver for now, having it as a function is something I want to utilize properly in the future for multithreading
driver=get_webdriver()

"""AgendaCenter"""
def agendacenter(url,locality):
    url_test = verify_url(url)
    if url_test==True:
        driver.get(url)
        time.sleep(5)
        messages = []
        agenda_links = driver.find_elements(By.CSS_SELECTOR, "a[href*='AgendaCenter/ViewFile'")
        table_rows = driver.find_elements(By.CSS_SELECTOR, "tr[class*=catAgendaRow")
        agenda_links_href = []
        agenda_dates = []
        agenda_titles = []
        for item in agenda_links:
            if item.text !='':
                agenda_links_href.append(item.get_attribute("href"))
                agenda_titles.append(item.text)
        for item in table_rows:
            if "\u2009" in item.text:
                agenda_dates.append(item.text.split("\u2009")[0])
            else:
                agenda_dates.append(item.text.split("\n")[0])
        for i in range(0,len(agenda_links_href)):
            future_date = check_meeting_date(agenda_dates[i])
            if future_date == True:
                meeting_title = agenda_titles[i] + " " + agenda_dates[i]
                driver.get(agenda_links_href[i])
                time.sleep(5)
                agenda_content = driver.find_elements(By.CSS_SELECTOR, "div[class*=textLayer")
                if agenda_content == []:
                    agenda_content = driver.find_elements(By.CSS_SELECTOR, "div[id*='divInner'")
                agenda_search = search_agenda_for_keywords(agenda_content)
                if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + locality + " in " + meeting_title  + ". " + agenda_links_href[i])
        return messages
    else:
        return url_test