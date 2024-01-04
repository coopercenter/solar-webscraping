from webscraping_driver import *

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
    #meeting_date = dateutil.parser.parse(meeting_time_string, fuzzy=True)
    if datetime.now() < dateutil.parser.parse(meeting_time_string, fuzzy=True) or datetime.now() == dateutil.parser.parse(meeting_time_string, fuzzy=True):
        return True
    else:
        return False

def check_readibility(agenda_content):
    agenda_string = ""
    for item in agenda_content:
        agenda_string = agenda_string + item.text
    if agenda_string == "":
        readibility = False
    else:
        readibility = True
    return readibility

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

"""Webscraping Functions"""

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

"""BoardDocs"""
def check_boarddocs_agendas(locality,meetings_page):
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
                #pause, give the page time to load
                time.sleep(2)
                #find the element to click to view the meeting agenda for this meeting
                meeting_agenda = driver.find_element(By.CSS_SELECTOR, "a[id*='btn-view-agenda'")
                #click the meeting agenda button
                meeting_agenda.click()
                #pause, give the page time to load
                time.sleep(2)
                #Now to get ALL the agenda content
                all_agenda_topics = driver.find_elements(By.CSS_SELECTOR, "span[class*='title'")
                #run the keyword search
                agenda_search = search_agenda_for_keywords(all_agenda_topics)
                if agenda_search !=[]:
                    update_messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + locality + " in " + meeting_title)
                meetings_page.click()
                time.sleep(2)
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
        time.sleep(2)
        messages = check_boarddocs_agendas(locality,meetings_page)
        if two_pages==True:
            govt_tab = driver.find_element(By.CSS_SELECTOR,"a[id*=btn-board")
            govt_tab.click()
            menu_options = driver.find_elements(By.CSS_SELECTOR,"a[class*=dropdown-item")
            for item in menu_options:
                if "Planning Commission" in item.text:
                    planning_commission=item
            planning_commission.click()
            time.sleep(2)
            pc_messages = check_boarddocs_agendas(locality,meetings_page)
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
        time.sleep(3)
        all_meetings = driver.find_elements(By.CSS_SELECTOR,"li[class*='cpp-MuiListItem-container'")
        meetings_with_agendas = []
        for item in all_meetings:
            try:
                #test if there's a download button, indicating agenda files have been posted. Lack of files to scan will throw an error, and we won't waste time checking that meeting link for keywords
                item.find_element(By.CSS_SELECTOR,"button[id*=downloadFilesMenu")
                meetings_with_agendas.append(item)
            except:
                continue
        meeting_titles = []
        for item in meetings_with_agendas:
            meeting_titles.append(item.text.replace("\n"," "))
        meeting_links = []
        for item in meetings_with_agendas:
            meeting_links.append(item.find_element(By.CSS_SELECTOR,"a").get_attribute("href"))
        for i in range(0,len(meeting_links)):
            driver.get(meeting_links[i])    
            time.sleep(2)
            pdf_viewer_frame = driver.find_elements(By.CSS_SELECTOR,"iframe[id*='file-id'")
            if pdf_viewer_frame != []:
                driver.switch_to.frame(pdf_viewer_frame[0])
                agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
                agenda_search = search_agenda_for_keywords(agenda_content)
                if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + locality + " in " + meeting_titles[i] + ". " + meeting_links[i])
        return messages
    else: 
        return url_test
    
"""CivicWeb"""
def civicweb(url,locality):
    driver.get(url)
    time.sleep(5)
    messages = []
    agenda_buttons = driver.find_elements(By.CSS_SELECTOR,"button[id*='ctl00_MainContent_MeetingButton'")
    for item in agenda_buttons:
        if item.text !="":
            future_meeting = check_meeting_date(item.text)
            if future_meeting == True:
                item.click()
                time.sleep(1)
                #switch to the agenda viewer frame
                agenda_frame = driver.find_element(By.CSS_SELECTOR,"iframe")
                driver.switch_to.frame(agenda_frame)
                agenda_content = driver.find_elements(By.CSS_SELECTOR,"html")
                agenda_search = search_agenda_for_keywords(agenda_content)
                if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + locality + " in " + item.text + ". " + url)
                driver.switch_to.window(driver.window_handles[0])
    return messages

"""DocumentCenter"""
def document_center(url,locality):
    driver.get(url)
    time.sleep(2)
    messages = []
    folders = driver.find_elements(By.CSS_SELECTOR,"span")
    time.sleep(1)
    for item in folders:
        if item.text == "Board of Supervisors":
            item.click()
            break
    time.sleep(2)
    new_folders = driver.find_elements(By.CSS_SELECTOR,"span")
    time.sleep(1)
    for item in new_folders:
        if item.text == "Agenda":
            item.click()
            break
    time.sleep(2)
    year_folders = driver.find_elements(By.CSS_SELECTOR,"span")
    time.sleep(1)
    for item in year_folders:
        if item.text == "2023":
            item.click()
            break
    time.sleep(2)
    agenda_links = driver.find_elements(By.CSS_SELECTOR,"a[class*=pdf")
    time.sleep(1)
    latest_agenda = agenda_links[-1].get_attribute("href")
    agenda_title = agenda_links[-1].text
    driver.get(latest_agenda)
    time.sleep(2)
    agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
    agenda_search = search_agenda_for_keywords(agenda_content)
    if agenda_search != []:
        messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for "+ locality + " in " + agenda_title + ". " + latest_agenda)
    return messages

"""eScribe"""
def escribe(url,locality):
    driver.get(url)
    time.sleep(5)
    messages = []
    future_meetings = driver.find_elements(By.CSS_SELECTOR,"div[class*='upcoming-meeting-container'")
    #since all the posted meetings are upcoming meetings, we can skip checking the date
    for item in future_meetings:
        meeting_title = item.text.replace("\n"," ")
        try:
            agenda_link = item.find_element(By.CSS_SELECTOR,'a[aria-label*="Agenda Cover Page"')
            agenda_url = agenda_link.get_attribute("href")
            agenda_link.click()
            time.sleep(2)
            driver.switch_to.window(driver.window_handles[1])
            agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
            agenda_search = search_agenda_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + locality + " in "  +  meeting_title + ". " + agenda_url)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        except:
            continue
    return messages

"""Event List"""
def event_list(url,locality):
    driver.get(url)
    time.sleep(5)
    messages = []
    pc_meetings = driver.find_elements(By.CSS_SELECTOR,"a[href*='planning-commission'")
    meeting_urls= []
    for item in pc_meetings:
        if item.text !='':
            meeting_urls.append(item.get_attribute('href'))
    bos_links = driver.find_elements(By.CSS_SELECTOR,"a[href*='board-of-supervisors'")
    for item in bos_links:
        if item.text !='':
            meeting_urls.append(item.get_attribute("href"))
    solar_meetings = driver.find_elements(By.CSS_SELECTOR,"a[href*='solar'")
    comp_plan_meetings = driver.find_elements(By.CSS_SELECTOR,"a[href*='comprehensive-plan-'")
    zoning_ordinance_meetings = driver.find_elements(By.CSS_SELECTOR,"a[href*='zoning-ordinance'")
    for item in solar_meetings:
        if solar_meetings !=[]:
            messages.append("Keyword 'solar' found in upcoming meeting title for " + locality + '. ' + item.get_attribute('href'))
    for item in comp_plan_meetings:
        if comp_plan_meetings !=[]:
            messages.append("Keyword 'comprehensive plan' found in upcoming meeting title for " +locality + ". " + item.get_attribute('href'))
    for item in zoning_ordinance_meetings:
        if zoning_ordinance_meetings !=[]:
            messages.append("Keyword 'zoning ordinance' found in upcoming meeting title for " + locality + ". " + item.get_attribute('href')) 
    for item in meeting_urls:
            driver.get(item)
            time.sleep(5)
            agenda_content = driver.find_elements(By.CSS_SELECTOR,"p")
            agenda_search = search_agenda_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + locality + ". " + item)
    return messages

