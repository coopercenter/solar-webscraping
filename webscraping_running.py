from webscraping_functions import *
from webscraping_dictionaries import *

locality_functions_single_use = {
    "Albemarle PC":albemarle_county_pc,
    "Alleghany BOS":alleghany_county,
    "Amelia PC":amelia_pc,
    "Bland":bland_county,
    "Brunswick":brunswick_county,
    "Buchanan":buchanan_county,
    "Buena Vista City Council":buena_vista_city_council,
    "Clifton Forge":clifton_forge,
    "Covington":covington,
    "Craig":craig_county,
    "Fairfax BOS":fairfax_county_bos,
    "Fairfax PC":fairfax_county_pc,
    "Franklin":city_of_franklin,
    "Galax":galax,
    "Giles":giles_county,
    "Henrico BOS":henrico_county_bos,
    "Henrico PC":henrico_county_pc,
    "Highland BOS":highland_county_bos,
    "Lee":lee_county,
    "Lexington":lexington_pc,
    "Loudoun":loudoun_pc,
    "Nelson":nelson_county,
    "Norton":norton_city,
    "Pittsylvania":pittsylvania_county,
    "Prince Edward PC":prince_edward_pc,
    "Prince Edward BOS":prince_edward_bos,
    "Richmond":richmond_county,
    "Sussex":sussex_county,
    "Virginia Beach CC":virginia_beach_cc,
    "Virginia Beach PC":virginia_beach_pc,
    "Wythe":wythe_county
}

locality_functions_multi_use = {
    "Bath BOS":bath_county,
    "Bath PC":bath_county,
    "Bath BZA":bath_county,
    "Greensville BOS":greensville_county,
    "Greensville PC":greensville_county,
    "King and Queen BOS":king_and_queen_county,
    "King and Queen PC":king_and_queen_county,
    "Manassas Park PC":manassas_park,
    "Manassas Park GB":manassas_park,
    "Nottoway BOS":nottoway_county,
    "Nottoway PC":nottoway_county,
    "Staunton PC":staunton,
    "Staunton CC":staunton,
    "Tazewell BOS":tazewell_county,
    "Tazewell PC":tazewell_county,
    "Wesmoreland BOS":westmoreland_county,
    "Westmoreland PC":westmoreland_county
}

