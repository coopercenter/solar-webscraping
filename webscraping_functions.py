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
    #all_meetings[i].text should be set as the meeting title for boarddocs sites
    if datetime.date(datetime.now()) < datetime.date(dateutil.parser.parse(meeting_time_string, fuzzy=True)) or datetime.date(datetime.now()) == datetime.date(dateutil.parser.parse(meeting_time_string, fuzzy=True)):
        return True
    else:
        return False
def get_future_rows(rows):
    future_rows =[]
    for item in rows:
        try:
            if check_meeting_date(item.text)==True:
                future_rows.append(item)
        except:
            try:
                if check_meeting_date(item.text.split("\u2009")[0]) ==True:
                    future_rows.append(item)
            except:
                try:
                    if check_meeting_date(item.text.split("\n")[0])==True:
                        future_rows.append(item)
                except:
                    try:
                        if check_meeting_date(item.text.split("-")[0])==True:
                            future_rows.append(item)
                    except:
                        try:
                            if check_meeting_date(item.text.split(" ")[0])==True:
                                future_rows.append(item)
                        except:
                            try:
                                if check_meeting_date(item.text.split("-")[1])==True:
                                    future_rows.append(item.get_attribute("href"))
                            except:
                                try:
                                    if check_meeting_date(item.text.split("-")[-1])==True:
                                        future_rows.append(item.get_attribute("href"))
                                except:
                                    continue
    return future_rows

def get_future_meeting_links(list):
    future_meetings=[]
    for item in list:
        try:
            if check_meeting_date(item.text)==True:
                future_meetings.append(item.get_attribute('href'))
        except:
            try:
                if check_meeting_date(item.text.split("\u2009")[0]) ==True:
                    future_meetings.append(item.get_attribute('href'))
            except:
                try:
                    if check_meeting_date(item.text.split("\n")[0])==True:
                        future_meetings.append(item.get_attribute('href'))
                except:
                    try:
                        if check_meeting_date(item.text.split("-")[1])==True:
                            future_meetings.append(item.get_attribute("href"))
                    except:
                        try:
                            if check_meeting_date(item.text.split("-")[-1])==True:
                                future_meetings.append(item.get_attribute("href"))
                        except:
                            try:
                                if check_meeting_date(item.text.split("-")[0])==True:
                                    future_meetings.append(item.get_attribute("href"))
                            except:
                                try:
                                    if check_meeting_date(item.text.split(" ")[0])==True:
                                        future_meetings.append(item.get_attribute('href'))
                                except:
                                    continue

    return future_meetings

def check_readability(agenda_content):
    agenda_string = ""
    for item in agenda_content:
        agenda_string = agenda_string + item.text
    if agenda_string == "":
        readability = False
    else:
        readability = True
    return readability

def search_pdf(meeting_links_list, locality):
    messages=[]
    for item in meeting_links_list:
        driver.get(item)
        time.sleep(10)
        pages = driver.find_elements(By.CSS_SELECTOR,"div[class*=page")
        for page in pages:
            driver.execute_script("arguments[0].scrollIntoView();", page)
            time.sleep(2)
            agenda_content = driver.find_elements(By.CSS_SELECTOR,'div[class*=textLayer')
            readable = check_readability(agenda_content)
            if readable==True:
                agenda_search = search_agenda_for_keywords(agenda_content)
                if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + locality + ". " + item)
            elif readable==False:
                messages.append("New meeting document available for " + locality + ". Part of the document cannot be scanned for keywords. " + item)
    return pd.Series(messages).unique().tolist()

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


def is_internet_active(timeout):
    try:
        requests.head("http://www.duckduckgo.com/", timeout=timeout)
        return True
    except requests.ConnectionError:
        return False

"""Webscraping Functions"""

"""AgendaCenter"""
def agendacenter(url,locality):
    driver.get(url)
    messages = []
    #table_rows = WebDriverWait(driver,20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "tr[class*=catAgendaRow")))
    time.sleep(5)
    table_rows = driver.find_elements(By.CSS_SELECTOR, "tr[class*=catAgendaRow")
    future_meetings = []
    for item in table_rows:
        try:
            if check_meeting_date(item.text.split("\u2009")[0]) ==True:
                future_meetings.append(item)
        except:
            if check_meeting_date(item.text.split("\n")[0])==True:
                future_meetings.append(item)
    agenda_links = [item.find_elements(By.CSS_SELECTOR,"a")[1].get_attribute("href") for item in future_meetings]
    for item in agenda_links:
        driver.get(item)
        time.sleep(20)
        agenda_content = driver.find_elements(By.CSS_SELECTOR, "div[class*=textLayer")
        #agenda_content = WebDriverWait(driver,20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div[class*=textLayer")))
        if agenda_content == []:
            agenda_content = driver.find_elements(By.CSS_SELECTOR, "div[id*='divInner'")
            #agenda_content = WebDriverWait(driver,20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div[id*='divInner'")))
        readable = check_readability(agenda_content)
        if readable==True:
            agenda_search = search_agenda_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + locality + ". " + item)
        elif readable==False:
            messages.append("New meeting document available for " + locality + ". Document cannot be scanned for keywords. " + item)
    return messages