"""Granicus"""
def granicus_version_2(url, locality):
    driver.get(url)
    messages = []
    all_meetings = driver.find_elements(By.CSS_SELECTOR,"a[href*='Citizens/Detail_Meeting")
    meeting_links = []
    meeting_titles = []
    for item in all_meetings:
        meeting_links.append(item.get_attribute("href"))
        meeting_titles.append(item.text)
    for i in range(0,len(all_meetings)):
        try:
            future_meeting = check_meeting_date(meeting_titles[i])
            if future_meeting == True:
                driver.get(meeting_links[i])
                time.sleep(2)
                try:
                    agenda_link = driver.find_element(By.CSS_SELECTOR,"a[id*=PublicAgendaFile")
                    agenda_link.click()
                    driver.switch_to.window(driver.window_handles[1])
                    agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
                    agenda_search = search_agenda_for_keywords(agenda_content)
                    if agenda_search != []:
                        messages.append("Keyword(s) " + ", ".join(agenda_search) +" found in upcoming meeting for " + locality + " in " + meeting_titles[i])
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                except:
                    continue
        except:
            continue
        else:
            break
    return messages

def granicus(url,locality):
    driver.get(url)
    time.sleep(3)
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
                    meeting_title = item.text.split("Agenda")[0]
                    agenda_packet.click()
                    time.sleep(4)
                    driver.switch_to.window(driver.window_handles[1])
                    agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
                    agenda_search = search_agenda_for_keywords(agenda_content)
                    if agenda_search != []:
                        messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + locality + " in " + meeting_title + ". " + agenda_url)
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
    messages=[]
    time.sleep(2)
    frame = driver.find_element(By.CSS_SELECTOR,"iframe[name=frame1")
    driver.switch_to.frame(frame)
    year_folders = driver.find_elements(By.CSS_SELECTOR,"td")
    #find the folder for the current yeaer
    current_folder = [item for item in year_folders if item.text==str(datetime.today().year)]
    current_folder_link = current_folder[0].find_element(By.CSS_SELECTOR,"a").get_attribute('href')
    meeting_folders = driver.find_elements(By.CSS_SELECTOR,"tr")
    driver.get(current_folder_link)
    future_meetings = []
    for item in meeting_folders:
        try:
            if check_meeting_date(item.text)==True:
                future_meetings.append(item.find_element(By.CSS_SELECTOR,"a").get_attribute('href'))
        except:
            continue 
    for item in future_meetings:
        driver.get(item)
        time.sleep(2)
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
        time.sleep(2)
        table_rows = driver.find_elements(By.CSS_SELECTOR,'tr[id*=ctl00_')
        future_meetings = [item for item in table_rows if check_meeting_date(item.text.split("/2023")[0])==True]
        meeting_urls = [item.find_element(By.CSS_SELECTOR,"a[id*=hypMeetingDetail").get_attribute('href') for item in future_meetings]
        meeting_titles = [item.text for item in future_meetings]
        for i in range(0,len(meeting_urls)):
            if meeting_urls[i] != None:
                driver.get(meeting_urls[i])
                time.sleep(2)
                agenda_content = driver.find_elements(By.CSS_SELECTOR,'tr[id*=ctl00')
                agenda_search = search_agenda_for_keywords(agenda_content)
                if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + locality + " in " + meeting_titles[i] + ". " + meeting_urls[i])
        return messages
    else:
        return url_test

"""Meetings Table"""
def meetings_table(url,locality):
    driver.get(url)
    time.sleep(5)
    messages = []
    all_rows = driver.find_elements(By.CSS_SELECTOR,"tr")[1:]
    future_meetings = []
    for item in all_rows:
        future_meeting = check_meeting_date(item.text.split("-")[0])
        if future_meeting==True:
            future_meetings.append(item)
    agenda_links = []
    meeting_titles = []
    for item in future_meetings:
        try:
            agenda_links.append(item.find_element(By.CSS_SELECTOR,"a[title*=Agenda"))
        except:
            #throws an error of no links are posted yet, so do this and keep going to keep the indices aligned
            agenda_links.append(None)
        finally:
            meeting_titles.append(item.text.split("Meeting")[0])
    for i in range(0,len(agenda_links)):
        if agenda_links[i] != None:
            agenda_links[i].click()
            time.sleep(2)
            driver.switch_to.window(driver.window_handles[1])
            agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
            agenda_search = search_agenda_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + locality + " in " + meeting_titles[i])
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
        #find the links to the ONLINE agendas (not the download pdf buttons)
        all_agenda_links = driver.find_elements(By.CSS_SELECTOR, "a[style*='cursor:pointer'")
        main_window = driver.window_handles[0]
        messages=[]
        for i in range(0,len(all_agenda_links)):
            agenda_links = driver.find_elements(By.CSS_SELECTOR, "a[style*='cursor:pointer'")
            agenda_links[i].click()
            time.sleep(5)
            #switch to the new window
            agenda_window = driver.window_handles[1]
            driver.switch_to.window(agenda_window)
            #find the date from the information in the agenda
            agenda_headings = driver.find_elements(By.CSS_SELECTOR, "span[style*='font'")
            for item in agenda_headings:
                try:
                    future_date=check_meeting_date(item.text)
                    meeting_date = item.text
                except:
                    continue
                else:
                    break
            if future_date==True:
                #find the rest of the agenda content
                agenda_content = driver.find_elements(By.CSS_SELECTOR, "td")
                agenda_search = search_agenda_for_keywords(agenda_content)
                if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + locality + " in " + agenda_headings[1].text + " " + meeting_date)
            else:
                break
            driver.close()
            driver.switch_to.window(main_window)
        return messages
    else:
        return url_test

"""PrimeGov"""
def prime_gov(url, locality):
    driver.get(url)
    time.sleep(2)
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
    url_test = verify_url(url)
    messages=[]
    empty_messages = []
    if url_test==True:
        driver.get(url)
        time.sleep(5)
        meeting_links = driver.find_elements(By.CSS_SELECTOR,"a[href*=Calendar")
        meeting_times = driver.find_elements(By.CSS_SELECTOR,"td[class*=event_datetime")
        meeting_links_href=[]
        for item in meeting_links:
            meeting_links_href.append(item.get_attribute("href"))
        meeting_times_text=[]
        for item in meeting_times:
            meeting_times_text.append(item.text)
        main_window = driver.window_handles[0]
        meeting_titles = []
        for i in range(0,len(meeting_times)):
            meeting_titles.append(meeting_links[i].text + " " + meeting_times[i].text)
        for i in range(0,len(meeting_links)):
            driver.get(meeting_links_href[i])
            time.sleep(2)
            main_window=driver.window_handles[0]
            try:
                agenda_link = driver.find_element(By.CSS_SELECTOR,"a[href*=showpublisheddocument")
                agenda_link.click()
                time.sleep(2)
                agenda_window=driver.window_handles[1]
                driver.switch_to.window(agenda_window)
                agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
                agenda_search=search_agenda_for_keywords(agenda_content)
                driver.close()
                driver.switch_to.window(main_window)
                driver.get(url)
                time.sleep(2)
                if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Albemarle County Planning Commission in " + meeting_titles[i])
            except:
                empty_messages.append("No agenda available for "+ meeting_titles[i])
    if url_test != True:
        messages.append(url_test)
    return messages

