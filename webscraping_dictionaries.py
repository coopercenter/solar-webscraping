from webscraping_functions import *
"Dictionaries for the localities that use the same type of document organization service"

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

    "Madison":["https://www.madisonco.virginia.gov/AgendaCenter/Search/?term=&CIDs=3,6,&startDate=&endDate=&dateRange=&dateSelector=","Madison County"],

    "Mecklenburg":["https://www.mecklenburgva.com/AgendaCenter/Search/?term=&CIDs=7,2,8,&startDate=&endDate=&dateRange=&dateSelector=","Mecklenburg County"],

    "Middlesex":["https://www.co.middlesex.va.us/AgendaCenter/Search/?term=&CIDs=4,2,&startDate=&endDate=&dateRange=&dateSelector=","Middlesex County"],

    "Page":["https://www.pagecounty.virginia.gov/AgendaCenter/Search/?term=&CIDs=2,5,&startDate=&endDate=&dateRange=&dateSelector=","Page County"],

    #doesn't always do PDF's, often it's document downloads
    "Patrick":["https://www.co.patrick.va.us/AgendaCenter/Search/?term=&CIDs=3,4,&startDate=&endDate=&dateRange=&dateSelector=", "Patrick County"],
    
    "Powhatan":["http://www.powhatanva.gov/AgendaCenter/Search/?term=&CIDs=2,7,&startDate=&endDate=&dateRange=&dateSelector=","Powhatan County"],

    "Rockbridge":["https://va-rockbridgecounty.civicplus.com/AgendaCenter/Planning-Commission-6","Rockbridge County Planning Commission"],

    "Rockingham":["https://www.rockinghamcountyva.gov/AgendaCenter/Search/?term=&CIDs=1,2,&startDate=&endDate=&dateRange=&dateSelector=","Rockingham County"],

    "Russell":["https://va-russellcounty.civicplus.com/AgendaCenter/Search/?term=&CIDs=5,3,&startDate=&endDate=&dateRange=&dateSelector=","Russell County"],

    "Shenandoah":["https://shenandoahcountyva.us/AgendaCenter/Search/?term=&CIDs=4,3,&startDate=&endDate=&dateRange=&dateSelector=","Shenandoah County"],

    "Wise":["https://www.wisecounty.org/AgendaCenter/Search/?term=&CIDs=3,6,&startDate=&endDate=&dateRange=&dateSelector=","Wise County"],

    "York":["https://www.yorkcounty.gov/AgendaCenter/Search/?term=&CIDs=4,3,&startDate=&endDate=&dateRange=&dateSelector=","York County"],

    "Bedford":["https://www.bedfordva.gov/AgendaCenter/Search/?term=&CIDs=3,2,&startDate=&endDate=&dateRange=&dateSelector=","Town of Bedford"],

    "Colonial Heights":["https://www.colonialheightsva.gov/AgendaCenter/Search/?term=&CIDs=1,4,&startDate=&endDate=&dateRange=&dateSelector=","City of Colonial Heights"],

    "Emporia":["https://www.ci.emporia.va.us/AgendaCenter/Search/?term=&CIDs=all&startDate=&endDate=&dateRange=&dateSelector=","City of Emporia"],

    "Fredricksburg":["https://www.fredericksburgva.gov/AgendaCenter/Search/?term=&CIDs=1,9,&startDate=&endDate=&dateRange=&dateSelector=","City of Fredericksburg"],

    "Hampton":["https://hampton.gov/AgendaCenter/Search/?term=&CIDs=1,6,&startDate=&endDate=&dateRange=&dateSelector=","Hampton City"],

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

"""BoardDocs localities"""
boarddocs_dictionary = {
    'Accomack':["https://go.boarddocs.com/va/coa/Board.nsf/Public","Accomack County",False],

    "Culpeper":["https://go.boarddocs.com/va/ccva/Board.nsf/Public","Culpeper County",False],

    "Essex":["https://go.boarddocs.com/va/essexco/Board.nsf/Public","Essex County",False],

    "Montgomery":["https://go.boarddocs.com/va/montva/Board.nsf/Public","Montgomery County",False],

    "Northampton":["https://go.boarddocs.com/va/northco/Board.nsf/Public","Northampton County",True],

    "Northumberland":["https://go.boarddocs.com/va/nuc/Board.nsf/vpublic?open","Northumberland County",False],

    "Prince George":["https://go.boarddocs.com/va/princegeorge/Board.nsf/Public","Prince George County",False],

    "Pulaski":["https://go.boarddocs.com/va/copva/Board.nsf/Public#","Pulaski County",True],

    "Rappahannock":["https://go.boarddocs.com/va/corva/Board.nsf/Public","Rappahannock County",True],

    "Rockbridge":["https://go.boarddocs.com/va/rcva/Board.nsf/Public","Rockbridge County Board of Supervisors",False],
}

