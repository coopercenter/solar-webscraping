# # type: docx or pdf
# def read_download(agenda_link, type):
#     query_parameters = {"downloadformat": type}
#     headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
#     agenda_file = requests.get(agenda_link, allow_redirects=True,params=query_parameters,headers=headers)
#     if agenda_file.status_code == 200:
#         temp_agenda = tempfile.TemporaryFile()
#         temp_agenda.write(agenda_file.content)
#         if type == 'docx':
#             agenda_content = docx2txt.process(temp_agenda)

#         elif type == 'pdf':
#             agenda_pdf = PdfReader(temp_agenda)
#             agenda_pages = agenda_pdf.pages
#             agenda_content = "\n".join([item.extract_text() for item in agenda_pages])
#             temp_agenda.close()
#     return agenda_content

# """AgendaCenter"""
# # repetitive
# def agendacenter(locality_dictionary):
#     from webscraping_dictionaries import agendacenter_dictionary, meetings_tags
#     driver.get(agendacenter_dictionary[locality_dictionary]['url'])
#     messages = []
#     time.sleep(5)
#     table_rows = driver.find_elements(By.CSS_SELECTOR, meetings_tags['agendacenter'])
#     future_meetings = [item for item in table_rows if check_meeting_date(search_dates(item.text,languages=['en'])[0][0])==True]
#     agenda_links = [item.find_elements(By.CSS_SELECTOR,"a")[1].get_attribute("href") for item in future_meetings]
#     if agendacenter_dictionary[locality_dictionary]['agenda_type']=='pdf':
#         for link in agenda_links:
#             driver.get(link)
#             time.sleep(60)
#             agenda_content = get_pdf_content(agendacenter_dictionary[locality_dictionary]['agenda_content'])
#             readable = check_agenda_readability(agenda_content)
#             if readable == True:
#                 agenda_search = search_text_for_keywords(agenda_content)
#                 if agenda_search != []:
#                     messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + agendacenter_dictionary[locality_dictionary]['name'] + ". " + link)
#             elif readable == False:
#                 messages.append("New meeting document available for "+ agendacenter_dictionary[locality_dictionary]['name'] + ". " + "Document cannot be scanned for keywords. " + link)
#     if agendacenter_dictionary[locality_dictionary]['agenda_type']=='webpage':
#         for link in agenda_links:
#             driver.get(link)
#             time.sleep(20)
#             agenda_content = get_webpage_content(agendacenter_dictionary[locality_dictionary]["agenda_content"])
#             agenda_search = search_text_for_keywords(agenda_content)
#             if agenda_search != []:
#                     messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + agendacenter_dictionary[locality_dictionary]['name'] + ". " + link)
#     return messages

# # repetitive
# def agendacenter2(locality_dictionary):
#     from webscraping_dictionaries import agendacenter2_dictionary, meetings_tags
#     driver.get(agendacenter2_dictionary[locality_dictionary]['url'])
#     messages =[]
#     time.sleep(5)
#     table_rows = driver.find_elements(By.CSS_SELECTOR, meetings_tags['agendacenter'])
#     future_meetings = [item for item in table_rows if check_meeting_date(search_dates(item.text,languages=['en'])[0][0])==True]
#     meetings_links = [item.find_elements(By.CSS_SELECTOR,"a")[1].get_attribute("href") for item in future_meetings]
#     #if agendacenter_dictionary[locality_dictionary]['agenda_type']=='pdf':
#     for link in meetings_links:
#         driver.get(link)
#         time.sleep(5)
#         documents = driver.find_elements(By.CSS_SELECTOR,'a')
#         agendas = [pdf_link.get_attribute('href') for pdf_link in documents if 'AGENDA' in pdf_link.text]
#         for agenda_link in agendas:
#             driver.get(agenda_link)
#             agenda_content = get_pdf_content(agendacenter2_dictionary[locality_dictionary]['agenda_content'])
#             readable = check_agenda_readability(agenda_content)
#             if readable == True:
#                 agenda_search = search_text_for_keywords(agenda_content)
#                 if agenda_search != []:
#                     messages.append("Keyword(s) " + ", ".join(agenda_search) + " found in upcoming meeting for " + agendacenter2_dictionary[locality_dictionary]['name'] + ". " + link)
#             elif readable ==False:
#                 messages.append("New meeting document available for "+ agendacenter2_dictionary[locality_dictionary]['name'] + ". " + "Document cannot be scanned for keywords. " + link)
#     #if agendacenter_dictionary[locality_dictionary]['agenda_type']=='webpage':
#         #messages = search_webpage(agenda_links, agendacenter2_dictionary, locality_dictionary)
#     return messages

########################################################################################################

def run_webscraping():
    New_Alerts = {
        "locality_name": None,
        "meeting_date": None,
        "keyword": None,
        "url": None
    }

    # Do for each dictionary in webscraping_dictionaries
    for locality_dictionary in agendacenter_dictionary:
        # info_list = extractor_helper(locality_dictionary);
        # info_list = [locality_name, meeting_date, keyword, url]

        for index in range(len(info_list)):
            if index == 0:
                New_Alerts["locality_name"].append(info_list[index])
            elif index == 1:
                New_Alerts["meeting_date"].append(info_list[index])
            elif index == 2:
                New_Alerts["keyword"].append(info_list[index])
            elif index == 3:
                New_Alerts["url"].append(info_list[index])

        # try:
        #     alert = agendacenter(locality_dictionary)
        #     if alert != []:
        #         for message in alert:
        #             New_Alerts.append(message)
        # except:
        #     error_alert = "Error webscraping " + agendacenter_dictionary[locality_dictionary]['name'] + " using AgendaCenter code"
        #     New_Alerts.append(error_alert)
        #     continue

    # agendacenter2_dictionary
    # boarddocs_dictionary
    # civicclerk_dictionary
    # civicweb_dictionary
    # document_center_dictionary
    # escribe_dictionary
    # folding_year_dictionary
    # granicus_dictionary
    # granicus_2_dictionary
    # laserfiche_dictionary
    # legistar_dictionary
    # links_by_year_dictionary
    # meetingstable_dictionary
    # novusagenda_dictionary
    # onbase_dictionary
    # primegov_dictionary
    # php_table_dictionary
    # locality_functions_single_use
    # locality_functions_multi_use

    # Return dictionary
    return New_Alerts

def extractor_helper(locality_dictionary):
    # HANDLE ERRORS SOMEHOW
    from webscraping_dictionaries import agendacenter_dictionary, meetings_tags

    all_info = []
    driver.get(agendacenter_dictionary[locality_dictionary]['url'])
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
    
    return all_info # [locality_name, meeting_date, keyword, url]

# Helper to transform that dictionary into a tabular format for pandas
# def alerts_to_dataframe(alerts_dict):
#     data = []
#     for category, messages in alerts_dict.items():
#         for msg in messages:
#             data.append({"Category": category, "Message": msg})

#     df = pd.DataFrame(data)
#     return df