"""Alleghany County"""
#only BOS agendas are available
def alleghany_county(bos_url):
    messages=[]
    url_test = verify_url(bos_url)
    if url_test==True:
        driver.get(bos_url)
        time.sleep(2)
        #hunt down the agenda links
        all_agenda_links = driver.find_elements(By.CSS_SELECTOR,"a[title*=Mtg")
        for item in all_agenda_links:
            future_date=check_meeting_date(item.text)
            if future_date==True:
                item.click()
                time.sleep(2)
                agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
                agenda_search = search_agenda_for_keywords(agenda_content)
                if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Alleghany County Board of Supervisors in " + item.text)
                driver.back()
                time.sleep(2)
        return messages
    else:
        return url_test

"""Arlington County"""
def main_method_arlington(url):
    messages=[]
    driver.get(url)
    time.sleep(2)
    meeting_names = driver.find_elements(By.CSS_SELECTOR,"td[headers*='EventName'")
    meeting_dates = driver.find_elements(By.CSS_SELECTOR,"td[headers*='EventDate'")
    a_tags = driver.find_elements(By.CSS_SELECTOR,"a[href*='AgendaViewer'")
    agenda_links=[]
    for item in a_tags:
        if item.text=="Agenda":
            agenda_links.append(item.get_attribute("href"))
        else:
            break
    meeting_titles = []
    for i in range(0,len(agenda_links)):
        meeting_titles.append(meeting_names[i].text + " " + meeting_dates[i].text)
    for i in range(0,len(agenda_links)):
        driver.get(agenda_links[i])
        time.sleep(2)
        agenda_content=driver.find_elements(By.CSS_SELECTOR, "body")
        agenda_search=search_agenda_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Arlington County in " + meeting_titles[i])
        driver.get(url)
        time.sleep(1)
    return messages   

def arlington_county(pc_url,bos_url):
    url_test_pc=verify_url(pc_url)
    url_test_bos=verify_url(bos_url)
    messages=[]
    if url_test_pc==True:
        pc_messages = main_method_arlington(pc_url)
        messages += pc_messages
    if url_test_pc!= True:
        messages.append(url_test_pc)
    if url_test_bos==True:
        bos_messages=main_method_arlington(bos_url)
        messages+=bos_messages
    if url_test_bos!=True:
        messages.append(url_test_bos)
    return messages

"""Bath County"""
def bath_county(url):
    messages=[]
    driver.get(url)
    time.sleep(5)
    #get whatever meeting links are available
    try:
        pc_links = driver.find_elements(By.CSS_SELECTOR,"a[title*='Planning'")
    except:
        pc_links = None
    try:
        bos_links = driver.find_elements(By.CSS_SELECTOR,"a[title*='Board of Supervisors'")
    except:
        bos_links = None
    meeting_titles = []
    meeting_urls = []
    for item in pc_links:
        if item != None:
            meeting_titles.append(item.text)
            meeting_urls.append(item.get_attribute("href"))
    for item in bos_links:
        if item != None:
            meeting_titles.append(item.text)
            meeting_urls.append(item.get_attribute("href"))
    for i in range(0,len(meeting_urls)):
        driver.get(meeting_urls[i])
        time.sleep(2)
        meeting_documents = driver.find_elements(By.CSS_SELECTOR, "a[href*=DisplayFile")
        meeting_document_urls = []
        for item in meeting_documents:
            meeting_document_urls.append(item.get_attribute("href"))
        for item in meeting_document_urls:
            driver.get(item)
            time.sleep(2)
            agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
            agenda_readibility = check_readibility(agenda_content)
            if agenda_readibility==True:
                agenda_search = search_agenda_for_keywords(agenda_content)
                if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Bath County in " + meeting_titles[i] + ". " + item)
            else:
                messages.append("New meeting document available for Bath County. Check for solar. " + item)
    return messages

"""Bland County"""
def bland_county(url):
    driver.get(url)
    time.sleep(2)
    messages = []
    table_rows = driver.find_elements(By.CSS_SELECTOR,"tr")
    latest_meeting = table_rows[-1]
    future_meeting = check_meeting_date(latest_meeting.text)
    if future_meeting == True:
        agenda_url = latest_meeting.find_element(By.CSS_SELECTOR,"a").get_attribute("href")
        messages.append("New meeting agenda available for Bland County Board of Supervisors. Check for new solar information. " + agenda_url)
    return messages

"Brunswick County"
def brunswick_county(url):
    messages=[]
    driver.get(url)
    time.sleep(2)
    latest_agenda = driver.find_elements(By.CSS_SELECTOR,'a[href*=".pdf"')[-1]
    future_meeting = check_meeting_date(latest_agenda.text)
    if future_meeting == True:
        agenda_link = latest_agenda.get_attribute('href')
        driver.get(agenda_link)
        time.sleep(2)
        agenda_content = driver.find_elements(By.CSS_SELECTOR, "div[class*=textLayer")
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search !=[]:
            messages.append('Keyword(s) ' + ", ".join(agenda_search)+' found in upcoming meeting for Brunswick County. ' + agenda_link)
    return messages

"""Buchanan County"""
def buchanan_county(url):
    driver.get(url)
    time.sleep(5)
    messages = []
    pdf_links = driver.find_elements(By.CSS_SELECTOR,"a[href*='.pdf")
    visible_documents = [item for item in pdf_links if item.text != '']
    latest_minutes = [item for item in visible_documents if "Minutes" in item.text][0]
    #since they're only posting minutes not agendas, and minutes are posted long after the fact, we'll skip the date checking
    minutes_url = latest_minutes.get_attribute("href")
    driver.get(minutes_url)
    time.sleep(1)
    agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
    agenda_search = search_agenda_for_keywords(agenda_content)
    if agenda_search != []:
        messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Buchanan County. " + minutes_url)
    return messages

"""Buckingham County"""
def buckingham_county(url):
    driver.get(url)
    time.sleep(5)
    messages = []
    all_meeting_rows = driver.find_elements(By.CSS_SELECTOR,"tr")
    latest_meeting = all_meeting_rows[0]
    #split around the colon, otherwise the date fails to register
    future_meeting = check_meeting_date(latest_meeting.text.split("  ")[0])
    if future_meeting == True:
        meeting_title = latest_meeting.text.split("  ")[0]
        agenda_url = latest_meeting.find_element(By.CSS_SELECTOR,"a").get_attribute("href")
        driver.get(agenda_url)
        time.sleep(2)
        agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Buckingham County in " + meeting_title + ". " + agenda_url)
    return messages    

"""Buena Vista City Council"""
def buena_vista_city_council(url):
    driver.get(url)
    time.sleep(2)
    messages = []
    links = driver.find_elements(By.CSS_SELECTOR,"a")
    agenda_links = []
    for item in links:
        if 'Council Agenda' in item.text:
            agenda_links.append(item)
    future_meeting = check_meeting_date(agenda_links[0].text)
    if future_meeting==True:
        messages.append("New agenda available for Buena Vista City Council. PDF cannot be read, check for solar updates. " + agenda_links[0].get_attribute("href"))
    return messages

"""Carroll County"""
def carroll_county(url):
    driver.get(url)
    time.sleep(2)
    messages = []
    table_rows = driver.find_elements(By.CSS_SELECTOR,'tr')
    for item in table_rows:
        future_meeting = check_meeting_date(item.text)
        if future_meeting == True:
            try:
                agenda_link = item.find_element(By.CSS_SELECTOR,"a[href*='Agenda.pdf'")
                meeting_header = item.text
                agenda_link.click()
                time.sleep(2)
                driver.switch_to.window(driver.window_handles[1])
                agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
                agenda_search = search_agenda_for_keywords(agenda_content)
                if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Carroll County in " + meeting_header)
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
            except:
                continue
        else:
            break
    return messages