"CivicClerk localities"
civicclerk_dictionary = {
"Amelia":["https://ameliacova.portal.civicclerk.com/?category_id=26,28","Amelia County"],

"Amherst":["https://amherstcova.portal.civicclerk.com/?category_id=27,29,33,32","Amherst County"],

"Appomattox":["https://appomattoxcova.portal.civicclerk.com/","Appomattox County"],

"Charles City":["https://charlescitycova.portal.civicclerk.com/?category_id=26,27,29","Charles City County"],

"Charlottesville":["https://charlottesvilleva.portal.civicclerk.com/","City of Charlottesville"],

"Chesterfield":["https://chesterfieldcova.portal.civicclerk.com/","Chesterfield County"],

"Danville":["https://danvilleva.portal.civicclerk.com/","City of Danville"],

"Hanover":["https://hanovercova.portal.civicclerk.com/?category_id=26,27","Hanover County"],

"James City":["https://jamescitycova.portal.civicclerk.com/","James City County"],

"King William":["https://kingwilliamcova.portal.civicclerk.com/","King William County"],

"Louisa":["https://louisacova.portal.civicclerk.com/", "Louisa County"],

"Lynchburg":["https://lynchburgva.portal.civicclerk.com/","City of Lynchburg"],

"Mathews":["https://mathewscova.portal.civicclerk.com/","Mathews County"],

"Orange":["https://orangecova.portal.civicclerk.com/","Orange County"],

"Roanoke":["https://roanokeva.portal.civicclerk.com/","City of Roanoke"],

"Scott":["https://scottcova.portal.civicclerk.com/","Scott County"],

"Spotsylvania":["https://spotsylvaniacova.portal.civicclerk.com/","Spotsylvania County"],

"Stafford":["https://staffordcova.portal.civicclerk.com/?category_id=26,31","Stafford County"],

"Surry":["https://surrycova.portal.civicclerk.com/","Surry County"],

"Warren":["https://warrencountyva.portal.civicclerk.com/?category_id=26,27","Warren County"],
}

"""CivicWeb localities"""
civicweb_dictionary = {
"Lancaster":["https://lancova.civicweb.net/Portal/MeetingTypeList.aspx","Lancaster County"],

"Lexington":["https://lexingtonva.civicweb.net/Portal/MeetingTypeList.aspx","City of Lexington"],

"Newport News":["https://nngov.civicweb.net/Portal/MeetingTypeList.aspx","City of Newport News"],

"Winchester":["https://winchesterva.civicweb.net/Portal/MeetingTypeList.aspx","City of Winchester"]
}

"""Document Center localities"""
document_center_dictionary = {
    "Dickenson":["https://www.dickensonva.org/DocumentCenter/Index/38","Dickenson County"]
}

"EScribe localities"
escribe_dictionary = {
    "Gloucester":["https://pub-gloucesterva.escribemeetings.com/?FillWidth=1","Gloucester County"]
}

"Event List localities"
event_list_dictionary = {
    "Nelson County":["https://www.nelsoncounty-va.gov/events/list/","Nelson County"],
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

"Roanoke":['https://roanokecountyva.iqm2.com/Citizens/default.aspx',"Roanoke County"],

"Washington":["https://washingtoncountyva.iqm2.com/citizens/default.aspx?frame=no","Washington County"]
}

"LaserFiche localities"
laserfiche_dictionary = {
    "Loudoun BOS":["https://www.loudoun.gov/3426/Board-of-Supervisors-Meetings-Packets","Loudoun County Board of Supervisors"]
}

