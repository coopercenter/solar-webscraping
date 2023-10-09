from webscraping_dictionaries import *
from webscraping_functions import *
New_Alerts = []

"""Run the repeated document management sites"""
#run the boarddocs localities
for item in boarddocs_dictionary:
    try:
        alert = boarddocs(boarddocs_dictionary[item][0],boarddocs_dictionary[item][1],boarddocs_dictionary[item][2])
        if alert != []:
            New_Alerts.append(", \n ".join(alert))
    except:
        error_alert = "Error webscraping " + item + " using BoardDocs code."
        New_Alerts.append("\n" + error_alert)
        continue

#run the agendacenter localities
for item in agendacenter_dictionary:
    try:
        alert = agendacenter(agendacenter_dictionary[item][0],agendacenter_dictionary[item][1])
        if alert != []:
            New_Alerts.append(", \n ".join(alert))
    except:
        error_alert = "Error webscraping " + item + " using AgendaCenter code."
        New_Alerts.append(error_alert)
        continue   
#run the granicus localities
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
#run the civicclerk localities
for item in civicclerk_dictionary:
    try:
        alert=civicclerk(civicclerk_dictionary[item][0],civicclerk_dictionary[item][1])
        if alert != []:
            New_Alerts.append(", \n ".join(alert))
    except:
        error_alert="Error webscraping " + item + " using CivicClerk code"
        New_Alerts.append(error_alert)
        continue

#run the novus agenda localities
for item in novusagenda_dictionary:
    try:
        alert=novusagenda(novusagenda_dictionary[item][0],novusagenda_dictionary[item][1])
        if alert != []:
            New_Alerts.append(", \n ".join(alert))
    except:
        error_alert="Error webscraping " + item + " using NovusAGENDA code"
        New_Alerts.append(error_alert)
        continue

#run civicweb localities
for item in civicweb_dictionary:
    try:
        alert=civicweb(civicweb_dictionary[item][0],civicweb_dictionary[item][1])
        if alert != []:
            New_Alerts.append(", \n ".join(alert))
    except:
        error_alert="Error webscraping " + item + " using CivicWeb code"
        New_Alerts.append(error_alert)
        continue

#run meetingstable localities
for item in meetingstable_dictionary:
    try:
        alert=meetings_table(meetingstable_dictionary[item][0],meetingstable_dictionary[item][1])
        if alert != []:
            New_Alerts.append(", \n ".join(alert))
    except:
        error_alert="Error webscraping " + item + " using MeetingsTable code"
        New_Alerts.append(error_alert)
        continue

#run document center localities
for item in document_center_dictionary:
    try:
        alert=document_center(document_center_dictionary[item][0],document_center_dictionary[item][1])
        if alert != []:
            New_Alerts.append(", \n ".join(alert))
    except:
        error_alert="Error webscraping " + item + " using Document Center code"
        New_Alerts.append(error_alert)
        continue

#run escribe localities
for item in escribe_dictionary:
    try:
        alert=escribe(escribe_dictionary[item][0],escribe_dictionary[item][1])
        if alert != []:
            New_Alerts.append(", \n ".join(alert))
    except:
        error_alert="Error webscraping " + item + " using EScribe code"
        New_Alerts.append(error_alert)
        continue

#run legistar localities
for item in legistar_dictionary:
    try:
        alert=legistar(legistar_dictionary[item][0],legistar_dictionary[item][1])
        if alert != []:
            New_Alerts.append(", \n ".join(alert))
    except:
        error_alert="Error webscraping " + item + " using Legistar code"
        New_Alerts.append(error_alert)
        continue

"""Run the website-specific code"""
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
New_Alerts_String = ", \n".join(New_Alerts)
email_new_alerts(New_Alerts_String)