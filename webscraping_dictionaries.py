from webscraping_functions import *
"Dictionaries for the localities that use the same type of document organization service"

"""BoardDocs localities"""
boarddocs_dictionary = {
    'Accomack':["https://go.boarddocs.com/va/coa/Board.nsf/Public","Accomack County",False],

    "Culpeper":["https://go.boarddocs.com/va/ccva/Board.nsf/Public","Culpeper County",False],

    "Essex":["https://go.boarddocs.com/va/essexco/Board.nsf/Public","Essex County",False],

    "Montgomery":["https://go.boarddocs.com/va/montva/Board.nsf/Public","Montgomery County",False],

    "Northampton":["https://go.boarddocs.com/va/northco/Board.nsf/Public","Northampton County",True],

    "Northumberland":["https://go.boarddocs.com/va/nuc/Board.nsf/vpublic?open","Northumberland County",False],

    "Pulaski":["https://go.boarddocs.com/va/copva/Board.nsf/Public#","Pulaski County",True],

    "Rappahannock":["https://go.boarddocs.com/va/corva/Board.nsf/Public","Rappahannock County",True],

    "Rockbridge":["https://go.boarddocs.com/va/rcva/Board.nsf/Public","Rockbridge County",False],
}

"AgendaCenter localities"
agendacenter_dictionary = {
    "Botetourt":["https://www.botetourtva.gov/AgendaCenter/Search/?term=&CIDs=3,6,&startDate=&endDate=&dateRange=&dateSelector=","Botetourt County"],

    "Campbell":["https://www.co.campbell.va.us/AgendaCenter/Search/?term=&CIDs=5,6,&startDate=&endDate=&dateRange=&dateSelector=","Campbell County"],

    "Caroline":["https://co.caroline.va.us/AgendaCenter/Search/?term=&CIDs=2,3,&startDate=&endDate=&dateRange=&dateSelector=","Caroline County"],

    "Cumberland":["https://www.cumberlandcounty.virginia.gov/AgendaCenter/Search/?term=&CIDs=2,3,&startDate=&endDate=&dateRange=&dateSelector=", "Cumberland County"],

    "Dinwiddie":["https://www.dinwiddieva.us/AgendaCenter/Search/?term=&CIDs=2,1,&startDate=&endDate=&dateRange=&dateSelector=","Dinwiddie County"],

    "Franklin":["https://www.franklincountyva.gov/AgendaCenter/Search/?term=&CIDs=7,4,&startDate=&endDate=&dateRange=&dateSelector=", "Franklin County"],

    "Halifax":["https://www.halifaxcountyva.gov/AgendaCenter/Search/?term=&CIDs=2,4,&startDate=&endDate=&dateRange=&dateSelector=", "Halifax County"],

    "Henry":["https://www.henrycountyva.gov/AgendaCenter","Henry County"],

    "King George":["https://www.kinggeorgecountyva.gov/AgendaCenter/Search/?term=&CIDs=2,5,&startDate=&endDate=&dateRange=&dateSelector=","King George County"],

    "Mecklenburg":["https://www.mecklenburgva.com/AgendaCenter/Search/?term=&CIDs=7,2,8,&startDate=&endDate=&dateRange=&dateSelector=","Mecklenburg County"],

    "Middlesex":["https://www.co.middlesex.va.us/AgendaCenter/Search/?term=&CIDs=4,2,&startDate=&endDate=&dateRange=&dateSelector=","Middlesex County"],

    "Page":["https://www.pagecounty.virginia.gov/AgendaCenter/Search/?term=&CIDs=2,5,&startDate=&endDate=&dateRange=&dateSelector=","Page County"],
    
    "Powhatan":["http://www.powhatanva.gov/AgendaCenter/Search/?term=&CIDs=2,7,&startDate=&endDate=&dateRange=&dateSelector=","Powhatan County"],

    "Rockbridge":["https://va-rockbridgecounty.civicplus.com/AgendaCenter/Planning-Commission-6","Rockbridge County"],

    "Rockingham":["https://www.rockinghamcountyva.gov/AgendaCenter/Search/?term=&CIDs=1,2,&startDate=&endDate=&dateRange=&dateSelector=","Rockingham County"],

    "Russell":["https://va-russellcounty.civicplus.com/AgendaCenter/Search/?term=&CIDs=5,3,&startDate=&endDate=&dateRange=&dateSelector=","Russell County"],

    "Scott":["https://www.scottcountyva.com/agendacenter","Scott County"],

    "Wise":["https://www.wisecounty.org/AgendaCenter/Search/?term=&CIDs=3,6,&startDate=&endDate=&dateRange=&dateSelector=","Wise County"],

    "York":["https://www.yorkcounty.gov/AgendaCenter/Search/?term=&CIDs=4,3,&startDate=&endDate=&dateRange=&dateSelector=","York County"],

    "Bedford":["https://www.bedfordva.gov/AgendaCenter/Search/?term=&CIDs=3,2,&startDate=&endDate=&dateRange=&dateSelector=","Town of Bedford"],

    "Colonial Heights":["https://www.colonialheightsva.gov/AgendaCenter/Search/?term=&CIDs=1,4,&startDate=&endDate=&dateRange=&dateSelector=","City of Colonial Heights"],

    "Fredricksburg":["https://www.fredericksburgva.gov/AgendaCenter/Search/?term=&CIDs=1,9,&startDate=&endDate=&dateRange=&dateSelector=","City of Fredericksburg"],

    "Hampton":["https://hampton.gov/AgendaCenter/Search/?term=&CIDs=6,&startDate=&endDate=&dateRange=&dateSelector=","Hampton City"],

    "Hopewell":["https://hopewellva.gov/AgendaCenter","City of Hopewell"],

    "Martinsville":["https://www.martinsville-va.gov/AgendaCenter/Search/?term=&CIDs=2,6,&startDate=&endDate=&dateRange=&dateSelector=","City of Martinsville"],

    "Norfolk":["https://www.norfolk.gov/AgendaCenter/Search/?term=&CIDs=25,13,14,&startDate=&endDate=&dateRange=&dateSelector=","City of Norfolk"],

    "Petersburg":["http://www.petersburg-va.org/AgendaCenter/Search/?term=&CIDs=1,3,&startDate=&endDate=&dateRange=&dateSelector=","City of Petersburg"],

    "Poquoson":["https://www.ci.poquoson.va.us/AgendaCenter/Search/?term=&CIDs=2,3,&startDate=&endDate=&dateRange=&dateSelector=","City of Poquoson"],

    "Portsmouth":["https://www.portsmouthva.gov/AgendaCenter/Search/?term=&CIDs=7,4,&startDate=&endDate=&dateRange=&dateSelector=","City of Portsmouth"],

    "Radford":["https://www.radfordva.gov/AgendaCenter/Search/?term=&CIDs=2,4,&startDate=&endDate=&dateRange=&dateSelector=","City of Radford"],

    "Suffolk":["https://www.suffolkva.us/AgendaCenter/Search/?term=&CIDs=11,4,12,3,&startDate=&endDate=&dateRange=&dateSelector=","City of Suffolk"],

    "Waynesboro":["https://www.waynesboro.va.us/AgendaCenter/Search/?term=&CIDs=1,4,&startDate=&endDate=&dateRange=&dateSelector=","City of Waynesboro"]
    }

