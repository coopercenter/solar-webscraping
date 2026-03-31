from webscraping_packages import * 
from webscraping_driver import *

"""Firefox Version"""  
def get_webdriver():
    options = webdriver.FirefoxOptions()
    options.headless = True #it's more scalable to work in headless mode (this means a simulation window won't appear) 
    options.page_load_strategy = 'none' 
    firefox_path = GeckoDriverManager().install() 
    firefox_service = Service(firefox_path)
    return webdriver.Firefox(options=options, service=firefox_service)

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

def check_meeting_date(meeting_time_string): 
    one_week = timedelta(days=29)
    last_week = datetime.date(datetime.now()) - one_week
    #all_meetings[i].text should be set as the meeting title for boarddocs sites
    if datetime.date(datetime.now()) < datetime.date(dateutil.parser.parse(meeting_time_string, fuzzy=True)) or datetime.date(datetime.now()) == datetime.date(dateutil.parser.parse(meeting_time_string, fuzzy=True)) or last_week < datetime.date(dateutil.parser.parse(meeting_time_string, fuzzy=True)) or last_week == datetime.date(dateutil.parser.parse(meeting_time_string, fuzzy=True)) :
        return True
    else:
        return False
 
def get_pdf_content(content_tag):
    pages = driver.find_elements(By.CSS_SELECTOR,"div[class*=page")
    text_layers = driver.find_elements(By.CSS_SELECTOR,content_tag)
    agenda_string = ""
    if len(pages) > len(text_layers):
        for page in pages:
            driver.execute_script("arguments[0].scrollIntoView();", page)
            time.sleep(5)
            agenda_content = driver.find_elements(By.CSS_SELECTOR,content_tag)
            for item in agenda_content:
                agenda_string = agenda_string + item.text
    elif len(pages)==len(text_layers):
        agenda_content = driver.find_elements(By.CSS_SELECTOR,content_tag)
        for item in agenda_content:
                agenda_string = agenda_string + item.text
    return agenda_string

#very simple version, maybe the ideal if every function uses get_pdf_content first
def check_agenda_readability(agenda_content):
    if agenda_content != "":
        return True
    else:
        return False
    
def get_webpage_content(content_tag):
    agenda_string =""
    agenda_content = driver.find_elements(By.CSS_SELECTOR,content_tag)
    for item in agenda_content:
        agenda_string = agenda_string + item.text
    return agenda_string

def read_docx_download(agenda_link):
    query_parameters = {"downloadformat": "docx"}
    headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    agenda_file = requests.get(agenda_link, allow_redirects=True,params=query_parameters,headers=headers)
    if agenda_file.status_code == 200:
        temp_agenda = tempfile.TemporaryFile()
        temp_agenda.write(agenda_file.content)
        agenda_content = docx2txt.process(temp_agenda)
    return agenda_content

def read_pdf_download(agenda_link):
    query_parameters = {"downloadformat": "pdf"}
    headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    agenda_file = requests.get(agenda_link, allow_redirects=True,params=query_parameters,headers=headers)
    if agenda_file.status_code == 200:
        temp_agenda = tempfile.TemporaryFile()
        temp_agenda.write(agenda_file.content)
        agenda_pdf = PdfReader(temp_agenda)
        agenda_pages = agenda_pdf.pages
        agenda_content = "\n".join([item.extract_text() for item in agenda_pages])
        temp_agenda.close()
    return agenda_content

#new version, hopefully more flexible?
#def check_pdf_readability(content_tag):
#    test_content = driver.find_elements(By.CSS_SELECTOR,content_tag)
#    agenda_string = ""
#    for item in test_content:
#        agenda_string = agenda_string + item.text
#    if agenda_string == "":
#        readability = False
#    else:
#        readability = True
#    return readability

def search_text_for_keywords(agenda_content):
    search_results = []
    if 'Solar'in agenda_content or 'solar' in agenda_content:
        search_results.append('Solar')
    if 'Zoning Ordinance' in agenda_content or 'Zoning ordinance' in agenda_content or 'zoning ordinance' in agenda_content:
        search_results.append("Zoning Ordinance")
    if 'Comprehensive Plan' in agenda_content or 'Comprehensive plan' in agenda_content or 'comprehensive plan' in agenda_content:
        search_results.append("Comprehensive Plan")
    if 'Siting Agreement' in agenda_content or 'Siting agreement' in agenda_content or 'siting agreement' in agenda_content:
        search_results.append('Siting Agreement')
    if 'Battery Storage' in agenda_content or "Battery storage" in agenda_content or "battery storage" in agenda_content or "Energy Storage" in agenda_content or "Energy storage" in agenda_content or "energy storage" in agenda_content or "BESS" in agenda_content:
        search_results.append("Battery Storage")
    return pd.Series(search_results).unique().tolist()


#def email_new_alerts(email_message):
 #   "Outlook Email Development"
    #steps from https://www.makeuseof.com/send-outlook-emails-using-python/
 #   ol = win32com.client.Dispatch('Outlook.Application')
    # size of the new email
 #   olmailitem = 0x0
#    newmail = ol.CreateItem(olmailitem)
 #   newmail.Subject = 'New Information for Review'
 #   newmail.SentOnBehalfOfName = "Solar Alerts"
 #   newmail.To = "egl6a@virginia.edu; emm2t@virginia.edu"
  #  newmail.Body= email_message
 #   newmail.Send()


def is_internet_active(timeout):
    try:
        requests.head("http://www.duckduckgo.com/", timeout=timeout)
        return True
    except requests.ConnectionError:
        return False

"""Webscraping Functions"""

"""AgendaCenter"""
def agendacenter(locality_dictionary):
    from webscraping_dictionaries import agendacenter_dictionary
    dictionary = agendacenter_dictionary[locality_dictionary]
    driver.get(dictionary['url'])
    messages = []
    time.sleep(5)
    table_rows = driver.find_elements(By.CSS_SELECTOR, dictionary["meeting_rows"])
    if table_rows == []:
        messages.append("No meetings found for " + dictionary["name"] + ". Tags may have changed or content may have moved.")
    future_meetings = [item for item in table_rows if check_meeting_date(search_dates(item.text,languages=['en'])[0][0])==True]
    agenda_links = [item.find_elements(By.CSS_SELECTOR,"a")[1].get_attribute("href") for item in future_meetings]
    for link in agenda_links:
        driver.get(link)
        time.sleep(60)
        if dictionary['agenda_type']=='pdf':
            agenda_content = get_pdf_content(dictionary['agenda_content'])
        elif dictionary['agenda_type']=='webpage':
            agenda_content = get_webpage_content(dictionary["agenda_content"])
        readable = check_agenda_readability(agenda_content)
        if readable == True:
            agenda_search = search_text_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + dictionary['name'] + ". " + link)
            elif readable == False:
                messages.append("New meeting document available for "+ dictionary['name'] + ". " + "Document cannot be scanned for keywords. " + link)
    return messages

def agendacenter2(locality_dictionary):
    from webscraping_dictionaries import agendacenter2_dictionary
    dictionary = agendacenter2_dictionary[locality_dictionary]
    driver.get(dictionary['url'])
    time.sleep(5)
    messages =[]
    table_rows = driver.find_elements(By.CSS_SELECTOR, dictionary["meeting_rows"])
    if table_rows == []:
        messages.append("No meetings found for " + dictionary["name"] + ". Tags may have changed or content may have moved.")
    future_meetings = [item for item in table_rows if check_meeting_date(search_dates(item.text,languages=['en'])[0][0])==True]
    meetings_links = [item.find_elements(By.CSS_SELECTOR,"a")[1].get_attribute("href") for item in future_meetings]
    #if agendacenter_dictionary[locality_dictionary]['agenda_type']=='pdf':
    for link in meetings_links:
        driver.get(link)
        time.sleep(5)
        documents = driver.find_elements(By.CSS_SELECTOR,'a')
        agendas = [pdf_link.get_attribute('href') for pdf_link in documents if 'AGENDA' in pdf_link.text]
        for agenda_link in agendas:
            driver.get(agenda_link)
            agenda_content = get_pdf_content(dictionary['agenda_content'])
            readable = check_agenda_readability(agenda_content)
            if readable == True:
                agenda_search = search_text_for_keywords(agenda_content)
                if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + dictionary['name'] + ". " + link)
            elif readable ==False:
                messages.append("New meeting document available for "+ dictionary['name'] + ". " + "Document cannot be scanned for keywords. " + link)
    #if agendacenter_dictionary[locality_dictionary]['agenda_type']=='webpage':
        #messages = search_webpage(agenda_links, agendacenter2_dictionary, locality_dictionary)
    return messages