"""BoardDocs"""
def check_boarddocs_agendas(locality,meetings_page,url):
    #get all the meeting links
    all_meetings = driver.find_elements(By.CSS_SELECTOR, "a[class*='icon prevnext meeting")
    update_messages = []
    for item in all_meetings:
        #if it's blank, skip it
        if item.text != '':
        #adding a fix for Culpeper that may help or break other locality websites
            if "\n" in item.text:
                future_meeting = check_meeting_date(item.text.split("\n")[0])
            else:
                future_meeting = check_meeting_date(item.text)
            if future_meeting == True:
                meeting_title = item.text
                #if the meeting hasn't happened yet, check for last minute agenda edits that might contain solar until it has passed
                item.click()
                time.sleep(10)
                #find the element to click to view the meeting agenda for this meeting
                meeting_agenda = driver.find_element(By.CSS_SELECTOR, "a[id*='btn-view-agenda'")
                #click the meeting agenda button
                meeting_agenda.click()
                time.sleep(10)
                #pause, give the page time to load
                #Now to get ALL the agenda content
                all_agenda_topics = driver.find_elements(By.CSS_SELECTOR, "span[class*='title'")
                #run the keyword search
                agenda_search = search_agenda_for_keywords(all_agenda_topics)
                if agenda_search !=[]:
                    update_messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + locality + " in " + meeting_title + ". " + url)
                meetings_page.click()
                time.sleep(10)
            else:
                break
    return update_messages

def boarddocs(url,locality,two_pages):
    url_test=verify_url(url)
    if url_test==True:
        driver.get(url)
        time.sleep(10)
        all_tabs=driver.find_elements(By.CSS_SELECTOR,"a[id*=ui-id-")
        meetings_page=all_tabs[1]
        meetings_page.click()
        time.sleep(10)
        time.sleep(10)
        messages = check_boarddocs_agendas(locality,meetings_page)
        if two_pages==True:
            govt_tab = driver.find_element(By.CSS_SELECTOR,"a[id*=btn-board")
            govt_tab.click()
            time.sleep(10)
            menu_options = driver.find_elements(By.CSS_SELECTOR,"a[class*=dropdown-item")
            for item in menu_options:
                if "Planning Commission" in item.text:
                    planning_commission=item
            planning_commission.click()
            time.sleep(10)
            pc_messages = check_boarddocs_agendas(locality,meetings_page,url)
            messages = messages + pc_messages
        return messages
    else:
        return url_test

"CivicClerk"
def civicclerk(url,locality):
    url_test = verify_url(url)
    if url_test==True:
        messages=[]
        driver.get(url)
        time.sleep(10)
        all_meetings = driver.find_elements(By.CSS_SELECTOR,"li[class*='cpp-MuiListItem-container'")
        meetings_with_agendas = []
        for item in all_meetings:
            try:
                #test if there's a download button, indicating agenda files have been posted. Lack of files to scan will throw an error, and we won't waste time checking that meeting link for keywords
                item.find_element(By.CSS_SELECTOR,"button[id*=downloadFilesMenu")
                meetings_with_agendas.append(item)
            except:
                continue
        meeting_links = [item.find_element(By.CSS_SELECTOR,"a").get_attribute("href") for item in meetings_with_agendas]
        for item in meeting_links:
            driver.get(item)
            time.sleep(10)   
            pdf_viewer_frame = driver.find_elements(By.CSS_SELECTOR,"iframe[id*=pdfViewerIframe")
            if pdf_viewer_frame != []:
                driver.switch_to.frame(pdf_viewer_frame[0])
                agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
                agenda_search = search_agenda_for_keywords(agenda_content)
                if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + locality + ". " + item)
        return messages
    else: 
        return url_test
    
"""CivicWeb"""
def civicweb(url,locality):
    driver.get(url)
    time.sleep(10)  
    messages = []
    all_meetings = driver.find_elements(By.CSS_SELECTOR,"a[class*='list-link'")
    relevant_meetings = [item for item in all_meetings if "Board of Supervisors" in item.text or "Planning Commission" in item.text or "City Council" in item.text]
    future_meetings=get_future_meeting_links(relevant_meetings)   
    for item in future_meetings:
        driver.get(item)
        time.sleep(10)
        #switch to the agenda viewer frame
        agenda_frame = driver.find_element(By.CSS_SELECTOR,"iframe")
        driver.switch_to.frame(agenda_frame)
        agenda_content = driver.find_elements(By.CSS_SELECTOR,"html")
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + locality + ". " + item)
    return messages

"""DocumentCenter"""
def document_center(url,locality):
    driver.get(url)
    time.sleep(10)  
    messages = []
    folders = driver.find_elements(By.CSS_SELECTOR,"span")
    for item in folders:
        if item.text == "Board of Supervisors":
            item.click()
            time.sleep(10)
            break
    new_folders = driver.find_elements(By.CSS_SELECTOR,"span")
    for item in new_folders:
        if item.text == "Agenda":
            item.click()
            time.sleep(10)
            break
    year_folders = driver.find_elements(By.CSS_SELECTOR,"span")
    for item in year_folders:
        if item.text == "2024":
            item.click()
            time.sleep(10)
            break
    agenda_links = driver.find_elements(By.CSS_SELECTOR,"a[class*=pdf")
    latest_agenda = agenda_links[-1].get_attribute("href")
    driver.get(latest_agenda)
    time.sleep(10)
    agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
    agenda_search = search_agenda_for_keywords(agenda_content)
    if agenda_search != []:
        messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for "+ locality + ". " + latest_agenda)
    return messages

"""eScribe"""
def escribe(url,locality):
    driver.get(url)
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
            driver.switch_to.window(driver.window_handles[1])
            agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
            agenda_search = search_agenda_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + locality +  ". " + agenda_url)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        except:
            continue
    return messages

"""Granicus"""
def granicus_version_2(url, locality):
    driver.get(url)
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
                    messages.append("Keyword(s) " + ", ".join(agenda_search) +" found in upcoming meeting for " + locality + ". " + agenda_link)
            except:
                continue
    return messages

def granicus(url,locality):
    driver.get(url)
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
                        messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + locality + ". " + agenda_url)
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                except:
                    continue 
            else:
                break
        except:
            continue
    return messages

