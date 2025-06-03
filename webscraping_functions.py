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
    one_day = timedelta(days=1)
    yesterday = datetime.date(datetime.now()) - one_day
    day_before_yesterday = yesterday - one_day
    #all_meetings[i].text should be set as the meeting title for boarddocs sites
    if datetime.date(datetime.now()) < datetime.date(dateutil.parser.parse(meeting_time_string, fuzzy=True)) or datetime.date(datetime.now()) == datetime.date(dateutil.parser.parse(meeting_time_string, fuzzy=True)) or yesterday == datetime.date(dateutil.parser.parse(meeting_time_string, fuzzy=True)) or day_before_yesterday == datetime.date(dateutil.parser.parse(meeting_time_string, fuzzy=True)):
        return True
    else:
        return False
    
def get_agenda_content(content_tag):
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

#very simple version, maybe the ideal if every function uses get_agenda_content first
def check_agenda_readability(agenda_content):
    if agenda_content != "":
        return True
    else:
        return False

#new version, hopefully more flexible?
def check_pdf_readability(content_tag):
    test_content = driver.find_elements(By.CSS_SELECTOR,content_tag)
    agenda_string = ""
    for item in test_content:
        agenda_string = agenda_string + item.text
    if agenda_string == "":
        readability = False
    else:
        readability = True
    return readability

def search_webpage(meeting_links_list, website_dictionary, locality_dictionary):
    messages=[]
    for item in meeting_links_list:
        driver.get(item)
        time.sleep(60)
        keywords = []
        agenda_content = driver.find_elements(By.CSS_SELECTOR,website_dictionary[locality_dictionary]['agenda_content'])
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search != []:
            keywords += agenda_search
        elif keywords != []:
            unique_keywords = pd.Series(keywords).unique().tolist()
            messages.append("Keyword(s) " + ", ".join(unique_keywords) + " found in upcoming meeting for " + website_dictionary[locality_dictionary]['name'] + ". " + item)
    return pd.Series(messages).unique().tolist()

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
    return pd.Series(search_results).unique().tolist()

def search_agenda_for_keywords(agenda_content):
    search_results = []
    for item in agenda_content:
        if 'Solar'in item.text or 'solar' in item.text:
            search_results.append('Solar')
        if 'Zoning Ordinance' in item.text or 'Zoning ordinance' in item.text or 'zoning ordinance' in item.text:
            search_results.append("Zoning Ordinance")
        if 'Comprehensive Plan' in item.text or 'Comprehensive plan' in item.text or 'comprehensive plan' in item.text:
            search_results.append("Comprehensive Plan")
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
    from webscraping_dictionaries import agendacenter_dictionary, meetings_tags
    driver.get(agendacenter_dictionary[locality_dictionary]['url'])
    messages = []
    time.sleep(5)
    table_rows = driver.find_elements(By.CSS_SELECTOR, meetings_tags['agendacenter'])
    future_meetings = [item for item in table_rows if check_meeting_date(search_dates(item.text,languages=['en'])[0][0])==True]
    agenda_links = [item.find_elements(By.CSS_SELECTOR,"a")[1].get_attribute("href") for item in future_meetings]
    if agendacenter_dictionary[locality_dictionary]['agenda_type']=='pdf':
        for link in agenda_links:
            driver.get(link)
            time.sleep(20)
            agenda_content = get_agenda_content(agendacenter_dictionary[locality_dictionary]['agenda_content'])
            readable = check_agenda_readability(agenda_content)
            if readable == True:
                agenda_search = search_text_for_keywords(agenda_content)
                if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + agendacenter_dictionary[locality_dictionary]['name'] + ". " + link)
            elif readable == False:
                messages.append("New meeting document available for "+ agendacenter_dictionary[locality_dictionary]['name'] + ". " + "Document cannot be scanned for keywords. " + link)
    if agendacenter_dictionary[locality_dictionary]['agenda_type']=='webpage':
        messages = search_webpage(agenda_links, agendacenter_dictionary, locality_dictionary)
    return messages

def agendacenter2(locality_dictionary):
    from webscraping_dictionaries import agendacenter2_dictionary, meetings_tags
    driver.get(agendacenter2_dictionary[locality_dictionary]['url'])
    time.sleep(5)
    messages =[]
    table_rows = driver.find_elements(By.CSS_SELECTOR, meetings_tags['agendacenter'])
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
            agenda_content = get_agenda_content(agendacenter2_dictionary[locality_dictionary]['agenda_content'])
            readable = check_agenda_readability(agenda_content)
            if readable == True:
                agenda_search = search_text_for_keywords(agenda_content)
                if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + agendacenter2_dictionary[locality_dictionary]['name'] + ". " + link)
            elif readable ==False:
                messages.append("New meeting document available for "+ agendacenter2_dictionary[locality_dictionary]['name'] + ". " + "Document cannot be scanned for keywords. " + link)
    #if agendacenter_dictionary[locality_dictionary]['agenda_type']=='webpage':
        #messages = search_webpage(agenda_links, agendacenter2_dictionary, locality_dictionary)
    return messages

"""BoardDocs"""
def check_boarddocs_agendas(locality_dictionary):
    from webscraping_dictionaries import boarddocs_dictionary
    all_tabs=driver.find_elements(By.CSS_SELECTOR,"a[id*=ui-id-")
    meetings_tab = [item for item in all_tabs if item.text in ['MEETINGS','Meetings']]
    meetings_tab[0].click()
    time.sleep(10)
    #get all the meeting links
    all_meetings = driver.find_elements(By.CSS_SELECTOR, "a[class*='icon prevnext meeting")
    update_messages = []
    future_meetings = []
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
            update_messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + boarddocs_dictionary[locality_dictionary]['name'] + " in " + meeting_title + ". " + boarddocs_dictionary[locality_dictionary]['url'])
        meetings_tab[0].click()
        time.sleep(10)
    return update_messages

def boarddocs(locality_dictionary):
    from webscraping_dictionaries import boarddocs_dictionary
    driver.get(boarddocs_dictionary[locality_dictionary]['url'])
    time.sleep(10)
    messages = check_boarddocs_agendas(locality_dictionary)
    if boarddocs_dictionary[locality_dictionary]['second_page']==True:
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

"CivicClerk"
def civicclerk(locality_dictionary):
    from webscraping_dictionaries import civicclerk_dictionary,meetings_tags
    messages=[]
    driver.get(civicclerk_dictionary[locality_dictionary]['url'])
    time.sleep(10)
    all_meetings = driver.find_elements(By.CSS_SELECTOR,meetings_tags['civicclerk'])
    meetings_with_agendas = []
    for item in all_meetings:
        try:
            #test if there's a download button, indicating agenda files have been posted. Lack of files to scan will throw an error, and we won't waste time checking that meeting link for keywords
            #consider making this a dictionary of options as well
            item.find_element(By.CSS_SELECTOR,"button[id*=downloadFilesMenu")
            meetings_with_agendas.append(item)
        except:
            continue
    future_meetings = [item.find_element(By.CSS_SELECTOR,"a").get_attribute("href")  for item in meetings_with_agendas if check_meeting_date(search_dates(item.text)[1][0])==True]
    for item in future_meetings:
        driver.get(item)
        time.sleep(10)
        #don't rely on this to always be the same, turn this into a dictionary of options, even if there's only one current option. It has changed in the past, it can change again.
        pdf_viewer_frame = driver.find_elements(By.CSS_SELECTOR,"iframe[id*=pdfViewerIframe")
        if pdf_viewer_frame != []:
            driver.switch_to.frame(pdf_viewer_frame[0])
            agenda_content = get_agenda_content(civicclerk_dictionary[locality_dictionary]['agenda_content'])
            readable=check_agenda_readability(agenda_content)
            if readable ==True:
                agenda_search = search_text_for_keywords(agenda_content)
                if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + civicclerk_dictionary[locality_dictionary]['name'] + ". " + item)
            elif readable ==False:
                messages.append("New meeting document available for " + civicclerk_dictionary[locality_dictionary]['name'] + ". " + "Document cannot be scanned for keywords. " + item)
    return messages
    