"""BoardDocs"""
def check_boarddocs_agendas(locality_dictionary):
    from webscraping_dictionaries import boarddocs_dictionary
    dictionary = boarddocs_dictionary[locality_dictionary]
    all_tabs=driver.find_elements(By.CSS_SELECTOR,"a[id*=ui-id-")
    meetings_tab = [item for item in all_tabs if item.text in ['MEETINGS','Meetings']]
    meetings_tab[0].click()
    time.sleep(10)
    #get all the meeting links
    #open the current year
    if dictionary['featured']==True:
        years = driver.find_elements(By.CSS_SELECTOR,"section[class*='ui-accordion-header")
        current_year = [year for year in years if year.text == datetime.now().strftime("%Y")]
        current_year[0].click()
        time.sleep(3)
    update_messages = []
    future_meetings = []
    all_meetings = driver.find_elements(By.CSS_SELECTOR, "a[class*='icon prevnext meeting")
    if all_meetings == []:
        update_messages.append("No meetings found for " + dictionary["name"] + ". Tags may have changed or content may have moved.")
    for item in all_meetings:
        if search_dates(item.text,languages=['en'])!=None and check_meeting_date(search_dates(item.text,languages=['en'])[0][1].strftime('%m/%d/%Y'))==True:
            future_meetings.append(item)
    for item in future_meetings:
        meeting_title = item.text
        #if the meeting hasn't happened yet, check for last minute agenda edits that might contain solar until it has passed
        item.click()
        time.sleep(10)
        #find the element to click to view the meeting agenda for this meeting
        #add a dictionary for accessing agenda links/buttons
        meeting_agenda = driver.find_element(By.CSS_SELECTOR, "a[id*='btn-view-agenda'")
        #click the meeting agenda button
        meeting_agenda.click()
        time.sleep(10)
        #pause, give the page time to load
        #Now to get ALL the agenda content
        all_agenda_topics = driver.find_elements(By.CSS_SELECTOR, "span[class*='title'")
        agenda_content = ""
        for item in all_agenda_topics:
            agenda_content += item.text
        #run the keyword search
        agenda_search = search_text_for_keywords(agenda_content)
        if agenda_search !=[]:
            update_messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + dictionary['name'] + " in " + meeting_title + ". " + dictionary['url'])
        meetings_tab[0].click()
        time.sleep(10)
    return update_messages

def boarddocs(locality_dictionary):
    from webscraping_dictionaries import boarddocs_dictionary
    dictionary = boarddocs_dictionary[locality_dictionary]
    driver.get(dictionary['url'])
    time.sleep(10)
    messages = check_boarddocs_agendas(locality_dictionary)
    if dictionary['second_page']==True:
        govt_tab = driver.find_element(By.CSS_SELECTOR,"a[id*=btn-board")
        govt_tab.click()
        time.sleep(10)
        menu_options = driver.find_elements(By.CSS_SELECTOR,"a[class*=dropdown-item")
        for item in menu_options:
            if "Planning Commission" in item.text:
                planning_commission=item
        planning_commission.click()
        time.sleep(10)
        pc_messages = check_boarddocs_agendas(locality_dictionary)
        messages += pc_messages
    return messages

"Calendar View"
def calendar_view(locality_dictionary):
    from webscraping_dictionaries import calendar_view_dictionary
    dictionary = calendar_view_dictionary[locality_dictionary]
    driver.get(dictionary['url'])
    time.sleep(20)
    messages = []
    meetings = driver.find_elements(By.CSS_SELECTOR,dictionary["meetings_tag"])
    if meetings == []:
        messages.append("No meetings found for " + dictionary["name"] + ". Tags may have changed or content may have moved.")
    meeting_links = [meeting.get_attribute("href") for meeting in meetings if "Board of Supervisors" in meeting.text or "Planning Commission" in meeting.text or "Board of Zoning Appeals" in meeting.text or "Solar" in meeting.text or "Battery" in meeting.text]
    for link in meeting_links:
        driver.get(link)
        time.sleep(10)
        if dictionary["agenda_type"] == "webpage":
            agenda_content = get_webpage_content(dictionary["content_tag"])
        elif dictionary["agenda_type"] == "pdf":
            try:
                agenda_link = driver.find_element(By.CSS_SELECTOR, dictionary["agenda_tag"]).get_attribute("href")
                driver.get(agenda_link)
                time.sleep(10)
                agenda_content = get_pdf_content(dictionary["content_tag"])
            except:
                agenda_content=[]
        readable = check_agenda_readability(agenda_content)
        if readable == True:
            agenda_search = search_text_for_keywords(agenda_content)
            if agenda_search !=[]:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + dictionary["name"] + ". " + link)
        elif readable == False:
            messages.append("New meeting document available for " + dictionary["name"] + ". Document cannot be scanned for keywords. " + link)         
    return messages

"CivicClerk"
def civicclerk(locality_dictionary):
    from webscraping_dictionaries import civicclerk_dictionary
    dictionary = civicclerk_dictionary[locality_dictionary]
    messages=[]
    driver.get(dictionary['url'])
    time.sleep(10)
    all_meetings = driver.find_elements(By.CSS_SELECTOR,dictionary["meeting_rows"])
    if all_meetings == []:
        messages.append("No meetings found for " + dictionary["name"] + ". Tags may have changed or content may have moved.")
    meetings_with_agendas = []
    for item in all_meetings:
        try:
            #test if there's a download button, indicating agenda files have been posted. Lack of files to scan will throw an error, and we won't waste time checking that meeting link for keywords
            #consider making this a dictionary of options as well
            item.find_element(By.CSS_SELECTOR,"button[id*=downloadFilesMenu")
            meetings_with_agendas.append(item)
        except:
            continue
    future_meetings = [item.find_element(By.CSS_SELECTOR,"a").get_attribute("href")  for item in meetings_with_agendas if check_meeting_date(search_dates(item.text,languages=['en'])[1][0])==True]
    for item in future_meetings:
        driver.get(item)
        time.sleep(10)
        #don't rely on this to always be the same, turn this into a dictionary of options, even if there's only one current option. It has changed in the past, it can change again.
        pdf_viewer_frame = driver.find_elements(By.CSS_SELECTOR,"iframe[id*=pdfViewerIframe")
        if pdf_viewer_frame != []:
            driver.switch_to.frame(pdf_viewer_frame[0])
            agenda_content = get_pdf_content(dictionary['agenda_content'])
            readable=check_agenda_readability(agenda_content)
            if readable ==True:
                agenda_search = search_text_for_keywords(agenda_content)
                if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + dictionary['name'] + ". " + item)
            elif readable ==False:
                messages.append("New meeting document available for " + dictionary['name'] + ". " + "Document cannot be scanned for keywords. " + item)
    return messages
    
