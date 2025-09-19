# type: docx or pdf
def read_download(agenda_link, type):
    query_parameters = {"downloadformat": type}
    headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    agenda_file = requests.get(agenda_link, allow_redirects=True,params=query_parameters,headers=headers)
    if agenda_file.status_code == 200:
        temp_agenda = tempfile.TemporaryFile()
        temp_agenda.write(agenda_file.content)
        if type == 'docx':
            agenda_content = docx2txt.process(temp_agenda)

        elif type == 'pdf':
            agenda_pdf = PdfReader(temp_agenda)
            agenda_pages = agenda_pdf.pages
            agenda_content = "\n".join([item.extract_text() for item in agenda_pages])
            temp_agenda.close()
    return agenda_content

"""AgendaCenter"""
# repetitive
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
            time.sleep(60)
            agenda_content = get_pdf_content(agendacenter_dictionary[locality_dictionary]['agenda_content'])
            readable = check_agenda_readability(agenda_content)
            if readable == True:
                agenda_search = search_text_for_keywords(agenda_content)
                if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + agendacenter_dictionary[locality_dictionary]['name'] + ". " + link)
            elif readable == False:
                messages.append("New meeting document available for "+ agendacenter_dictionary[locality_dictionary]['name'] + ". " + "Document cannot be scanned for keywords. " + link)
    if agendacenter_dictionary[locality_dictionary]['agenda_type']=='webpage':
        for link in agenda_links:
            driver.get(link)
            time.sleep(20)
            agenda_content = get_webpage_content(agendacenter_dictionary[locality_dictionary]["agenda_content"])
            agenda_search = search_text_for_keywords(agenda_content)
            if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + agendacenter_dictionary[locality_dictionary]['name'] + ". " + link)
    return messages

# repetitive
def agendacenter2(locality_dictionary):
    from webscraping_dictionaries import agendacenter2_dictionary, meetings_tags
    driver.get(agendacenter2_dictionary[locality_dictionary]['url'])
    messages =[]
    time.sleep(5)
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
            agenda_content = get_pdf_content(agendacenter2_dictionary[locality_dictionary]['agenda_content'])
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
            agenda_content = get_pdf_content(locality_dictionary_single_use['Albemarle PC']['content_tag'])
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
    agenda_content = get_pdf_content(locality_dictionary_single_use['Buchanan']['content_tag'])
    readable = check_agenda_readability(agenda_content)
    if readable == True:
        agenda_search = search_text_for_keywords(agenda_content)
        if agenda_search != []:
            messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Buchanan County Board of Supervisors. " + minutes_url)
    elif readable == False:
        messages.append('New meeting document available for Buchanan County. Document cannot be scanned for keywords' + minutes_url)
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
                agenda_content = get_pdf_content(locality_dictionary_single_use['Fairfax PC']['content_tag'])
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
            agenda_content = get_pdf_content(locality_dictionary_single_use['Fairfax PC']['content_tag'])
            readable = check_agenda_readability(agenda_content)
            if readable == True:
                agenda_search = search_text_for_keywords(agenda_content)
                if agenda_search != []:
                    messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for Fairfax County Planning Commission. " + item)
            elif readable == False:
                messages.append("New agenda available for upcoming meeting for Fairfax County Planning Commission. Document cannot be scanned for keywords. " + item)
    return messages

def scrape_platform(locality, link_extractor, content_extractor):
    if not verify_url(locality["url"]):
        return [f"{locality['locality']} - URL not working"]

    driver = get_webdriver()
    driver.get(locality["url"])

    messages = []
    for agenda_link, date in link_extractor(driver):
        if not check_meeting_date(date):
            continue

        agenda_content = content_extractor(agenda_link)
        if check_agenda_readability(agenda_content):
            keywords = search_text_for_keywords(agenda_content)
            if keywords:
                messages.append(f"{locality['locality']} - Agenda {agenda_link} contains {keywords}")
        else:
            messages.append(f"{locality['locality']} - Agenda {agenda_link} could not be scanned")

    driver.quit()
    return messages

########################################################################################################