"CivicClerk localities"
civicclerk_dictionary = {
"Amelia":["https://ameliacova.portal.civicclerk.com/?category_id=26,28","Amelia County"],

"Amherst":["https://amherstcova.portal.civicclerk.com/?category_id=27,29,33,32","Amherst County"],

"Charles City":["https://charlescitycova.portal.civicclerk.com/?category_id=26,27,29","Charles City County"],

"Chesterfield":["https://chesterfieldcova.portal.civicclerk.com/","Chesterfield County"],

"Hanover":["https://hanovercova.portal.civicclerk.com/?category_id=26,27","Hanover County"],

"King William":["https://kingwilliamcova.portal.civicclerk.com/","King William County"],

"Mathews":["https://mathewscova.portal.civicclerk.com/","Mathews County"],

"Orange":["https://orangecova.portal.civicclerk.com/","Orange County"],

"Spotsylvania":["https://spotsylvaniacova.portal.civicclerk.com/","Spotsylvania County"],

"Stafford":["https://staffordcova.portal.civicclerk.com/?category_id=26,31","Stafford County"],

"Surry":["https://surrycova.portal.civicclerk.com/","Surry County"],

"Warren":["https://warrencountyva.portal.civicclerk.com/?category_id=26,27","Warren County"],

"Charlottesville":["https://charlottesvilleva.portal.civicclerk.com/","City of Charlottesville"],

"Danville":["https://danvilleva.portal.civicclerk.com/","City of Danville"],

"Lynchburg":["https://lynchburgva.portal.civicclerk.com/","City of Lynchburg"],

"Roanoke":["https://roanokeva.portal.civicclerk.com/","City of Roanoke"]
}