"""Charlotte County"""
#Documents must be read individually for now, since they're scans of physical documents
def charlotte_county(url):
    driver.get(url)
    time.sleep(5)
    messages = []
    table_rows = driver.find_elements(By.CSS_SELECTOR,"div[class*='table-responsive'")
    meetings_with_agendas = []
    for item in table_rows:
        if "Agenda" in item.text:
            meetings_with_agendas.append(item)
        elif "Packet" in item.text:
            meetings_with_agendas.append(item)
    for item in meetings_with_agendas:
        future_meeting = check_meeting_date(item.text.split(" ")[0])
        if future_meeting == True:
            meeting_title = item.text
            #documents aren't readable, they're scans, need a different alert
            if " Solar " in meeting_title:
                messages.append("New solar information available for Charlotte County in " + meeting_title)
            elif " solar " in meeting_title:
                messages.append("New solar information available for Charlotte County in " + meeting_title)
            else:
                messages.append("New meeting information available for Charlotte County in " + meeting_title + ", check documents for solar information")
        else:
            break
    return messages

"""Clarke County"""
def clarke_county(url):
    driver.get(url)
    time.sleep(5)
    messages = []
    #skip the first two entries since they're just the file path links
    all_meeting_links = driver.find_elements(By.CSS_SELECTOR,"a[class*='content_link'")[2:]
    latest_meeting = all_meeting_links[0]
    #split around the colon, otherwise the date fails to register
    future_meeting = check_meeting_date(latest_meeting.text.split("  ")[0])
    if future_meeting == True:
        meeting_title = latest_meeting.text
        agenda_url = latest_meeting.get_attribute("href")
        driver.get(agenda_url)
        time.sleep(2)
        agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Clarke County in " + meeting_title + ". " + agenda_url)
    return messages  

"""Town of Clifton Forge"""
def clifton_forge(url):
    driver.get(url)
    time.sleep(2)
    messages = []
    agenda_links = driver.find_elements(By.CSS_SELECTOR,"a[class*='attachment-link'")
    agenda_urls = []
    agenda_titles = []
    for item in agenda_links:
        agenda_urls.append(item.get_attribute("href"))
        agenda_titles.append(item.text)
    for i in range(0,len(agenda_urls)):
        future_meeting = check_meeting_date(agenda_titles[i])
        if future_meeting == True:
            driver.get(agenda_urls[i])
            time.sleep(2)
            agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
            agenda_search = search_agenda_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for the Town of Clifton Forge in " + agenda_titles[i] + ". " + agenda_urls[i])
        else:
            #since the most recent meeting is posted first, no need to keep looking
            break
    return messages

"""Town of Covington"""
def covington(url):
    driver.get(url)
    time.sleep(4)
    messages = []
    year_expand = driver.find_elements(By.CSS_SELECTOR, "div[class*='accordion-item'")
    #the labels won't show up, but the latest year will be the first one
    year_expand[0].click()
    time.sleep(2)
    agendas = driver.find_elements(By.CSS_SELECTOR,"a[href*='.pdf'")
    agendas_visible = []
    for item in agendas:
        if item.text !='':
            agendas_visible.append(item)
    #check the date for the most recently posted agenda
    latest_agenda = agendas_visible[-1]
    future_date = check_meeting_date(latest_agenda.text)
    if future_date == True:
        agenda_url = latest_agenda.get_attribute('href')
        driver.get(agenda_url)
        time.sleep(1)
        agenda_content = driver.find_elements(By.CSS_SELECTOR,'div[class*=textLayer')
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for the Town of Covington. " + agenda_url)
    return messages

"Craig County"
def craig_county(url):
    messages = []
    driver.get(url)
    time.sleep(2)
    #Find the link and check the date. That's as far as we go because the PDFs are scans.
    latest_agenda = driver.find_element(By.CSS_SELECTOR,"a[href*=Agenda")
    future_meeting = check_meeting_date(latest_agenda.text)
    if future_meeting==True:
        messages.append("New meeting agenda available for Craig County Board of Supervisors. Check for solar. " + latest_agenda.get_attribute('href'))
    return messages

"""Town of Emporia"""
#will need to update the links, currently browsing the 2023 link
def emporia(url):
    driver.get(url)
    time.sleep(2)
    messages = []
    latest_meeting = driver.find_element(By.CSS_SELECTOR,'div[class*="views-row"')
    future_meeting = check_meeting_date(latest_meeting.text.split('\n')[0])
    if future_meeting == True:
        meeting_title = latest_meeting.text.replace('\n',' ')
        agenda_link = latest_meeting.find_element(By.CSS_SELECTOR,"a")
        meeting_url = agenda_link.get_attribute("href")
        driver.get(meeting_url)
        time.sleep(2)
        agenda_content = driver.find_elements(By.CSS_SELECTOR, "div[class*=textLayer")
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for the Town of Emporia in " + meeting_title + ". " + meeting_url)
    return messages