# Focuses on collecting and categorizing alerts
def run_webscraping():
    New_Alerts = []

    for locality_dictionary in agendacenter_dictionary:
        try:
            alert = agendacenter(locality_dictionary)
            if alert != []:
                for message in alert:
                    New_Alerts.append(message)
        except:
            error_alert = "Error webscraping " + agendacenter_dictionary[locality_dictionary]['name'] + " using AgendaCenter code"
            New_Alerts.append(error_alert)
            continue

    for locality_dictionary in agendacenter2_dictionary:
        try:
            alert = agendacenter2(locality_dictionary)
            if alert != []:
                for message in alert:
                    New_Alerts.append(message)
        except:
            error_alert = "Error webscraping " + agendacenter2_dictionary[locality_dictionary]['name'] + " using AgendaCenter Alternate code"
            New_Alerts.append(error_alert)
            continue
            
    for locality_dictionary in boarddocs_dictionary:
        try:
            alert = boarddocs(locality_dictionary)
            if alert != []:
                for message in alert:
                    New_Alerts.append(message)
        except:
            error_alert = "Error webscraping " + boarddocs_dictionary[locality_dictionary]['name'] + " using BoardDocs code"
            New_Alerts.append(error_alert)
            continue

    for locality_dictionary in civicclerk_dictionary:
        try:
            alert=civicclerk(locality_dictionary)
            if alert != []:
                for message in alert:
                    New_Alerts.append(message)
        except:
            error_alert="Error webscraping " + civicclerk_dictionary[locality_dictionary]['name'] + " using CivicClerk code"
            New_Alerts.append(error_alert)
            continue
        
    for locality_dictionary in civicweb_dictionary:
        try:
            alert=civicweb(locality_dictionary)
            if alert != []:
                for message in alert:
                    New_Alerts.append(message)
        except:
            error_alert="Error webscraping " + civicweb_dictionary[locality_dictionary]['name'] + " using CivicWeb code"
            New_Alerts.append(error_alert)
            continue
        
    for locality_dictionary in document_center_dictionary:
        try:
            alert=document_center(locality_dictionary)
            if alert != []:
                for message in alert:
                    New_Alerts.append(message)
        except:
            error_alert="Error webscraping " + document_center_dictionary[locality_dictionary]['name'] + " using Document Center code"
            New_Alerts.append(error_alert)
            continue

    for locality_dictionary in escribe_dictionary:
        try:
            alert=escribe(locality_dictionary)
            if alert != []:
                for message in alert:
                    New_Alerts.append(message)
        except:
            error_alert="Error webscraping " + escribe_dictionary[locality_dictionary]['name'] + " using EScribe code"
            New_Alerts.append(error_alert)
            continue
    
    for locality_dictionary in folding_year_dictionary:
        try:
            alert=folding_year(locality_dictionary)
            if alert != []:
                for message in alert:
                    New_Alerts.append(message)
        except:
            error_alert="Error webscraping " + folding_year_dictionary[locality_dictionary]['name'] + " using Folding Year code"
            New_Alerts.append(error_alert)
            continue

    for locality_dictionary in granicus_dictionary:
        try:
            alert = granicus(locality_dictionary)
            if alert != []:
                for message in alert:
                    New_Alerts.append(message)
        except:
            error_alert = "Error webscraping " + granicus_dictionary[locality_dictionary]['name'] + " using Granicus code"
            New_Alerts.append(error_alert)
            continue
        
    for locality_dictionary in granicus_2_dictionary:
        try:
            alert = granicus_version_2(locality_dictionary)
            if alert != []:
                for message in alert:
                    New_Alerts.append(message)
        except:
            error_alert = "Error webscraping " + granicus_2_dictionary[locality_dictionary]['name'] + " using Granicus Version 2 code"
            New_Alerts.append(error_alert)
            continue

    for locality_dictionary in laserfiche_dictionary:
        try:
            alert=laserfiche(locality_dictionary)
            if alert != []:
                for message in alert:
                    New_Alerts.append(message)
        except:
            error_alert="Error webscraping " + laserfiche_dictionary[locality_dictionary]['name'] + " using LaserFiche code"
            New_Alerts.append(error_alert)
            continue

    for locality_dictionary in legistar_dictionary:
        try:
            alert=legistar(locality_dictionary)
            if alert != []:
                for message in alert:
                    New_Alerts.append(message)
        except:
            error_alert="Error webscraping " + legistar_dictionary[locality_dictionary]['name'] + " using Legistar code"
            New_Alerts.append(error_alert)
            continue

    for locality_dictionary in links_by_year_dictionary:
        try:
            alert=links_by_year(locality_dictionary)
            if alert != []:
                for message in alert:
                    New_Alerts.append(message)
        except:
            error_alert="Error webscraping " + links_by_year_dictionary[locality_dictionary]['name'] + " using Links by Year code"
            New_Alerts.append(error_alert)
            continue

    for locality_dictionary in meetingstable_dictionary:
        try:
            alert=meetings_table(locality_dictionary)
            if alert != []:
                for message in alert:
                    New_Alerts.append(message)
        except:
            error_alert="Error webscraping " + meetingstable_dictionary[locality_dictionary]['name'] + " using MeetingsTable code"
            New_Alerts.append(error_alert)
            continue

    for locality_dictionary in novusagenda_dictionary:
        try:
            alert=novusagenda(locality_dictionary)
            if alert != []:
                for message in alert:
                    New_Alerts.append(message)
        except:
            error_alert="Error webscraping " + novusagenda_dictionary[locality_dictionary]['name'] + " using NovusAGENDA code"
            New_Alerts.append(error_alert)
            continue

    for locality_dictionary in onbase_dictionary:
        try:
            alert=onbase(locality_dictionary)
            if alert != []:
                for message in alert:
                    New_Alerts.append(message)
        except:
            error_alert="Error webscraping " + onbase_dictionary[locality_dictionary]['name'] + " using OnBase code"
            New_Alerts.append(error_alert)
            continue

    for locality_dictionary in primegov_dictionary:
        try:
            alert=prime_gov(locality_dictionary)
            if alert != []:
                for message in alert:
                    New_Alerts.append(message)
        except:
            error_alert="Error webscraping " + primegov_dictionary[locality_dictionary]['name'] + " using PrimeGov code"
            New_Alerts.append(error_alert)
            continue

    for locality_dictionary in php_table_dictionary:
        try:
            alert=php_table(locality_dictionary)
            if alert != []:
                for message in alert:
                    New_Alerts.append(message)
        except:
            error_alert="Error webscraping " + php_table_dictionary[locality_dictionary]['name'] + " using PHP Table code"
            New_Alerts.append(error_alert)
            continue

    for locality in locality_functions_single_use:
        try:
            alert=locality_functions_single_use[locality]()
            if alert != []:
                for message in alert:
                    New_Alerts.append(message)
        except:
            error_alert = "Error webscraping " + locality_dictionary_single_use[locality]['name']
            New_Alerts.append(error_alert)
            continue

    for locality in locality_functions_multi_use:
        try:
            alert=locality_functions_multi_use[locality](locality)
            if alert != []:
                for message in alert:
                    New_Alerts.append(message)
        except:
            error_alert = "Error webscraping " + locality_dictionary_multi_use[locality]["name"]
            New_Alerts.append(error_alert)
            continue

    # Empty lists
    categorized_alerts = {
        "Solar": [],
        "Battery": [],
        "Siting": [],
        "Unreadable": [],
        "Error": [],
        "Other": []
    }

    # Sort into categories
    # If the word in the meeting agenda is in the list of keyword, append to empty list
    for message in New_Alerts:
        if "Solar" in message:
            categorized_alerts["Solar"].append(message)
        elif "Battery" in message:
            categorized_alerts["Battery"].append(message)
        elif "Error" in message or "Not Reachable" in message:
            categorized_alerts["Error"].append(message)
        elif "scanned" in message:
            categorized_alerts["Unreadable"].append(message)
        elif "Siting Agreement" in message:
            categorized_alerts["Siting"].append(message)
        else:
            categorized_alerts["Other"].append(message)

    # Return dictionary
    return categorized_alerts

# Helper to transform that dictionary into a tabular format for pandas
def alerts_to_dataframe(alerts_dict):
    data = []
    for category, messages in alerts_dict.items():
        for msg in messages:
            data.append({"Category": category, "Message": msg})

    df = pd.DataFrame(data)
    return df