"""NovusAGENDA localities"""
novusagenda_dictionary = {
"Isle of Wight PC":["https://isleofwight.novusagenda.com/agendapublic/meetingsgeneral.aspx?MeetingType=2","Isle of Wight County"],

"Isle of Wight BOS":["https://isleofwight.novusagenda.com/agendapublic/meetingsgeneral.aspx?MeetingType=1","Isle of Wight County"],

"James City":["https://jamescity.novusagenda.com/AgendaPublic/MeetingsGeneral.aspx","James City County"],

"New Kent BOS":["https://newkent.novusagenda.com/agendapublic/meetingsgeneral.aspx","New Kent County"]
}

"Granicus localities"
granicus_dictionary = {
"Augusta":["https://augustava.granicus.com/ViewPublisher.php?view_id=1","Augusta County"],

"Fauquier":["https://fauquier-va.granicus.com/ViewPublisher.php?view_id=3","Fauquier County"],

"Frederick":["https://fcva.granicus.com/ViewPublisher.php?view_id=1","Frederick County"],

"Greene":["https://gcva.granicus.com/ViewPublisher.php?view_id=1","Greene County"],

"Prince William BOS":["https://pwcgov.granicus.com/ViewPublisher.php?view_id=23","Prince William County"],

"Alexandria":["https://alexandria.granicus.com/ViewPublisher.php?view_id=57","City of Alexandria"],

"Bristol":["https://bristolva.granicus.com/ViewPublisher.php?view_id=1","City of Bristol"],

"Chesapeake CC":["https://chesapeake.granicus.com/ViewPublisher.php?view_id=29","City of Chesapeake"],

"Chesapeake PC":["https://chesapeake.granicus.com/ViewPublisher.php?view_id=35","City of Chesapeake"],

"Fairfax":["https://fairfax.granicus.com/ViewPublisher.php?view_id=11","City of Fairfax"],

"Falls Church":["https://fallschurch-va.granicus.com/ViewPublisher.php?view_id=2","City of Falls Church"],

"Manassas":["https://manassascity.granicus.com/ViewPublisher.php?view_id=1","Manassas City"]
}

"""Granicus version 2 localities"""
granicus_2_dictionary = {
"Goochland":["https://goochlandcountyva.iqm2.com/Citizens/Default.aspx","Goochland County"],

"Washington":["https://washingtoncountyva.iqm2.com/citizens/default.aspx?frame=no","Washington County"]
}

"""CivicWeb localities"""
civicweb_dictionary = {
"Lancaster PC":["https://lancova.civicweb.net/Portal/MeetingInformation.aspx?Id=133","Lancaster County"],

"Lancaster BOS":["https://lancova.civicweb.net/Portal/MeetingInformation.aspx?Id=135","Lancaster County"],

"Lexington CC":["https://lexingtonva.civicweb.net/Portal/MeetingInformation.aspx?Id=224","City of Lexington"],

"Newport News CC":["https://nngov.civicweb.net/Portal/MeetingInformation.aspx?Id=942","City of Newport News"],

"Newport News PC":["https://nngov.civicweb.net/Portal/MeetingInformation.aspx?Id=962","City of Newport News"],

"Winchester CC":["https://winchesterva.civicweb.net/Portal/MeetingInformation.aspx?Id=3826","City of Winchester"],

"Winchester PC":["https://winchesterva.civicweb.net/Portal/MeetingInformation.aspx?Id=4285","City of Winchester"]
}