"""CivicWeb"""
def civicweb(locality_dictionary):
    from webscraping_dictionaries import civicweb_dictionary,meetings_tags, agenda_content_tags
    driver.get(civicweb_dictionary[locality_dictionary]['url'])
    time.sleep(10)  
    all_meetings = driver.find_elements(By.CSS_SELECTOR,meetings_tags['civicweb'])
    relevant_meetings = [item for item in all_meetings if "Board of Supervisors" in item.text or "Planning Commission" in item.text or "City Council" in item.text]
    future_meetings = []
    for item in relevant_meetings:
        if search_dates(item.text) != None:
            try:
                if check_meeting_date(search_dates(item.text)[1][0])==True:
                    future_meetings.append(item.get_attribute("href"))
            except:
                if check_meeting_date(search_dates(item.text)[0][0])==True:
                    future_meetings.append(item.get_attribute("href"))
    messages = []
    for item in future_meetings:
        driver.get(item)
        time.sleep(10)
        #switch to the agenda viewer frame
        agenda_frame = driver.find_element(By.CSS_SELECTOR,"iframe")
        driver.switch_to.frame(agenda_frame)
        agenda_content = driver.find_elements(By.CSS_SELECTOR,agenda_content_tags['civicweb'])
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + civicweb_dictionary[locality_dictionary]['name'] + ". " + item)
    return messages

"""DocumentCenter"""
def document_center(locality_dictionary):
    from webscraping_dictionaries import document_center_dictionary
    driver.get(document_center_dictionary[locality_dictionary]['url'])
    time.sleep(10)  
    messages = []
    folders = driver.find_elements(By.CSS_SELECTOR,"div[class*='ant-tree-treenode'")
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
    agenda_content = get_agenda_content(document_center_dictionary[locality_dictionary]["content_tag"])
    readable = check_agenda_readability(agenda_content)
    if readable == True:
        agenda_search = search_text_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for "+ document_center_dictionary[locality_dictionary]['name'] + ". " + latest_agenda)
    elif readable == False:
        messages.append("New meeting document available for " + document_center_dictionary[locality_dictionary]["name"] + ". Document cannot be scanned for keywords. " + latest_agenda)
    return messages

"""eScribe"""
def escribe(locality_dictionary):
    from webscraping_dictionaries import escribe_dictionary
    driver.get(escribe_dictionary[locality_dictionary]['url'])
    time.sleep(10)
    messages = []
    future_meetings = driver.find_elements(By.CSS_SELECTOR,"div[class*='upcoming-meeting-container'")
    #since all the posted meetings are upcoming meetings, we can skip checking the date
    for item in future_meetings:
        try:
            agenda_link = item.find_element(By.CSS_SELECTOR,'a[aria-label*="Agenda Cover Page"')
            agenda_url = agenda_link.get_attribute("href")
            agenda_link.click()
            time.sleep(10)
            agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
            agenda_search = search_agenda_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + escribe_dictionary[locality_dictionary]['name'] +  ". " + agenda_url)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        except:
            continue
    return messages

"""Granicus"""
def granicus_version_2(locality_dictionary):
    from webscraping_dictionaries import granicus_2_dictionary
    driver.get(granicus_2_dictionary[locality_dictionary]['url'])
    time.sleep(10)
    messages = []
    table_rows = driver.find_elements(By.CSS_SELECTOR, 'div[class*=RowTop')
    future_meetings = [item.find_element(By.CSS_SELECTOR,"a[href*='Citizens/Detail_Meeting'").get_attribute("href") for item in table_rows if check_meeting_date(item.text)==True]
    for item in future_meetings:
            driver.get(item)
            time.sleep(10)
            try:
                agenda_link = driver.find_element(By.CSS_SELECTOR,"a[id*=PublicAgendaFile").get_attribute("href")
                driver.get(agenda_link)
                time.sleep(10)
                agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
                agenda_search = search_agenda_for_keywords(agenda_content)
                if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) +" found in upcoming meeting for " + granicus_2_dictionary[locality_dictionary]['name'] + ". " + agenda_link)
            except:
                continue
    return messages

def granicus(locality_dictionary):
    from webscraping_dictionaries import granicus_dictionary
    driver.get(granicus_dictionary[locality_dictionary]['url'])
    time.sleep(10)
    messages=[]
    #gets all the table rows that contain meeting entries
    table_rows=driver.find_elements(By.CSS_SELECTOR,"tr[class*=listingRow")
    #narrowing down to just future dates
    for item in table_rows:
        try:
            meeting_date = item.find_elements(By.CSS_SELECTOR,"td")[1].text.split("-")[0]
            future_date = check_meeting_date(meeting_date)
            if future_date == True:
                try:
                    #check to see if the agenda or agenda packet is available
                    agenda_packet = item.find_element(By.CSS_SELECTOR,"a[href*='.pdf'")
                    agenda_url = agenda_packet.get_attribute("href")
                    agenda_packet.click()
                    time.sleep(10)
                    driver.switch_to.window(driver.window_handles[1])
                    agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
                    agenda_search = search_agenda_for_keywords(agenda_content)
                    if agenda_search != []:
                        messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + granicus_dictionary[locality_dictionary]['name'] + ". " + agenda_url)
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                except:
                    continue 
            else:
                break
        except:
            continue
    return messages

"LaserFiche" #not finding the keyword present in the 05/20/25 meeting
def laserfiche(locality_dictionary):
    from webscraping_dictionaries import laserfiche_dictionary
    driver.get(laserfiche_dictionary[locality_dictionary]['url'])
    time.sleep(10)
    messages=[]
    frame = driver.find_element(By.CSS_SELECTOR,"iframe[name=frame1")
    driver.switch_to.frame(frame)
    year_folders = driver.find_elements(By.CSS_SELECTOR,"td")
    #find the folder for the current yeaer
    current_folder = [item for item in year_folders if item.text==str(datetime.today().year)]
    current_folder_link = current_folder[0].find_element(By.CSS_SELECTOR,"a").get_attribute('href')
    meeting_folders = driver.find_elements(By.CSS_SELECTOR,"tr")
    driver.get(current_folder_link)
    time.sleep(10)
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
        agenda_link = driver.find_element(By.CSS_SELECTOR,"a[href*='Agenda.pdf'").get_attribute('href')
        #turn this into a replicable method for whenever downloads come up
        agenda_file = requests.get(agenda_link, allow_redirects=True)
        temp_agenda = tempfile.TemporaryFile()
        temp_agenda.write(agenda_file.content)
        agenda_pdf = PdfReader(temp_agenda)
        agenda_pages = agenda_pdf.pages
        #join the text of each page with a new line symbol into one object of text for the agenda content
        agenda_content = "\n".join([item.extract_text() for item in agenda_pages])
        #Since this is a string not a webdriver item, this can't use the existing search_agenda_for_keywords function
        #replace with search_text_for_keywords function
        keywords=[]
        if 'Solar' in agenda_content or 'solar' in agenda_content:
            keywords.append('Solar')
        if 'Comprehensive Plan' in agenda_content or 'Comprehensive plan' in agenda_content or 'comprehensive plan' in agenda_content:
            keywords.append('Comprehensive Plan')
        if 'Zoning Ordinance' in agenda_content or 'Zoning ordinance' in agenda_content or 'zoning ordinance' in agenda_content:
            keywords.append('Zoning Ordinance')
        if keywords!=[]:
            messages.append('Keyword(s) ' + ", ".join(keywords)+' found in upcoming meeting for ' + laserfiche_dictionary[locality_dictionary]['name'] + '. ' + agenda_link)
        #close and delete the temp file
        temp_agenda.close()
    return messages               

"""Legistar"""
def legistar(locality_dictionary):
    from webscraping_dictionaries import legistar_dictionary
    url_test = verify_url(legistar_dictionary[locality_dictionary]['url'])
    messages = []
    if url_test == True:
        driver.get(legistar_dictionary[locality_dictionary]['url'])
        time.sleep(10)
        table_rows = driver.find_elements(By.CSS_SELECTOR,'tr[id*=ctl00_')
        future_meetings = [item for item in table_rows if check_meeting_date(search_dates(item.text)[0][0])==True]
        meeting_urls = [item.find_element(By.CSS_SELECTOR,"a[id*=hypMeetingDetail").get_attribute('href') for item in future_meetings]
        for item in meeting_urls:
            if item != None:
                driver.get(item)
                time.sleep(10)
                agenda_content = driver.find_elements(By.CSS_SELECTOR,'tr[id*=ctl00')
                agenda_search = search_agenda_for_keywords(agenda_content)
                if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + legistar_dictionary[locality_dictionary]['name'] + ". " + item)
        return messages
    else:
        return url_test