def run_webscraping():
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
    
    for locality_dictionary in agendacenter2_dictionary:
        try:
            alert = agendacenter2(locality_dictionary)
            if alert != []:
                New_Alerts.append(", \n ".join(alert))
        except:
            error_alert = "Error webscraping " + agendacenter2_dictionary[locality_dictionary]['name'] + " using AgendaCenter Alternate code"
            New_Alerts.append(error_alert)
            continue
            
    for locality_dictionary in boarddocs_dictionary:
        try:
            alert = boarddocs(locality_dictionary)
            if alert != []:
                New_Alerts.append(", \n ".join(alert))
        except:
            error_alert = "Error webscraping " + boarddocs_dictionary[locality_dictionary]['name'] + " using BoardDocs code"
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
        
    for locality_dictionary in document_center_dictionary:
        try:
            alert=document_center(locality_dictionary)
            if alert != []:
                New_Alerts.append(", \n ".join(alert))
        except:
            error_alert="Error webscraping " + document_center_dictionary[locality_dictionary]['name'] + " using Document Center code"
            New_Alerts.append(error_alert)
            continue

    for locality_dictionary in escribe_dictionary:
        try:
            alert=escribe(locality_dictionary)
            if alert != []:
                New_Alerts.append(", \n ".join(alert))
        except:
            error_alert="Error webscraping " + escribe_dictionary[locality_dictionary]['name'] + " using EScribe code"
            New_Alerts.append(error_alert)
            continue

    for locality_dictionary in granicus_dictionary:
        try:
            alert = granicus(locality_dictionary)
            if alert != []:
                New_Alerts.append(", \n ".join(alert))
        except:
            error_alert = "Error webscraping " + granicus_dictionary[locality_dictionary]['name'] + " using Granicus code"
            New_Alerts.append(error_alert)
            continue
        
    for locality_dictionary in granicus_2_dictionary:
        try:
            alert = granicus_version_2(locality_dictionary)
            if alert != []:
                New_Alerts.append(", \n ".join(alert))
        except:
            error_alert = "Error webscraping " + granicus_2_dictionary[locality_dictionary]['name'] + " using Granicus Version 2 code"
            New_Alerts.append(error_alert)
            continue

    for locality_dictionary in laserfiche_dictionary:
        try:
            alert=laserfiche(locality_dictionary)
            if alert != []:
                New_Alerts.append(", \n ".join(alert))
        except:
            error_alert="Error webscraping " + laserfiche_dictionary[locality_dictionary]['name'] + " using LaserFiche code"
            New_Alerts.append(error_alert)
            continue

    for locality_dictionary in legistar_dictionary:
        try:
            alert=legistar(locality_dictionary)
            if alert != []:
                New_Alerts.append(", \n ".join(alert))
        except:
            error_alert="Error webscraping " + legistar_dictionary[locality_dictionary]['name'] + " using Legistar code"
            New_Alerts.append(error_alert)
            continue

    for locality_dictionary in links_by_year_dictionary:
        try:
            alert=links_by_year(locality_dictionary)
            if alert != []:
                New_Alerts.append(", \n ".join(alert))
        except:
            error_alert="Error webscraping " + links_by_year_dictionary[locality_dictionary]['name'] + " using Links by Year code"
            New_Alerts.append(error_alert)
            continue

    for locality_dictionary in meetingstable_dictionary:
        try:
            alert=meetings_table(locality_dictionary)
            if alert != []:
                New_Alerts.append(", \n ".join(alert))
        except:
            error_alert="Error webscraping " + meetingstable_dictionary[locality_dictionary]['name'] + " using MeetingsTable code"
            New_Alerts.append(error_alert)
            continue

    for locality_dictionary in novusagenda_dictionary:
        try:
            alert=novusagenda(locality_dictionary)
            if alert != []:
                New_Alerts.append(", \n ".join(alert))
        except:
            error_alert="Error webscraping " + novusagenda_dictionary[locality_dictionary]['name'] + " using NovusAGENDA code"
            New_Alerts.append(error_alert)
            continue

    for locality_dictionary in onbase_dictionary:
        try:
            alert=onbase(locality_dictionary)
            if alert != []:
                New_Alerts.append(", \n ".join(alert))
        except:
            error_alert="Error webscraping " + onbase_dictionary[locality_dictionary]['name'] + " using OnBase code"
            New_Alerts.append(error_alert)
            continue

    for locality_dictionary in primegov_dictionary:
        try:
            alert=prime_gov(locality_dictionary)
            if alert != []:
                New_Alerts.append(", \n ".join(alert))
        except:
            error_alert="Error webscraping " + primegov_dictionary[locality_dictionary]['name'] + " using PrimeGov code"
            New_Alerts.append(error_alert)
            continue

    for locality_dictionary in php_table_dictionary:
        try:
            alert=php_table(locality_dictionary)
            if alert != []:
                New_Alerts.append(", \n ".join(alert))
        except:
            error_alert="Error webscraping " + php_table_dictionary[locality_dictionary]['name'] + " using PHP Table code"
            New_Alerts.append(error_alert)
            continue

    for locality in locality_functions_single_use:
        try:
            alert=locality_functions_single_use[locality]()
            if alert != []:
                New_Alerts.append(", \n ".join(alert))
        except:
            error_alert = "Error webscraping " + locality_dictionary_single_use[locality]['name']
            New_Alerts.append(error_alert)
            continue

    for locality in locality_functions_multi_use:
        try:
            alert=locality_functions_multi_use[locality](locality)
            if alert != []:
                New_Alerts.append(", \n ".join(alert))
        except:
            error_alert = "Error webscraping " + locality_dictionary_multi_use[locality]["name"]
            New_Alerts.append(error_alert)
            continue

    

    #empty list 
    Solar_Alerts = []
    Siting_Alerts = []
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
        elif "Siting Agreement" in message:
            Siting_Alerts.append(message)
        else:
            Other_Alerts.append(message)

    # Convert categorized alerts to strings
    solar_alerts_str = ", \n".join(Solar_Alerts)
    siting_alerts_str = ", \n".join(Siting_Alerts)
    error_alerts_str = ", \n".join(Error_Alerts)
    unread_alerts_str = ", \n".join(Unreadable_File_Alerts)
    other_alerts_str = ", \n".join(Other_Alerts)

    alerts = ("Solar Alerts:\n" + solar_alerts_str + "\n\nSiting Agreement Alerts:\n" + siting_alerts_str + "\n\nUnreadable Alerts:\n" + unread_alerts_str + "\n\nError Alerts:\n" + error_alerts_str + "\n\nOther Alerts:\n" + other_alerts_str)

    return(alerts)


#email results
#email_new_alerts("Solar Alerts:\n" + solar_alerts_str + 
#                "\n\nUnreadable Alerts: \n" + unread_alerts_str +
#                "\n\nOrdinance Alerts:\n" + ordinance_alerts_str +
#                 "\n\nComprehensive Plan Alerts:\n" + comprehensive_plan_alerts_str +
#                 "\n\nError Alerts:\n" + error_alerts_str)