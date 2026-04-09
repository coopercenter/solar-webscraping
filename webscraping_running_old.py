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