"""MeetingsTable localities"""
meetingstable_dictionary = {
"Essex PC":["https://www.essex-virginia.org/meetings?date_filter%5Bvalue%5D%5Bmonth%5D=1&date_filter%5Bvalue%5D%5Bday%5D=1&date_filter%5Bvalue%5D%5Byear%5D=2023&date_filter_1%5Bvalue%5D%5Bmonth%5D=12&date_filter_1%5Bvalue%5D%5Bday%5D=31&date_filter_1%5Bvalue%5D%5Byear%5D=2023&field_microsite_tid=All&field_microsite_tid_1=28","Essex County"],

"Fluvanna PC":["https://www.fluvannacounty.org/meetings?field_microsite_tid_1=28","Fluvanna County"],

"Fluvanna BOS":["https://www.fluvannacounty.org/meetings?field_microsite_tid_1=27","Fluvanna County"],

"Madison":["https://www.madisonco.virginia.gov/meetings","Madison County"],

"Northumberland PC":["https://www.co.northumberland.va.us/meetings?field_microsite_tid_1=28","Northumberland County"]
}

"""Document Center localities"""
document_center_dictionary = {
    "Dickenson":["https://www.dickensonva.org/DocumentCenter/Index/38","Dickenson County"]
}

"EScribe localities"
escribe_dictionary = {
    "Gloucester":["https://pub-gloucesterva.escribemeetings.com/?FillWidth=1","Gloucester County"]
}

"Legistar localities"
legistar_dictionary = {
    "Albemarle":["https://albemarle.legistar.com/Calendar.aspx","Albemarle County"],
    "Hampton CC":["https://hampton.legistar.com/Calendar.aspx","Hampton City"]
}