"Links by Year" #see dictionary entry for explanation on website commonalities
def links_by_year(locality_dictionary):
    from webscraping_dictionaries import links_by_year_dictionary
    driver.get(links_by_year_dictionary[locality_dictionary]['url'])
    time.sleep(10)
    messages = []
    #the year links will be stored as list items
    list_items = driver.find_elements(By.CSS_SELECTOR,"li")
    #this will catch the list entry that represents the current year
    current_year = [item for item in list_items if str(datetime.date(datetime.now()).year) in item.text]
    #now navigate to the agenda page for the current year
    driver.get(current_year[0].find_element(By.CSS_SELECTOR,"a").get_attribute("href"))
    #find all the agenda document links
    links = driver.find_elements(By.CSS_SELECTOR,links_by_year_dictionary[locality_dictionary]['agenda_link_tag'])
    future_meetings = []
    for item in links:
        try:
            if search_dates(item.text,languages=['en']) != None:
                if check_meeting_date(search_dates(item.text)[0][0])==True:
                    future_meetings.append(item.get_attribute('href'))
        except:
            continue
    for link in future_meetings:
        driver.get(link)
        time.sleep(10)
        #one is a page, the other is a PDF, so the agenda content is stored in site-specific tags as recorded in the dictionary
        agenda_content = driver.find_elements(By.CSS_SELECTOR,links_by_year_dictionary[locality_dictionary]['agenda_content_tag'])
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + links_by_year_dictionary[locality_dictionary]['name'] + ". " + link)
    return messages

"""Meetings Table"""
def meetings_table(locality_dictionary):
    from webscraping_dictionaries import meetingstable_dictionary
    driver.get(meetingstable_dictionary[locality_dictionary]['url'])
    time.sleep(10)
    messages = []
    all_rows = driver.find_elements(By.CSS_SELECTOR,meetingstable_dictionary[locality_dictionary]['meetings_tag'])[1:]
    future_meetings = []
    for item in all_rows:
        if search_dates(item.text) != None:
            future_meeting = check_meeting_date(search_dates(item.text)[0][0])
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
            agenda_content = get_agenda_content(meetingstable_dictionary[locality_dictionary]['agenda_content_tag'])
            readable = check_agenda_readability(agenda_content)
            if readable == True:
                agenda_search = search_text_for_keywords(agenda_content)
                if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + meetingstable_dictionary[locality_dictionary]['name'] + ". " + item)
            elif readable == False:
                messages.append('New agenda available for upcoming meeting in ' + meetingstable_dictionary[locality_dictionary]['name'] + ". Document cannot be scanned for keywords. " + item)
    return messages

"""NovusAGENDA"""
def novusagenda(locality_dictionary):
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
    
"""OnBase"""
def onbase(locality_dictionary):
    from webscraping_dictionaries import onbase_dictionary
    messages=[]
    driver.get(onbase_dictionary[locality_dictionary]['url'])
    time.sleep(10)
    table_rows = driver.find_elements(By.CSS_SELECTOR,"tr")
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
        agenda_content=driver.find_elements(By.CSS_SELECTOR, "body")
        agenda_search=search_agenda_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + onbase_dictionary[locality_dictionary]['name'] + ". " + item)
    return messages
    
"""PHP Table"""
def php_table(locality_dictionary):
    from webscraping_dictionaries import php_table_dictionary
    driver.get(php_table_dictionary[locality_dictionary]['url'])
    time.sleep(10)
    messages = []
    table_rows = driver.find_elements(By.CSS_SELECTOR,'tr')
    future_meetings = []
    for item in table_rows:
        try:
            future=check_meeting_date(search_dates(item.text)[0][0])
            if future==True:
                future_meetings.append(item)
        except:
            continue
    future_agendas = [item.find_element(By.CSS_SELECTOR, "a[href*='.pdf'").get_attribute('href') for item in future_meetings if php_table_dictionary[locality_dictionary]['web_document'] in item.text]
    if future_agendas !=[]:
        for agenda_link in future_agendas:
            driver.get(agenda_link)
            time.sleep(20)
            agenda_content = get_agenda_content("div[class*=textLayer")
            readable = check_agenda_readability(agenda_content)
            if readable == True:
                agenda_search = search_text_for_keywords(agenda_content)
                if agenda_search !=[]:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + php_table_dictionary[locality_dictionary]['name'] + ". " + agenda_link)
            elif readable == False:
                messages.append("New meeting agenda available for " + php_table_dictionary[locality_dictionary]['name'] + ". Document cannot be scanned for keywords. " + agenda_link)
    return messages

"""PrimeGov"""
def prime_gov(locality_dictionary):
    from webscraping_dictionaries import primegov_dictionary
    driver.get(primegov_dictionary[locality_dictionary]['url'])
    time.sleep(10)
    messages=[]
    #find all the table rows
    table_rows = driver.find_elements(By.CSS_SELECTOR,'tr[role*=row')
    #filter for upcoming meetings
    upcoming_meetings=[]
    for item in table_rows:
        try:
            date_test = check_meeting_date(item.text)
            if date_test == True:
                upcoming_meetings.append(item)
        except:
            continue
    #if we have any upcoming meetings at all:
    if upcoming_meetings != []:
        #for each row of information in an upcoming meeting, take the following steps:
            #read the pdf from the link
            #search the pdf text for keywords
            #if a keyword is present, add the meeting info and document link to the message list
            #if not, move to the next item
        for item in upcoming_meetings:
            agenda_link = item.find_element(By.CSS_SELECTOR,"a[class*=document").get_attribute('href')
            #download the agenda link
            agenda_file = requests.get(agenda_link, allow_redirects=True)
            #write the content to a temporary file
            temp_agenda = tempfile.TemporaryFile()
            temp_agenda.write(agenda_file.content)
            #use PDFQuery to parse the PDF
            agenda_pdf = PdfReader(temp_agenda)
            agenda_page = agenda_pdf.pages[0]
            agenda_content = agenda_page.extract_text()
            #Since this is a string not a webdriver item, this can't use the existing search_agenda_for_keywords function
            keywords=[]
            if 'Solar' in agenda_content:
                keywords.append('Solar')
            if 'solar' in agenda_content:
                keywords.append('solar')
            if keywords!=[]:
                messages.append('Keyword(s) ' + ", ".join(keywords)+' found in upcoming meeting for ' + primegov_dictionary[locality_dictionary]['name'] + '. ' + agenda_link)
            #close and delete the temp file
            temp_agenda.close()
    return messages

"""Locality Specific Functions"""

"""Albemarle County"""
def albemarle_county_pc():
    from webscraping_dictionaries import locality_dictionary_single_use
    messages=[]
    driver.get(locality_dictionary_single_use['Albemarle PC']['url'])
    time.sleep(10)
    table_rows = driver.find_elements(By.CSS_SELECTOR, "tr")
    #page we're looking at only has upcoming meetings, so no need to check the date
    meeting_links = []
    for item in table_rows:
        try:
            meeting_links.append(item.find_element(By.CSS_SELECTOR,"a[href*=Calendar").get_attribute("href"))
        except:
            continue
    for item in meeting_links:
        driver.get(item)
        time.sleep(10)
        try:
            document_links = driver.find_elements(By.CSS_SELECTOR,"a[href*=showpublisheddocument")
            agenda_link = [item.get_attribute("href") for item in document_links if "Agenda" in item.text]
            driver.get(agenda_link[0])
            time.sleep(10)
            agenda_content = get_agenda_content(locality_dictionary_single_use['Albemarle PC']['content_tag'])
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


"""Alleghany County"""
#only BOS agendas are available
def alleghany_county():
    from webscraping_dictionaries import locality_dictionary_single_use
    messages=[]
    url_test = verify_url(locality_dictionary_single_use['Alleghany BOS']['url'])
    if url_test==True:
        driver.get(locality_dictionary_single_use['Alleghany BOS']['url'])
        time.sleep(10)
        #hunt down the agenda links
        all_agenda_links = driver.find_elements(By.CSS_SELECTOR,"a[class*='attachment-link'")
        future_meetings = [item.get_attribute('href') for item in all_agenda_links if check_meeting_date(item.text)==True]
        for item in future_meetings:
            driver.get(item)
            time.sleep(10)
            agenda_content = get_agenda_content(locality_dictionary_single_use['Alleghany BOS']["content_tag"])
            readable = check_agenda_readability(agenda_content)
            if readable == True:
                agenda_search = search_text_for_keywords(agenda_content)
                if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Alleghany County Board of Supervisors. " + item)
            elif readable==False:
                messages.append("New meeting document available for Alleghany County Board of Supervisors. Document cannot be scanned for keywords. " + item)
        return messages
    else:
        return url_test

