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
    "OnBase":{"function":onbase,
              "dictionary":onbase_dictionary},
    "PHP Table":{"function":php_table,
                 "dictionary":php_table_dictionary},
    "PrimeGov":{"function":prime_gov,
                "dictionary":primegov_dictionary},
    "The Lists":{"function":the_lists,
                 "dictionary":the_lists_dictionary},
    "The Split Lists":{"function":the_split_lists,
                       "dictionary":the_split_lists_dictionary}
    
}

locality_functions_single_use = {
    "Albemarle PC":albemarle_county_pc,
    "Buchanan":buchanan_county,
    "Fairfax BOS":fairfax_county_bos,
    "Fairfax PC":fairfax_county_pc,
    "Giles":giles_county,
    "Highland BOS":highland_county_bos,
    "Loudoun":loudoun_pc,
    "Virginia Beach CC":virginia_beach_cc
}

locality_functions_multi_use = {
    "Bath BOS":bath_county,
    "Bath PC":bath_county,
    "Bath BZA":bath_county,
}

def run_webscraping():
    #NewAlerts = pd.DataFrame([],columns=["locality","meeting_date","keyword","url"]) for getting the results as a table from the beginning
    New_Alerts = []

    for function_dictionary in repeated_system_functions:
        for locality_dictionary in repeated_system_functions[function_dictionary]["dictionary"]:
            try:
                alert = repeated_system_functions[function_dictionary]["function"](locality_dictionary)
                if alert != []:
                    for message in alert:
                        New_Alerts.append(message)
            except:
                error_alert = "Error webscraping " + repeated_system_functions[function_dictionary]["dictionary"][locality_dictionary]["name"] + " using " + function_dictionary + " code."
                New_Alerts.append(error_alert)

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
    Bad_Tag_Alerts = []
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
        if "Tags" in message:
            Bad_Tag_Alerts.append(message)
        else:
            Other_Alerts.append(message)

    # Convert categorized alerts to strings
    solar_alerts_str = ", \n".join(Solar_Alerts)
    battery_alerts_str = ", \n".join(Battery_Alerts)
    siting_alerts_str = ", \n".join(Siting_Alerts)
    error_alerts_str = ", \n".join(Error_Alerts)
    unread_alerts_str = ", \n".join(Unreadable_File_Alerts)
    bad_tag_alerts_str = ", \n".join(Bad_Tag_Alerts)
    other_alerts_str = ", \n".join(Other_Alerts)

    alerts = ("Solar Alerts:\n" + solar_alerts_str + "\n\nBattery Storage Alerts:\n" + battery_alerts_str + "\n\nSiting Agreement Alerts:\n" + siting_alerts_str + "\n\nUnreadable Alerts:\n" + unread_alerts_str + "\n\nError Alerts:\n" + error_alerts_str + "\n\nBad Tag Alerts:\n" + bad_tag_alerts_str + "\n\nOther Alerts:\n" + other_alerts_str)

    return(alerts)


#email results
#email_new_alerts("Solar Alerts:\n" + solar_alerts_str + 
#                "\n\nUnreadable Alerts: \n" + unread_alerts_str +
#                "\n\nOrdinance Alerts:\n" + ordinance_alerts_str +
#                 "\n\nComprehensive Plan Alerts:\n" + comprehensive_plan_alerts_str +
#                 "\n\nError Alerts:\n" + error_alerts_str)