"""CivicWeb"""
def civicweb(locality_dictionary):
    from webscraping_dictionaries import civicweb_dictionary
    dictionary=civicweb_dictionary[locality_dictionary]
    driver.get(dictionary['url'])
    time.sleep(10) 
    messages = [] 
    all_meetings = driver.find_elements(By.CSS_SELECTOR,dictionary["meetings_tag"])
    if all_meetings == []:
        messages.append("No meetings found for " + dictionary["name"] + ". Tags may have changed or content may have moved.")
    relevant_meetings = [item for item in all_meetings if "Board of Supervisors" in item.text or "Planning Commission" in item.text or "City Council" in item.text or "Board of Zoning Appeals" in item.text]
    future_meetings = []
    for item in relevant_meetings:
        if search_dates(item.text) != None:
            try:
                if check_meeting_date(search_dates(item.text,languages=['en'])[1][0])==True:
                    future_meetings.append(item.get_attribute("href"))
            except:
                if check_meeting_date(search_dates(item.text,languages=['en'])[0][0])==True:
                    future_meetings.append(item.get_attribute("href"))
    for item in future_meetings:
        driver.get(item)
        time.sleep(10)
        #switch to the agenda viewer frame
        agenda_frame = driver.find_element(By.CSS_SELECTOR,"iframe")
        driver.switch_to.frame(agenda_frame)
        agenda_content = get_pdf_content(dictionary['content_tag'])
        readable = check_agenda_readability(agenda_content)
        if readable ==True:
            agenda_search = search_text_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + dictionary['name'] + ". " + item)
        elif readable == False:
            messages.append("New meeting document available for " + dictionary["name"] + ". Document cannot be scanned for keywords. " + item)
    return messages

"""DocumentCenter"""
def document_center(locality_dictionary):
    from webscraping_dictionaries import document_center_dictionary
    dictionary = document_center_dictionary[locality_dictionary]
    driver.get(dictionary['url'])
    time.sleep(10)  
    messages = []
    folders = driver.find_elements(By.CSS_SELECTOR,"div[class*='ant-tree-treenode'")
    if folders == []:
        messages.append("No meetings found for " + dictionary["name"] + ". Tags may have changed or content may have moved.")
    bos_folder = [item for item in folders if 'Board of Supervisors' in item.text]
    bos_folder[0].click()
    time.sleep(2)
    bos_doc_folders = driver.find_elements(By.CSS_SELECTOR,"div[class*='ant-tree-treenode'")
    agenda_folder = [item for item in bos_doc_folders if item.text=='Agenda']
    agenda_folder[0].click()
    time.sleep(2)
    year_folders = driver.find_elements(By.CSS_SELECTOR,"div[class*='ant-tree-treenode'")
    current_year = [item for item in year_folders if item.text == datetime.now().strftime("%Y")]
    current_year[0].click()
    time.sleep(2)
    agenda_links = driver.find_elements(By.CSS_SELECTOR,"a[class*=pdf")
    latest_agenda = agenda_links[-1].get_attribute("href")
    driver.get(latest_agenda)
    time.sleep(10)
    agenda_content = get_pdf_content(dictionary["content_tag"])
    readable = check_agenda_readability(agenda_content)
    if readable == True:
        agenda_search = search_text_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + dictionary['name'] + ". " + latest_agenda)
    elif readable == False:
        messages.append("New meeting document available for " + dictionary["name"] + ". Document cannot be scanned for keywords. " + latest_agenda)
    return messages

"""eScribe"""
def escribe(locality_dictionary):
    from webscraping_dictionaries import escribe_dictionary
    dictionary = escribe_dictionary[locality_dictionary]
    driver.get(dictionary['url'])
    time.sleep(10)
    messages = []
    archive_tabs = driver.find_elements(By.CSS_SELECTOR,"a[id*='ctl00_MainContent")
    relevant_tabs = []
    for item in archive_tabs:
        if "Board of Supervisors" in item.text or "Board of Zoning Appeals" in item.text or "Planning Commission" in item.text:
            relevant_tabs.append(item)
    document_links = []
    for item in relevant_tabs:
        item.click()
        time.sleep(10)
        archive_meetings = driver.find_elements(By.CSS_SELECTOR,"div[class*='calendar-item'")
        relevant_meetings = [meeting for meeting in archive_meetings if "Board of Supervisors" in meeting.text or "Board of Zoning Appeals" in meeting.text or "Planning Commission" in item.text]
        current_meetings = [meeting for meeting in relevant_meetings if search_dates(meeting.text) != None and check_meeting_date(search_dates(meeting.text,languages=['en'])[0][0])==True]
        for meeting in current_meetings:
            links = meeting.find_elements(By.CSS_SELECTOR,"a[href*='DocumentId'")
            for link in links:
                document_links.append(link.get_attribute("href"))
    if document_links == []:
        messages.append("No meetings found for " + dictionary["name"] + ". Tags may have changed or content may have moved.")
    for link in document_links:
        driver.get(link)
        time.sleep(10)
        agenda_content = get_pdf_content("div[class*=textLayer")
        readable = check_agenda_readability(agenda_content)
        if readable == True:
            agenda_search = search_text_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + escribe_dictionary[locality_dictionary]['name'] +  ". " + link)
        elif readable==False:
            messages.append("New meeting document available for "+ dictionary['name'] + ". " + "Document cannot be scanned for keywords. " + link)
    return messages

"Folding Year" #generalized function for websites that operate on an accordioned year archive style
def folding_year(locality_dictionary):
    from webscraping_dictionaries import folding_year_dictionary
    dictionary = folding_year_dictionary[locality_dictionary]
    driver.get(dictionary["url"])
    time.sleep(5)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, dictionary["years_tag"])))
    messages = []
    if folding_year_dictionary[locality_dictionary]["archive_type"] == "closed":
        years = driver.find_elements(By.CSS_SELECTOR,dictionary["years_tag"])
        current_year = [year for year in years if datetime.now().strftime("%Y") in year.text]
        current_year[0].click()
        time.sleep(2)
    if dictionary["agenda_subfolder"]==True:
        content_tabs = driver.find_elements(By.CSS_SELECTOR, dictionary["agenda_folder_tag"])
        agenda_tab = [item for item in content_tabs if "Agenda" in item.text]
        agenda_tab[0].click()
        time.sleep(2)
    if dictionary["month_subfolder"]==True:
        months = driver.find_elements(By.CSS_SELECTOR, dictionary["months_tag"])
        relevant_months = [month for month in months if datetime.now().strftime("%B") in month.text.title() or (datetime.date(datetime.now()) - timedelta(days=8)).strftime("%B") in month.text.title()]
        for month in relevant_months:
            month.click()
            meetings = driver.find_elements(By.CSS_SELECTOR,dictionary["meetings_tag"])
            if meetings == []:
                messages.append("No meetings found for " + dictionary["name"] + ". Tags may have changed or content may have moved.")
            future_meetings = [item.get_attribute("href") for item in meetings if search_dates(item.text, languages=['en']) != None  and check_meeting_date(search_dates(item.text, languages=['en'])[0][0])==True]
            for agenda_link in future_meetings:
                driver.get(agenda_link)
                time.sleep(20)
                agenda_content = get_pdf_content(dictionary["content_tag"])
                readable = check_agenda_readability(agenda_content)
                if readable == True:
                    agenda_search = search_text_for_keywords(agenda_content)
                    if agenda_search != []:
                        messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + dictionary['name'] + ". " + agenda_link)
                elif readable ==False:
                    messages.append("New meeting document available for "+ dictionary['name'] + ". " + "Document cannot be scanned for keywords. " + agenda_link)
    elif folding_year_dictionary[locality_dictionary]["month_subfolder"]==False:
        meetings = driver.find_elements(By.CSS_SELECTOR,dictionary["meetings_tag"])
        if meetings == []:
            messages.append("No meetings found for " + dictionary["name"] + ". Tags may have changed or content may have moved.")
        future_meetings = [item.get_attribute("href") for item in meetings if search_dates(item.text, languages=['en']) != None  and check_meeting_date(search_dates(item.text, languages=['en'])[0][0])==True]
        for agenda_link in future_meetings:
            driver.get(agenda_link)
            time.sleep(20)
            agenda_content = get_pdf_content(dictionary["content_tag"])
            readable = check_agenda_readability(agenda_content)
            if readable == True:
                agenda_search = search_text_for_keywords(agenda_content)
                if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + dictionary['name'] + ". " + agenda_link)
            elif readable ==False:
                messages.append("New meeting document available for "+ dictionary['name'] + ". " + "Document cannot be scanned for keywords. " + agenda_link)   
    return messages

