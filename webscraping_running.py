from webscraping_dictionaries import *
from webscraping_functions import *
New_Alerts = []

"Run all the webscraping functions, single thread version"
while True:
    if is_internet_active(30) is True:
        for item in agendacenter_dictionary:
            try:
                alert = agendacenter(agendacenter_dictionary[item][0],agendacenter_dictionary[item][1])
                if alert != []:
                    New_Alerts.append(", \n ".join(alert))
            except:
                error_alert = "Error webscraping " + item + " using AgendaCenter code."
                New_Alerts.append(error_alert)
                continue
            
        for item in boarddocs_dictionary:
            try:
                alert = boarddocs(boarddocs_dictionary[item][0],boarddocs_dictionary[item][1],boarddocs_dictionary[item][2])
                if alert != []:
                    New_Alerts.append(", \n ".join(alert))
            except:
                error_alert = "Error webscraping " + item + " using BoardDocs code."
                New_Alerts.append("\n" + error_alert)
                continue

        for item in civicclerk_dictionary:
            try:
                alert=civicclerk(civicclerk_dictionary[item][0],civicclerk_dictionary[item][1])
                if alert != []:
                    New_Alerts.append(", \n ".join(alert))
            except:
                error_alert="Error webscraping " + item + " using CivicClerk code"
                New_Alerts.append(error_alert)
                continue
        
        for item in civicweb_dictionary:
            try:
                alert=civicweb(civicweb_dictionary[item][0],civicweb_dictionary[item][1])
                if alert != []:
                    New_Alerts.append(", \n ".join(alert))
            except:
                error_alert="Error webscraping " + item + " using CivicWeb code"
                New_Alerts.append(error_alert)
                continue
        
        for item in document_center_dictionary:
            try:
                alert=document_center(document_center_dictionary[item][0],document_center_dictionary[item][1])
                if alert != []:
                    New_Alerts.append(", \n ".join(alert))
            except:
                error_alert="Error webscraping " + item + " using Document Center code"
                New_Alerts.append(error_alert)
                continue

        for item in escribe_dictionary:
            try:
                alert=escribe(escribe_dictionary[item][0],escribe_dictionary[item][1])
                if alert != []:
                    New_Alerts.append(", \n ".join(alert))
            except:
                error_alert="Error webscraping " + item + " using EScribe code"
                New_Alerts.append(error_alert)
                continue
        
        for item in event_list_dictionary:
            try:
                alert=event_list(event_list_dictionary[item][0],escribe_dictionary[item][1])
                if alert != []:
                    New_Alerts.append(", \n ".join(alert))
            except:
                error_alert="Error webscraping " + item + " using Event List code"
                New_Alerts.append(error_alert)
                continue

        for item in granicus_dictionary:
            try:
                alert = granicus(granicus_dictionary[item][0],granicus_dictionary[item][1])
                if alert != []:
                    New_Alerts.append(", \n ".join(alert))
            except:
                error_alert = "Error webscraping " + item + " using Granicus code"
                New_Alerts.append(error_alert)
                continue
        
        for item in granicus_2_dictionary:
            try:
                alert = granicus_version_2(granicus_2_dictionary[item][0],granicus_2_dictionary[item][1])
                if alert != []:
                    New_Alerts.append(", \n ".join(alert))
            except:
                error_alert = "Error webscraping " + item + " using Granicus Version 2 code"
                New_Alerts.append(error_alert)
                continue

        for item in laserfiche_dictionary:
            try:
                alert=laserfiche(laserfiche_dictionary[item][0],laserfiche_dictionary[item][1])
                if alert != []:
                    New_Alerts.append(", \n ".join(alert))
            except:
                error_alert="Error webscraping " + item + " using LaserFiche code"
                New_Alerts.append(error_alert)
                continue

        for item in legistar_dictionary:
            try:
                alert=legistar(legistar_dictionary[item][0],legistar_dictionary[item][1])
                if alert != []:
                    New_Alerts.append(", \n ".join(alert))
            except:
                error_alert="Error webscraping " + item + " using Legistar code"
                New_Alerts.append(error_alert)
                continue

        for item in meetingstable_dictionary:
            try:
                alert=meetings_table(meetingstable_dictionary[item][0],meetingstable_dictionary[item][1])
                if alert != []:
                    New_Alerts.append(", \n ".join(alert))
            except:
                error_alert="Error webscraping " + item + " using MeetingsTable code"
                New_Alerts.append(error_alert)
                continue

        for item in novusagenda_dictionary:
            try:
                alert=novusagenda(novusagenda_dictionary[item][0],novusagenda_dictionary[item][1])
                if alert != []:
                    New_Alerts.append(", \n ".join(alert))
            except:
                error_alert="Error webscraping " + item + " using NovusAGENDA code"
                New_Alerts.append(error_alert)
                continue

        for item in primegov_dictionary:
            try:
                alert=prime_gov(primegov_dictionary[item][0],primegov_dictionary[item][1])
                if alert != []:
                    New_Alerts.append(", \n ".join(alert))
            except:
                error_alert="Error webscraping " + item + " using PrimeGov code"
                New_Alerts.append(error_alert)
                continue

        for item in php_table_dictionary:
            try:
                alert=php_table(php_table_dictionary[item][0],php_table_dictionary[item][1])
                if alert != []:
                    New_Alerts.append(", \n ".join(alert))
            except:
                error_alert="Error webscraping " + item + " using PHP Table code"
                New_Alerts.append(error_alert)
                continue

        for item in county_dictionary_single_variable:
            try:
                alert=county_dictionary_single_variable[item][0](county_dictionary_single_variable[item][1])
                if alert != []:
                    New_Alerts.append(", \n ".join(alert))
            except:
                error_alert = "Error webscraping " + item
                New_Alerts.append(error_alert)
                continue

        for item in county_dictionary_double_variable:
            try:
                alert=county_dictionary_double_variable[item][0](county_dictionary_double_variable[item][1],county_dictionary_double_variable[item][2])
                if alert != []:
                    New_Alerts.append(", \n ".join(alert))
            except:
                error_alert = "Error webscraping " + item
                New_Alerts.append(error_alert)
                continue

        for item in city_dictionary_single_variable:
            try:
                alert=city_dictionary_single_variable[item][0](city_dictionary_single_variable[item][1])
                if alert != []:
                    New_Alerts.append(", \n ".join(alert))
            except:
                error_alert = "Error webscraping " + item
                New_Alerts.append(error_alert)
                continue

        for item in city_dictionary_double_variable:
            try:
                alert=city_dictionary_double_variable[item][0](city_dictionary_double_variable[item][1],city_dictionary_double_variable[item][2])
                if alert != []:
                    New_Alerts.append(", \n ".join(alert))
            except:
                error_alert = "Error webscraping " + item
                New_Alerts.append(error_alert)
                continue   
        break
    else:
        pass 