"""Amelia County"""
def amelia_pc():
    from webscraping_dictionaries import locality_dictionary_single_use
    messages=[]
    driver.get(locality_dictionary_single_use['Amelia PC']['url'])
    agendas = driver.find_elements(By.CSS_SELECTOR,'a[href*="Packet.pdf"')
    future_meetings=[]
    for item in agendas:
            if item.text != '':
                if check_meeting_date(item.text)==True:
                    future_meetings.append(item.get_attribute('href'))
    for item in future_meetings:
        driver.get(item)
        time.sleep(10)
        agenda_content = get_agenda_content(locality_dictionary_single_use['Amelia PC']['content_tag'])
        readable = check_agenda_readability(agenda_content)
        if readable == True:
            agenda_search = search_text_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Amelia County Planning Commission. " + item)
        elif readable == False:
            messages.append("New meeting document available for Amelia County Planning Commission. Document cannot be scanned for keywords. " + item)
    return messages

"""Bath County"""
def bath_county(locality_dictionary):
    from webscraping_dictionaries import locality_dictionary_multi_use
    driver.get(locality_dictionary_multi_use[locality_dictionary]['url'])
    time.sleep(10)
    messages = []
    archive_pages = driver.find_elements(By.CSS_SELECTOR,'a[class*="pageButton number"')
    valid_pages = [item for item in archive_pages if item.text !='']
    valid_pages[-1].click()
    time.sleep(5)
    years = driver.find_elements(By.CSS_SELECTOR,"div[class*='item docTitle")
    current_year = [item for item in years if str(datetime.date(datetime.now()).year) in item.text]
    current_year[0].click()
    time.sleep(5)
    minutes_pages = driver.find_elements(By.CSS_SELECTOR,'a[class*="pageButton number"')
    valid_minutes_pages = [item for item in minutes_pages if item.text !='']
    if valid_minutes_pages[-1].text != '1':
        valid_minutes_pages[-1].click()
        time.sleep(5)
    minutes = driver.find_elements(By.CSS_SELECTOR,"a[class*='docItemTitle")
    latest_minutes = minutes[-1].get_attribute('href')
    driver.get(latest_minutes)
    time.sleep(10)
    agenda_content = get_agenda_content(locality_dictionary_multi_use[locality_dictionary]['content_tag'])
    readable = check_agenda_readability(agenda_content)
    if readable == True:
        agenda_search = search_text_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + locality_dictionary_multi_use[locality_dictionary]['name'] + ". " + latest_minutes)
    elif readable ==False:
        messages.append("New meeting document available for "+ locality_dictionary_multi_use[locality_dictionary]['name'] + ". " + "Document cannot be scanned for keywords. " + latest_minutes)
    return messages

"""Bland County"""
def bland_county():
    from webscraping_dictionaries import locality_dictionary_single_use
    url_check = verify_url(locality_dictionary_single_use['Bland']['url'])
    if url_check == True:
        driver.get(locality_dictionary_single_use['Bland']['url'])
        time.sleep(10)
        messages = []
        #get all the table rows
        table_rows = driver.find_elements(By.CSS_SELECTOR,"tr")
        #filter for just the ones where agendas are posted
        posted_agendas = [item for item in table_rows if "AGENDA" in item.text]
        #check the date for the last posted meeting
        try: 
            future_meeting = check_meeting_date(search_dates(posted_agendas[-1].text)[0][0])
        except:
            future_meeting=None
        if future_meeting == True:
            agenda_url = future_meeting.find_element(By.CSS_SELECTOR,"a").get_attribute("href")
            #as of 05/23/25, Bland County still posts scanned documents that are not yet readable by this webscraper
            messages.append("New meeting agenda available for Bland County Board of Supervisors. Document cannot be scanned for keywords. " + agenda_url)
    else:
        messages.append(url_check)
    return messages

"Brunswick County"
def brunswick_county():
    from webscraping_dictionaries import locality_dictionary_single_use
    messages=[]
    driver.get(locality_dictionary_single_use['Brunswick']['url'])
    time.sleep(10)
    pdfs = driver.find_elements(By.CSS_SELECTOR,'a[href*=".pdf"')
    future_meeting = [item.get_attribute("href") for item in pdfs if item.text != "" and item.text != " " and check_meeting_date(item.text) == True]
    for item in future_meeting:
        driver.get(item)
        time.sleep(10)
        agenda_content = get_agenda_content(locality_dictionary_single_use['Brunswick']['content_tag'])
        readable = check_agenda_readability(agenda_content)
        if readable == True:
            agenda_search = search_text_for_keywords(agenda_content)
            if agenda_search !=[]:
                messages.append('Keyword(s) ' + ", ".join(agenda_search)+' found in upcoming meeting for Brunswick County. ' + item)
        elif readable == False:
            messages.append('New meeting document available for Brunswick County. Document cannot be scanned for keywords' + item)
    return messages

"""Buchanan County"""
def buchanan_county():
    from webscraping_dictionaries import locality_dictionary_single_use
    driver.get(locality_dictionary_single_use['Buchanan']['url'])
    time.sleep(10)
    messages = []
    pdf_links = driver.find_elements(By.CSS_SELECTOR,"a[href*='.pdf")
    latest_minutes = [item for item in pdf_links if "Minutes" in item.text][0]
    #since they're only posting minutes not agendas, and minutes are posted long after the fact, we'll skip the date checking
    minutes_url = latest_minutes.get_attribute("href")
    driver.get(minutes_url)
    time.sleep(10)
    agenda_content = get_agenda_content(locality_dictionary_single_use['Buchanan']['content_tag'])
    readable = check_agenda_readability(agenda_content)
    if readable == True:
        agenda_search = search_text_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Buchanan County Board of Supervisors. " + minutes_url)
    elif readable == False:
        messages.append('New meeting document available for Buchanan County. Document cannot be scanned for keywords' + minutes_url)
    return messages   

"""Buena Vista City Council"""
def buena_vista_city_council():
    from webscraping_dictionaries import locality_dictionary_single_use
    driver.get(locality_dictionary_single_use['Buena Vista City Council']['url'])
    time.sleep(10)
    messages = []
    links = driver.find_elements(By.CSS_SELECTOR,"a[href*=sharepoint")
    future_meetings = []
    for link in links:
        if link.text != "2025 City Council Schedule":
            try:
                future = check_meeting_date(link.text)
                if future == True:
                    future_meetings.append(link.get_attribute('href'))
            except:
                continue
    for item in future_meetings:
        messages.append("New agenda available for Buena Vista City Council. Document cannot be scanned for keywords. " + item)
    return messages

"""Town of Clifton Forge"""
def clifton_forge():
    from webscraping_dictionaries import locality_dictionary_single_use
    driver.get(locality_dictionary_single_use['Clifton Forge']['url'])
    time.sleep(10)
    messages = []
    latest_year = driver.find_element(By.CSS_SELECTOR,"button[id*='de-accordion")
    latest_year.click()
    agenda_links = driver.find_elements(By.CSS_SELECTOR,'a[href*=".pdf"')
    active_links = [item for item in agenda_links if item.text != '']
    future_meetings = [item.get_attribute('href') for item in active_links if check_meeting_date(search_dates(item.text)[0][0])==True]
    for link in future_meetings:
        driver.get(link)
        time.sleep(10)
        agenda_content = get_agenda_content(locality_dictionary_single_use['Clifton Forge']['content_tag'])
        readable = check_agenda_readability(agenda_content)
        if readable==True:
            agenda_search = search_text_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for the Town of Clifton Forge. " + link)
        elif readable == False:
            messages.append("New agenda available for Town of Clifton Forge. Document cannot be scanned for keywords. " + link)
    return messages

"""Town of Covington""" #new site design, code needs an update but nothing useful is posted yet
def covington():
    from webscraping_dictionaries import locality_dictionary_single_use
    driver.get(locality_dictionary_single_use["Covington"]["url"])
    time.sleep(10)
    messages = []
    year_expand = driver.find_elements(By.CSS_SELECTOR, "div[class*='accordion-item'")
    #the labels won't show up, but the latest year will be the first one
    year_expand[0].click()
    time.sleep(10)
    pdfs = driver.find_elements(By.CSS_SELECTOR,"a[href*='.pdf'")
    agendas = [item for item in pdfs if "Agenda" in item.text]
    future_meetings = [item.get_attribute("href") for item in agendas if check_meeting_date(item.text)==True]
    for item in future_meetings:
        driver.get(item)
        time.sleep(10)
        agenda_content = driver.find_elements(By.CSS_SELECTOR,'div[class*=textLayer')
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for the Town of Covington. " + item)
    return messages