"LaserFiche"
def laserfiche(url,locality):
    driver.get(url)
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
        if 'Comprehensive Plan' in agenda_content or 'Comprehensive plan' in agenda_content or 'comprehensive plan' in agenda_content:
            keywords.append('Comprehensive Plan')
        if 'Zoning Ordinance' in agenda_content or 'Zoning ordinance' in agenda_content or 'zoning ordinance' in agenda_content:
            keywords.append('Zoning Ordinance')
        if keywords!=[]:
            messages.append('Keyword(s) ' + ", ".join(keywords)+' found in upcoming meeting for ' + locality + '. ' + agenda_link)
        #close and delete the temp file
        temp_agenda.close()
    return messages               

"""Legistar"""
def legistar(url,locality):
    url_test = verify_url(url)
    messages = []
    if url_test == True:
        driver.get(url)
        time.sleep(10)
        table_rows = driver.find_elements(By.CSS_SELECTOR,'tr[id*=ctl00_')
        future_meetings = [item for item in table_rows if check_meeting_date(item.text.split("/2024")[0])==True]
        meeting_urls = [item.find_element(By.CSS_SELECTOR,"a[id*=hypMeetingDetail").get_attribute('href') for item in future_meetings]
        for item in meeting_urls:
            if item != None:
                driver.get(item)
                time.sleep(10)
                agenda_content = driver.find_elements(By.CSS_SELECTOR,'tr[id*=ctl00')
                agenda_search = search_agenda_for_keywords(agenda_content)
                if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + locality + ". " + item)
        return messages
    else:
        return url_test

"""Meetings Table"""
def meetings_table(url,locality):
    driver.get(url)
    time.sleep(10)
    messages = []
    all_rows = driver.find_elements(By.CSS_SELECTOR,"tr")[1:]
    future_meetings = []
    for item in all_rows:
        future_meeting = check_meeting_date(item.text.split("-")[0])
        if future_meeting==True:
            future_meetings.append(item)
    agenda_links = []
    for item in future_meetings:
        try:
            agenda_links.append(item.find_element(By.CSS_SELECTOR,"a[title*=Agenda"))
        except:
            #throws an error of no links are posted yet, so do this and keep going to keep the indices aligned
            agenda_links.append(None)
    for item in agenda_links:
        if item != None:
            item.click()
            time.sleep(10)
            driver.switch_to.window(driver.window_handles[1])
            agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
            agenda_search = search_agenda_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + locality + ". " + item)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
    return messages

"""NovusAGENDA"""
def novusagenda(url,locality):
    #validate the URL
    url_test  = verify_url(url)
    if url_test == True:
        #fetch the URL and give it a few seconds to load the scripts
        driver.get(url)
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
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + locality + ". " + agenda_url)
            driver.close()
            driver.switch_to.window(main_window)
        return messages
    else:
        return url_test
    
"""OnBase"""
def onbase(url,locality):
    messages=[]
    driver.get(url)
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
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + locality + ". " + item)
    return messages
    
"""PHP Table"""
def php_table(url,locality):
    driver.get(url)
    time.sleep(10)
    messages = []
    table_rows = driver.find_elements(By.CSS_SELECTOR,'tr')
    future_meetings = []
    for item in table_rows:
        try:
            future=check_meeting_date(item.text)
            if future==True:
                future_meetings.append(item)
        except:
            continue
    future_agendas = [item for item in future_meetings if "Agenda" in item.text]
    if future_agendas !=[]:
        for item in future_agendas:
            agenda_link = item.find_element(By.CSS_SELECTOR, "a[href*='.pdf'").get_attribute('href')
            driver.get(agenda_link)
            time.sleep(10)
            agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
            agenda_readability = check_readability(agenda_content)
            if agenda_readability == True:
                agenda_search = search_agenda_for_keywords(agenda_content)
                if agenda_search !=[]:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + locality + ". " + agenda_link)
            elif agenda_readability == False:
                messages.append("New meeting agenda available for " + locality + ". Document cannot be scanned for keywords. " + agenda_link)
    return messages

"""PrimeGov"""
def prime_gov(url, locality):
    driver.get(url)
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
                messages.append('Keyword(s) ' + ", ".join(keywords)+' found in upcoming meeting for ' + locality + '. ' + agenda_link)
            #close and delete the temp file
            temp_agenda.close()
    return messages

"""Locality Specific Functions"""

"""Albemarle County"""
def albemarle_county_pc(url):
    messages=[]
    driver.get(url)
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
            agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
            agenda_search=search_agenda_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Albemarle County Planning Commission. " + agenda_link)
        except:
            continue
    return messages


"""Alleghany County"""
#only BOS agendas are available
def alleghany_county(bos_url):
    messages=[]
    url_test = verify_url(bos_url)
    if url_test==True:
        driver.get(bos_url)
        time.sleep(10)
        #hunt down the agenda links
        all_agenda_links = driver.find_elements(By.CSS_SELECTOR,"a[class*='attachment-link'")
        future_meetings = [item.get_attribute('href') for item in all_agenda_links if check_meeting_date(item.text)==True]
        for item in future_meetings:
            driver.get(item)
            time.sleep(10)
            agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
            agenda_search = search_agenda_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Alleghany County Board of Supervisors. " + item)
        return messages
    else:
        return url_test

