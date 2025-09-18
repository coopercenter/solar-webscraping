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