"Dictionaries for localities that need individual code"
county_dictionary_single_variable = {
    "Albemarle County Planning Commission":[albemarle_county_pc,"https://www.albemarle.org/government/community-development/boards-and-commissions/planning-commission"],

    "Alleghany County":[alleghany_county,"https://www.co.alleghany.va.us/board-of-supervisors/agendas/"],

    "Arlington County":[arlington_county,"https://arlington.granicus.com/ViewPublisher.php?view_id=44","https://arlington.granicus.com/ViewPublisher.php?view_id=2"],

    "Bath County":[bath_county,"https://www.bathcountyva.gov/public_information/agendas_and_public_notices"],

    "Bland County":[bland_county,"https://www.blandcountyva.gov/page/agendas-and-minutes/"],

    "Buchanan County":[buchanan_county,"https://www.buchanancountyonline.com/index.htm"],

    "Buckingham County Board of Supervisors":[buckingham_county,"https://www.buckinghamcountyva.org/administration/boards___commissions/board_of_supervisors/board_agenda_minutes_youtube.php"],

    "Buckingham County Planning Commission":[buckingham_county,"https://www.buckinghamcountyva.org/administration/boards___commissions/planning_commission.php"],

    "Carroll County":[carroll_county,"https://www.carrollcountyva.gov/government/bos_meeting_agendas.php"],

    "Charlotte County Board of Supervisors":[charlotte_county,"https://www.charlottecountyva.gov/government/board_of_supervisors/agendas___minutes.php"],

    "Charlotte County Planning Commission":[charlotte_county,"https://www.charlottecountyva.gov/departments/planning___zoning/agendas___minutes.php"],

    "Clarke County Board of Supervisors":[clarke_county,"https://www.clarkecounty.gov/government/boards-commissions/board-of-supervisors/bos-agendas/-folder-1324"],

    "Clarke County Planning Commission":[clarke_county,"https://www.clarkecounty.gov/government/boards-commissions/planning-commission/pc-agendas/-folder-1352"],

    "Fairfax County Board of Supervisors":[fairfax_county_bos,"https://www.fairfaxcounty.gov/boardofsupervisors/"],

    "Floyd County":[floyd_county,"https://www.floydcova.gov/agendas-minutes"],

    "Giles County":[giles_county,"https://virginiasmtnplayground.com/bos/"],

    "Henrico County Board of Supervisors":[henrico_county_bos,"https://henrico.us/supervisors/supervisors-agenda-o-gram/"],

    "Henrico County Planning Commission":[henrico_county_pc,"https://henrico.us/planning/meetings/"],

    "King and Queen County Board of Supervisors":[king_and_queen_county_bos,"http://www.kingandqueenco.net/html/Govt/board.html"],

    "King and Queen County Planning Commission":[king_and_queen_county_pc,"http://www.kingandqueenco.net/html/Govt/bzoning.html"],

    "Lee County":[lee_county,"http://www.leecova.org/AgendaandMinutes.htm"],

    "Lunenberg County Board of Supervisors":[lunenburg_county,"https://www.lunenburgva.gov/government/board_of_supervisors/agendas___minutes.php"],

    "Lunenburg County Planning Commission":[lunenburg_county,"https://www.lunenburgva.gov/government/planning_commission/agendas___minutes.php"],

    "Montgomery County Planning Commission":[montgomery_pc,"https://www.montva.com/departments/Planning-GIS/planning--commission/meetings-1"],

    "Nelson County":[nelson_county,"https://www.nelsoncounty-va.gov/events/list/"],

    "New Kent County Planning Commission":[new_kent_county_pc,"https://www.co.new-kent.va.us/Archive.aspx?AMID=422"],

    #monitor for PC updates and change code accordingly
    "Nottoway County":[nottoway_county,"https://nottoway.org/administration/boards___commissions/board_of_supervisors_(bos)/board_agendas_minutes.php#outer-388"],

    "Patrick County Board of Supervisors":[patrick_county_bos,"https://www.co.patrick.va.us/supervisors/meeting-agendas"],

    "Pittsylvania County":[pittsylvania_county,"https://www.pittsylvaniacountyva.gov/government/agenda-center"],

    "Prince George County Planning Commission":[prince_george_county_pc,"https://www.princegeorgecountyva.gov/residents/community_development_and_code_compliance/planning_commission/meetings.php#outer-2780"],

    "Prince George County Board of Supervisors":[prince_george_county_bos,"https://www.princegeorgecountyva.gov/departments/board_of_supervisors/meetings_agendas_and_board_packets.php"],

    "Prince William County Planning Commission":[prince_william_pc,"https://www.pwcva.gov/department/planning-office/planning-commission"],

    "Richmond County":[richmond_county,"https://co.richmond.va.us/board-of-supervisors-agenda-packets"],

    "Roanoke County Planning Commission":[roanoke_county_pc,"https://www.roanokecountyva.gov/278/Planning-Commission"],

    "Roanoke County Board of Supervisors":[roanoke_county_bos,"https://www.roanokecountyva.gov/287/Agendas-Minutes"],

    "Shenandoah County Board of Supervisors":[shenandoah_county_bos,"https://shenandoahcountyva.us/bos/meeting-schedule/"],

    "Shenandoah County Planning Commission":[shenandoah_county_pc,"https://shenandoahcountyva.us/planning-committee/meeting-schedule/"],

    "Smyth County Planning Commission":[smyth_county_pc,"http://www.smythcounty.org/planning_commission/planning_commission_agendas_minutes.htm"],

    "Smyth County Board of Supervisors":[smyth_county_bos,"http://www.smythcounty.org/board_of_supervisors/agendas_minutes_videos.htm"],

    "Southampton County board of Supervisors":[southampton_county,"https://www.southamptoncounty.org/departments/board_of_supervisors/bos_agendas_2023.php","Board of Supervisors"],

    "Southamptom County Planning Commission":[southampton_county,"https://www.southamptoncounty.org/departments/planning/year_2023.php","Planning Commission"],

    "Sussex County":[sussex_county,"https://www.sussexcountyva.gov/events/index/future/"],

    "Wythe County Board of Supervisors":[wythe_county,"http://www.wytheco.org/index.php/resources/meeting-minutes/packages/bos-packages"],

    "Wythe County Planning Commission":[wythe_county,"http://www.wytheco.org/index.php/resources/meeting-minutes/packages/planning-commission"],

}