"""Bath County"""
def bath_county(url):
    messages=[]
    driver.get(url)
    time.sleep(10)
    #get whatever meeting links are available
    try:
        pc_links = driver.find_elements(By.CSS_SELECTOR,"a[title*='Planning'")
    except:
        pc_links = None
    try:
        bos_links = driver.find_elements(By.CSS_SELECTOR,"a[title*='Board of Supervisors'")
    except:
        bos_links = None
    meeting_urls = []
    for item in pc_links:
        if item != None:
            meeting_urls.append(item.get_attribute("href"))
    for item in bos_links:
        if item != None:
            meeting_urls.append(item.get_attribute("href"))
    for item in meeting_urls:
        driver.get(item)
        time.sleep(10)
        meeting_documents = driver.find_elements(By.CSS_SELECTOR, "a[href*=DisplayFile")
        meeting_document_urls = []
        for document in meeting_documents:
            meeting_document_urls.append(document.get_attribute("href"))
        for link in meeting_document_urls:
            driver.get(link)
            time.sleep(10)
            agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
            agenda_readability = check_readability(agenda_content)
            if agenda_readability==True:
                agenda_search = search_agenda_for_keywords(agenda_content)
                if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Bath County. " + link)
            else:
                messages.append("New meeting document available for Bath County. Document cannot be scanned for keywords. " + link)
    return messages

"""Bland County"""
def bland_county(url):
    url_check = verify_url(url)
    if url_check == True:
        driver.get(url)
        time.sleep(10)
        messages = []
        #get all the table rows
        table_rows = driver.find_elements(By.CSS_SELECTOR,"tr")
        #filter for just the ones where agendas are posted
        posted_agendas = [item for item in table_rows if "AGENDA" in item.text]
        #latest meeting will be the last one in the list
        latest_meeting = posted_agendas[-1]
        #check the date for the last posted meeting
        future_meeting = check_meeting_date(latest_meeting.text)
        if future_meeting == True:
            agenda_url = latest_meeting.find_element(By.CSS_SELECTOR,"a").get_attribute("href")
            #as of 01/17/24, Bland County still posts scanned documents that are not yet readable by this webscraper
            messages.append("New meeting agenda available for Bland County Board of Supervisors. Document cannot be scanned for keywords. " + agenda_url)
    else:
        messages.append(url_check)
    return messages

"Brunswick County"
def brunswick_county(url):
    messages=[]
    driver.get(url)
    time.sleep(10)
    pdfs = driver.find_elements(By.CSS_SELECTOR,'a[href*=".pdf"')
    future_meeting = [item.get_attribute("href") for item in pdfs if item.text != "" and item.text != " " and check_meeting_date(item.text) == True]
    for item in future_meeting:
        driver.get(item)
        time.sleep(10)
        agenda_content = driver.find_elements(By.CSS_SELECTOR, "div[class*=textLayer")
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search !=[]:
            messages.append('Keyword(s) ' + ", ".join(agenda_search)+' found in upcoming meeting for Brunswick County. ' + item)
    return messages

"""Buchanan County"""
def buchanan_county(url):
    driver.get(url)
    time.sleep(10)
    messages = []
    pdf_links = driver.find_elements(By.CSS_SELECTOR,"a[href*='.pdf")
    latest_minutes = [item for item in pdf_links if "Minutes" in item.text][0]
    #since they're only posting minutes not agendas, and minutes are posted long after the fact, we'll skip the date checking
    minutes_url = latest_minutes.get_attribute("href")
    driver.get(minutes_url)
    time.sleep(10)
    agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
    agenda_search = search_agenda_for_keywords(agenda_content)
    if agenda_search != []:
        messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Buchanan County Board of Supervisors. " + minutes_url)
    return messages   

"""Buena Vista City Council"""
def buena_vista_city_council(url):
    driver.get(url)
    time.sleep(10)
    messages = []
    links = driver.find_elements(By.CSS_SELECTOR,"a")
    agendas = [item for item in links if "Council Agenda" in item.text]
    future_meetings=[item.get_attribute("href") for item in agendas if check_meeting_date(item.text)==True]
    for item in future_meetings:
        messages.append("New agenda available for Buena Vista City Council. Document cannot be scanned for keywords. " + item)
    return messages

"Charlotte County"
def charlotte_county(url,governing_body):
    messages=[]
    driver.get(url)
    time.sleep(10)
    table_rows = driver.find_elements(By.CSS_SELECTOR,"tr")
    if "Solar" in table_rows[0].text:
        messages.append("Solar Public Hearing posted for Charlotte County. " + url)
    future_meetings = []
    for item in table_rows[1:]:
        try:
            if check_meeting_date(item.text.split(" ")[0]) == True:
                future_meetings.append(item)
            else:
                break
        except:
            continue
    agendas = [item for item in future_meetings if "Agenda" in item.text]
    packets = [item for item in future_meetings if "Packet" in item.text and "Agenda" not in item.text]
    agenda_links = [item.find_element(By.CSS_SELECTOR,"a").get_attribute("href") for item in agendas]
    packet_links=[item.find_element(By.CSS_SELECTOR,"a").get_attribute("href") for item in packets]
    for item in agenda_links:
        driver.get(item)
        time.sleep(10)
        agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
        readability = check_readability(agenda_content)
        if readability == False:
            messages.append("New agenda available for Charlotte County " + governing_body + ". Document cannot be scanned for keywords. " + item)
        else:
            agenda_search = search_agenda_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Charlotte County " + governing_body + ". " + item)
    for item in packet_links:
        driver.get(item)
        time.sleep(10)
        packet_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
        packet_readability = check_readability(packet_content)
        if packet_readability == False:
            messages.append("New agenda available for Charlotte County " + governing_body + ". Document cannot be scanned for keywords. " + item)
        else:
            packet_search = search_agenda_for_keywords(packet_content)
            if packet_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Charlotte County " + governing_body + ". " + item)
    return messages