"""Fairfax County"""
def fairfax_county_bos(url):
    driver.get(url)
    time.sleep(2)
    messages = []
    meetings = driver.find_elements(By.CSS_SELECTOR,"div[class*='calendar-title'")
    meeting_urls = []
    meeting_titles = []
    for item in meetings:
        meeting_urls.append(item.find_element(By.CSS_SELECTOR,"a").get_attribute("href"))
        meeting_titles.append(item.text)
    for i in range(0,len(meeting_urls)):
        driver.get(meeting_urls[i])
        time.sleep(2)
        try:
            agenda_link = driver.find_element(By.CSS_SELECTOR,"a[href*='.pdf'").get_attribute("href")
            driver.get(agenda_link)
            time.sleep(2)
            for i in range(0,10):
                webdriver.common.action_chains.ActionChains(driver).send_keys(webdriver.common.keys.Keys.PAGE_DOWN).perform()
                agenda_content = (driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer"))
                agenda_search = search_agenda_for_keywords(agenda_content)
                if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Fairfax County Board of Supervisors in " + meeting_titles[i] + ". " + meeting_urls[i])
                    break
        except:
            continue
    return messages

def fairfax_county_pc(url,year):
    driver.get(url)
    time.sleep(5)
    messages = []
    months_tag = "a[href*=" + year
    months = driver.find_elements(By.CSS_SELECTOR,months_tag)
    relevant_months = []
    for item in months:
        if item.text == datetime.now().strftime("%B"):
            relevant_months.append(item.get_attribute('href'))
        elif item.text == (datetime.now() + dateutil.relativedelta.relativedelta(months=1)).strftime('%B'):
            relevant_months.append(item.get_attribute('href'))
    for item in relevant_months:
        driver.get(item)
        time.sleep(2)
        agenda_links = driver.find_elements(By.CSS_SELECTOR,"a[href*='.pdf'")
        agenda_urls = []
        for item in agenda_links:
            agenda_urls.append(item.get_attribute("href"))
        for item in agenda_urls:
            try:
                future = check_meeting_date(item.split('/')[-1].split('.pdf')[0])
                if future==True:
                    driver.get(item)
                    time.sleep(2)
                    agenda_content = (driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer"))
                    agenda_search = search_agenda_for_keywords(agenda_content)
                    if agenda_search != []:
                        messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Fairfax County Planning Commission in " + item)
            except:
                driver.get(item)
                time.sleep(2)
                agenda_content = (driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer"))
                agenda_search = search_agenda_for_keywords(agenda_content)
                if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Fairfax County Planning Commission in " + item)
    return messages

"""Floyd County"""
def floyd_county(url):
    driver.get(url)
    time.sleep(5)
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
        meeting_title = latest_meeting.text
        agenda_url = latest_meeting.find_element(By.CSS_SELECTOR,"a").get_attribute("href")
        driver.get(agenda_url)
        time.sleep(2)
        agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Floyd County Board of Supervisors in " + meeting_title + ". " + agenda_url)
    return messages        

"""City of Franklin"""
def city_of_franklin(url):
    driver.get(url)
    time.sleep(5)
    messages=[]
    #this website requires several steps to get to the right data, as it automatically lands on the 2013 agendas page
    years = driver.find_elements(By.CSS_SELECTOR,'li[class*="top-tab"')
    latest_year = years[-1]
    latest_year.click()
    time.sleep(1)
    months = driver.find_elements(By.CSS_SELECTOR,"tr[class*='month-label'")
    latest_month = months[-1]
    latest_month.click()
    time.sleep(1)
    agendas = driver.find_elements(By.CSS_SELECTOR, "a[href*='agenda.pdf'")
    latest_agenda = agendas[-1]
    future_meeting = check_meeting_date(latest_agenda.text)
    if future_meeting == True:
        meeting_title = latest_agenda.text
        meeting_url = latest_agenda.get_attribute("href")
        latest_agenda.click()
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[1])
        agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for the City of Franklin in " + meeting_title + ". " + meeting_url)
    return messages

"""City of Galax"""
def galax(url):
    driver.get(url)
    time.sleep(2)
    messages = []
    agenda_links = driver.find_elements(By.CSS_SELECTOR,"a[class*='pb_button'")
    latest_agenda = agenda_links[len(agenda_links) - 1]
    future_meeting = check_meeting_date(latest_agenda.text)
    if future_meeting == True:
        agenda_title = latest_agenda.text
        agenda_url = latest_agenda.get_attribute("href")
        latest_agenda.click()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[1])
        agenda_content = driver.find_elements(By.CSS_SELECTOR,"div")
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for the City of Galax in " + agenda_title + ". " + agenda_url)
    return messages

"""Giles County Board of Supervisors"""
def giles_county(url):
    driver.get(url)
    time.sleep(2)
    messages = []
    #follow the link to the latest agenda
    agenda_link = driver.find_element(By.CSS_SELECTOR,'a[class*="qbutton"').get_attribute("href")
    driver.get(agenda_link)
    time.sleep(2)
    agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
    agenda_search = search_agenda_for_keywords(agenda_content)
    if agenda_search != []:
        messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Giles County in next agenda")
    return messages

"Grayson County"
def grayson_county(url):
    driver.get(url)
    messages=[]
    time.sleep(2)
    links = driver.find_elements(By.CSS_SELECTOR,'a[class*="brz-a"')
    agendas=[]
    for item in links:
        if 'Agenda' in item.text:
            agendas.append(item)
    future_meeting=check_meeting_date(agendas[0].text)
    if future_meeting==True:
        agenda_link=agendas[0].get_attribute("href")
        driver.get(agenda_link)
        time.sleep(5)
        download_link = driver.find_element(By.CSS_SELECTOR,"a[class*='gde-link'").get_attribute('href')
        driver.get(download_link)
        time.sleep(2)
        agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search !=[]:
            messages.append('Keyword(s) ' + ", ".join(agenda_search)+' found in upcoming meeting for Grayson County. ' + download_link)
    return messages

"""Greensville County"""
def greensville_county(url,government_body):
    driver.get(url)
    time.sleep(2)
    messages = []
    pdf_links = driver.find_elements(By.CSS_SELECTOR,"a[href*='.pdf'")
    agenda_links=[]
    for item in pdf_links:
        if item.text != "":
            agenda_links.append(item)
    for item in agenda_links:
        future_meeting = check_meeting_date(item.text)
        if future_meeting==True:
            meeting_title = item.text
            item.click()
            driver.switch_to.window(driver.window_handles[1])
            agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
            agenda_search = search_agenda_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) +  " found in upcoming meeting for Greensville in " + government_body + ' ' + meeting_title)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        else:
            break
    return messages
    
"""Henrico County"""
def henrico_county_bos(url):
    driver.get(url)
    time.sleep(1)
    messages = []
    #ignore the first entry in the table rows since it's just the column headers
    table_rows = driver.find_elements(By.CSS_SELECTOR,'tr')[1:]
    latest_meeting = table_rows[0]
    future_meeting = check_meeting_date(latest_meeting.text)
    if future_meeting == True:
        meeting_url = latest_meeting.find_element(By.CSS_SELECTOR,"a").get_attribute("href")
        meeting_title = latest_meeting.text.split("Meeting")[0]
        driver.get(meeting_url)
        time.sleep(2)
        agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Henrico County Board of Supervisors in " + meeting_title + ". " + meeting_url)
    return messages   

def henrico_county_pc(url):
    driver.get(url)
    time.sleep(1)
    messages = []
    current_agendas = driver.find_elements(By.CSS_SELECTOR,"a[href*='next.pdf'")
    #there's not a good way to check the date, so we'll just check the current agendas for the board of zoning appeals
    agenda_urls = []
    for item in current_agendas:
        agenda_urls.append(item.get_attribute("href"))
    for item in agenda_urls:
        driver.get(item)
        time.sleep(2)
        agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Henrico County in the latest Planning Commission/Board of Zoning Appeals agenda. " + item)
    return messages        

"""King and Queen County"""
def king_and_queen_county_bos(url):
    driver.get(url)
    time.sleep(5)
    messages = []
    current_agenda = driver.find_element(By.CSS_SELECTOR,"a[href*='/agenda.htm'").get_attribute('href')
    driver.get(current_agenda)
    time.sleep(1)
    agenda_content = driver.find_elements(By.CSS_SELECTOR,"td")
    agenda_search = search_agenda_for_keywords(agenda_content)
    if agenda_search != []:
        messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for King and Queen County Board of Supervisors in current agenda. " +  current_agenda)
    return messages

def king_and_queen_county_pc(url):
    driver.get(url)
    time.sleep(5)
    messages = []
    all_agenda_links = driver.find_elements(By.CSS_SELECTOR,"a[href*='bzondocs/2023 Agendas/'")
    latest_agenda = all_agenda_links[-1]
    future_meeting = check_meeting_date(latest_agenda.text)
    if future_meeting == True:
        meeting_title = latest_agenda.text
        agenda_link = latest_agenda.get_attribute("href")
        latest_agenda.click()
        time.sleep(6)
        driver.switch_to.window(driver.window_handles[1])
        agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for King and Queen County Planning Commission in " + meeting_title + ". " +  agenda_link)
    return messages

"""Lee County"""
def lee_county(url):
    driver.get(url)
    time.sleep(5)
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
    agenda_titles = []
    agenda_urls = []
    for item in upcoming_meetings:
        agenda_titles.append(item.text)
        agenda_urls.append(item.get_attribute("href"))
    for i in range(0,len(agenda_urls)):
        driver.get(agenda_urls[i])
        time.sleep(2)
        agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Lee County Board of Supervisors in " + agenda_titles[i] + ". " +  agenda_urls[i])
    return messages