county_dictionary_double_variable = {
    "Appomattox County":[appomattox_county,"https://www.appomattoxcountyva.gov/government/local-boards-commissions/planning-commission/pc-agendas-minutes-new/-selyear-2023","https://www.appomattoxcountyva.gov/government/board-of-supervisors/bos-agendas-minutes-new"],

    "Fairfax County Planning Commission":[fairfax_county_pc,"https://www.fairfaxcounty.gov/planningcommission/meetingcalendar","\'2023\'"],

    "Greensville County Board of Supervisors":[greensville_county,"https://www.greensvillecountyva.gov/boards___commissions/board_of_supervisors/agendas___minutes/board_of_supervisors.php#outer-1174sub-1176","Board of Supervisors"],

    "Greensville County Planning Commission":[greensville_county,"https://www.greensvillecountyva.gov/boards___commissions/board_of_supervisors/agendas___minutes/planning_commission.php#outer-1188sub-1189","Planning Commission"],

    "Tazewell County Board of Supervisors":[tazewell_county,"https://tazewellcountyva.org/government/boards-and-commissions/board-of-supervisors/", "Board of Supervisors"],

    "Tazewell County Planning Commission":[tazewell_county,"https://tazewellcountyva.org/government/boards-and-commissions/planning-commission/", "Planning Commission"]
}

city_dictionary_single_variable = {
    "Buena Vista City Council":[buena_vista_city_council,"https://www.buenavistava.org/city-services/government/city-council/council-agenda-minutes/"],

    "Clifton Forge":[clifton_forge,"https://www.cliftonforgeva.gov/council/council-agenda-and-minutes/"],

    "Covington":[covington,"https://covington.va.us/agendas-minutes/"],

    "Emporia City Council":[emporia,"https://www.ci.emporia.va.us/node/15/agenda/2023"],

    "Emporia Planning Commission":[emporia,"https://www.ci.emporia.va.us/node/25/agenda/2023"],

    "City of Franklin":[city_of_franklin,"https://www.franklinva.com/government/city-council-agendas/"],

    "City of Galax":[galax,"https://galaxva.com/2023-city-council-agendas/"],

    "City of Lexington Planning Commission":[lexington_pc,"https://www.lexingtonva.gov/government/boards-and-commissions/planning-commission"],

    "City of Lynchburg Planning Commission":[lynchburg_pc,"https://www.lynchburgva.gov/planning-commission-information-agendas-and-legal-notices"],

    "City of Norfolk Planning Commission":[norfolk_pc,"https://norfolkcityva.iqm2.com/Citizens/Board/1018-Planning-Commission"],

    "Norton City":[norton_city,"https://www.nortonva.gov/Archive.aspx?AMID=37"],

    "South Boston":[south_boston,"https://www.southboston.com/departments/council/council_minutes_of_meetings.php"],

    "Staunton Planning Commission":[staunton,"https://www.ci.staunton.va.us/government/city-council-/board-commissions/agendas-minutes-for-boards-commissions/-selmt-1078"],

    "Staunton City Council":[staunton,"https://www.ci.staunton.va.us/agendas-minutes"],

    "Virginia Beach City Council":[virginia_beach_cc,"https://virginiabeach.gov/city-hall/departments-offices/city-clerk/city-council"],

    "Virginia Beach Planning Commission":[virginia_beach_pc,"https://planning.virginiabeach.gov/boards-commissions/planning-commission"]
}

city_dictionary_double_variable = {
    "Manassas Park Planning Commission":[manassas_park,"https://www.manassasparkva.gov/government/governing_body/meetings_agendas___minutes/planning_commission_meeting_agendas.php","Planning Commission"],

    "Manassas Park Governing Body":[manassas_park,"https://www.manassasparkva.gov/government/governing_body/meetings_agendas___minutes/index.php","Governing Body"]
}