#empty list 
Solar_Alerts = []
Ordinance_Alerts = []
Comprehensive_Plan_Alerts = []
Error_Alerts = []
Unreadable_File_Alerts = []

#categorizing keywords
Solar_Keyword = ['Solar', 'solar']
Ordinance_Keyword = ['Zoning Ordinance', 'Zoning ordinance', 'zoning ordinance']
Comprehensive_Plan_Keyword = ['Comprehensive Plan', 'Comprehensive plan', 'comprehensive plan']
Error_Keyword = ['Error', 'Not Reachable']
Unread_Keyword = ["New", "cannot"]

#loop that checks if the word in the meeting agenda is in the list of keywords...if that happens, append to empty list
for messages in New_Alerts:
    if any(keyword in messages for keyword in Ordinance_Keyword):
        Ordinance_Alerts.append(messages)
    if any(keyword in messages for keyword in Comprehensive_Plan_Keyword):
        Comprehensive_Plan_Alerts.append(messages)
    if any(keyword in messages for keyword in Error_Keyword):
        Error_Alerts.append(messages)
    elif any(keyword in messages for keyword in Unread_Keyword):
        Unreadable_File_Alerts.append(messages)
    elif any(keyword in messages for keyword in Solar_Keyword):
        Solar_Alerts.append(messages)

# Convert categorized alerts to strings
solar_alerts_str = ", \n".join(Solar_Alerts)
ordinance_alerts_str = ", \n".join(Ordinance_Alerts)
comprehensive_plan_alerts_str = ", \n".join(Comprehensive_Plan_Alerts)
error_alerts_str = ", \n".join(Error_Alerts)
unread_alerts_str = ", \n".join(Unreadable_File_Alerts)

#email results
email_new_alerts("Solar Alerts:\n" + solar_alerts_str + 
                 "\n\nUnreadable Alerts: \n" + unread_alerts_str +
                 "\n\nOrdinance Alerts:\n" + ordinance_alerts_str +
                 "\n\nComprehensive Plan Alerts:\n" + comprehensive_plan_alerts_str +
                 "\n\nError Alerts:\n" + error_alerts_str)