"""Folding Year Version 2"""
def folding_year_v2(locality_dictionary):
    from webscraping_dictionaries import folding_year_v2_dictionary
    dictionary = folding_year_v2_dictionary[locality_dictionary]
    driver.get(dictionary["url"])
    time.sleep(10)
    messages = []
    if dictionary["archive_type"] == "closed":
        folders = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, dictionary["years_tag"])))
        current_year = [year for year in folders if datetime.now().strftime("%Y") in year.text]
        if locality_dictionary=="Virginia Beach PC":
            driver.execute_script("arguments[0].scrollIntoView(true);", current_year[0])
            current_year[1].click()
            time.sleep(1)
        else:
            current_year[0].click()
            time.sleep(1)
        meetings = driver.find_elements(By.CSS_SELECTOR,dictionary["row_tag"])
        if meetings == []:
            messages.append("No meetings found for " + dictionary["name"] + ". Tags may have changed or content may have moved.")
        #future_meetings=[item.find_element(By.CSS_SELECTOR,folding_year_v2_dictionary[locality_dictionary]["document_tag"]).get_attribute("href") for item in meetings if search_dates(item.text,languages=["en"]) != None and check_meeting_date(search_dates(item.text,languages=["en"])[0][1].strftime("%m/%d/%Y"))==True]
        future_meetings = []
        for item in meetings:
            if search_dates(item.text,languages=["en"]) != None:
                if search_dates(item.text,languages=["en"]) != None and datetime.now().strftime("%Y") in search_dates(item.text,languages=["en"])[0][1].strftime("%m/%d/%Y") and check_meeting_date(search_dates(item.text,languages=["en"])[0][1].strftime("%m/%d/%Y"))==True:
                    try:
                        future_meetings.append(item.find_element(By.CSS_SELECTOR,dictionary["document_tag"]).get_attribute("href"))
                    except:
                        continue 
        for agenda_link in future_meetings:
            driver.get(agenda_link)
            time.sleep(10)
            agenda_content = get_pdf_content(dictionary["content_tag"])
            readable = check_agenda_readability(agenda_content)
            if readable == True:
                agenda_search = search_text_for_keywords(agenda_content)
                if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + dictionary['name'] + ". " + agenda_link)
            elif readable ==False:
                messages.append("New meeting document available for "+ dictionary['name'] + ". " + "Document cannot be scanned for keywords. " + agenda_link)   
    return messages

"""Granicus"""
def granicus(locality_dictionary):
    from webscraping_dictionaries import granicus_dictionary
    dictionary = granicus_dictionary[locality_dictionary]
    driver.get(dictionary['url'])
    time.sleep(10)
    messages=[]
    #to be able to search through the last week, some archive tabs need to be opened
    if dictionary["archive_type"]=="closed":
        archive_tabs = driver.find_elements(By.CSS_SELECTOR,dictionary["archive_tag"])
        if archive_tabs == []:
            messages.append("No archives available for " + dictionary["name"] + ". Tags may have changed or content may have moved.")
        for item in archive_tabs:
            if "Planning" in item.text or "City Council" in item.text or "Board of Supervisors" in item.text or "Board of Zoning Appeals" in item.text:
                item.click()
    #gets all the table rows that contain meeting entries
    table_rows=driver.find_elements(By.CSS_SELECTOR,dictionary["meeting_rows"])
    if table_rows == []:
        messages.append("No meetings found for " + dictionary["name"] + ". Tags may have changed or content may have moved.")
    #narrowing down to just future dates
    future_meetings = [item for item in table_rows if search_dates(item.text) != None and search_dates(item.text)[0][0] != 'Minutes' and check_meeting_date(search_dates(item.text,languages=['en'])[0][0])==True]
    agendas = []
    for item in future_meetings:
        try:
            #try/except is used here to move through errors where an agenda or agenda packet is not posted and the find_element results are null
            #packets first, more details available
            agendas.append(item.find_element(By.CSS_SELECTOR,dictionary["agendas_tag"]).get_attribute("href"))
        except:
            continue
    if agendas == []:
        messages.append("No agendas found for " + dictionary["name"] + ". Tags may have changed or content may have moved.")
    for agenda_url in agendas:
        driver.get(agenda_url)
        time.sleep(15)
        if dictionary["agenda_type"]=="pdf":
            agenda_content = get_pdf_content(dictionary["content_tag"])
        elif dictionary["agenda_type"]=="webpage":
            agenda_content = get_webpage_content(dictionary["content_tag"])
        readable = check_agenda_readability(agenda_content)
        if readable==True:
            agenda_search = search_text_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + dictionary['name'] + ". " + agenda_url)
        elif readable==False:
            messages.append("New meeting document available for " + dictionary["name"] + ". Document cannot be scanned for keywords. " + agenda_url)
    return messages

def granicus_version_2(locality_dictionary):
    from webscraping_dictionaries import granicus_2_dictionary
    dictionary = granicus_2_dictionary[locality_dictionary]
    driver.get(dictionary['url'])
    time.sleep(10)
    messages = []
    table_rows = driver.find_elements(By.CSS_SELECTOR, 'div[class*=RowTop')
    if table_rows == []:
        messages.append("No meetings found for " + dictionary["name"] + ". Tags may have changed or content may have moved.")
    future_meetings = [item.find_element(By.CSS_SELECTOR,"a[href*='Citizens/Detail_Meeting'").get_attribute("href") for item in table_rows if check_meeting_date(item.text)==True]
    for item in future_meetings:
            driver.get(item)
            time.sleep(10)
            try:
                if dictionary["agenda_type"]=="webpage":
                    agenda_content = get_webpage_content(dictionary["content_tag"])
                elif dictionary["agenda_type"]=="pdf":
                    agenda_link = driver.find_element(By.CSS_SELECTOR,"a[id*=PublicAgendaFile").get_attribute("href")
                    driver.get(agenda_link)
                    time.sleep(20)
                    agenda_content=get_pdf_content(dictionary["content_tag"])
                agenda_search = search_text_for_keywords(agenda_content)
                readable=check_agenda_readability(agenda_content)
                if readable == True:
                    agenda_search = search_text_for_keywords(agenda_content)
                    if agenda_search != []:
                        messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + dictionary['name'] + ". " + agenda_link)
                elif readable==False:
                    messages.append("New meeting document available for " + dictionary["name"] + ". Document cannot be scanned for keywords. " + agenda_link)
            except:
                continue
    return messages

"LaserFiche"
def laserfiche(locality_dictionary):
    from webscraping_dictionaries import laserfiche_dictionary
    dictionary = laserfiche_dictionary[locality_dictionary]
    driver.get(dictionary['url'])
    time.sleep(10)
    messages=[]
    frame = driver.find_element(By.CSS_SELECTOR,"iframe[name=frame1")
    driver.switch_to.frame(frame)
    year_folders = driver.find_elements(By.CSS_SELECTOR,"td")
    #find the folder for the current yeaer
    current_folder = [item for item in year_folders if item.text==str(datetime.today().year)]
    current_folder_link = current_folder[0].find_element(By.CSS_SELECTOR,"a").get_attribute('href')
    driver.get(current_folder_link)
    time.sleep(10)
    meeting_folders = driver.find_elements(By.CSS_SELECTOR,"tr")
    if meeting_folders == []:
        messages.append("No meetings found for " + dictionary["name"] + ". Tags may have changed or content may have moved.")
    future_meetings = []
    for item in meeting_folders:
        try:
            if check_meeting_date(item.text)==True:
                future_meetings.append(item.find_element(By.CSS_SELECTOR,"a").get_attribute('href'))
        except:
            continue 
    for item in future_meetings:
        driver.get(item)
        time.sleep(10)
        try:
            agenda_link = driver.find_element(By.CSS_SELECTOR,"a[href*='Agenda.pdf'").get_attribute('href')
        except:
            agenda_link = driver.find_element(By.CSS_SELECTOR,"a[href*='Agenda-REVISED.pdf'").get_attribute('href')
        #turn this into a replicable method for whenever downloads come up
        agenda_content = read_pdf_download(agenda_link)
        readable = check_agenda_readability(agenda_content)
        if readable == True:
            agenda_search = search_text_for_keywords(agenda_content)
            if agenda_search!=[]:
                messages.append('Keyword(s) ' + ", ".join(agenda_search)+' found in upcoming meeting for ' + dictionary['name'] + '. ' + agenda_link)
        elif readable == False:
            messages.append('New agenda available for upcoming meeting in ' + dictionary['name'] + ". Document cannot be scanned for keywords. " + item)
    return messages                 