"Craig County"
def craig_county():
    from webscraping_dictionaries import locality_dictionary_single_use
    messages = []
    driver.get(locality_dictionary_single_use['Craig']['url'])
    time.sleep(10)
    #Find the link and check the date. That's as far as we go because the PDFs are scans.
    links = driver.find_elements(By.CSS_SELECTOR,'a')
    agenda_links = [item for item in links if 'Agenda' in item.text]
    future_meetings = [item.get_attribute('href') for item in agenda_links if check_meeting_date(search_dates(item.text)[0][0])==True]
    for item in future_meetings:
        messages.append("New meeting agenda available for Craig County Board of Supervisors. Document cannot be scanned for keywords. " + item)
    return messages

"""Fairfax County"""
def fairfax_county_bos():
    from webscraping_dictionaries import locality_dictionary_single_use
    driver.get(locality_dictionary_single_use['Fairfax BOS']['url'])
    time.sleep(10)
    messages = []
    meetings = driver.find_elements(By.CSS_SELECTOR,"div[class*='calendar-title'")
    meeting_urls = []
    for item in meetings:
        meeting_urls.append(item.find_element(By.CSS_SELECTOR,"a").get_attribute("href"))
    for item in meeting_urls:
        driver.get(item)
        time.sleep(10)
        try:
            agenda_link = driver.find_element(By.CSS_SELECTOR,"a[href*='.pdf'").get_attribute("href")
            driver.get(agenda_link)
            time.sleep(10)
            agenda_content = get_agenda_content(locality_dictionary_single_use['Fairfax BOS']['agenda_content_tag'])
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
    driver.get(locality_dictionary_single_use['Fairfax PC']['url'])
    time.sleep(10)
    messages = []
    latest_year = driver.find_element(By.CSS_SELECTOR,"table[align*=center")
    months = latest_year.find_elements(By.CSS_SELECTOR,"td[align*=center")
    current_month = [item.find_element(By.CSS_SELECTOR,"a").get_attribute('href') for item in months if item.text == datetime.now().strftime("%B")]
    driver.get(current_month[0])
    time.sleep(10)
    agenda_links = driver.find_elements(By.CSS_SELECTOR,"a[href*='.pdf'")
    agenda_urls = [item.get_attribute("href") for item in agenda_links]
    for item in agenda_urls:
        try:
            future = check_meeting_date(item.split('/')[-1].split('.pdf')[0])
            if future==True:
                driver.get(item)
                time.sleep(10)
                agenda_content = get_agenda_content(locality_dictionary_single_use['Fairfax PC']['content_tag'])
                readable = check_agenda_readability(agenda_content)
                if readable == True:
                    agenda_search = search_text_for_keywords(agenda_content)
                    if agenda_search != []:
                        messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Fairfax County Planning Commission. " + item)
                elif readable == False:
                    messages.append("New agenda available for upcoming meeting in Fairfax County Planning Commission. Document cannot be scanned for keywords. " + item)
        except:
            driver.get(item)
            time.sleep(10)
            agenda_content = get_agenda_content(locality_dictionary_single_use['Fairfax PC']['content_tag'])
            readable = check_agenda_readability(agenda_content)
            if readable == True:
                agenda_search = search_text_for_keywords(agenda_content)
                if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Fairfax County Planning Commission. " + item)
            elif readable == False:
                messages.append("New agenda available for upcoming meeting for Fairfax County Planning Commission. Document cannot be scanned for keywords. " + item)
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
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Floyd County Board of Supervisors. " + agenda_url)
    return messages

"""City of Franklin"""
def city_of_franklin():
    from webscraping_dictionaries import locality_dictionary_single_use
    driver.get(locality_dictionary_single_use['Franklin']['url'])
    time.sleep(10)
    messages=[]
    #this website requires several steps to get to the right data, as it automatically lands on the 2013 agendas page
    years = driver.find_elements(By.CSS_SELECTOR,'li[class*="top-tab"')
    latest_year = years[-1]
    latest_year.click()
    time.sleep(10)
    months = driver.find_elements(By.CSS_SELECTOR,'tr[class*="month-label"')
    current_month = months[-1]
    if current_month.text.strip() != 'January':
        current_month.click()
        time.sleep(10)
    pdf_links = driver.find_elements(By.CSS_SELECTOR, "a[href*='.pdf'")
    agendas = [pdf for pdf in pdf_links if pdf.text != '']
    future_meetings = [agenda.get_attribute('href') for agenda in agendas if check_meeting_date(agenda.text) == True]
    for agenda_link in future_meetings:
        driver.get(agenda_link)
        time.sleep(10)
        agenda_content = get_agenda_content(locality_dictionary_single_use['Franklin']['content_tag'])
        readable = check_agenda_readability(agenda_content)
        if readable==True:
            agenda_search = search_text_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for the City of Franklin. " + agenda_link)
        elif readable == False:
            messages.append("New agenda available for upcoming meeting for the City of Franklin. Document cannot be scanned for keywords" + agenda_link)
    return messages

"""City of Galax"""
def galax():
    from webscraping_dictionaries import locality_dictionary_single_use
    driver.get(locality_dictionary_single_use['Galax']['url'])
    time.sleep(10)
    messages = []
    agenda_links = driver.find_elements(By.CSS_SELECTOR,"a[class*='pb_button'")
    latest_agenda = agenda_links[len(agenda_links) - 1]
    future_meeting = check_meeting_date(latest_agenda.text)
    if future_meeting == True:
        #ccome back and check necessity of this switch window thing, can't I just use driver.get(href)?
        agenda_url = latest_agenda.get_attribute("href")
        latest_agenda.click()
        time.sleep(10)
        driver.switch_to.window(driver.window_handles[1])
        agenda_content = get_agenda_content(locality_dictionary_single_use['Galax']['content_tag'])
        readable = check_agenda_readability(agenda_content)
        if readable == True:
            agenda_search = search_text_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for the City of Galax. " + agenda_url)
        elif readable == False:
            messages.append("New document available for upcoming meeting for City of Galax. Document could not be scanned for keywords. " + agenda_url)
    return messages

"""Giles County Board of Supervisors"""
def giles_county():
    from webscraping_dictionaries import locality_dictionary_single_use
    driver.get(locality_dictionary_single_use['Giles']['url'])
    time.sleep(10)
    messages = []
    #follow the link to the latest agenda
    agenda_link = driver.find_element(By.CSS_SELECTOR,'a[class*="qbutton"').get_attribute("href")
    driver.get(agenda_link)
    time.sleep(10)
    agenda_content = get_agenda_content(locality_dictionary_single_use["Giles"]["content_tag"])
    readable = check_agenda_readability(agenda_content)
    if readable==True:
        agenda_search = search_text_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Giles County in next agenda. " + agenda_link)
    elif readable == False:
        messages.append("New document available for upcoming meeting for Giles County. Document cannot be scanned for keywords. " + agenda_link)
    return messages


"""Greensville County"""
def greensville_county(locality_dictionary):
    from webscraping_dictionaries import locality_dictionary_multi_use
    driver.get(locality_dictionary_multi_use[locality_dictionary]['url'])
    time.sleep(10)
    messages = []
    latest_year = driver.find_element(By.CSS_SELECTOR,"h3[class*='docs-toggle'")
    latest_year.click()
    time.sleep(10)
    agenda_tab = driver.find_element(By.CSS_SELECTOR,"h4[class*='docs-toggle'")
    agenda_tab.click()
    time.sleep(10)
    pdf_links = driver.find_elements(By.CSS_SELECTOR,"a[href*='.pdf'")
    current_links = [item for item in pdf_links if item.text != '']
    future_meetings = []
    for item in current_links:
        if search_dates(item.text) != None:
            if check_meeting_date(search_dates(item.text)[0][0])==True:
                future_meetings.append(item.get_attribute('href'))
    for item in future_meetings:
        driver.get(item)
        time.sleep(10)
        agenda_content = get_agenda_content(locality_dictionary_multi_use[locality_dictionary]["content_tag"])
        readable = check_agenda_readability(agenda_content)
        if readable==True:
            agenda_search = search_text_for_keywords(agenda_content)
            if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) +  " found in upcoming meeting for " + locality_dictionary_multi_use[locality_dictionary]['name'] + ". " + item )
        elif readable==False:
             messages.append("New meeting agenda available for " + locality_dictionary_multi_use[locality_dictionary]['name'] + ". Document cannot be scanned for keywords. " + item)
    return messages
    