"Legistar localities"
legistar_dictionary = {
    "Albemarle":["https://albemarle.legistar.com/Calendar.aspx","Albemarle County"],

    "Hampton CC":["https://hampton.legistar.com/Calendar.aspx","Hampton City"],

    "City of Harrisonburg":["https://harrisonburg-va.legistar.com/Calendar.aspx","City of Harrisonburg"],

    'City of Richmond':['https://richmondva.legistar.com/Calendar.aspx','City of Richmond']
}

"""MeetingsTable localities"""
meetingstable_dictionary = {
"Essex PC":["https://www.essex-virginia.org/meetings?date_filter%5Bvalue%5D%5Bmonth%5D=1&date_filter%5Bvalue%5D%5Bday%5D=1&date_filter%5Bvalue%5D%5Byear%5D=2023&date_filter_1%5Bvalue%5D%5Bmonth%5D=12&date_filter_1%5Bvalue%5D%5Bday%5D=31&date_filter_1%5Bvalue%5D%5Byear%5D=2023&field_microsite_tid=All&field_microsite_tid_1=28","Essex County"],

"Fluvanna PC":["https://www.fluvannacounty.org/meetings?field_microsite_tid_1=28","Fluvanna County"],

"Fluvanna BOS":["https://www.fluvannacounty.org/meetings?field_microsite_tid_1=27","Fluvanna County"],

"Northumberland PC":["https://www.co.northumberland.va.us/meetings?field_microsite_tid_1=28","Northumberland County"]
}

"""NovusAGENDA localities"""
novusagenda_dictionary = {
"Isle of Wight PC":["https://isleofwight.novusagenda.com/agendapublic/meetingsgeneral.aspx?MeetingType=2","Isle of Wight County"],

"Isle of Wight BOS":["https://isleofwight.novusagenda.com/agendapublic/meetingsgeneral.aspx?MeetingType=1","Isle of Wight County"],

"New Kent BOS":["https://newkent.novusagenda.com/agendapublic/meetingsgeneral.aspx","New Kent County"],

"Salem CC":["https://salemcity.novusagenda.com/AgendaPublic/MeetingsResponsive.aspx?MeetingType=1&Date=6ms", "Salem City Council"],

"Salem PC":["https://salemcity.novusagenda.com/agendapublic/meetingsresponsive.aspx?MeetingType=3","Salem Planning Commission"]
}

"php table localities"
php_table_dictionary = {
    "Buckingham BOS":["https://www.buckinghamcountyva.org/administration/boards___commissions/board_of_supervisors/board_agenda_minutes_youtube.php","Buckingham County Board of Supervisors"],

    "Buckingham PC":["https://www.buckinghamcountyva.org/administration/boards___commissions/planning_commission.php","Buckingham County Planning Commission"],

    "Carroll County":["https://www.carrollcountyva.gov/government/bos_meeting_agendas.php","Carroll County Board of Supervisors"],

    "Smyth County BOS":["https://smythcounty.org/government/agendas___minutes_/board_of_supervisors_agendas___minutes.php","Smyth County Board of Supervisors"],

    "Smyth County PC":["https://smythcounty.org/government/agendas___minutes_/planning_commission_agendas___minutes.php","Smyth County Planning Commission"]
}

"PrimeGov localities"
primegov_dictionary = {
    "Bedford":["https://bedfordcounty.primegov.com/public/portal","Bedford County"]
}