"""Legistar"""
def legistar(locality_dictionary):
    from webscraping_dictionaries import legistar_dictionary
    dictionary = legistar_dictionary[locality_dictionary]
    messages = []
    driver.get(dictionary['url'])
    time.sleep(10)
    table_rows = driver.find_elements(By.CSS_SELECTOR,'tr[id*=ctl00_')
    if table_rows == []:
        messages.append("No meetings found for " + dictionary["name"] + ". Tags may have changed or content may have moved.")
    future_meetings = [item for item in table_rows if check_meeting_date(search_dates(item.text,languages=['en'])[0][0])==True]
    meeting_urls = [item.find_element(By.CSS_SELECTOR,"a[id*=hypMeetingDetail").get_attribute('href') for item in future_meetings]
    for item in meeting_urls:
        if item != None:
            driver.get(item)
            time.sleep(10)
            agenda_content = get_webpage_content(dictionary["content_tag"])
            readable = check_agenda_readability(agenda_content)
            if readable == True:
                agenda_search = search_text_for_keywords(agenda_content)
                if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + dictionary['name'] + ". " + item)
            elif readable == False:
                messages.append('New agenda available for upcoming meeting in ' + dictionary['name'] + ". Document cannot be scanned for keywords. " + item)
    return messages

"Links by Year" #see dictionary entry for explanation on website commonalities
def links_by_year(locality_dictionary):
    from webscraping_dictionaries import links_by_year_dictionary
    dictionary = links_by_year_dictionary[locality_dictionary]
    driver.get(dictionary['url'])
    time.sleep(10)
    messages = []
    #the year links will be stored as list items
    list_items = driver.find_elements(By.CSS_SELECTOR,dictionary['year_list_tag'])
    #this will catch the list entry that represents the current year
    current_year = [item for item in list_items if str(datetime.date(datetime.now()).year) in item.text]
    #now navigate to the agenda page for the current year
    driver.get(current_year[0].get_attribute("href"))
    time.sleep(5)
    #find all the agenda document links
    links = driver.find_elements(By.CSS_SELECTOR,dictionary['agenda_link_tag'])
    if links == []:
        messages.append("No meetings found for " + dictionary["name"] + ". Tags may have changed or content may have moved.")
    future_meetings = []
    for item in links:
        try:
            if search_dates(item.text,languages=['en']) != None:
                if check_meeting_date(search_dates(item.text,languages=['en'])[0][0])==True:
                    future_meetings.append(item.get_attribute('href'))
        except:
            continue
    for link in future_meetings:
        driver.get(link)
        time.sleep(10)
        if dictionary["agenda_type"] == "pdf":
            agenda_content = get_pdf_content(dictionary['agenda_content_tag'])
        if dictionary["agenda_type"] == "webpage":
            agenda_content = get_webpage_content(dictionary['agenda_content_tag'])
        readable = check_agenda_readability(agenda_content)
        if readable == True:
            agenda_search = search_text_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + dictionary['name'] + ". " + link)
        elif readable == False:
            messages.append('New agenda available for upcoming meeting in ' + dictionary['name'] + ". Document cannot be scanned for keywords. " + item)
    return messages

"""Meetings Table"""
def meetings_table(locality_dictionary):
    from webscraping_dictionaries import meetingstable_dictionary
    dictionary = meetingstable_dictionary[locality_dictionary]
    driver.get(dictionary['url'])
    time.sleep(10)
    messages = []
    all_rows = driver.find_elements(By.CSS_SELECTOR,dictionary['meetings_tag'])[1:]
    if all_rows == []:
        messages.append("No meetings found for " + dictionary["name"] + ". Tags may have changed or content may have moved.")
    future_meetings = []
    for item in all_rows:
        if search_dates(item.text) != None:
            future_meeting = check_meeting_date(search_dates(item.text,languages=['en'])[0][0])
            if future_meeting==True:
                future_meetings.append(item)
    agenda_links = []
    for item in future_meetings:
        try:
            agenda_links.append(item.find_element(By.CSS_SELECTOR,"a[title*=Agenda").get_attribute('href'))
        except:
            continue
    for item in agenda_links:
            driver.get(item)
            time.sleep(10)
            agenda_content = get_pdf_content(dictionary['agenda_content_tag'])
            readable = check_agenda_readability(agenda_content)
            if readable == True:
                agenda_search = search_text_for_keywords(agenda_content)
                if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + dictionary['name'] + ". " + item)
            elif readable == False:
                messages.append('New agenda available for upcoming meeting in ' + dictionary['name'] + ". Document cannot be scanned for keywords. " + item)
    return messages

"""NovusAGENDA"""
"""def novusagenda(locality_dictionary):
    from webscraping_dictionaries import novusagenda_dictionary
    #validate the URL
    url_test  = verify_url(novusagenda_dictionary[locality_dictionary]['url'])
    if url_test == True:
        #fetch the URL and give it a few seconds to load the scripts
        driver.get(novusagenda_dictionary[locality_dictionary]['url'])
        time.sleep(10)
        main_window = driver.window_handles[0]
        messages=[]
        table_rows = driver.find_elements(By.CSS_SELECTOR,"tr")
        future_meetings = []
        for item in table_rows:
            try:
                future=check_meeting_date(item.text)
                if future==True:
                    future_meetings.append(item)
            except:
                continue
        #find the links to the ONLINE agendas (not the download pdf buttons)
        agenda_links = []
        for item in future_meetings:
            try:
                agenda_links.append(item.find_element(By.CSS_SELECTOR, "a[style*='cursor:pointer'"))
            except:
                continue
        for item in agenda_links:
            item.click()
            time.sleep(10)
            #switch to the new window
            agenda_window = driver.window_handles[1]
            driver.switch_to.window(agenda_window)
            #find the rest of the agenda content
            agenda_content = driver.find_elements(By.CSS_SELECTOR, "td")
            agenda_search = search_agenda_for_keywords(agenda_content)
            if agenda_search != []:
                agenda_url = driver.current_url
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + novusagenda_dictionary[locality_dictionary]['name'] + ". " + agenda_url)
            driver.close()
            driver.switch_to.window(main_window)
        return messages
    else:
        return url_test
    """
"""OnBase"""
def onbase(locality_dictionary):
    from webscraping_dictionaries import onbase_dictionary
    dictionary = onbase_dictionary[locality_dictionary]
    messages=[]
    driver.get(dictionary['url'])
    time.sleep(10)
    table_rows = driver.find_elements(By.CSS_SELECTOR,"tr")
    if table_rows == []:
        messages.append("No meetings found for " + dictionary["name"] + ". Tags may have changed or content may have moved.")
    future_meetings = []
    for item in table_rows:
        try:
            future=check_meeting_date(item.text)
            if future==True:
                future_meetings.append(item)
        except:
            continue
    agenda_links = []
    for item in future_meetings:
        try:
            agenda = item.find_element(By.CSS_SELECTOR,"a[id*='MeetingAgenda'")
            agenda_links.append(agenda.get_attribute("href"))
        except:
            continue
    for item in agenda_links:
        driver.get(item)
        time.sleep(10)
        agenda_content=get_webpage_content("body")
        readable = check_agenda_readability(agenda_content)
        if readable == True:
            agenda_search=search_text_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + dictionary['name'] + ". " + item)
        elif readable == False:
            messages.append("New meeting agenda available for " + dictionary['name'] + ". Document cannot be scanned for keywords. " + item)
    return messages
    