"""Henrico County"""
def henrico_county_bos():
    from webscraping_dictionaries import locality_dictionary_single_use
    driver.get(locality_dictionary_single_use['Henrico BOS']['url'])
    time.sleep(10)
    messages = []
    #ignore the first entry in the table rows since it's just the column headers
    table_rows = driver.find_elements(By.CSS_SELECTOR,'tr')[1:]
    latest_meeting = table_rows[0]
    future_meeting = check_meeting_date(latest_meeting.text)
    if future_meeting == True:
        meeting_url = latest_meeting.find_element(By.CSS_SELECTOR,"a").get_attribute("href")
        driver.get(meeting_url)
        time.sleep(10)
        agenda_content = get_agenda_content(locality_dictionary_single_use["Henrico BOS"]["content_tag"])
        readable = check_agenda_readability(agenda_content)
        if readable == True:
            agenda_search = search_text_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Henrico County Board of Supervisors. " + meeting_url)
        elif readable == False:
            messages.append("New document available for upcoming meeting for Henrico County. Document cannot be scanned for keywords. " + meeting_url)
    return messages   

def henrico_county_pc(): #make sure to check the BZA current agenda too
    from webscraping_dictionaries import locality_dictionary_single_use
    driver.get(locality_dictionary_single_use['Henrico PC']['url'])
    time.sleep(10)
    messages = []
    current_agendas = driver.find_elements(By.CSS_SELECTOR,"a[href*='next.pdf'")
    #there's not a good way to check the date, so we'll just check the current agendas for the board of zoning appeals
    agenda_urls = []
    for item in current_agendas:
        agenda_urls.append(item.get_attribute("href"))
    for item in agenda_urls:
        driver.get(item)
        time.sleep(10)
        agenda_content = get_agenda_content(locality_dictionary_single_use["Henrico PC"]["content_tag"])
        readable = check_agenda_readability(agenda_content)
        if readable == True:
            agenda_search = search_text_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Henrico County in the latest Planning Commission/Board of Zoning Appeals agenda. " + item)
        elif readable == False:
            messages.append("New document available for upcoming meeting for Henrico County Planning Commission. Document cannot be scanned for keywords. " + item)
    return messages        

"Highland County" #consider addition to Links by Year localities?
#needs review, latest posted agenda was a docx download, also timestamp checking errors
def highland_county_bos():
    from webscraping_dictionaries import locality_dictionary_single_use
    messages = []
    driver.get(locality_dictionary_single_use['Highland BOS']['url'])
    time.sleep(10)
    folders = driver.find_elements(By.CSS_SELECTOR,"a[href*=agenda")
    current_year = [item for item in folders if item.text==str(datetime.now().year)]
    driver.get(current_year[0].get_attribute('href'))
    time.sleep(10)
    meetings = driver.find_elements(By.CSS_SELECTOR,"div[class*='views-row'")
    future_meetings = [item.find_element(By.CSS_SELECTOR,"a").get_attribute("href") for item in meetings if check_meeting_date(item.text) == True]
    for item in future_meetings:
        driver.get(item)
        time.sleep(10)
        agenda_link = driver.find_element(By.CSS_SELECTOR,"a[href*='.pdf'").get_attribute('href')
        driver.get(agenda_link)
        time.sleep(10)
        agenda_content = get_agenda_content(locality_dictionary_single_use["Highland BOS"]["content_tag"])
        readable = check_agenda_readability(agenda_content)
        if readable == True:
            agenda_search = search_text_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Highland County Board of Supervisors. " + agenda_link)
        elif readable == False:
            messages.append("New document available for upcoming meeting for Highland County Board of Supervisors. Document cannot be scanned for keywords. " + agenda_link)
    return messages

"""King and Queen County"""
def king_and_queen_county(locality_dictionary):
    from webscraping_dictionaries import locality_dictionary_multi_use
    driver.get(locality_dictionary_multi_use[locality_dictionary]['url'])
    time.sleep(10)
    messages = []
    table_rows = driver.find_elements(By.CSS_SELECTOR,"tr")
    for item in table_rows:
        try:
            if check_meeting_date(item.text)==True:
                if 'Agenda' in item.text:
                    agenda_link = item.find_elements(By.CSS_SELECTOR,"td")[1].find_element(By.CSS_SELECTOR,'a').get_attribute('href')
                    driver.get(agenda_link)
                    time.sleep(10)
                    agenda_content = get_agenda_content(locality_dictionary_multi_use[locality_dictionary]["content_tag"])
                    readable = check_agenda_readability(agenda_content)
                    if readable == True:
                        agenda_search = search_text_for_keywords(agenda_content)
                        if agenda_search != []:
                            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + locality_dictionary_multi_use[locality_dictionary]['name'] + ". " + agenda_link)
                    elif readable == False:
                        messages.append("New document available for upcoming meeting for " + locality_dictionary_multi_use[locality_dictionary]['name'] + ". Document cannot be scanned for keywords. " + agenda_link )         
        except:
            continue
    return messages

"""Lee County""" #NEW WEBSITE, REDO!!
def lee_county():
    from webscraping_dictionaries import locality_dictionary_single_use
    driver.get(locality_dictionary_single_use['Lee']['url'])
    time.sleep(10)
    messages = []
    all_agenda_links = driver.find_elements(By.CSS_SELECTOR,"a[href*='.pdf'")
    upcoming_meetings = []
    for item in all_agenda_links:
        future_meeting = check_meeting_date(item.text)
        if future_meeting == True:
            upcoming_meetings.append(item)
        else:
            #since all the meeting agendas for the last few years are posted, we don't want to run through all available agendas
            break
    agenda_urls = []
    for item in upcoming_meetings:
        agenda_urls.append(item.get_attribute("href"))
    for item in agenda_urls:
        driver.get(item)
        time.sleep(10)
        agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Lee County Board of Supervisors. " +  item)
    return messages

"""Lexington Planning Commission"""
def lexington_pc():
    from webscraping_dictionaries import locality_dictionary_single_use
    driver.get(locality_dictionary_single_use['Lexington']['url'])
    time.sleep(10)
    messages = []
    list_items = driver.find_elements(By.CSS_SELECTOR,"a[class*='content_link'")
    future_meetings = [item.get_attribute("href") for item in list_items if check_meeting_date(item.text)==True]
    for item in future_meetings:
        driver.get(item)
        time.sleep(10)
        agenda_content = get_agenda_content(locality_dictionary_single_use["Lexington"]["content_tag"])
        readable = check_agenda_readability(agenda_content)
        if readable == True:
            agenda_search = search_text_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for the City of Lexington Planning Commission. " + item)
        elif readable == False:
            messages.append("New document available for upcoming meeting for the City of Lexington. Document cannot be scanned for keywords. " + item)
    return messages

"LaserFiche for Loudoun Planning Commission" #not convinced this is searching the document download properly
def loudoun_pc():
    from webscraping_dictionaries import locality_dictionary_single_use
    driver.get(locality_dictionary_single_use['Loudoun']['url'])
    time.sleep(10)
    messages=[]
    all_links = driver.find_elements(By.CSS_SELECTOR,"a")
    meeting_doc_folder = [item for item in all_links if item.text == 'Public Hearings & Work Sessions']
    driver.get(meeting_doc_folder[0].get_attribute('href'))
    time.sleep(10)
    #find the folder for the current year
    year_folders = driver.find_elements(By.CSS_SELECTOR,"td")
    current_folder = [item for item in year_folders if item.text==str(datetime.today().year)]
    current_folder_link = current_folder[0].find_element(By.CSS_SELECTOR,"a").get_attribute('href')
    driver.get(current_folder_link)
    time.sleep(10)
    meeting_folders = driver.find_elements(By.CSS_SELECTOR,"tr")
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
            agenda_file = requests.get(agenda_link, allow_redirects=True)
            temp_agenda = tempfile.TemporaryFile()
            temp_agenda.write(agenda_file.content)
            agenda_pdf = PdfReader(temp_agenda)
            agenda_pages = agenda_pdf.pages
            #join the text of each page with a new line symbol into one object of text for the agenda content
            agenda_content = "\n".join([item.extract_text() for item in agenda_pages])
            #Since this is a string not a webdriver item, this can't use the existing search_agenda_for_keywords function
            keywords=[]
            if 'Solar' in agenda_content or 'solar' in agenda_content:
                keywords.append('Solar')
            if 'Siting Agreement' in agenda_content or 'siting agreement' in agenda_content or "Siting agreement" in agenda_content:
                keywords.append('Siting Agreement')
            if 'Comprehensive Plan' in agenda_content or 'Comprehensive plan' in agenda_content or 'comprehensive plan' in agenda_content:
                keywords.append('Comprehensive Plan')
            if 'Zoning Ordinance' in agenda_content or 'Zoning ordinance' in agenda_content or 'zoning ordinance' in agenda_content:
                keywords.append('Zoning Ordinance')
            if keywords!=[]:
                keywords = pd.Series(keywords).unique().tolist()
                messages.append('Keyword(s) ' + ", ".join(keywords)+' found in upcoming meeting for  Loudoun County Planning Commission. ' + agenda_link)
            #close and delete the temp file
            temp_agenda.close()
        except:
            continue
    return messages