"Dictionaries for localities that need individual code"
county_dictionary_single_variable = {
    "Albemarle County Planning Commission":[albemarle_county_pc,"https://www.albemarle.org/government/community-development/boards-and-commissions/planning-commission"],

    "Alleghany County":[alleghany_county,"https://www.co.alleghany.va.us/board-of-supervisors/agendas/"],

    "Bath County":[bath_county,"https://www.bathcountyva.gov/public_information/agendas_and_public_notices"],

    "Bland County":[bland_county,"https://www.blandcountyva.gov/page/agendas-and-minutes/"],

    "Brunswick County":[brunswick_county,"https://www.brunswickco.com/government/board_of_supervisors/agendas___minutes"],

    "Buchanan County":[buchanan_county,"https://buchanancountyvirginia.gov/board-of-supervisors/"],

    "Clarke County Board of Supervisors":[clarke_county,"https://www.clarkecounty.gov/government/boards-commissions/board-of-supervisors/bos-agendas/-folder-1324"],

    "Clarke County Planning Commission":[clarke_county,"https://www.clarkecounty.gov/government/boards-commissions/planning-commission/pc-agendas/-folder-1352"],

    "Craig County":[craig_county,"https://craigcountyva.gov/government/board-of-supervisors/"],
    
    "Fairfax County Board of Supervisors":[fairfax_county_bos,"https://www.fairfaxcounty.gov/boardofsupervisors/"],

    "Floyd County":[floyd_county,"https://www.floydcova.gov/agendas-minutes"],

    "Giles County":[giles_county,"https://virginiasmtnplayground.com/bos/"],

    "Grayson County":[grayson_county,"https://www.graysoncountyva.gov/2021-board-of-supervisors/"],

    "Henrico County Board of Supervisors":[henrico_county_bos,"https://henrico.us/supervisors/supervisors-agenda-o-gram/"],

    "Henrico County Planning Commission":[henrico_county_pc,"https://henrico.us/planning/meetings/"],

    "Highland County Board of Supervisors":[highland_county_bos,"https://www.highlandcova.org/node/666/agenda"],

    "Lee County":[lee_county,"http://www.leecova.org/AgendaandMinutes.htm"],

    "Loudoun County":[loudoun_pc,"https://lfportal.loudoun.gov/LFPortalInternet/Browse.aspx?startid=305808&row=1&dbid=0"],

    "Lunenberg County Board of Supervisors":[lunenburg_county,"https://www.lunenburgva.gov/government/board_of_supervisors/agendas___minutes.php"],

    "Lunenburg County Planning Commission":[lunenburg_county,"https://www.lunenburgva.gov/government/planning_commission/agendas___minutes.php"],

    "Montgomery County Planning Commission":[montgomery_pc,"https://www.montva.com/departments/Planning-GIS/planning--commission/meetings-1"],

    "New Kent County Planning Commission":[new_kent_county_pc,"https://www.co.new-kent.va.us/843/Meeting-Agendas"],

    "Pittsylvania County":[pittsylvania_county,"https://www.pittsylvaniacountyva.gov/government/agenda-center"],

    'Prince Edward County Planning Commission':[prince_edward_pc,"https://www.co.prince-edward.va.us/departments/planning-zoning/planning-commission-meetings"],

    'Prince Edward County Board of Supervisors':[prince_edward_bos,"https://www.co.prince-edward.va.us/government/board-of-supervisors/board-meeting-agendas-and-meeting-minutes"],

    "Prince William County Planning Commission":[prince_william_pc,"https://www.pwcva.gov/department/planning-office/planning-commission"],

    "Richmond County":[richmond_county,"https://co.richmond.va.us/board-of-supervisors-agenda-packets"],
 
    "Sussex County":[sussex_county,"https://www.sussexcountyva.gov/page/agendas-and-minutes/"],

    "Wythe County Board of Supervisors":[wythe_county,"http://www.wytheco.org/index.php/resources/meeting-minutes/packages/bos-packages"],

    "Wythe County Planning Commission":[wythe_county,"http://www.wytheco.org/index.php/resources/meeting-minutes/packages/planning-commission"],

}