"""PHP Table"""
def php_table(locality_dictionary):
    from webscraping_dictionaries import php_table_dictionary
    dictionary = php_table_dictionary[locality_dictionary]
    driver.get(dictionary['url'])
    time.sleep(10)
    messages = []
    table_rows = driver.find_elements(By.CSS_SELECTOR,'tr')
    if table_rows == []:
        messages.append("No meetings found for " + dictionary["name"] + ". Tags may have changed or content may have moved.")
    future_meetings = []
    for item in table_rows:
        try:
            future=check_meeting_date(search_dates(item.text,languages=['en'])[0][0])
            if future==True:
                future_meetings.append(item)
        except:
            continue
    future_agendas = [item.find_element(By.CSS_SELECTOR, "a[href*='.pdf'").get_attribute('href') for item in future_meetings if dictionary['web_document'] in item.text]
    if future_agendas !=[]:
        for agenda_link in future_agendas:
            driver.get(agenda_link)
            time.sleep(20)
            agenda_content = get_pdf_content("div[class*=textLayer")
            readable = check_agenda_readability(agenda_content)
            if readable == True:
                agenda_search = search_text_for_keywords(agenda_content)
                if agenda_search !=[]:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + dictionary['name'] + ". " + agenda_link)
            elif readable == False:
                messages.append("New meeting agenda available for " + dictionary['name'] + ". Document cannot be scanned for keywords. " + agenda_link)
    return messages

"""PrimeGov"""
def prime_gov(locality_dictionary):
    from webscraping_dictionaries import primegov_dictionary
    dictionary = primegov_dictionary[locality_dictionary]
    driver.get(dictionary['url'])
    time.sleep(10)
    messages=[]
    #find all the table rows
    table_rows = driver.find_elements(By.CSS_SELECTOR,'tr[role*=row')
    if table_rows == []:
        messages.append("No meetings found for " + dictionary["name"] + ". Tags may have changed or content may have moved.")
    #filter for upcoming meetings
    current_meetings = [row.find_element(By.CSS_SELECTOR,"a[class*='document'").get_attribute("href") for row in table_rows if search_dates(row.text,languages=["en"]) != None and check_meeting_date(search_dates(row.text,languages=["en"])[0][0]) == True]
    for link in current_meetings:
        try:
            agenda_content = read_pdf_download(link)
        except:
            agenda_content = read_docx_download(link)
        readable = check_agenda_readability(agenda_content)
        if readable == True:
            agenda_search = search_text_for_keywords(agenda_content)
            if agenda_search !=[]:
                messages.append('Keyword(s) ' + ", ".join(agenda_search)+' found in upcoming meeting for ' + dictionary['name'] + '. ' + link)
        elif readable == False:
            messages.append("New meeting document available for " + dictionary['name'] + ". Document cannot be scanned for keywords. " + link)
    return messages

"The Lists" #websites whose layout boil down to a list of links with the document link containing the name and date in the hyperlink text
def the_lists(locality_dictionary):
    from webscraping_dictionaries import the_lists_dictionary
    dictionary = the_lists_dictionary[locality_dictionary]
    messages = []
    driver.get(dictionary["url"])
    time.sleep(10)
    meetings = driver.find_elements(By.CSS_SELECTOR,dictionary["meetings_tag"])
    if meetings == []:
        messages.append("No meetings found for " + dictionary["name"] + ". Tags may have changed or content may have moved.")
    current_meetings = [item.get_attribute("href") for item in meetings if search_dates(item.text) != None and check_meeting_date(search_dates(item.text,languages=["en"])[0][0])==True]
    for link in current_meetings:
        driver.get(link)
        time.sleep(20)
        agenda_content = get_pdf_content(dictionary["content_tag"])
        readable = check_agenda_readability(agenda_content)
        if readable == True:
            agenda_search = search_text_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) "  + ", ".join(agenda_search) + " found in upcoming meeting for "  + dictionary["name"] + ". " + link)
        elif readable == False:
            messages.append("New meeting document available for " + dictionary["name"] + ". Document cannot be scanned for keywords. " + link)
    return messages

#subset of the list type websites where the agenda link is distinct from the date-containing title
def the_split_lists(locality_dictionary):
    from webscraping_dictionaries import the_split_lists_dictionary
    dictionary = the_split_lists_dictionary[locality_dictionary]
    messages = []
    driver.get(dictionary["url"])
    time.sleep(10)
    meetings = driver.find_elements(By.CSS_SELECTOR,dictionary["meeting_rows"])
    driver.execute_script("arguments[0].scrollIntoView(true);", meetings[0])
    time.sleep(1)
    if meetings == []:
        messages.append("No meetings found for " + dictionary["name"] + ". Tags may have changed or content may have moved.")
    agenda_links = []
    for item in meetings:
        if search_dates(item.text.title().replace("Minutes",""),languages=["en"]) != None and check_meeting_date(search_dates(item.text.title().replace("Minutes",""),languages=["en"])[0][0]) == True:
            try:
                agenda_links.append(item.find_element(By.CSS_SELECTOR,dictionary["agenda_tag"]).get_attribute("href"))
            except:
                continue
    for link in agenda_links:
        driver.get(link)
        time.sleep(10)
        agenda_content = get_pdf_content(dictionary["content_tag"])
        readable = check_agenda_readability(agenda_content)
        if readable == True:
            agenda_search = search_text_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + dictionary["name"] + ". " + link)
        elif readable == False:
            messages.append("New meeting document available for " + dictionary["name"] + ". Document cannot be scanned for keywords. " + link)
    return messages

"""Locality Specific Functions"""

"""Albemarle County"""
def albemarle_county_pc():
    from webscraping_dictionaries import locality_dictionary_single_use
    dictionary = locality_dictionary_single_use['Albemarle PC']
    messages=[]
    driver.get(dictionary['url'])
    time.sleep(10)
    table_rows = driver.find_elements(By.CSS_SELECTOR, dictionary["rows_tag"])
    if table_rows == []:
        messages.append("No meetings found for " + dictionary["name"] + ". Tags may have changed or content may have moved.")
    recent_and_upcoming = [row for row in table_rows if search_dates(row.text, languages=["en"]) != None and check_meeting_date(search_dates(row.text, languages=["en"])[0][0]) == True]
    meeting_links = []
    for item in recent_and_upcoming:
        try:
            meeting_links.append(item.find_element(By.CSS_SELECTOR,dictionary["meetings_tag"]).get_attribute("href"))
        except:
            continue
    for item in meeting_links:
        driver.get(item)
        time.sleep(10)
        try:
            document_links = driver.find_elements(By.CSS_SELECTOR,dictionary["documents_tag"])
            agenda_link = [item.get_attribute("href") for item in document_links if "Agenda" in item.text]
            driver.get(agenda_link[0])
            time.sleep(10)
            agenda_content = get_pdf_content(dictionary['content_tag'])
            readable = check_agenda_readability(agenda_content)
            if readable == True:
                agenda_search=search_text_for_keywords(agenda_content)
                if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Albemarle County Planning Commission. " + agenda_link)
            elif readable == False:
                messages.append("New meeting document available for Albemarle County Planning Commission. Document cannot be scanned for keywords. " + agenda_link)
        except:
            continue
    return messages

