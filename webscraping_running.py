from webscraping_dictionaries import *
from webscraping_functions import *
New_Alerts = []

"""Run the repeated document management sites"""
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

#run the boarddocs localities
for item in boarddocs_dictionary:
    try:
        alert = boarddocs(boarddocs_dictionary[item][0],boarddocs_dictionary[item][1],boarddocs_dictionary[item][2])
        if alert != []:
            New_Alerts.append(", \n ".join(alert))
    except:
        error_alert = "Error webscraping " + item + " using BoardDocs code"
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

#run the event list localities
for item in event_list_dictionary:
    try:
        alert=event_list(event_list_dictionary[item][0],escribe_dictionary[item][1])
        if alert != []:
            New_Alerts.append(", \n ".join(alert))
    except:
        error_alert="Error webscraping " + item + " using Event List code"
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

#run LaserFiche localities
for item in laserfiche_dictionary:
    try:
        alert=laserfiche(laserfiche_dictionary[item][0],laserfiche_dictionary[item][1])
        if alert != []:
            New_Alerts.append(", \n ".join(alert))
    except:
        error_alert="Error webscraping " + item + " using LaserFiche code"
        New_Alerts.append(error_alert)
        continue

#run Legistar localities
for item in legistar_dictionary:
    try:
        alert=legistar(legistar_dictionary[item][0],legistar_dictionary[item][1])
        if alert != []:
            New_Alerts.append(", \n ".join(alert))
    except:
        error_alert="Error webscraping " + item + " using Legistar code"
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

#run PrimeGov localities
for item in primegov_dictionary:
    try:
        alert=prime_gov(primegov_dictionary[item][0],primegov_dictionary[item][1])
        if alert != []:
            New_Alerts.append(", \n ".join(alert))
    except:
        error_alert="Error webscraping " + item + " using PrimeGov code"
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


meeting_agenda = ['Keyword(s) Zoning Ordinance found in upcoming meeting for Rockingham County in This is the agenda packet for the January 2, 2024 Planning Commission regular meeting. Jan 2, 2024 . https://www.rockinghamcountyva.gov/AgendaCenter/ViewFile/Agenda/_01022024-775',
 'Keyword(s) Zoning Ordinance, Comprehensive Plan found in upcoming meeting for City of Petersburg in January 2, 2024 - Petersburg City Council Work Session Agenda Jan 2, 2024 . http://www.petersburg-va.org/AgendaCenter/ViewFile/Agenda/_01022024-825',
 'Keyword(s) Comprehensive Plan, Comprehensive Plan found in upcoming meeting for City of Portsmouth in Planning Commission January 2024 Meeting Agenda Jan 2, 2024 . https://www.portsmouthva.gov/AgendaCenter/ViewFile/Agenda/_01022024-1065',
 '\nError webscraping Accomack using BoardDocs code.',
 '\nError webscraping Culpeper using BoardDocs code.',
 '\nError webscraping Essex using BoardDocs code.',
 '\nError webscraping Montgomery using BoardDocs code.',
 '\nError webscraping Northampton using BoardDocs code.',
 '\nError webscraping Northumberland using BoardDocs code.',
 '\nError webscraping Prince George using BoardDocs code.',
 '\nError webscraping Pulaski using BoardDocs code.',
 '\nError webscraping Rappahannock using BoardDocs code.',
 'Error webscraping Amherst using CivicClerk code',
 'Error webscraping Stafford using CivicClerk code',
 'Error webscraping Warren using CivicClerk code',
 'Error webscraping Amherst using CivicClerk code',
 'Error webscraping Warren using CivicClerk code',
 'Error webscraping Dickenson using Document Center code',
 'Error webscraping Nelson County using Event List code',
 'Error webscraping Westmoreland County using Event List code',
 'Error webscraping City of Richmond using Legistar code',
 'Error webscraping Isle of Wight BOS using NovusAGENDA code',
 'Error webscraping Salem CC using NovusAGENDA code',
 'Error webscraping Salem PC using NovusAGENDA code',
 'https://www.albemarle.org/government/community-development/boards-and-commissions/planning-commission: is Not reachable, status_code: 503',
 'Error webscraping Bland County',
 'Error webscraping Buchanan County',
 'New meeting information available for Charlotte County in 01/01/24 Organizational Meeting Agenda       Packet      , check documents for solar information',
 'New meeting agenda available for Craig County Board of Supervisors. Check for solar. https://craigcountyva.gov/wp-content/uploads/2023/12/January-4th-2024-Agenda-and-Packet.pdf',
 'Keyword(s) Comprehensive Plan, Zoning Ordinance, Comprehensive Plan found in upcoming meeting for Henrico County in the latest Planning Commission/Board of Zoning Appeals agenda. https://henrico.us/pdfs/planning/meetnext.pdf',
 'Error webscraping King and Queen County Board of Supervisors',
 'Error webscraping King and Queen County Planning Commission',
 'Error webscraping Lee County',
 'Error webscraping Loudoun County',
 'Keyword(s) Solar found in upcoming meeting for Lunenburg County in 01/04/24 January 4, 2024 Planning Commission Mtg . https://www.lunenburgva.gov/PC%20agenda%201.4.24.pdf',
 'New agenda available for Buena Vista City Council. PDF cannot be read, check for solar updates. https://cityofbuenavista-my.sharepoint.com/:b:/g/personal/sarah_burch_bvcity_org/EevfRFf9uOVEldzkatCiS7sBpllj1jNxGvuvqKlP2WOIZA?e=ZAufcm',
 'Error webscraping Covington',
 'Error webscraping Emporia Planning Commission',
 'Error webscraping Virginia Beach City Council',
 'Error webscraping Virginia Beach Planning Commission']


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