county_dictionary_double_variable = {
    "Arlington County":[arlington_county,"https://arlington.granicus.com/ViewPublisher.php?view_id=44","https://arlington.granicus.com/ViewPublisher.php?view_id=2"],

    "Charlotte County Board of Supervisors":[charlotte_county,"https://www.charlottecountyva.gov/government/board_of_supervisors/agendas___minutes.php","Board of Supervisors"],

    "Charlotte County Planning Commission":[charlotte_county,"https://www.charlottecountyva.gov/departments/planning___zoning/agendas___minutes.php","Planning Commission"],

    "Fairfax County Planning Commission":[fairfax_county_pc,"https://www.fairfaxcounty.gov/planningcommission/meetingcalendar","\'2023\'"],

    #switch to reading minutes, can actually get text
    "Greensville County Board of Supervisors":[greensville_county,"https://www.greensvillecountyva.gov/boards___commissions/board_of_supervisors/agendas___minutes/board_of_supervisors.php#outer-1174sub-1176","Board of Supervisors"],
    
    #switch to reading minutes, can actually get text
    "Greensville County Planning Commission":[greensville_county,"https://www.greensvillecountyva.gov/boards___commissions/board_of_supervisors/agendas___minutes/planning_commission.php#outer-1188sub-1189","Planning Commission"],

    "King and Queen County Board of Supervisors":[king_and_queen_county,"https://kingandqueenco.net/board-of-supervisors-meetings/", "Board of Supervisors"],

    "King and Queen County Planning Commission":[king_and_queen_county,"https://kingandqueenco.net/planning-commission-meetings/","Planning Commission"],

    "Nottoway County Board of Supervisors":[nottoway_county,"https://nottoway.org/administration/boards___commissions/board_of_supervisors_(bos)/board_agendas_minutes.php","Board of Supervisors"],

    "Nottoway County Planning Commission":[nottoway_county,"https://nottoway.org/administration/boards___commissions/agenda_packets_minutes.php","Planning Commission"],

    "Southampton County Board of Supervisors":[southampton_county,"https://www.southamptoncounty.org/departments/board_of_supervisors/bos_meeting_agendas.php","Board of Supervisors"],

    "Southampton County Planning Commission":[southampton_county,"https://www.southamptoncounty.org/departments/planning/archived_planning_agendas.php","Planning Commission"],

    "Tazewell County Board of Supervisors":[tazewell_county,"https://tazewellcountyva.org/government/boards-and-commissions/board-of-supervisors/", "Board of Supervisors"],

    "Tazewell County Planning Commission":[tazewell_county,"https://tazewellcountyva.org/government/boards-and-commissions/planning-commission/", "Planning Commission"],

    "Westmoreland County Board of Supervisors":[westmoreland_county,"https://www.westmoreland-county.org/bos","Board of Supervisors"],

    "Westmoreland County Planning Commission":[westmoreland_county,"https://www.westmoreland-county.org/pc","Planning Commission"]
}

city_dictionary_single_variable = {
    "Buena Vista City Council":[buena_vista_city_council,"https://www.buenavistava.org/city-services/government/city-council/council-agenda-minutes/"],

    "Clifton Forge":[clifton_forge,"https://www.cliftonforgeva.gov/council/council-agenda-and-minutes/"],

    "Covington":[covington,"https://covington.va.us/agendas-minutes/"],

    "City of Franklin":[city_of_franklin,"https://www.franklinva.com/government/city-council-agendas/"],

    "City of Galax":[galax,"https://galaxva.com/2024-city-council-agendas/"],

    "City of Lexington Planning Commission":[lexington_pc,"https://www.lexingtonva.gov/government/boards-and-commissions/planning-commission"],

    "City of Norfolk Planning Commission":[norfolk_pc,"https://norfolkcityva.iqm2.com/Citizens/Board/1018-Planning-Commission"],

    "Norton City":[norton_city,"https://www.nortonva.gov/Archive.aspx?AMID=37"],

    "South Boston":[south_boston,"https://www.southboston.com/departments/council/council_minutes_of_meetings.php"],

    "Staunton Planning Commission":[staunton,"https://www.ci.staunton.va.us/government/city-council-/board-commissions/agendas-minutes-for-boards-commissions/-selmt-1078"],

    "Staunton City Council":[staunton,"https://www.ci.staunton.va.us/agendas-minutes"],

    "Virginia Beach City Council":[virginia_beach_cc,"https://clerk.virginiabeach.gov/city-council"],

    "Virginia Beach Planning Commission":[virginia_beach_pc,"https://planning.virginiabeach.gov/boards-commissions/planning-commission"]
}

city_dictionary_double_variable = {
    "Manassas Park Planning Commission":[manassas_park,"https://www.manassasparkva.gov/government/governing_body/meetings_agendas___minutes/planning_commission_meeting_agendas.php","Planning Commission"],

    "Manassas Park Governing Body":[manassas_park,"https://www.manassasparkva.gov/government/governing_body/meetings_agendas___minutes/index.php","Governing Body"],

    "City of Williamsburg City Council":[williamsburg,"https://williamsburg.civicweb.net/filepro/documents/1021/","City Council"],

    "City of Williamsburg Planning Commission":[williamsburg,"https://williamsburg.civicweb.net/filepro/documents/6018/","Planning Commission"]
}