from webscraping_dictionaries import *
from webscraping_functions import *
New_Alerts = []

#run the boarddocs localities
for item in boarddocs_dictionary:
    try:
        alert = boarddocs(boarddocs_dictionary[item][0],boarddocs_dictionary[item][1],boarddocs_dictionary[item][2])
        New_Alerts.append(alert)
    except:
        error_alert = "Error webscraping " + item + "using BoardDocs code."
        New_Alerts.append(error_alert)
        continue

"run the agendacenter localities"
for item in agendacenter_dictionary:
    try:
        alert = agendacenter_alternate(agendacenter_dictionary[item][0],agendacenter_dictionary[item][1])
        New_Alerts.append(alert)
    except:
        error_alert = "Error webscraping " + item + "using AgendaCenter code."
        New_Alerts.append(error_alert)
        continue   
print(New_Alerts)