"""Lexington Planning Commission"""
def lexington_pc(url):
    driver.get(url)
    time.sleep(2)
    messages = []
    agenda_links = driver.find_elements(By.CSS_SELECTOR,"a[class*='content_link'")
    for item in agenda_links:
        future_date = check_meeting_date(item.text.replace("-","/"))
        if future_date == True:
            meeting_title = item.text
            item.click()
            time.sleep(2)
            driver.switch_to.window(driver.window_handles[1])
            agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
            agenda_search = search_agenda_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " ", ".join(agenda_search) + " found in upcoming meeting for the City of Lexington Planning Commission in " + meeting_title)
        else:
            break
    return messages

"LaserFiche for Loudoun Planning Commission"
def loudoun_pc(url):
    driver.get(url)
    messages=[]
    time.sleep(2)
    all_links = driver.find_elements(By.CSS_SELECTOR,"a")
    meeting_doc_folder = [item for item in all_links if item.text == 'Public Hearings & Work Sessions']
    driver.get(meeting_doc_folder[0].get_attribute('href'))
    #find the folder for the current year
    year_folders = driver.find_elements(By.CSS_SELECTOR,"td")
    current_folder = [item for item in year_folders if item.text==str(datetime.today().year)]
    current_folder_link = current_folder[0].find_element(By.CSS_SELECTOR,"a").get_attribute('href')
    meeting_folders = driver.find_elements(By.CSS_SELECTOR,"tr")
    driver.get(current_folder_link)
    future_meetings = []
    for item in meeting_folders:
        try:
            if check_meeting_date(item.text)==True:
                future_meetings.append(item.find_element(By.CSS_SELECTOR,"a").get_attribute('href'))
        except:
            continue 
    for item in future_meetings:
        driver.get(item)
        time.sleep(2)
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
        if 'Solar' or 'solar' in agenda_content:
            keywords.append('Solar')
        if 'Comprehensive Plan' or 'Comprehensive plan' or 'comprehensive plan' in agenda_content:
            keywords.append('Comprehensive Plan')
        if 'Zoning Ordinance' or 'Zoning ordinance' or 'zoning ordinance' in agenda_content:
            keywords.append('Zoning Ordinance')
        if keywords!=[]:
            messages.append('Keyword(s) ' + ", ".join(keywords)+' found in upcoming meeting for  Loudoun County Planning Commission. ' + agenda_link)
        #close and delete the temp file
        temp_agenda.close()
    return messages

"""Lunenburg County"""
def lunenburg_county(url):
    driver.get(url)
    time.sleep(5)
    messages = []
    all_meeting_rows = driver.find_elements(By.CSS_SELECTOR,"tr")
    latest_meeting = all_meeting_rows[0]
    future_meeting = check_meeting_date(latest_meeting.text.split(" ")[0])
    if future_meeting == True:
        meeting_title = latest_meeting.text.split("Agenda")[0]
        agenda_url = latest_meeting.find_element(By.CSS_SELECTOR,"a").get_attribute("href")
        driver.get(agenda_url)
        time.sleep(5)
        agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Lunenburg County in " + meeting_title + ". " + agenda_url)
    return messages  

"""Lynchburg Planning Commission"""
#will hopefully be moved to civic clerk version 2 soon
def lynchburg_pc(url):
    driver.get(url)
    time.sleep(2)
    messages = []
    agenda_links = driver.find_elements(By.CSS_SELECTOR,"a[href*='Agenda.pdf'")
    agenda_href = []
    agenda_title = []
    for item in agenda_links:
        future_meeting = check_meeting_date(item.text)
        if future_meeting == True:
            agenda_href.append(item.get_attribute('href'))
            agenda_title.append(item.text)
        else:
            break
    for i in range(0,len(agenda_href)):
        driver.get(agenda_href[i])
        time.sleep(2)
        agenda_content = driver.find_elements(By.CSS_SELECTOR, "div[class*=textLayer")
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for the City of Lynchburg Planning Commission in " + agenda_title[i])
    return messages

"""Manassas Park"""
def manassas_park(url,government_body):
    driver.get(url)
    time.sleep(2)
    messages = []
    year_buttons = driver.find_elements(By.CSS_SELECTOR,"div[class*='agenda_heading'")
    year_buttons[0].click()
    time.sleep(1)
    table_rows = driver.find_elements(By.CSS_SELECTOR,"tr")
    agenda_links=[]
    for item in table_rows:
        if 'Agenda' in item.text:
            future_meeting = check_meeting_date(item.text)
            if future_meeting == True:
                agenda_links.append(item.find_element(By.CSS_SELECTOR,"a"))
    for item in agenda_links:
        meeting_title = item.text
        item.click()
        driver.switch_to.window(driver.window_handles[1])
        agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Manassas Park in " + government_body + ' ' + meeting_title)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    return messages

"""Montgomery County Planning Commission"""
def montgomery_pc(url):
    driver.get(url)
    time.sleep(5)
    messages = []
    agenda_links = driver.find_elements(By.CSS_SELECTOR,'a[href*="agenda.pdf')
    for item in agenda_links:
        future_meeting = check_meeting_date(item.text)
        if future_meeting==True:
            item.click()
            time.sleep(2)
            driver.switch_to.window(driver.window_handles[1])
            agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
            agenda_search = search_agenda_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Montgomery County Planning Commission in " + item.text)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
    return messages

"""New Kent County Planning Commission"""
def new_kent_county_pc(url):
    driver.get(url)
    time.sleep(5)
    messages = []
    #skip the first entry since it's the link to all archived agendas
    all_agenda_links = driver.find_elements(By.CSS_SELECTOR,"a[href*='Archive'")[1:]
    latest_meeting = all_agenda_links[0]
    future_meeting = check_meeting_date(latest_meeting.text)
    if future_meeting == True:
        agenda_url = latest_meeting.get_attribute("href")
        agenda_title = latest_meeting.text
        latest_meeting.click()
        time.sleep(2)
        agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for New Kent County Planning Commission in " + agenda_title + ". " +  agenda_url)
    return messages

"""Norfolk Planning Commission"""
def norfolk_pc(url):
    driver.get(url)
    time.sleep(10)
    meeting_links = driver.find_elements(By.CSS_SELECTOR,"a[href*='/Citizens/Detail'")
    meeting_links_href = []
    meeting_titles = []
    messages=[]
    for item in meeting_links:
        future_meeting = check_meeting_date(item.text)
        if future_meeting==True:
            meeting_links_href.append(item.get_attribute("href"))
            meeting_titles.append(item.text)
    for i in range(0,len(meeting_links_href)):
        driver.get(meeting_links_href[i])
        time.sleep(5)
        #search for the link to the agenda that opens it in a new tab instead of a download
        try:
            agenda_link = driver.find_element(By.CSS_SELECTOR,'a[id*=PublicAgendaFile')
            agenda_link.click()
            time.sleep(5)
            agenda_window = driver.window_handles[1]
            driver.switch_to.window(agenda_window)
            agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
            agenda_search = search_agenda_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Norfolk Planning Commission in " + meeting_titles[i])
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        except:
            continue
    return messages

"""Norton City Council"""
def norton_city(url):
    driver.get(url)
    time.sleep(3)
    messages = []
    #start from the second entry, since the first result is the link to view all available archives
    all_agendas = driver.find_elements(By.CSS_SELECTOR,"a[href*=Archive")[1:]
    latest_agenda = all_agendas[0]
    future_meeting = check_meeting_date(latest_agenda.text.split("-")[1])
    if future_meeting == True:
        meeting_title = latest_agenda.text
        agenda_url = latest_agenda.get_attribute("href")
        driver.get(agenda_url)
        time.sleep(1)
        agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for City of Norton City Council in " + meeting_title + ". " + agenda_url)
    return messages

