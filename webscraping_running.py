from webscraping_dictionaries import *
from webscraping_functions import *
New_Alerts = []

#run the boarddocs localities
for item in boarddocs_dictionary:
    try:
        alert = boarddocs(boarddocs_dictionary[item][0],boarddocs_dictionary[item][1],boarddocs_dictionary[item][2])
        New_Alerts.append(alert)
    except:
        error_alert = "Error webscraping " + item + " using BoardDocs code."
        New_Alerts.append(error_alert)
        continue

#run the agendacenter localities
for item in agendacenter_dictionary:
    try:
        alert = agendacenter(agendacenter_dictionary[item][0],agendacenter_dictionary[item][1])
        New_Alerts.append(alert)
    except:
        error_alert = "Error webscraping " + item + " using AgendaCenter code."
        New_Alerts.append(error_alert)
        continue   
#run the granicus localities
for item in granicus_dictionary:
    try:
        alert = granicus_b(granicus_dictionary[item][0],granicus_dictionary[item][1])
        New_Alerts.append(alert)
    except:
        error_alert = "Error webscraping " + item + " using Granicus code"
        New_Alerts.append(error_alert)
        continue
for item in granicus_2_dictionary:
    try:
        alert = granicus_version_2(granicus_2_dictionary[item][0],granicus_2_dictionary[item][1])
        New_Alerts.append(alert)
    except:
        error_alert = "Error webscraping " + item + " using Granicus Version 2 code"
        New_Alerts.append(error_alert)
print(New_Alerts)