"""Manassas Park"""
def manassas_park(locality_dictionary):
    from webscraping_dictionaries import locality_dictionary_multi_use
    driver.get(locality_dictionary_multi_use[locality_dictionary]['url'])
    time.sleep(10)
    messages = []
    years = driver.find_elements(By.CSS_SELECTOR,"div[class*='agenda_heading'")
    latest_year = [item for item in years if str(datetime.today().year) in item.text]
    latest_year[0].click()
    time.sleep(10)
    table_rows = driver.find_elements(By.CSS_SELECTOR,"tr")
    future_meetings = []
    for item in table_rows:
        try:
            if check_meeting_date(item.text)==True:
                future_meetings.append(item.find_element(By.CSS_SELECTOR,'a[href*=Agenda').get_attribute("href")) 
        except:
            continue
    for item in future_meetings:
        driver.get(item)
        time.sleep(10)
        agenda_content = get_agenda_content(locality_dictionary_multi_use[locality_dictionary]["content_tag"])
        readable = check_agenda_readability(agenda_content)
        if readable == True:
            agenda_search = search_text_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + locality_dictionary_multi_use[locality_dictionary]['name'] + '. ' + item)
        elif readable == False:
            messages.append("New doccument available for upcoming meeting for " + locality_dictionary_multi_use[locality_dictionary]["name"] + ". Document cannot be scanned for keywords. " + item)
    return messages

"""Nelson County""" #come back and evaluate get_agenda_content viability for this function. Need a version that gets webpage content across any webpage
def nelson_county():
    from webscraping_dictionaries import locality_dictionary_single_use
    driver.get(locality_dictionary_single_use['Nelson']['url'])
    time.sleep(10)
    messages = []
    all_events = driver.find_elements(By.CSS_SELECTOR,'h3')[1:]
    event_urls = []
    for item in all_events:
        try:
            event_urls.append(item.find_element(By.CSS_SELECTOR,'a').get_attribute("href"))
        except:
            continue
    for item in event_urls:
        driver.get(item)
        time.sleep(10)
        event_description = driver.find_elements(By.CSS_SELECTOR,'div[class*="fusion-text"')
        event_search = search_agenda_for_keywords(event_description)
        if event_search !=[]:
            messages.append("Keyword(s) " + ", ".join(event_search) + " found in upcoming meeting for Nelson County. " + item)
    return messages

"""Norton City Council"""
def norton_city():
    from webscraping_dictionaries import locality_dictionary_single_use
    driver.get(locality_dictionary_single_use['Norton']['url'])
    time.sleep(10)
    messages = []
    #start from the second entry, since the first result is the link to view all available archives
    all_agendas = driver.find_elements(By.CSS_SELECTOR,"a[href*=Archive")[1:]
    latest_agenda = all_agendas[0]
    future_meeting = check_meeting_date(latest_agenda.text.split("-")[1])
    if future_meeting == True:
        agenda_url = latest_agenda.get_attribute("href")
        driver.get(agenda_url)
        time.sleep(10)
        agenda_content = get_agenda_content(locality_dictionary_single_use["Norton"]["content_tag"])
        readable = check_agenda_readability(agenda_content)
        if readable == True:
            agenda_search = search_text_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for City of Norton City Council. " + agenda_url)
        elif readable == False:
            messages.apend("New document available for upcoming meeting for City of Norton City Council. Document cannot be scanned for keywords. " + agenda_url)
    return messages

"""Nottoway County"""
def nottoway_county(locality_dictionary):
    from webscraping_dictionaries import locality_dictionary_multi_use
    driver.get(locality_dictionary_multi_use[locality_dictionary]["url"])
    time.sleep(10)
    messages = []
    years = driver.find_elements(By.CSS_SELECTOR,"h3[class*='agenda-toggle'")
    current_year = [item for item in years if str(datetime.date(datetime.now()).year) in item.text]
    current_year[0].click()
    time.sleep(10)
    table_rows = driver.find_elements(By.CSS_SELECTOR,"tr")
    meetings = [item for item in table_rows if item.text != ""]
    future_meetings = [item for item in meetings if check_meeting_date(item.text.split("\n")[0])==True]
    agenda_links=[item.find_element(By.CSS_SELECTOR,"a[href*=Agenda").get_attribute("href") for item in future_meetings if 'Agenda' in item.text]
    for item in agenda_links:
        driver.get(item)
        time.sleep(10)
        agenda_content = get_agenda_content(locality_dictionary_multi_use[locality_dictionary]["content_tag"])
        readable = check_agenda_readability(agenda_content)
        if readable==True:
            agenda_search = search_text_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + locality_dictionary_multi_use[locality_dictionary]["name"] + ". " + item)
        elif readable==False:
            messages.append("New meeting document available for " + locality_dictionary_multi_use[locality_dictionary]["name"] +". Document cannot be scanned for keywords. " + item)
    return messages

"""Pittsylvania County, All Boards and Commissions""" #just like Prince Edward BoS
def pittsylvania_county():
    from webscraping_dictionaries import locality_dictionary_single_use
    driver.get(locality_dictionary_single_use["Pittsylvania"]["url"])
    time.sleep(10)
    messages = []
    table_rows = driver.find_elements(By.CSS_SELECTOR,"tr")[1:]
    for item in table_rows:
        #since they're all upcoming events only, no need to check the date
        try:
            agenda_link = item.find_element(By.CSS_SELECTOR,"a[class*='agenda_minutes_link'").get_attribute("href")
            driver.get(agenda_link)
            time.sleep(10)
            agenda_content = get_agenda_content(locality_dictionary_single_use["Pittsylvania"]["content_tag"])
            readable = check_agenda_readability(agenda_content)
            if readable==True:
                agenda_search = search_text_for_keywords(agenda_content)
                if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Pittsylvania County. " + agenda_link)
            elif readable == False:
                messages.append("New meeting document available for Pittsylvania County. Document cannot be scanned for keywords. " + agenda_link)
        except:
            continue
    return messages

"Prince Edward County Board of Supervisors" #just like Pittsylvania
def prince_edward_bos():
    from webscraping_dictionaries import locality_dictionary_single_use
    driver.get(locality_dictionary_single_use["Prince Edward BOS"]["url"])
    time.sleep(10)
    messages = []
    #row 0 is the column headers, latest meeting will be index 1
    table_rows = driver.find_elements(By.CSS_SELECTOR,"tr")
    future_meetings = [item for item in table_rows[1:] if item.text !="   " and check_meeting_date(item.text.split("Meeting")[1].split("-")[0])==True]
    meeting_links = [item.find_elements(By.CSS_SELECTOR,'a')[1].get_attribute("href") for item in future_meetings]
    for item in meeting_links:
        driver.get(item)
        time.sleep(10)
        agenda_content = get_agenda_content(locality_dictionary_single_use["Prince Edward BOS"]["content_tag"])
        readable = check_agenda_readability(agenda_content)
        if readable == True:
            agenda_search = search_text_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Prince Edward County Board of Supervisors. " + item)
    return pd.Series(messages).unique().tolist()

"Prince Edward County Planning Commission" #consider addition to Links by Year localities, needs an extra step to get to agenda document though
def prince_edward_pc():
    from webscraping_dictionaries import locality_dictionary_single_use
    driver.get(locality_dictionary_single_use["Prince Edward PC"]["url"])
    time.sleep(10)
    messages = []
    latest_year = driver.find_element(By.CSS_SELECTOR,"a[class*='content_link'").get_attribute('href')
    driver.get(latest_year)
    time.sleep(10)
    latest_agenda = driver.find_elements(By.CSS_SELECTOR,"a[class*='content_link'")[-1]
    future_meeting = check_meeting_date(latest_agenda.text)
    if future_meeting==True:
        meeting_link = latest_agenda.get_attribute('href')
        driver.get(meeting_link)
        time.sleep(10)
        documents = driver.find_elements(By.CSS_SELECTOR,"a[href*=showpublisheddocument")
        #check for a little while to make sure Packet continues to be a good keyword here
        agenda = [item.get_attribute("href") for item in documents if "Packet" in item.text]
        driver.get(agenda[0])
        time.sleep(10)
        agenda_content = get_agenda_content(locality_dictionary_single_use["Prince Edward PC"]["content_tag"])
        readable = check_agenda_readability(agenda_content)
        if readable == False:
            messages.append("New Planning Commission Agenda available for Prince Edward County. Document cannot be scanned for keywords. " + agenda[0])
        elif readable==True:
            agenda_search = search_text_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Prince Edward County Planning Commission. " + agenda[0])  
    return messages 