"""Buchanan County"""
def buchanan_county():
    from webscraping_dictionaries import locality_dictionary_single_use
    dictionary = locality_dictionary_single_use['Buchanan']
    driver.get(dictionary['url'])
    time.sleep(10)
    messages = []
    pdfs = driver.find_elements(By.CSS_SELECTOR,dictionary["pdfs_tag"])
    if pdfs == []:
        messages.append("No meetings found for " + dictionary["name"] + ". Tags may have changed or content may have moved.")
    latest_minutes = [item for item in pdfs if "Minutes" in item.text][0]
    #since they're only posting minutes not agendas, and minutes are posted long after the fact, we'll skip the date checking
    minutes_url = latest_minutes.get_attribute("href")
    driver.get(minutes_url)
    time.sleep(10)
    agenda_content = get_pdf_content(dictionary['content_tag'])
    readable = check_agenda_readability(agenda_content)
    if readable == True:
        agenda_search = search_text_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Buchanan County Board of Supervisors. " + minutes_url)
    elif readable == False:
        messages.append('New meeting document available for Buchanan County. Document cannot be scanned for keywords' + minutes_url)
    return messages   

"""Fairfax County"""
def fairfax_county_bos():
    from webscraping_dictionaries import locality_dictionary_single_use
    dictionary = locality_dictionary_single_use['Fairfax BOS']
    driver.get(dictionary['url'])
    time.sleep(10)
    messages = []
    meetings = driver.find_elements(By.CSS_SELECTOR,dictionary["meetings_tag"])
    if meetings == []:
         messages.append("No meetings found for " + dictionary["name"] + ". Tags may have changed or content may have moved.")
    meeting_links = [meeting.get_attribute("href") for meeting in meetings if search_dates(meeting.get_attribute("href").replace("-"," ").replace("/"," "),languages=["en"]) != None and check_meeting_date(search_dates(meeting.get_attribute("href").replace("-"," ").replace("/"," "),languages=["en"])[0][0])==True and search_dates(meeting.get_attribute("href").replace("-"," ").replace("/"," "),languages=["en"])[0][0] != '2026']
    for link in meeting_links:
        driver.get(link)
        time.sleep(10)
        try:
            agenda_link = driver.find_element(By.CSS_SELECTOR,dictionary["agendas_tag"]).get_attribute("href")
            driver.get(agenda_link)
            time.sleep(10)
            agenda_content = get_pdf_content(dictionary['agenda_content_tag'])
            readable = check_agenda_readability(agenda_content)
            if readable == True:
                agenda_search = search_text_for_keywords(agenda_content)
                if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Fairfax County Board of Supervisors. " + agenda_link)
            elif readable == False:
                messages.append('New agenda available for upcoming meeting in Fairfax Count Board of Supervisors. Document cannot be scanned for keywords. ' + agenda_link)
        except:
            continue
    return messages

def fairfax_county_pc():
    from webscraping_dictionaries import locality_dictionary_single_use
    dictionary = locality_dictionary_single_use['Fairfax PC']
    driver.get(dictionary['url'])
    time.sleep(10)
    messages = []
    latest_year = driver.find_element(By.CSS_SELECTOR,dictionary["years_tag"])
    if latest_year == None:
        messages.append("No years found for " + dictionary["name"] + ". Tags may have changed or content may have moved.")
    months = latest_year.find_elements(By.CSS_SELECTOR,dictionary["months_tag"])
    if months == []:
        messages.append("No months found for " + dictionary["name"] + ". Tags may have changed or content may have moved.")
    current_months = [item.find_element(By.CSS_SELECTOR,"a").get_attribute('href') for item in months if item.text == datetime.now().strftime("%B") or item.text == (datetime.date(datetime.now()) - timedelta(days=8)).strftime("%B") ]
    for month in current_months:
        driver.get(month)
        time.sleep(15)
        agendas = driver.find_elements(By.CSS_SELECTOR,dictionary["agendas_tag"])
        if agendas == []:
            messages.append("No meetings found for " + dictionary["name"] + ". Tags may have changed or content may have moved.")
        agenda_links = [item.get_attribute("href") for item in agendas]
        current_meetings = []
        for item in agenda_links:
            try:
                if check_meeting_date(item.split('/')[-1].split('.pdf')[0]) == True:
                    current_meetings.append(item)
            except:
                messages.append("Error: Date cannot be verified for Fairfax County Planning Commission meeting " + item)
                continue
        for item in current_meetings:
            driver.get(item)
            time.sleep(10)
            agenda_content = get_pdf_content(dictionary['content_tag'])
            readable = check_agenda_readability(agenda_content)
            if readable == True:
                agenda_search = search_text_for_keywords(agenda_content)
                if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Fairfax County Planning Commission. " + item)
            elif readable == False:
                messages.append("New agenda available for upcoming meeting in Fairfax County Planning Commission. Document cannot be scanned for keywords. " + item)
    return messages

"""Floyd County""" #how to even get this working again, horrible new website with total lack of tag coherence
def floyd_county():
    from webscraping_dictionaries import locality_dictionary_single_use
    driver.get(locality_dictionary_single_use['Floyd']['url'])
    time.sleep(10)
    messages = []
    all_meeting_rows = driver.find_elements(By.CSS_SELECTOR,"span[class*='wixui-rich-text__text'")
    current_meeting_rows = [item for item in all_meeting_rows if item.text != '']
    latest_meeting = current_meeting_rows[-1]
    #split around the colon, otherwise the date fails to register
    future_meeting = check_meeting_date(latest_meeting.text.split(":")[0])
    if future_meeting == True:
        agenda_url = latest_meeting.find_element(By.CSS_SELECTOR,"a").get_attribute("href")
        driver.get(agenda_url)
        time.sleep(10)
        agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
        #agenda_search = search_agenda_for_keywords(agenda_content)
        #if agenda_search != []:
        #    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Floyd County Board of Supervisors. " + agenda_url)
    return messages

"""Giles County Board of Supervisors"""
def giles_county():
    from webscraping_dictionaries import locality_dictionary_single_use
    dictionary = locality_dictionary_single_use['Giles']
    driver.get(dictionary['url'])
    time.sleep(10)
    messages = []
    buttons = driver.find_elements(By.CSS_SELECTOR,dictionary["buttons_tag"])
    if buttons == []:
        messages.append("No site buttons found for " + dictionary["name"] + ". Tags may have changed or content may have moved.")
    #follow the link to the latest agenda. Third button is the NEXT AGENDA button
    agenda_link = buttons[2].find_element(By.CSS_SELECTOR,dictionary["agendas_tag"]).get_attribute("href")
    driver.get(agenda_link)
    time.sleep(10)
    agenda_content = get_pdf_content(dictionary["content_tag"])
    readable = check_agenda_readability(agenda_content)
    if readable==True:
        agenda_search = search_text_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Giles County in next agenda. " + agenda_link)
    elif readable == False:
        messages.append("New document available for upcoming meeting for Giles County. Document cannot be scanned for keywords. " + agenda_link)
    return messages      