"""Nottoway County"""
def nottoway_county(url):
    driver.get(url)
    time.sleep(2)
    messages = []
    table_rows = driver.find_elements(By.CSS_SELECTOR,"tr")
    agenda_links=[]
    meeting_titles = []
    for item in table_rows:
        if 'Agenda' in item.text:
            future_meeting = check_meeting_date(item.text)
            if future_meeting == True:
                agenda_links.append(item.find_element(By.CSS_SELECTOR,"a[href*=Agenda"))
                meeting_titles.append(item.text.replace("\n"," ").split("Agenda")[0])
    for i in range(0,len(agenda_links)):
        agenda_links[i].click()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[1])
        agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Nottoway County in " + meeting_titles[i])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    return messages

"""Pittsylvania County, All Boards and Commissions"""
def pittsylvania_county(url):
    driver.get(url)
    time.sleep(2)
    messages = []
    table_rows = driver.find_elements(By.CSS_SELECTOR,"tr")[1:]
    for item in table_rows:
        #since they're all upcoming events only, no need to check the date
        try:
            meeting_title = item.text.split("-")[0]
            agenda_link = item.find_element(By.CSS_SELECTOR,"a[class*='agenda_minutes_link'")
            agenda_link.click()
            time.sleep(5)
            driver.switch_to.window(driver.window_handles[1])
            for i in range(0,100):
                webdriver.common.action_chains.ActionChains(driver).send_keys(webdriver.common.keys.Keys.PAGE_DOWN).perform()
                time.sleep(2)
                agenda_content = (driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer"))
                agenda_search = search_agenda_for_keywords(agenda_content)
                if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Pittsylvania County in " + meeting_title)
                    break
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        except:
            continue
    return messages

"Prince Edward County Planning Commission"
def prince_edward_pc(url):
    driver.get(url)
    time.sleep(5)
    messages = []
    latest_year = driver.find_element(By.CSS_SELECTOR,"a[class*='content_link'").get_attribute('href')
    driver.get(latest_year)
    time.sleep(2)
    latest_agenda = driver.find_elements(By.CSS_SELECTOR,"a[class*='content_link'")[-1]
    future_meeting = check_meeting_date(latest_agenda.text)
    if future_meeting==True:
        meeting_link = latest_agenda.get_attribute('href')
        messages.append("New Planning Commission Agenda available for Prince Edward County. PDF Cannot be read, please check for new solar information. " + meeting_link)  
    return messages 

"Prince Edward County Board of Supervisors"
def prince_edward_bos(url):
    driver.get(url)
    time.sleep(5)
    messages = []
    table_rows = driver.find_elements(By.CSS_SELECTOR,"tr")
    #row 0 is the column headers, latest meeting will be index 1
    table_rows = driver.find_elements(By.CSS_SELECTOR,"tr")
    #check the attachments at index 1 for a meeting date, index 0 is just a link to the BOS
    future_meeting=check_meeting_date(table_rows[1].find_elements(By.CSS_SELECTOR,'a')[1].text)
    if future_meeting==False:
        links = table_rows[1].find_elements(By.CSS_SELECTOR,'a')
        meeting_docs = [item for item in links if 'Packet' in item.text]
        for item in meeting_docs:
            agenda_link = item.get_attribute('href')
            driver.get(agenda_link)
            time.sleep(2)
            for i in range(0,100):
                webdriver.common.action_chains.ActionChains(driver).send_keys(webdriver.common.keys.Keys.PAGE_DOWN).perform()
                time.sleep(1)
                agenda_content = driver.find_elements(By.CSS_SELECTOR,'div[class*=textLayer')
                agenda_search = search_agenda_for_keywords(agenda_content)
                if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Prince Edward County Board of Supervisors. " + agenda_link) 
    return messages

"""Prince William County Planning Commission"""
def prince_william_pc(url):
    driver.get(url)
    time.sleep(2)
    messages = []
    #it seems that only upcoming agendas are posted, past meetings and agendas are archived on Granicus. Curse them.
    agenda_links = driver.find_elements(By.CSS_SELECTOR,"a[href*=Agenda")
    agenda_links_href = []
    for item in agenda_links:
        #since clicking on the link navigates away from the page, and I want to allow for the possibility of multiple meeting agendas, we'll just tell the driver to "get" the links one by one instead of switching windows
        agenda_links_href.append(item.get_attribute("href"))
    for item in agenda_links_href:
        driver.get(item)
        time.sleep(2)
        agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search ==True:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Prince William Planning Commission in the latest agenda")
    return messages

"""Richmond County"""
def richmond_county(url):
    driver.get(url)
    time.sleep(2)
    messages = []
    agenda_links = driver.find_elements(By.CSS_SELECTOR, "a[href*='.pdf'")
    for item in agenda_links:
        if item.text != "":
            future_meeting = check_meeting_date(item.text)
            if future_meeting == True:
                messages.append("New Board of Supervisors Meeting Agenda posted for Richmond County. Check for Solar")
            else:
                break
    return messages

"""Shenandoah County"""
#Can't actually get text out of the PDFs, only alerts that there's a new meeting agenda available for review
def shenandoah_county_pc(url):
    driver.get(url)
    time.sleep(2)
    messages = []
    #since these are all upcoming, no need to check the dates
    all_links = driver.find_elements(By.CSS_SELECTOR,"a[href*='planning-commission-joint-public-hearing'")
    meeting_links = []
    for item in all_links:
        if item.text == 'More Info':
            meeting_links.append(item.get_attribute("href"))
    info_blocks = driver.find_elements(By.CSS_SELECTOR,"div[class*='em-event em-item'")
    meeting_titles = []
    for item in info_blocks:
        meeting_titles.append(item.text.replace('\n', " ").split("-")[0])
    for i in range(0,len(meeting_links)):
        driver.get(meeting_links[i])
        time.sleep(1)
        try:
            agenda_link = driver.find_elements(By.CSS_SELECTOR,"a[href*='Agenda-Packet.pdf'")
            if len(agenda_link) == 1:
                messages.append("New meeting agenda available for Shenandoah County in " + meeting_titles[i] + ". Check for solar information. " + meeting_links[i])
        except:
            continue
    return messages

def shenandoah_county_bos(url):
    driver.get(url)
    time.sleep(2)
    messages = []
    #skip the forst entry since it's just the table column names
    table_rows = driver.find_elements(By.CSS_SELECTOR,"tr")[1:]
    meeting_titles = []
    meeting_links = []
    for item in table_rows:
        meeting_titles.append(item.text.replace("\n"," "))
        meeting_links.append(item.find_element(By.CSS_SELECTOR,"a").get_attribute("href"))
    for i in range(0,len(meeting_links)):
        driver.get(meeting_links[i])
        time.sleep(1)
        try:
            agenda_link = driver.find_elements(By.CSS_SELECTOR,"a[href*='Agenda-Packet.pdf'")
            if len(agenda_link) == 1:
                messages.append("New meeting agenda posted for Shenandoah County in " + meeting_titles[i] + ". Check for new solar information. " + meeting_links[i])
        except:
            continue
    return messages

"""Smyth County"""
def smyth_county_pc(url):
    driver.get(url)
    time.sleep(1)
    messages = []
    agenda_link = driver.find_element(By.CSS_SELECTOR,"a[href*='pc_agenda'")
    future_meeting = check_meeting_date(agenda_link.text)
    if future_meeting == False:
        meeting_title = agenda_link.text
        link = agenda_link.get_attribute("href")
        agenda_link.click()
        time.sleep(5)
        agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Smyth County Planning Commission in " + meeting_title + ". " + link)
    return messages

def smyth_county_bos(url):
    driver.get(url)
    time.sleep(1)
    messages = []
    agenda_link = driver.find_element(By.CSS_SELECTOR,"a[href*='agn_bos'")
    future_meeting = check_meeting_date(agenda_link.text)
    if future_meeting == False:
        meeting_title = agenda_link.text
        link = agenda_link.get_attribute("href")
        agenda_link.click()
        time.sleep(5)
        agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Smyth County Planning Commission in " + meeting_title + ". " + link)
    return messages

"""Southampton County"""
#keep this one updated with the new year as needed
def southampton_county(url,governing_body):
    driver.get(url)
    time.sleep(2)
    messages = []
    if governing_body == "Board of Supervisors":
        agenda_links = driver.find_elements(By.CSS_SELECTOR,"a[href*='regular_session.php'")
    elif governing_body == "Planning Commission":
        links = driver.find_elements(By.CSS_SELECTOR,"a[href*='2023.php'")
        agenda_links = []
        for item in links:
            if '2023' in item.text:
                agenda_links.append(item)
    latest_agenda = agenda_links[-1]
    future_meeting = check_meeting_date(latest_agenda.text)
    if future_meeting==True:
        meeting_title = governing_body + " " + latest_agenda.text
        meeting_url = latest_agenda.get_attribute("href")
        latest_agenda.click()
        time.sleep(2)
        agenda_content = driver.find_elements(By.CSS_SELECTOR,"section[class*='main-content-wrap'")
        agenda_search = search_agenda_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Southampton County in " + meeting_title + ". " + meeting_url)
    return messages

"""South Boston City Council"""
def south_boston(url):
    driver.get(url)
    time.sleep(2)
    messages = []
    table_rows = driver.find_elements(By.CSS_SELECTOR,'tr')
    for item in table_rows:
        future_date = check_meeting_date(item.text)
        if future_date == True:
            messages.append("New meeting information available for South Boston City Council in " + item.text +". Cannot read PDF. Check for solar.")
        else:
            break
    return messages

"""Staunton"""
def staunton(url):
    driver.get(url)
    time.sleep(2)
    messages = []
    table_rows = driver.find_elements(By.CSS_SELECTOR,'tr[class*="meeting_widget_item"')
    for item in table_rows:
        future_meeting = check_meeting_date(item.text)
        if future_meeting == True:
            try:
                agenda_link = item.find_element(By.CSS_SELECTOR,"a[class*='pdf_icon'")
                meeting_title = item.text.split("PM")[0]
                agenda_link.click()
                driver.switch_to.window(driver.window_handles[1])
                agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
                agenda_search = search_agenda_for_keywords(agenda_content)
                if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Staunton in " + meeting_title)
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
            except:
                continue
    return messages

"""Sussex County"""
#no agendas have been posted for any upcoming meetings, so not sure how far I'll be able to get with this
def sussex_county(url):
    driver.get(url)
    time.sleep(2)
    messages = []
    event_links = driver.find_elements(By.CSS_SELECTOR,"div[class*='event-post'")
    event_urls = []
    event_titles = []
    for item in event_links:
        event_urls.append(item.find_element(By.CSS_SELECTOR,"a").get_attribute("href"))
        event_titles.append(item.text.replace("\n"," ").split("until")[0])
    for i in range(0,len(event_urls)):
        driver.get(event_urls[i])
        time.sleep(2)
        try:
            agenda_link = driver.find_element(By.CSS_SELECTOR,"a[href*='.pdf'")
            agenda_link.click()
            time.sleep(1)
            driver.switch_to.window(driver.window_handles[1])
            agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
            agenda_search = search_agenda_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Sussex County in " + event_titles[i] + ". " + event_links[i])
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        except:
            continue
    return messages

"""Tazewell County"""
def tazewell_county(url, government_body):
    driver.get(url)
    time.sleep(2)
    messages = []
    all_rows = driver.find_elements(By.CSS_SELECTOR,"li")
    meeting_rows = []
    for item in all_rows:
        if "2023" in item.text:
            meeting_rows.append(item)
    for item in meeting_rows:
        future_meeting = check_meeting_date(item.text)
        if future_meeting == True:
            try:
                #agenda is listed first, so can just return the first search result
                meeting_title = government_body + " " + item.text
                agenda_link = item.find_element(By.CSS_SELECTOR,"a")
                agenda_url = agenda_link.get_attribute("href")
                agenda_link.click()
                time.sleep(2)
                driver.switch_to.window(driver.window_handles[1])
                agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
                agenda_search = search_agenda_for_keywords(agenda_content)
                if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Tazewell County in " + meeting_title + ". " + agenda_url)
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
            except:
                continue
            #if there's no agenda posted yet and the initial agenda link search fails, just move on to the next meeting
    return messages

"""Virginia Beach"""
def virginia_beach_cc(url):
    driver.get(url)
    time.sleep(3)
    messages = []
    current_agenda = driver.find_element(By.CSS_SELECTOR,"a[href*=CurrentBriefAgenda")
    agenda_url = current_agenda.get_attribute("href")
    driver.get(agenda_url)
    time.sleep(1)
    agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
    agenda_search = search_agenda_for_keywords(agenda_content)
    if agenda_search != []:
        messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Virginia Beach in latest City Council meeting agenda. " + agenda_url)
    return messages

def virginia_beach_pc(url):
    driver.get(url)
    time.sleep(3)
    messages = []
    agendas_part_1 = driver.find_elements(By.CSS_SELECTOR,"a[title*='agenda'")
    agendas_part_2 = driver.find_elements(By.CSS_SELECTOR,"a[title*='Agenda'")
    all_agendas = agendas_part_1
    for item in agendas_part_2:
        all_agendas.append(item)
    for item in all_agendas:
        future_meeting = check_meeting_date(item.get_attribute("title"))
        if future_meeting == True:
            agenda_url = item.get_attribute("href")
            driver.get(agenda_url)
            time.sleep(1)
            agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
            agenda_search = search_agenda_for_keywords(agenda_content)
            if agenda_search != []:
                messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Virginia Beach in latest Planning Commission meeting agenda. " + agenda_url)
    return messages

"City of Williamsburg"
def williamsburg(url,governing_body):
    driver.get(url)
    time.sleep(5)
    messages = []
    #latest year will be the top folder
    current_year = driver.find_element(By.CSS_SELECTOR,'a[class*="folder-link').get_attribute('href')
    driver.get(current_year)
    time.sleep(5)
    agendas = driver.find_elements(By.CSS_SELECTOR,'a[class*="document-link"')
    html_agendas = [item for item in agendas if 'Html' in item.text]
    future_meetings = []
    for item in html_agendas:
        try:
            if check_meeting_date(item.text)==True:
                future_meetings.append(item)
        except:
            continue
    for item in future_meetings:
        messages.append("New meeting information available for the City of Williamsburg " + governing_body + ". Check for solar updates. " + item.get_attribute('href'))
    return messages

"""Wythe County"""
def wythe_county(url):
    driver.get(url)
    time.sleep(2)
    messages = []
    agenda_links = driver.find_elements(By.CSS_SELECTOR,"a[href*=package")
    for item in agenda_links:
        if item.text != '':
            try:
                future_meeting = check_meeting_date(item.text)
                if future_meeting == True:
                    meeting_title = item.text
                    item.click()
                    driver.switch_to.window(driver.window_handles[1])
                    agenda_content = driver.find_elements(By.CSS_SELECTOR,"svg[class*=textLayer")
                    if agenda_content == []:
                        agenda_content = driver.find_elements(By.CSS_SELECTOR,"div[class*=textLayer")
                    agenda_search = search_agenda_for_keywords(agenda_content)
                    if agenda_search != []:
                        messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Wythe County in " + meeting_title)
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
            except:
                continue
    return messages