"""Clarke County"""
def clarke_county(url):
    driver.get(url)
    time.sleep(10)
    messages = []
    year_folders = driver.find_elements(By.CSS_SELECTOR,'a[class*="content_link"')
    latest_year = year_folders[0].get_attribute("href")
    driver.get(latest_year)
    time.sleep(10)
    #skip the first two entries since they're just the file path links
    all_meeting_links = driver.find_elements(By.CSS_SELECTOR,"a[class*='content_link'")[2:]
    latest_meeting = all_meeting_links[0]
    #split around the colon, otherwise the date fails to register
    future_meeting = check_meeting_date(latest_meeting.text.split("  ")[0])
    if future_meeting == True:
        agenda_url = latest_meeting.get_attribute("href")
        driver.get(agenda_url)
        time.sleep(10)
        agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Clarke County. " + agenda_url)
    return messages 

"""Town of Clifton Forge"""
def clifton_forge(url):
    driver.get(url)
    time.sleep(10)
    messages = []
    list_rows = driver.find_elements(By.CSS_SELECTOR,"li[class*=pdf")
    #title format is inconsistent, no good way to reliably check for dates at this time. However, most recent meeting is at the top of the list, so we'll check that
    latest_agenda = list_rows[0].find_element(By.CSS_SELECTOR,"a").get_attribute("href")
    driver.get(latest_agenda)
    time.sleep(10)
    agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
    agenda_search = search_agenda_for_keywords(agenda_content)
    if agenda_search != []:
        messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for the Town of Clifton Forge. " + latest_agenda)
    return messages

"""Town of Covington"""
def covington(url):
    driver.get(url)
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
def craig_county(url):
    messages = []
    driver.get(url)
    time.sleep(10)
    #Find the link and check the date. That's as far as we go because the PDFs are scans.
    links = driver.find_elements(By.CSS_SELECTOR,'a')
    future_meetings = get_future_meeting_links(links)
    for item in future_meetings:
        messages.append("New meeting agenda available for Craig County Board of Supervisors. Document cannot be scanned for keywords. " + item)
    return messages

"""Town of Emporia"""
def emporia(url):
    driver.get(url)
    time.sleep(10)
    messages = []
    all_links = driver.find_elements(By.CSS_SELECTOR,"li")
    latest_year = [item for item in all_links if item.text == str(datetime.today().year)]
    if latest_year != []:
        driver.get(latest_year[0].find_element(By.CSS_SELECTOR,'a').get_attribute('href'))
        time.sleep(10)
        latest_meeting = driver.find_element(By.CSS_SELECTOR,'div[class*="views-row"')
        future_meeting = check_meeting_date(latest_meeting.text.split('\n')[0])
        if future_meeting == True:
            agenda_link = latest_meeting.find_element(By.CSS_SELECTOR,"a")
            meeting_url = agenda_link.get_attribute("href")
            driver.get(meeting_url)
            time.sleep(10)
            agenda_content = driver.find_elements(By.CSS_SELECTOR, "div[class*=textLayer")
            agenda_search = search_agenda_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for the Town of Emporia. " + meeting_url)
    return messages

"""Essex County PC"""
def essex_pc(url):
    driver.get(url)
    time.sleep(10)
    messages = []
    all_rows = driver.find_elements(By.CSS_SELECTOR,"div[class*='views-row'")
    future_meetings = []
    for item in all_rows:
        try:
            future_meeting = check_meeting_date(item.text.split("-")[0])
            if future_meeting==True:
                future_meetings.append(item)
        except:
            continue
    agenda_links = []
    for item in future_meetings:
        try:
            agenda_links.append(item.find_element(By.CSS_SELECTOR,"a[title*=Agenda").get_attribute("href"))
        except:
            #throws an error of no links are posted yet, so do this and keep going to keep the indices aligned
            agenda_links.append(None)
    for item in agenda_links:
        if item != None:
            driver.get(item)
            time.sleep(10)
            agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
            agenda_search = search_agenda_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Essex County Planning Commission. " + item)
    return messages