"Highland County"
def highland_county_bos():
    from webscraping_dictionaries import locality_dictionary_single_use
    dictionary = locality_dictionary_single_use['Highland BOS']
    messages = []
    driver.get(dictionary['url'])
    time.sleep(10)
    folders = driver.find_elements(By.CSS_SELECTOR,dictionary["folders_tag"])
    if folders == []:
        messages.append("No folders found for " + dictionary["name"] + ". Tags may have changed or content may have moved.")
    current_year = [item for item in folders if item.text==str(datetime.now().year)]
    driver.get(current_year[0].get_attribute('href'))
    time.sleep(10)
    meetings = driver.find_elements(By.CSS_SELECTOR,dictionary["meetings_tag"])
    if meetings == []:
        messages.append("No meetings found for " + dictionary["name"] + ". Tags may have changed or content may have moved.")
    future_meetings = [item.find_element(By.CSS_SELECTOR,"a").get_attribute("href") for item in meetings if check_meeting_date(search_dates(item.text,languages=['en'])[0][0]) == True]
    for item in future_meetings:
        driver.get(item)
        time.sleep(10)
        agenda_link = driver.find_element(By.CSS_SELECTOR,dictionary["agendas_tag"]).get_attribute('href')
        if ".pdf" in agenda_link:
            driver.get(agenda_link)
            time.sleep(10)
            agenda_content = get_pdf_content(dictionary["content_tag"])
            readable = check_agenda_readability(agenda_content)
            if readable == True:
                agenda_search = search_text_for_keywords(agenda_content)
                if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Highland County Board of Supervisors. " + agenda_link)
            elif readable == False:
                messages.append("New document available for upcoming meeting for Highland County Board of Supervisors. Document cannot be scanned for keywords. " + agenda_link)
        elif ".docx" in agenda_link:
            agenda_content = read_docx_download(agenda_link)
            readable = check_agenda_readability(agenda_content)
            if readable == True:
                agenda_search = search_text_for_keywords(agenda_content)
                if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Highland County Board of Supervisors. " + agenda_link)
            elif readable == False:
                messages.append("New document available for upcoming meeting for Highland County Board of Supervisors. Document cannot be scanned for keywords. " + agenda_link)
    return messages

"LaserFiche for Loudoun Planning Commission"
def loudoun_pc():
    from webscraping_dictionaries import locality_dictionary_single_use
    dictionary = locality_dictionary_single_use['Loudoun']
    driver.get(dictionary['url'])
    time.sleep(10)
    messages=[]
    all_links = driver.find_elements(By.CSS_SELECTOR,dictionary["links_tag"])
    meeting_doc_folder = [item for item in all_links if item.text == 'Public Hearings & Work Sessions']
    driver.get(meeting_doc_folder[0].get_attribute('href'))
    time.sleep(10)
    #find the folder for the current year
    year_folders = driver.find_elements(By.CSS_SELECTOR,dictionary["years_tag"])
    current_folder = [item for item in year_folders if item.text==str(datetime.today().year)]
    current_folder_link = current_folder[0].find_element(By.CSS_SELECTOR,dictionary["current_year_tag"]).get_attribute('href')
    driver.get(current_folder_link)
    time.sleep(10)
    meeting_folders = driver.find_elements(By.CSS_SELECTOR,dictionary["folders_tag"])
    if meeting_folders == []:
        messages.append("No meetings found for " + dictionary["name"] + ". Tags may have changed or content may have moved.")
    future_meetings = []
    for item in meeting_folders:
        try:
            if check_meeting_date(item.text)==True:
                future_meetings.append(item.find_element(By.CSS_SELECTOR,dictionary["meetings_tag"]).get_attribute('href'))
        except:
            continue 
    for item in future_meetings:
        driver.get(item)
        time.sleep(10)
        try:
            agenda_link = driver.find_element(By.CSS_SELECTOR,dictionary["agendas_tag"]).get_attribute('href')
            agenda_content = read_pdf_download(agenda_link)
            readable = check_agenda_readability(agenda_content)
            if readable == True:
                agenda_search = search_text_for_keywords(agenda_content)
                if agenda_search != []:
                    messages.append('Keyword(s) ' + ", ".join(agenda_search)+' found in upcoming meeting for  Loudoun County Planning Commission. ' + agenda_link)
            elif readable == False:
                messages.append("New document available for upcoming meeting for Loudoun County Planning Commission. Document cannot be scanned for keywords. " + agenda_link)
        except:
            continue
    return messages

"""Virginia Beach"""
def virginia_beach_cc():
    from webscraping_dictionaries import locality_dictionary_single_use
    dictionary = locality_dictionary_single_use['Virginia Beach CC']
    driver.get(dictionary["url"])
    time.sleep(10)
    messages = []
    current_agenda = driver.find_element(By.CSS_SELECTOR,dictionary["agendas_tag"])
    if current_agenda == []:
        messages.append("No meetings found for " + dictionary["name"] + ". Tags may have changed or content may have moved.")
    agenda_url = current_agenda.get_attribute("href")
    driver.get(agenda_url)
    time.sleep(10)
    agenda_content = get_pdf_content(dictionary["content_tag"])
    readable = check_agenda_readability(agenda_content)
    if readable == True:
        agenda_search = search_text_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Virginia Beach in latest City Council meeting agenda. " + agenda_url)
    elif readable == False:
        messages.append("New meeting document available for Virginia Beach City Council. Document cannot be scanned for keywords. " + agenda_url)
    return messages

"""Wythe County"""
#check public notices for now until agenda links work again
def wythe_county():
    from webscraping_dictionaries import locality_dictionary_single_use
    dictionary = locality_dictionary_single_use['Wythe']
    driver.get(dictionary["url"])
    time.sleep(10)
    messages = []
    public_notice_links = driver.find_elements(By.CSS_SELECTOR,dictionary["notice_tags"])
    if public_notice_links == []:
        messages.append("No meetings found for " + dictionary["name"] + ". Tags may have changed or content may have moved.")
    solar_notices = [item.get_attribute('href') for item in public_notice_links if 'Solar' in item.text]
    if solar_notices != []:
        for link in solar_notices:
            messages.append('Keyword(s) Solar found in Public Notice for Wythe County ' + link)
    return messages
#def wythe_county(url):
 #   driver.get(url)
 #   time.sleep(10)
 #   messages = []
 #   agenda_links = driver.find_elements(By.CSS_SELECTOR,"a[href*=package")
 #   active_links = [item for item in agenda_links if item.text !='']
 #   future_meetings = [item.get_attribute('href') for item in active_links if check_meeting_date(search_dates(item.text)[0][0])==True]
 #   for item in future_meetings:
 #       driver.get(item)
 #       time.sleep(10)
 #       agenda_content = driver.find_elements(By.CSS_SELECTOR,"svg[class*=textLayer")
 #       if agenda_content == []:
 #           agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
 #       agenda_search = search_agenda_for_keywords(agenda_content)
 #       if agenda_search != []:
 #           messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Wythe County. " + item)
 #   return messages

 """Bath County"""
def bath_county(locality_dictionary): #add a clause that allows it to finish without an error if there's no current year for meetings in the BZA
    from webscraping_dictionaries import locality_dictionary_multi_use
    dictionary = locality_dictionary_multi_use[locality_dictionary]
    driver.get(dictionary['url'])
    time.sleep(10)
    messages = []
    archive_pages = driver.find_elements(By.CSS_SELECTOR,dictionary["archive_page_tag"])
    valid_pages = [item for item in archive_pages if item.text !='']
    valid_pages[-1].click()
    time.sleep(5)
    years = driver.find_elements(By.CSS_SELECTOR,dictionary["years_tag"])
    try:
        current_year = [item for item in years if str(datetime.date(datetime.now()).year) in item.text]
        current_year[0].click()
        time.sleep(5)
    except:
        return messages
    minutes_pages = driver.find_elements(By.CSS_SELECTOR,dictionary["minutes_page_tag"])
    valid_minutes_pages = [item for item in minutes_pages if item.text !='']
    if valid_minutes_pages[-1].text != '1':
        valid_minutes_pages[-1].click()
        time.sleep(5)
    minutes = driver.find_elements(By.CSS_SELECTOR,dictionary["minutes_tag"])
    if minutes == []:
        messages.append("No meetings found for " + dictionary["name"] + ". Tags may have changed or content may have moved.")
    latest_minutes = minutes[-1].get_attribute('href')
    driver.get(latest_minutes)
    time.sleep(10)
    agenda_content = get_pdf_content(dictionary['content_tag'])
    readable = check_agenda_readability(agenda_content)
    if readable == True:
        agenda_search = search_text_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + dictionary['name'] + ". " + latest_minutes)
    elif readable ==False:
        messages.append("New meeting document available for "+ dictionary['name'] + ". " + "Document cannot be scanned for keywords. " + latest_minutes)
    return messages