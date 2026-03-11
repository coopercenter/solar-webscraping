from webscraping_functions import *
from webscraping_dictionaries import *

repeated_system_functions = {
    "AgendaCenter":{"function":agendacenter,
                    "dictionary":agendacenter_dictionary},
    "AgendaCenter Alternate":{"function":agendacenter2,
                              "dictionary":agendacenter2_dictionary},
    "BoardDocs":{"function":boarddocs,
                 "dictionary":boarddocs_dictionary},
    "Calendar View":{"function":calendar_view,
                     "dictionary":calendar_view_dictionary},
    "CivicClerk":{"function":civicclerk,
                  "dictionary":civicclerk_dictionary},
    "CivicWeb":{"function":civicweb,
                "dictionary":civicweb_dictionary},
    "Document Center":{"function":document_center,
                       "dictionary":document_center_dictionary},
    "EScribe":{"function":escribe,
               "dictionary":escribe_dictionary},
    "Folding Year":{"function":folding_year,
                    "dictionary":folding_year_dictionary},
    "Folding Year Alternate":{"function":folding_year_v2,
                              "dictionary":folding_year_v2_dictionary},
    "Granicus":{"function":granicus,
                "dictionary":granicus_dictionary},
    "Granicus Alternate":{"functiion":granicus_version_2,
                          "dictionary":granicus_2_dictionary},
    "LaserFiche":{"function":laserfiche,
                  "dictionary":laserfiche_dictionary},
    "Legistar":{"function":legistar,
                "dictionary":legistar_dictionary},
    "Links by Year":{"function":links_by_year,
                     "dictionary":links_by_year_dictionary},
    "MeetingsTable":{"function":meetings_table,
                     "dictionary":meetingstable_dictionary},
    
    

}

locality_functions_single_use = {
    "Albemarle PC":albemarle_county_pc,
    "Buchanan":buchanan_county,
    "Fairfax BOS":fairfax_county_bos,
    "Fairfax PC":fairfax_county_pc,
    "Giles":giles_county,
    "Highland BOS":highland_county_bos,
    "Loudoun":loudoun_pc,
    "Virginia Beach CC":virginia_beach_cc,
    "Wythe":wythe_county
}

locality_functions_multi_use = {
    "Bath BOS":bath_county,
    "Bath PC":bath_county,
    "Bath BZA":bath_county,
}

def run_webscraping():
    NewAlerts = pd.DataFrame([],columns=["locality","meeting_date","keyword","url"])
    New_Alerts = []

    "Run all the webscraping functions, single thread version"
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
            error_alert = "Error webscraping " + agendacenter2_dictionary[locality_dictionary]['name'] + " using AgendaCenter Alternate code" + ". " + agendacenter2_dictionary[locality_dictionary]["url"]
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

    for locality_dictionary in calendar_view_dictionary:
        try:
            alert = calendar_view(locality_dictionary)
            if alert != []:
                for message in alert:
                    New_Alerts.append(message)
        except:
            error_alert = "Error webscraping " + calendar_view_dictionary[locality_dictionary]['name'] + " using Calendar View code"
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

    for locality_dictionary in folding_year_v2_dictionary:
        try:
            alert=folding_year_v2(locality_dictionary)
            if alert != []:
                for message in alert:
                    New_Alerts.append(message)
        except:
            error_alert="Error webscraping " + folding_year_v2_dictionary[locality_dictionary]['name'] + " using Folding Year V2 code"
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
    for locality_dictionary in the_lists_dictionary:
        try:
            alert=the_lists(locality_dictionary)
            if alert != []:
                for message in alert:
                    New_Alerts.append(message)
        except:
            error_alert="Error webscraping " + the_lists_dictionary[locality_dictionary]['name'] + " using The Lists code"
            New_Alerts.append(error_alert)
            continue
    for locality_dictionary in the_split_lists_dictionary:
        try:
            alert=the_split_lists(locality_dictionary)
            if alert != []:
                for message in alert:
                    New_Alerts.append(message)
        except:
            error_alert="Error webscraping " + the_split_lists_dictionary[locality_dictionary]['name'] + " using The Split Lists code"
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

    

    #empty list 
    Solar_Alerts = []
    Siting_Alerts = []
    Battery_Alerts = []
    Error_Alerts = []
    Unreadable_File_Alerts = []
    Other_Alerts = []

    #loop that checks if the word in the meeting agenda is in the list of keywords...if that happens, append to empty list
    for message in New_Alerts:
        if "Solar" in message:
            Solar_Alerts.append(message)
        if "Battery" in message:
            Battery_Alerts.append(message)
        if "Error" in message or "Not Reachable" in message:
            Error_Alerts.append(message)
        if "scanned" in message:
            Unreadable_File_Alerts.append(message)
        if "Siting Agreement" in message:
            Siting_Alerts.append(message)
        else:
            Other_Alerts.append(message)

    # Convert categorized alerts to strings
    solar_alerts_str = ", \n".join(Solar_Alerts)
    battery_alerts_str = ", \n".join(Battery_Alerts)
    siting_alerts_str = ", \n".join(Siting_Alerts)
    error_alerts_str = ", \n".join(Error_Alerts)
    unread_alerts_str = ", \n".join(Unreadable_File_Alerts)
    other_alerts_str = ", \n".join(Other_Alerts)

    alerts = ("Solar Alerts:\n" + solar_alerts_str + "\n\nBattery Storage Alerts:\n" + battery_alerts_str + "\n\nSiting Agreement Alerts:\n" + siting_alerts_str + "\n\nUnreadable Alerts:\n" + unread_alerts_str + "\n\nError Alerts:\n" + error_alerts_str + "\n\nOther Alerts:\n" + other_alerts_str)

    return(alerts)


#email results
#email_new_alerts("Solar Alerts:\n" + solar_alerts_str + 
#                "\n\nUnreadable Alerts: \n" + unread_alerts_str +
#                "\n\nOrdinance Alerts:\n" + ordinance_alerts_str +
#                 "\n\nComprehensive Plan Alerts:\n" + comprehensive_plan_alerts_str +
#                 "\n\nError Alerts:\n" + error_alerts_str)