"""Richmond County""" #assuming everything is still scanned and unreadable, revise later
def richmond_county():
    from webscraping_dictionaries import locality_dictionary_single_use
    driver.get(locality_dictionary_single_use["Richmond"]["url"])
    time.sleep(10)
    messages = []
    agenda_links = driver.find_elements(By.CSS_SELECTOR, "a[href*='.pdf'")
    for item in agenda_links:
        if item.text != "":
            future_meeting = check_meeting_date(item.text)
            if future_meeting == True:
                messages.append("New Board of Supervisors Meeting Agenda posted for Richmond County. Document cannot be scanned for keywords. " + item)
            else:
                break
    return messages

"""Staunton"""
def staunton(locality_dictionary):
    from webscraping_dictionaries import locality_dictionary_multi_use
    driver.get(locality_dictionary_multi_use[locality_dictionary]["url"])
    time.sleep(10)
    messages = []
    table_rows = driver.find_elements(By.CSS_SELECTOR,'tr[class*="meeting_widget_item"')
    future_meetings = [item.find_element(By.CSS_SELECTOR,"a").get_attribute("href") for item in table_rows if check_meeting_date(item.text)==True]
    for item in future_meetings:
        driver.get(item)
        time.sleep(10)
        agenda_link = driver.find_element(By.CSS_SELECTOR,"a[class*='pdf_icon'").get_attribute("href")
        driver.get(agenda_link)
        time.sleep(10)
        agenda_content = get_agenda_content(locality_dictionary_multi_use[locality_dictionary]["content_tag"])
        readable = check_agenda_readability(agenda_content)
        if readable == True:
            agenda_search = search_text_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + locality_dictionary_multi_use[locality_dictionary]["name"] + ". " + agenda_link)
        elif readable == False:
            messages.append("New meeting document available for " + locality_dictionary_multi_use[locality_dictionary]["name"] + ". Document cannot be scanned for keywords. " + agenda_link)
    return messages

"""Sussex County"""
def sussex_county():
    from webscraping_dictionaries import locality_dictionary_single_use
    driver.get(locality_dictionary_single_use["Sussex"]["url"])
    time.sleep(10)
    messages=[]
    list_rows = driver.find_elements(By.CSS_SELECTOR,"li")[1:]
    meetings = [item for item in list_rows if "Agenda" in item.text and item.text != "Agendas And Minutes"]
    current_meetings = [item for item in meetings if "Archived" not in item.text]
    future_meetings = [item for item in current_meetings if check_meeting_date(search_dates(item.text)[0][0])==True]
    document_links =[]
    for item in future_meetings:
        documents = item.find_elements(By.CSS_SELECTOR,"a")
        for item in documents:
            document_links.append(item.get_attribute("href")) 
    for link in document_links:
        driver.get(link)
        time.sleep(10)
        agenda_content = get_agenda_content(locality_dictionary_single_use["Sussex"]["content_tag"])
        readable = check_agenda_readability(agenda_content)
        if readable ==True:
            agenda_search = search_text_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Sussuex County. " + link)
        elif readable == False:
            messages.append("New meeting document available for Sussex County. Document cannot be scanned for keywords. " + link)
    return messages

"""Tazewell County"""
def tazewell_county(locality_dictionary):
    from webscraping_dictionaries import locality_dictionary_multi_use
    driver.get(locality_dictionary_multi_use[locality_dictionary]["url"])
    time.sleep(10)
    messages = []
    all_rows = driver.find_elements(By.CSS_SELECTOR,"li")
    meeting_rows = []
    for item in all_rows:
        if "2024" in item.text:
            meeting_rows.append(item)
    for item in meeting_rows:
        future_meeting = check_meeting_date(item.text)
        if future_meeting == True:
            try:
                #agenda is listed first, so can just return the first search result
                agenda_link = item.find_element(By.CSS_SELECTOR,"a")
                agenda_url = agenda_link.get_attribute("href")
                driver.get(agenda_url)
                time.sleep(10)
                agenda_content = get_agenda_content(locality_dictionary_multi_use[locality_dictionary]["content_tag"])
                readable = check_agenda_readability(agenda_content)
                if readable == True:
                    agenda_search = search_text_for_keywords(agenda_content)
                    if agenda_search != []:
                        messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + locality_dictionary_multi_use[locality_dictionary]["name"] + ". " + agenda_url)
                elif readable == False:
                    messages.append("New meeting document available for " + locality_dictionary_multi_use[locality_dictionary]["name"] + ". Document cannot be scanned for keywords. " + agenda_url)
            except:
                continue
            #if there's no agenda posted yet and the initial agenda link search fails, just move on to the next meeting
    return messages

"""Virginia Beach"""
def virginia_beach_cc():
    from webscraping_dictionaries import locality_dictionary_single_use
    driver.get(locality_dictionary_single_use["Virginia Beach CC"]["url"])
    time.sleep(10)
    messages = []
    current_agenda = driver.find_element(By.CSS_SELECTOR,"a[href*='Brief-Agenda'")
    agenda_url = current_agenda.get_attribute("href")
    driver.get(agenda_url)
    time.sleep(10)
    agenda_content = get_agenda_content(locality_dictionary_single_use["Virginia Beach CC"]["content_tag"])
    readable = check_agenda_readability(agenda_content)
    if readable == True:
        agenda_search = search_text_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Virginia Beach in latest City Council meeting agenda. " + agenda_url)
    elif readable == False:
        messages.append("New meeting document available for Virginia Beach City Council. Document cannot be scanned for keywords. " + agenda_url)
    return messages

def virginia_beach_pc():
    from webscraping_dictionaries import locality_dictionary_single_use
    driver.get(locality_dictionary_single_use["Virginia Beach PC"]["url"])
    time.sleep(10)
    messages = []
    all_rows = driver.find_elements(By.CSS_SELECTOR,'li')
    meetings = [item for item in all_rows if "Agenda" in item.text]
    future_meetings =[item for item in meetings if check_meeting_date(item.text.split(":")[0])==True]
    meeting_urls = [item.find_element(By.CSS_SELECTOR,"a").get_attribute("href") for item in future_meetings]
    for item in meeting_urls:
        driver.get(item)
        time.sleep(10)
        agenda_content = get_agenda_content(locality_dictionary_single_use["Virginia Beach PC"]["content_tag"])
        readable = check_agenda_readability(agenda_content)
        if readable == True:
            agenda_search = search_text_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Virginia Beach in latest Planning Commission meeting agenda. " + item)
        elif readable == False:
            messages.append("New meeting document available for Virginia Beach Planning Commission. Document cannot be scanned for keywords. " + item)
    return messages

#revise, something seems off about the site
"Westmoreland County"
def westmoreland_county(locality_dictionary):
    from webscraping_dictionaries import locality_dictionary_multi_use
    messages = []
    driver.get(locality_dictionary_multi_use[locality_dictionary]["url"])
    time.sleep(10)
    #selected URLs only show upcoming meetings, no need for a date check. Just check the nearest meeting since it's unlikely that agendas will be posted too far out
    next_meeting = driver.find_element(By.CSS_SELECTOR,"h3").find_element(By.CSS_SELECTOR,"a").get_attribute('href')
    driver.get(next_meeting)
    time.sleep(10)
    pdfs = driver.find_elements(By.CSS_SELECTOR,"a[href*='.pdf'")
    agenda_links =[item.get_attribute('href') for item in pdfs if "Agenda" in item.text or "agenda" in item.text]
    for item in agenda_links:
        driver.get(item)
        time.sleep(10)
        agenda_content = get_agenda_content(locality_dictionary_multi_use[locality_dictionary]["content_tag"])
        readable = check_agenda_readability(agenda_content)
        if readable == True:
            agenda_search = search_text_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + locality_dictionary_multi_use[locality_dictionary]["name"] + ". " + item)
        elif readable == False:
            messages.append("New meeting document available for " + locality_dictionary_multi_use[locality_dictionary]["name"] +". Document cannot be scanned for keywords. " + item)
    return messages

"""Wythe County"""
#check public notices for now until agenda links work again
def wythe_county():
    from webscraping_dictionaries import locality_dictionary_single_use
    driver.get(locality_dictionary_single_use["Wythe"]["url"])
    time.sleep(10)
    messages = []
    public_notice_links = driver.find_elements(By.CSS_SELECTOR,'a[href*="public-notices"')
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