"""Fairfax County"""
def fairfax_county_bos(url):
    driver.get(url)
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
            for i in range(0,10):
                webdriver.common.action_chains.ActionChains(driver).send_keys(webdriver.common.keys.Keys.PAGE_DOWN).perform()
                agenda_content = (driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer"))
                agenda_search = search_agenda_for_keywords(agenda_content)
                if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Fairfax County Board of Supervisors. " + agenda_link)
                    break
        except:
            continue
    return messages

def fairfax_county_pc(url):
    driver.get(url)
    time.sleep(10)
    messages = []
    latest_year = driver.find_element(By.CSS_SELECTOR,"table[align*=center")
    months = latest_year.find_elements(By.CSS_SELECTOR,"td[align*=center")
    relevant_months = []
    for item in months:
        if item.text == datetime.now().strftime("%B"):
            relevant_months.append(item.find_element(By.CSS_SELECTOR,"a").get_attribute('href'))
    for item in relevant_months:
        driver.get(item)
        time.sleep(10)
        agenda_links = driver.find_elements(By.CSS_SELECTOR,"a[href*='.pdf'")
        agenda_urls = []
        for item in agenda_links:
            agenda_urls.append(item.get_attribute("href"))
        for item in agenda_urls:
            try:
                future = check_meeting_date(item.split('/')[-1].split('.pdf')[0])
                if future==True:
                    driver.get(item)
                    time.sleep(10)
                    agenda_content = (driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer"))
                    agenda_search = search_agenda_for_keywords(agenda_content)
                    if agenda_search != []:
                        messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Fairfax County Planning Commission. " + item)
            except:
                driver.get(item)
                time.sleep(10)
                agenda_content = (driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer"))
                agenda_search = search_agenda_for_keywords(agenda_content)
                if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Fairfax County Planning Commission. " + item)
    return messages

"""Floyd County"""
def floyd_county(url):
    driver.get(url)
    time.sleep(10)
    messages = []
    all_meeting_rows = driver.find_elements(By.CSS_SELECTOR,"p[class*='font_7'")
    current_meeting_rows = []
    for item in all_meeting_rows:
        if item.text !='':
            current_meeting_rows.append(item)
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
def city_of_franklin(url):
    driver.get(url)
    time.sleep(10)
    messages=[]
    #this website requires several steps to get to the right data, as it automatically lands on the 2013 agendas page
    years = driver.find_elements(By.CSS_SELECTOR,'li[class*="top-tab"')
    latest_year = years[-1]
    latest_year.click()
    time.sleep(10)
    months = driver.find_elements(By.CSS_SELECTOR,"tr[class*='month-label'")
    latest_month = months[-1]
    latest_month.click()
    time.sleep(10)
    agendas = driver.find_elements(By.CSS_SELECTOR, "a[href*='agenda.pdf'")
    latest_agenda = agendas[-1]
    future_meeting = check_meeting_date(latest_agenda.text)
    if future_meeting == True:
        meeting_url = latest_agenda.get_attribute("href")
        latest_agenda.click()
        time.sleep(10)
        driver.switch_to.window(driver.window_handles[1])
        agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for the City of Franklin. " + meeting_url)
    return messages

"""City of Galax"""
def galax(url):
    driver.get(url)
    time.sleep(10)
    messages = []
    agenda_links = driver.find_elements(By.CSS_SELECTOR,"a[class*='pb_button'")
    latest_agenda = agenda_links[len(agenda_links) - 1]
    future_meeting = check_meeting_date(latest_agenda.text)
    if future_meeting == True:
        agenda_url = latest_agenda.get_attribute("href")
        latest_agenda.click()
        time.sleep(10)
        driver.switch_to.window(driver.window_handles[1])
        agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for the City of Galax. " + agenda_url)
    return messages

"""Giles County Board of Supervisors"""
def giles_county(url):
    driver.get(url)
    time.sleep(10)
    messages = []
    #follow the link to the latest agenda
    agenda_link = driver.find_element(By.CSS_SELECTOR,'a[class*="qbutton"').get_attribute("href")
    driver.get(agenda_link)
    time.sleep(10)
    agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
    agenda_search = search_agenda_for_keywords(agenda_content)
    if agenda_search != []:
        messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Giles County in next agenda. " + agenda_link)
    return messages

"Grayson County"
def grayson_county(url):
    driver.get(url)
    time.sleep(10)
    messages=[]
    links = driver.find_elements(By.CSS_SELECTOR,'a[class*="brz-a"')
    future_meetings = get_future_meeting_links(links)
    for item in future_meetings:
        driver.get(item)
        time.sleep(10)
        download_link = driver.find_element(By.CSS_SELECTOR,"a[class*='gde-link'").get_attribute('href')
        driver.get(download_link)
        time.sleep(10)
        agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search !=[]:
            messages.append('Keyword(s) ' + ", ".join(agenda_search)+' found in upcoming meeting for Grayson County. ' + download_link)
    return messages

"""Greensville County"""
def greensville_county(url,government_body):
    driver.get(url)
    time.sleep(10)
    messages = []
    latest_year = driver.find_element(By.CSS_SELECTOR,"h3[class*='docs-toggle'")
    latest_year.click()
    time.sleep(10)
    agenda_tab = driver.find_element(By.CSS_SELECTOR,"h4[class*='docs-toggle'")
    agenda_tab.click()
    time.sleep(10)
    pdf_links = driver.find_elements(By.CSS_SELECTOR,"a[href*='.pdf'")
    future_meetings=get_future_meeting_links(pdf_links)
    for item in future_meetings:
        driver.get(item)
        time.sleep(10)
        agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
        readable = check_readability(agenda_content)
        if readable==True:
            agenda_search = search_agenda_for_keywords(agenda_content)
            if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) +  " found in upcoming meeting for Greensville County" + government_body + ". " + item )
        elif readable==False:
             messages.append("New meeting againda available for Greensville County " + government_body + ". Document cannot be scanned for keywords. " + item)
    return messages
    
"""Henrico County"""
def henrico_county_bos(url):
    driver.get(url)
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
        agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Henrico County Board of Supervisors. " + meeting_url)
    return messages   

def henrico_county_pc(url):
    driver.get(url)
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
        agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Henrico County in the latest Planning Commission/Board of Zoning Appeals agenda. " + item)
    return messages        

"Highland County"
def highland_county_bos(url):
    messages = []
    driver.get(url)
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
        agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Highland County Board of Supervisors. " + agenda_link)
    return messages

"""King and Queen County"""
def king_and_queen_county(url,governing_body):
    driver.get(url)
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
                    agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
                    agenda_search = search_agenda_for_keywords(agenda_content)
                    if agenda_search != []:
                        messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for King and Queen County " + governing_body + ". " + agenda_link)           
        except:
            continue
    return messages

"""Lee County"""
def lee_county(url):
    driver.get(url)
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
def lexington_pc(url):
    driver.get(url)
    time.sleep(10)
    messages = []
    list_items = driver.find_elements(By.CSS_SELECTOR,"a[class*='content_link'")
    future_meetings = [item.get_attribute("href") for item in list_items if check_meeting_date(item.text)==True]
    for item in future_meetings:
        driver.get(item)
        time.sleep(10)
        agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for the City of Lexington Planning Commission. " + item)
    return messages

"LaserFiche for Loudoun Planning Commission"
def loudoun_pc(url):
    driver.get(url)
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
            if 'Comprehensive Plan' in agenda_content or 'Comprehensive plan' in agenda_content or 'comprehensive plan' in agenda_content:
                keywords.append('Comprehensive Plan')
            if 'Zoning Ordinance' in agenda_content or 'Zoning ordinance' in agenda_content or 'zoning ordinance' in agenda_content:
                keywords.append('Zoning Ordinance')
            if keywords!=[]:
                messages.append('Keyword(s) ' + ", ".join(keywords)+' found in upcoming meeting for  Loudoun County Planning Commission. ' + agenda_link)
            #close and delete the temp file
            temp_agenda.close()
        except:
            continue
    return messages

"""Lunenburg County"""
def lunenburg_county(url):
    driver.get(url)
    time.sleep(10)
    messages = []
    all_meeting_rows = driver.find_elements(By.CSS_SELECTOR,"tr")
    latest_meeting = all_meeting_rows[0]
    future_meeting = check_meeting_date(latest_meeting.text.split(" ")[0])
    if future_meeting == True:
        agenda_url = latest_meeting.find_element(By.CSS_SELECTOR,"a").get_attribute("href")
        driver.get(agenda_url)
        time.sleep(10)
        agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Lunenburg County. " + agenda_url)
    return messages  

"""Manassas Park"""
def manassas_park(url,government_body):
    driver.get(url)
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
        agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Manassas Park " + government_body + '. ' + item)
    return messages

"""Nelson County"""
def nelson_county(url):
    driver.get(url)
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

"""New Kent County Planning Commission"""
def new_kent_county_pc(url):
    driver.get(url)
    time.sleep(10)
    messages = []
    years = driver.find_elements(By.CSS_SELECTOR,'li')
    latest_year = [item for item in years if str(datetime.date(datetime.now()).year) in item.text]
    driver.get(latest_year[0].find_element(By.CSS_SELECTOR,"a").get_attribute('href'))
    time.sleep(10)
    #skip the first entry since it's the link to all archived agendas
    all_agenda_links = driver.find_elements(By.CSS_SELECTOR,"a[href*='Archive'")[1:]
    latest_meeting = all_agenda_links[0]
    future_meeting = check_meeting_date(latest_meeting.text)
    if future_meeting == True:
        agenda_url = latest_meeting.get_attribute("href")
        driver.get(agenda_url)
        time.sleep(10)
        agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
        agenda_readability = check_readability(agenda_content)
        if agenda_readability == True:
            agenda_search = search_agenda_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for New Kent County Planning Commission. " +  agenda_url)
        else:
            messages.append("New agenda available for New Kent County Planning Commission. Document cannot be scanned for keywords. " + agenda_url)
    return messages

"""Norton City Council"""
def norton_city(url):
    driver.get(url)
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
        agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for City of Norton City Council. " + agenda_url)
    return messages

"""Nottoway County"""
def nottoway_county(url, governing_body):
    driver.get(url)
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
        agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
        readable = check_readability(agenda_content)
        if readable==True:
            agenda_search = search_agenda_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Nottoway County " + governing_body + ". " + item)
        elif readable==False:
            messages.append("New meeting document available for Nottoway County " + governing_body +". Document cannot be scanned for keywords. " + item)
    return messages

"""Pittsylvania County, All Boards and Commissions"""
def pittsylvania_county(url):
    driver.get(url)
    time.sleep(10)
    messages = []
    table_rows = driver.find_elements(By.CSS_SELECTOR,"tr")[1:]
    for item in table_rows:
        #since they're all upcoming events only, no need to check the date
        try:
            agenda_link = item.find_element(By.CSS_SELECTOR,"a[class*='agenda_minutes_link'").get_attribute("href")
            driver.get(agenda_link)
            time.sleep(10)
            for i in range(0,100):
                webdriver.common.action_chains.ActionChains(driver).send_keys(webdriver.common.keys.Keys.PAGE_DOWN).perform()
                agenda_content = (driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer"))
                agenda_search = search_agenda_for_keywords(agenda_content)
                if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Pittsylvania County. " + agenda_link)
                    break
        except:
            continue
    return messages

"Prince Edward County Planning Commission"
def prince_edward_pc(url):
    driver.get(url)
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
        agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
        readable = check_readability(agenda_content)
        if readable == False:
            messages.append("New Planning Commission Agenda available for Prince Edward County. Document cannot be scanned for keywords. " + agenda[0])
        elif readable==True:
            agenda_search = search_agenda_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Prince Edward County Planning Commission. " + agenda[0])  
    return messages 

"Prince Edward County Board of Supervisors"
def prince_edward_bos(url):
    driver.get(url)
    time.sleep(10)
    messages = []
    #row 0 is the column headers, latest meeting will be index 1
    table_rows = driver.find_elements(By.CSS_SELECTOR,"tr")
    future_meetings = [item for item in table_rows[1:] if item.text !="   " and check_meeting_date(item.text.split("Meeting")[1].split("-")[0])==True]
    meeting_links = [item.find_elements(By.CSS_SELECTOR,'a')[1].get_attribute("href") for item in future_meetings]
    for item in meeting_links:
        driver.get(item)
        time.sleep(10)
        pages = driver.find_elements(By.CSS_SELECTOR,"div[class*=page")
        for page in pages:
            driver.execute_script("arguments[0].scrollIntoView();", page)
            time.sleep(2)
            agenda_content = driver.find_elements(By.CSS_SELECTOR,'div[class*=textLayer')
            agenda_search = search_agenda_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Prince Edward County Board of Supervisors. " + item)
    return pd.Series(messages).unique().tolist()

"""Prince William County Planning Commission"""
def prince_william_pc(url):
    driver.get(url)
    time.sleep(10)
    messages = []
    agenda_links = driver.find_elements(By.CSS_SELECTOR,"a[href*=Agenda")
    agenda_links_href = []
    for item in agenda_links:
        agenda_links_href.append(item.get_attribute("href"))
    for item in agenda_links_href:
        driver.get(item)
        time.sleep(10)
        agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search ==True:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Prince William Planning Commission. " + item)
    return messages

"""Richmond County"""
def richmond_county(url):
    driver.get(url)
    time.sleep(10)
    messages = []
    agenda_links = driver.find_elements(By.CSS_SELECTOR, "a[href*='.pdf'")
    for item in agenda_links:
        if item.text != "":
            future_meeting = check_meeting_date(item.text)
            if future_meeting == True:
                messages.append("New Board of Supervisors Meeting Agenda posted for Richmond County. Document cannot be scanned for keywords. ")
            else:
                break
    return messages

"""Southampton County"""
def southampton_county(url,governing_body):
    driver.get(url)
    time.sleep(10)
    messages = []
    list_items = driver.find_elements(By.CSS_SELECTOR,"li")
    current_year = [item for item in list_items if str(datetime.date(datetime.now()).year) in item.text]
    driver.get(current_year[0].find_element(By.CSS_SELECTOR,"a").get_attribute("href"))
    time.sleep(10)
    links = driver.find_elements(By.CSS_SELECTOR,"a")
    future_meetings = get_future_meeting_links(links)
    for link in future_meetings:
        driver.get(link)
        time.sleep(10)
        agenda_content = driver.find_elements(By.CSS_SELECTOR,"section[class*='main-content-wrap'")
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Southampton County " + governing_body + ". " + link)
    return messages

"""South Boston City Council"""
def south_boston(url):
    driver.get(url)
    time.sleep(10)
    messages = []
    table_rows = driver.find_elements(By.CSS_SELECTOR,'tr')
    for item in table_rows:
        future_date = check_meeting_date(item.text)
        if future_date == True:
            messages.append("New meeting information available for South Boston City Council in " + item.text +". Document cannot be scanned for keywords. " + url)
        else:
            break
    return messages

"""Staunton"""
def staunton(url):
    driver.get(url)
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
        agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Staunton. " + agenda_link)
    return messages

"""Sussex County"""
def sussex_county(url):
    driver.get(url)
    time.sleep(10)
    list_rows = driver.find_elements(By.CSS_SELECTOR,"li")
    meetings = [item for item in list_rows if "Agenda" in item.text]
    current_meetings = [item for item in meetings if "Archived" not in item.text]
    future_meetings = [item for item in current_meetings if check_meeting_date(item.text)==True]
    document_links =[]
    for item in future_meetings:
        documents = item.find_elements(By.CSS_SELECTOR,"a")
        for item in documents:
            document_links.append(item.get_attribute("href")) 
    messages = search_pdf(document_links,"Sussex County")
    return messages

"""Tazewell County"""
def tazewell_county(url, government_body):
    driver.get(url)
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
                agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
                agenda_search = search_agenda_for_keywords(agenda_content)
                if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Tazewell County " + government_body + ". " + agenda_url)
            except:
                continue
            #if there's no agenda posted yet and the initial agenda link search fails, just move on to the next meeting
    return messages

"""Virginia Beach"""
def virginia_beach_cc(url):
    driver.get(url)
    time.sleep(10)
    messages = []
    current_agenda = driver.find_element(By.CSS_SELECTOR,"a[href*=CurrentBriefAgenda")
    agenda_url = current_agenda.get_attribute("href")
    driver.get(agenda_url)
    time.sleep(10)
    agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
    agenda_search = search_agenda_for_keywords(agenda_content)
    if agenda_search != []:
        messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Virginia Beach in latest City Council meeting agenda. " + agenda_url)
    return messages

def virginia_beach_pc(url):
    driver.get(url)
    time.sleep(10)
    messages = []
    all_rows = driver.find_elements(By.CSS_SELECTOR,'li')
    meetings = [item for item in all_rows if "Agenda" in item.text]
    future_meetings =[item for item in meetings if check_meeting_date(item.text.split(":")[0])==True]
    meeting_urls = [item.find_element(By.CSS_SELECTOR,"a").get_attribute("href") for item in future_meetings]
    for item in meeting_urls:
        driver.get(item)
        time.sleep(10)
        agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Virginia Beach in latest Planning Commission meeting agenda. " + item)
    return messages

"Westmoreland County"
def westmoreland_county(url,governing_body):
    messages = []
    driver.get(url)
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
        agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Westmoreland County " + governing_body + ". " + item)
    return messages

"City of Williamsburg"
def williamsburg(url,governing_body):
    driver.get(url)
    time.sleep(10)
    messages = []
    #latest year will be the top folder
    current_year = driver.find_element(By.CSS_SELECTOR,'a[class*="folder-link').get_attribute('href')
    driver.get(current_year)
    time.sleep(10)
    agendas = driver.find_elements(By.CSS_SELECTOR,'a[class*="document-link"')
    html_agendas = [item for item in agendas if 'Html' in item.text]
    future_meetings = get_future_meeting_links(html_agendas)
    for item in future_meetings:
        messages.append("New meeting document available for Williamsburg " + governing_body + ". Document cannot be scanned for keywords. " + item)
    return messages

"""Wythe County"""
def wythe_county(url):
    driver.get(url)
    time.sleep(10)
    messages = []
    agenda_links = driver.find_elements(By.CSS_SELECTOR,"a[href*=package")
    future_meetings = get_future_meeting_links(agenda_links)
    for item in future_meetings:
        driver.get(item)
        time.sleep(10)
        agenda_content = driver.find_elements(By.CSS_SELECTOR,"svg[class*=textLayer")
        if agenda_content == []:
            agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Wythe County. " + item)
    return messages