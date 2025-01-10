from webscraping_dictionaries import *
from webscraping_functions import *
New_Alerts = []

"Run all the webscraping functions, single thread version"
for locality_dictionary in agendacenter_dictionary:
    try:
        alert = agendacenter(locality_dictionary)
        if alert != []:
            New_Alerts.append(", \n ".join(alert))
    except:
        error_alert = "Error webscraping " + agendacenter_dictionary[locality_dictionary]['name'] + " using AgendaCenter code."
        New_Alerts.append(error_alert)
        continue
            
for locality_dictionary in boarddocs_dictionary:
    try:
        alert = boarddocs(locality_dictionary)
        if alert != []:
            New_Alerts.append(", \n ".join(alert))
    except:
        error_alert = "Error webscraping " + boarddocs_dictionary[locality_dictionary]['name'] + " using BoardDocs code."
        New_Alerts.append("\n" + error_alert)
        continue

for locality_dictionary in civicclerk_dictionary:
    try:
        alert=civicclerk(locality_dictionary)
        if alert != []:
            New_Alerts.append(", \n ".join(alert))
    except:
        error_alert="Error webscraping " + civicclerk_dictionary[locality_dictionary]['name'] + " using CivicClerk code"
        New_Alerts.append(error_alert)
        continue
        
for locality_dictionary in civicweb_dictionary:
    try:
        alert=civicweb(locality_dictionary)
        if alert != []:
            New_Alerts.append(", \n ".join(alert))
    except:
        error_alert="Error webscraping " + civicweb_dictionary[locality_dictionary]['name'] + " using CivicWeb code"
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

for item in onbase_dictionary:
    try:
        alert=onbase(onbase_dictionary[item][0],onbase_dictionary[item][1])
        if alert != []:
            New_Alerts.append(", \n ".join(alert))
    except:
        error_alert="Error webscraping " + item + " using OnBase code"
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

#empty list 
Solar_Alerts = []
Error_Alerts = []
Unreadable_File_Alerts = []
Other_Alerts = []

#loop that checks if the word in the meeting agenda is in the list of keywords...if that happens, append to empty list
for message in New_Alerts:
    if "Solar" in message:
        Solar_Alerts.append(message)
    elif "Error" in message or "Not Reachable" in message:
        Error_Alerts.append(message)
    elif "scanned" in message:
        Unreadable_File_Alerts.append(message)
    else:
        Other_Alerts.append(message)

# Convert categorized alerts to strings
solar_alerts_str = ", \n".join(Solar_Alerts)
error_alerts_str = ", \n".join(Error_Alerts)
unread_alerts_str = ", \n".join(Unreadable_File_Alerts)
other_alerts_str = ", \n".join(Other_Alerts)

alerts = ("Solar Alerts:\n" + solar_alerts_str + "\n\nUnreadable Alerts: \n" + unread_alerts_str + "\n\nError Alerts:\n" + error_alerts_str + "\n\nOther Alerts:\n" + other_alerts_str)


#email results
#email_new_alerts("Solar Alerts:\n" + solar_alerts_str + 
#                "\n\nUnreadable Alerts: \n" + unread_alerts_str +
#                "\n\nOrdinance Alerts:\n" + ordinance_alerts_str +
#                 "\n\nComprehensive Plan Alerts:\n" + comprehensive_plan_alerts_str +
#                 "\n\nError Alerts:\n" + error_alerts_str)