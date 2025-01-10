from webscraping_functions import *
meetings_tags = {
    'agendacenter':"tr[class*=catAgendaRow",

    'boarddocs':"a[class*='icon prevnext meeting",

    'civicclerk':"li[class*='cpp-MuiListItem-container'",

    'civicweb':"a[class*='list-link'",

    'documentcenter':"a[class*=pdf",

    'escribe':"div[class*='upcoming-meeting-container'",

    'granicus2':'div[class*=RowTop',

    'granicus':"tr[class*=listingRow",

    'table_rows':"tr",

    'legistar':'tr[id*=ctl00_',

    'primegov':'tr[role*=row',

    'attachmentlink':"a[class*='attachment-link'",

    'planningtitle':"a[title*='Planning'",

    'pdflink':'a[href*=".pdf"',

    'generallink':"a",

    'contentlink':"a[class*='content_link'",

    'pdflist':"li[class*=pdf",

    'list':"li",

    'divrows':"div[class*='views-row'",

    'divcalendar':"div[class*='calendar-title'",

    'pfont':"p[class*='font_7'",

    'agendapdf':"a[href*='agenda.pdf'",

    'pbuttonlink':"a[class*='pb_button'",

    'qbuttonlink':'a[class*="qbutton"',

    'brzlink':'a[class*="brz-a"',

    'nextpdf':"a[href*='next.pdf'",

    'header3':'h3',

    'archivelink':"a[href*='Archive'",

    'tablewidget':'tr[class*="meeting_widget_item"',

    'currentlink':"a[href*=CurrentBriefAgenda",

    'documentlink':'a[class*="document-link"',

    'packagelink':"a[href*=package"
}

agenda_link_or_button_tags = {
    'boarddocs':"a[id*='btn-view-agenda'"
}

pdf_page_tags ={
    'agendacenter':'"div[class*=page"',

    'civicclerk':'"div[class*=page"'
}

agenda_content_tags = {
    'pdf_1':'div[class*=textLayer',

    'pdf_2':"svg[class*=textLayer",

    'webpage_1':"div[id*='divInner'",

    'webpage_2':'div[class*="fusion-text"',

    'webpage_3':"section[class*='main-content-wrap'",

    'boarddocs':"span[class*='title'",

    'civicweb':"html",

    'legistar':'tr[id*=ctl00',

    'novusagenda':"td",

    'onbase':"body"
}

"Dictionaries for the localities that use the same type of document organization service"

"AgendaCenter localities"
agendacenter_dictionary = {
    "Botetourt":{
        'name':'Botetourt County',
        'url':"https://www.botetourtva.gov/AgendaCenter/Search/?term=&CIDs=3,8,6,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'pdf_1'},

    "Campbell":{
        'name':"Campbell County",
        'url':"https://www.co.campbell.va.us/AgendaCenter/Search/?term=&CIDs=5,12,6,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'webpage',
        'agenda_content':'webpage_1'},

    "Caroline":{
        'name':"Caroline County",
        'url':"https://co.caroline.va.us/AgendaCenter/Search/?term=&CIDs=2,3,4,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'webpage',
        'agenda_content':'webpage_1'},

    "Cumberland":{
        'name':"Cumberland County",
        'url':"https://www.cumberlandcounty.virginia.gov/AgendaCenter/Search/?term=&CIDs=2,4,3,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'pdf_1'},

    "Dinwiddie":{
        'name':"Dinwiddie County",
        'url':"https://www.dinwiddieva.us/AgendaCenter/Search/?term=&CIDs=2,3,4,1,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'webpage',
        'agenda_content':'webpage_1'},

    "Franklin":{
        'name':"Franklin County",
        'url':"https://www.franklincountyva.gov/AgendaCenter/Search/?term=&CIDs=7,3,13,4,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'pdf_1'},

    "Halifax":{
        'name':"Halifax County",
        'url':"https://www.halifaxcountyva.gov/AgendaCenter/Search/?term=&CIDs=2,3,4,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'pdf_1'},

    "Henry":{
        'name':"Henry County",
        'url':"https://www.henrycountyva.gov/AgendaCenter/Search/?term=&CIDs=3,9,7,8,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'pdf_1'},

    "King George":{
        'name':"King George County",
        'url':"https://www.kinggeorgecountyva.gov/AgendaCenter/Search/?term=&CIDs=2,3,5,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'pdf_1'},

    "Madison":{
        'name':"Madison County",
        'url':"https://www.madisonco.virginia.gov/AgendaCenter/Search/?term=&CIDs=3,5,7,6,11,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'pdf_1'}, 

    "Mecklenburg":{
        'name':"Mecklenburg County",
        'url':"https://www.mecklenburgva.com/AgendaCenter/Search/?term=&CIDs=2,5,8,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'pdf_1'},

    "Middlesex":{
        'name':"Middlesex County",
        'url':"https://www.co.middlesex.va.us/AgendaCenter/Search/?term=&CIDs=4,8,2,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'pdf_1'},

    "Page":{
        'name':"Page County",
        'url':"https://www.pagecounty.virginia.gov/AgendaCenter/Search/?term=&CIDs=2,7,5,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'pdf_1'},

   "Patrick":{
       'name':"Patrick County",
       'url':"https://www.co.patrick.va.us/AgendaCenter/Search/?term=&CIDs=3,4,&startDate=&endDate=&dateRange=&dateSelector=",
       'agenda_type':'pdf',
       'agenda_content':'pdf_1'},
    
    "Powhatan":{
        'name':"Powhatan County",
        'url':"https://www.powhatanva.gov/AgendaCenter/Search/?term=&CIDs=2,10,7,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'pdf_1'},

   "Rockbridge":{
       'name':"Rockbridge County",
       'url':"https://va-rockbridgecounty.civicplus.com/AgendaCenter/Search/?term=&CIDs=3,6,5,&startDate=&endDate=&dateRange=&dateSelector=",
       'agenda_type':'pdf',
       'agenda_content':'pdf_1'},

    "Rockingham":{
        'name':"Rockingham County",
        'url':"https://www.rockinghamcountyva.gov/AgendaCenter",
        'agenda_type':'pdf',
        'agenda_content':'pdf_1'},

    "Russell":{
        'name':"Russell County",
        'url':"https://va-russellcounty.civicplus.com/AgendaCenter/Search/?term=&CIDs=5,4,3,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'pdf_1'},

    "Shenandoah":{
        'name':"Shenandoah County",
        'url':"https://shenandoahcountyva.us/AgendaCenter/Search/?term=&CIDs=4,11,3,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'pdf_1'},

    "Wise":{
        'name':"Wise County",
        'url':"https://www.wisecounty.org/AgendaCenter/Search/?term=&CIDs=3,6,4,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'pdf_1'},

    "York":{
        'name':"York County",
        'url':"https://www.yorkcounty.gov/AgendaCenter/Search/?term=&CIDs=4,3,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'pdf_1'},

    "Bedford":{
        'name':"Town of Bedford",
        'url':"https://www.bedfordva.gov/AgendaCenter/Search/?term=&CIDs=3,2,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'pdf_1'},

    "Charles City":{
        'name':'Charles City County',
        'url':'https://www.charlescityva.us/AgendaCenter/Search/?term=&CIDs=6,2,8,&startDate=&endDate=&dateRange=&dateSelector=',
        'agenda_type':'pdf',
        'agenda_content':'pdf_1'
    },

    "Colonial Heights BZA PC":{
        'name':"City of Colonial Heights",
        'url':"https://www.colonialheightsva.gov/AgendaCenter/Search/?term=&CIDs=4,6,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'pdf_1'},

    "Colonial Heights CC":{
        'name':"City of Colonial Heights",
        'url':"https://www.colonialheightsva.gov/AgendaCenter/Search/?term=&CIDs=1,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'webpage',
        'agenda_content':'webpage_1'},

    "Emporia":{
        'name':"City of Emporia",
        'url':"https://www.ci.emporia.va.us/AgendaCenter/Search/?term=&CIDs=2,6,8,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'pdf_1'},

    "Fredericksburg":{
        'name':"City of Fredericksburg",
        'url':"https://www.fredericksburgva.gov/AgendaCenter/Search/?term=&CIDs=6,1,9,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'webpage',
        'agenda_content':'webpage_1'},

    "Hampton":{
        'name':"Hampton City",
        'url':"https://www.hampton.gov/AgendaCenter/Search/?term=&CIDs=2,6,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'pdf_1'},

    "Hopewell":{
        'name':"City of Hopewell",
        'url':"https://hopewellva.gov/AgendaCenter",
        'agenda_type':'pdf',
        'agenda_content':'pdf_1'},

    "Martinsville":{
        'name':"City of Martinsville",
        'url':"https://www.martinsville-va.gov/AgendaCenter/Search/?term=&CIDs=2,6,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'pdf_1'},

    "Norfolk CC":{
        'name':"City of Norfolk",
        'url':"https://www.norfolk.gov/AgendaCenter/Search/?term=&CIDs=25,13,14,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'pdf_1'},

    "Petersburg":{
        'name':"City of Petersburg",
        'url':"http://www.petersburg-va.org/AgendaCenter/Search/?term=&CIDs=9,1,3,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'pdf_1'},

   "Poquoson":{
       'name':"City of Poquoson",
       'url':"https://www.ci.poquoson.va.us/AgendaCenter/Search/?term=&CIDs=2,3,&startDate=&endDate=&dateRange=&dateSelector=",
       'agenda_type':'pdf',
       'agenda_content':'pdf_1'}, #takes extra steps to arrive at agenda, maybe shouldn't be in generic agenda center code

    "Portsmouth":{
        'name':"City of Portsmouth",
        'url':"https://www.portsmouthva.gov/AgendaCenter/Search/?term=&CIDs=11,7,4,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'pdf_1'},

    "Radford":{
        'name':"City of Radford",
        'url':"https://www.radfordva.gov/AgendaCenter/Search/?term=&CIDs=2,4,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'pdf_1'},

    "Suffolk":{
        'name':"City of Suffolk",
        'url':"https://www.suffolkva.us/AgendaCenter/Search/?term=&CIDs=20,21,11,4,12,3,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'pdf_1'},

    "Waynesboro BZA PC":{
        'name':"City of Waynesboro",
        'url':"https://www.waynesboro.va.us/AgendaCenter/Search/?term=&CIDs=7,4,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'pdf_1'},

    "Waynesboro CC":{
        'name':"City of Waynesboro",
        'url':"https://www.waynesboro.va.us/AgendaCenter/Search/?term=&CIDs=1,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'webpage',
        'agenda_content':'webpage_1'}
    }

"""BoardDocs localities"""
boarddocs_dictionary = {
    'Accomack':{
        'url':"https://go.boarddocs.com/va/coa/Board.nsf/Public",
        'name':"Accomack County",
        'second_page':False},

    "Culpeper":{
        'url':"https://go.boarddocs.com/va/ccva/Board.nsf/Public",
        'name':"Culpeper County",
        'second_page':False},

    "Essex":{
        'url':"https://go.boarddocs.com/va/essexco/Board.nsf/Public",
        'name':"Essex County",
        'second_page':False},

    "Montgomery":{
        'url':"https://go.boarddocs.com/va/montva/Board.nsf/Public",
        'name':"Montgomery County",
        'second_page':True},

    "Northampton":{
        'url':"https://go.boarddocs.com/va/northco/Board.nsf/Public",
        'name':"Northampton County",
        'second_page':True},

    "Northumberland":{
        'url':"https://go.boarddocs.com/va/nuc/Board.nsf/vpublic?open",
        'name':"Northumberland County",
        'second_page':False},

    "Prince George":{
        'url':"https://go.boarddocs.com/va/princegeorge/Board.nsf/Public",
        'name':"Prince George County",
        'second_page':False},

    "Pulaski":{
        'url':"https://go.boarddocs.com/va/copva/Board.nsf/Public#",
        'name':"Pulaski County",
        'second_page':True},

    "Rappahannock":{
        'url':"https://go.boarddocs.com/va/corva/Board.nsf/Public",
        'name':"Rappahannock County",
        'second_page':True},

    "Rockbridge":{
        'url':"https://go.boarddocs.com/va/rcva/Board.nsf/Public",
        'name':"Rockbridge County Board of Supervisors",
        'second_page':False},
}

"CivicClerk localities"
civicclerk_dictionary = {
"Amelia":{
    'url':"https://ameliacova.portal.civicclerk.com/?category_id=26,28", #not loading, 12/19/24
    'name':"Amelia County",
    'agenda_type':'pdf',
    'agenda_content':'pdf_1'},

"Amherst":{
    'url':"https://amherstcova.portal.civicclerk.com/?category_id=27,29,33,32",
    'name':"Amherst County",
    'agenda_type':'pdf',
    'agenda_content':'pdf_1'},

"Appomattox":{
    'url':"https://appomattoxcova.portal.civicclerk.com/",
    'name':"Appomattox County",
    'agenda_type':'pdf',
    'agenda_content':'pdf_1'},

#More updates at the AgendaCenter site, table this entry until there is a complete switch
#"Charles City":{
    #'url':"https://charlescitycova.portal.civicclerk.com/?category_id=26,27,29",
    #'name':"Charles City County"},

"Charlottesville":{
    'url':"https://charlottesvilleva.portal.civicclerk.com/",
    'name':"City of Charlottesville",
    'agenda_type':'pdf',
    'agenda_content':'pdf_1'},

"Chesterfield":{
    'url':"https://chesterfieldcova.portal.civicclerk.com/",
    'name':"Chesterfield County",
    'agenda_type':'pdf',
    'agenda_content':'pdf_1'},

"Danville":{
    'url':"https://danvilleva.portal.civicclerk.com/",
    'name':"City of Danville",
    'agenda_type':'pdf',
    'agenda_content':'pdf_1'},

"Hanover":{
    'url':"https://hanovercova.portal.civicclerk.com/?category_id=26,27",
    'name':"Hanover County",
    'agenda_type':'pdf',
    'agenda_content':'pdf_1'},

"James City":{
    'url':"https://jamescitycova.portal.civicclerk.com/",
    'name':"James City County",
    'agenda_type':'pdf',
    'agenda_content':'pdf_1'},

"King William":{
    'url':"https://kingwilliamcova.portal.civicclerk.com/",
    'name':"King William County",
    'agenda_type':'pdf',
    'agenda_content':'pdf_1'},

"Louisa":{
    'url':"https://louisacova.portal.civicclerk.com/",
    'name':"Louisa County",
    'agenda_type':'pdf',
    'agenda_content':'pdf_1'},

"Lynchburg":{
    'url':"https://lynchburgva.portal.civicclerk.com/",
    'name':"City of Lynchburg",
    'agenda_type':'pdf',
    'agenda_content':'pdf_1'},

"Mathews":{
    'url':"https://mathewscova.portal.civicclerk.com/",
    'name':"Mathews County",
    'agenda_type':'pdf',
    'agenda_content':'pdf_1'},

"Orange":{
    'url':"https://orangecova.portal.civicclerk.com/",
    'name':"Orange County",
    'agenda_type':'pdf',
    'agenda_content':'pdf_1'},

"Petersburg CC":{
    'url':"https://petersburgva.portal.civicclerk.com/",
    'name':"City of Petersburg",
    'agenda_type':'pdf',
    'agenda_content':'pdf_1'},

"Roanoke":{
    'url':"https://roanokeva.portal.civicclerk.com/",
    'name':"City of Roanoke",
    'agenda_type':'pdf',
    'agenda_content':'pdf_1'},

"Scott":{
    'url':"https://scottcova.portal.civicclerk.com/",
    'name':"Scott County",
    'agenda_type':'pdf',
    'agenda_content':'pdf_1'},

"Spotsylvania":{
    'url':"https://spotsylvaniacova.portal.civicclerk.com/",
    'name':"Spotsylvania County",
    'agenda_type':'pdf',
    'agenda_content':'pdf_1'},

"Stafford":{
    'url':"https://staffordcova.portal.civicclerk.com/?category_id=26,31",
    'name':"Stafford County",
    'agenda_type':'pdf',
    'agenda_content':'pdf_1'},

"Surry":{
    'url':"https://surrycova.portal.civicclerk.com/",
    'name':"Surry County",
    'aagenda_type':'pdf',
    'agenda_content':'pdf_1'},

"Warren":{
    'url':"https://warrencountyva.portal.civicclerk.com/?category_id=26,27",
    'name':"Warren County",
    'agenda_type':'pdf',
    'agenda_content':'pdf_1'}
}

"""CivicWeb localities"""
civicweb_dictionary = {
"Lancaster":{
    'url':"https://lancova.civicweb.net/Portal/MeetingTypeList.aspx",
    'name':"Lancaster County"},

"Lexington":{
    'url':"https://lexingtonva.civicweb.net/Portal/MeetingTypeList.aspx",
    'name':"City of Lexington"},

"Newport News":{
    'url':"https://nngov.civicweb.net/Portal/MeetingTypeList.aspx",
    'name':"City of Newport News"},

"Winchester":{
    'url':"https://winchesterva.civicweb.net/Portal/MeetingTypeList.aspx",
    'name':"City of Winchester"}
}

"""Document Center localities"""
document_center_dictionary = {
    "Dickenson":["https://www.dickensonva.org/DocumentCenter/Index/38","Dickenson County"]
}

"EScribe localities"
escribe_dictionary = {
    "Gloucester":["https://pub-gloucesterva.escribemeetings.com/?FillWidth=1","Gloucester County"]
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

"Norfolk Planning Commission":["https://norfolkcityva.iqm2.com/Citizens/Board/1018-Planning-Commission","City of Norfolk Planning Commission"],

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
"Fluvanna PC":["https://www.fluvannacounty.org/meetings?field_microsite_tid_1=28","Fluvanna County"],

"Fluvanna BOS":["https://www.fluvannacounty.org/meetings?field_microsite_tid_1=27","Fluvanna County"],

"Northumberland PC":["https://www.co.northumberland.va.us/meetings?field_microsite_tid_1=28","Northumberland County"]
}

"""NovusAGENDA localities"""
novusagenda_dictionary = {
"Isle of Wight PC":["https://isleofwight.novusagenda.com/agendapublic/meetingsgeneral.aspx?MeetingType=2","Isle of Wight County Planning Commission"],

"Isle of Wight BOS":["https://isleofwight.novusagenda.com/agendapublic/meetingsgeneral.aspx?MeetingType=1","Isle of Wight County Board of Supervisors"],

"New Kent BOS":["https://newkent.novusagenda.com/agendapublic/meetingsgeneral.aspx","New Kent County"],

"Salem CC":["https://salemcity.novusagenda.com/AgendaPublic/MeetingsResponsive.aspx?MeetingType=1&Date=6ms", "Salem City Council"],

"Salem PC":["https://salemcity.novusagenda.com/agendapublic/meetingsresponsive.aspx?MeetingType=3","Salem Planning Commission"]
}

"""OnBase localities"""
onbase_dictionary = {
    "Arlington County Board":["https://meetings.arlingtonva.us/CountyBoard","Arlington County Board"],
    
    "Arlington County PC":["https://meetings.arlingtonva.us/Planning","Arlington County Planning Commission"]
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
    "Albemarle County Planning Commission":[albemarle_county_pc,"https://www.albemarle.org/government/community-development/boards-and-commissions/planning-commission/-toggle-next30days"],

    "Alleghany County":[alleghany_county,"https://www.co.alleghany.va.us/board-of-supervisors/agendas/"],

    "Bath County":[bath_county,"https://www.bathcountyva.gov/public_information/agendas_and_public_notices"],

    "Bland County":[bland_county,"https://www.blandcountyva.gov/page/agendas-and-minutes/"],

    "Brunswick County":[brunswick_county,"https://www.brunswickco.com/government/board_of_supervisors/agendas___minutes"],

    "Buchanan County":[buchanan_county,"https://buchanancountyvirginia.gov/board-of-supervisors/"],

    "Clarke County Board of Supervisors":[clarke_county,"https://www.clarkecounty.gov/government/boards-commissions/board-of-supervisors/bos-agendas/-folder-1017"],

    "Clarke County Planning Commission":[clarke_county,"https://www.clarkecounty.gov/government/boards-commissions/planning-commission/pc-agendas/-folder-1031"],

    "Craig County":[craig_county,"https://craigcountyva.gov/government/board-of-supervisors/"],

    "Essex County Planning Commission":[essex_pc,"https://www.essex-virginia.org/meetings?date_filter%5Bvalue%5D%5Bmonth%5D=1&date_filter%5Bvalue%5D%5Bday%5D=1&date_filter%5Bvalue%5D%5Byear%5D=2023&date_filter_1%5Bvalue%5D%5Bmonth%5D=12&date_filter_1%5Bvalue%5D%5Bday%5D=31&date_filter_1%5Bvalue%5D%5Byear%5D=2023&field_microsite_tid=All&field_microsite_tid_1=28"],
    
    "Fairfax County Board of Supervisors":[fairfax_county_bos,"https://www.fairfaxcounty.gov/boardofsupervisors/"],

    "Fairfax County Planning Commission":[fairfax_county_pc,"https://www.fairfaxcounty.gov/planningcommission/meetingcalendar"],

    "Floyd County":[floyd_county,"https://www.floydcova.gov/agendas-minutes"],

    "Giles County":[giles_county,"https://virginiasmtnplayground.com/bos/"],

    "Grayson County":[grayson_county,"https://www.graysoncountyva.gov/board-agendas-and-minutes/"],

    "Henrico County Board of Supervisors":[henrico_county_bos,"https://henrico.us/supervisors/supervisors-agenda-o-gram/"],

    "Henrico County Planning Commission":[henrico_county_pc,"https://henrico.us/planning/meetings/"],

    "Highland County Board of Supervisors":[highland_county_bos,"https://www.highlandcova.org/node/666/agenda"],

    "Lee County":[lee_county,"http://www.leecova.org/AgendaandMinutes.htm"],

    "Loudoun County":[loudoun_pc,"https://lfportal.loudoun.gov/LFPortalInternet/Browse.aspx?startid=305808&row=1&dbid=0"],

    "Lunenberg County Board of Supervisors":[lunenburg_county,"https://www.lunenburgva.gov/government/board_of_supervisors/agendas___minutes.php"],

    "Lunenburg County Planning Commission":[lunenburg_county,"https://www.lunenburgva.gov/government/planning_commission/agendas___minutes.php"],

    "Nelson County":[nelson_county,"https://www.nelsoncounty-va.gov/events/list/"],

    "New Kent County Planning Commission":[new_kent_county_pc,"https://www.newkent-va.us/843/Meeting-Agendas"],

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
    "Charlotte County Board of Supervisors":[charlotte_county,"https://www.charlottecountyva.gov/government/board_of_supervisors/agendas___minutes.php","Board of Supervisors"],

    "Charlotte County Planning Commission":[charlotte_county,"https://www.charlottecountyva.gov/departments/planning___zoning/agendas___minutes.php","Planning Commission"],

    "Greensville County Board of Supervisors":[greensville_county,"https://www.greensvillecountyva.gov/boards___commissions/board_of_supervisors/agendas___minutes/board_of_supervisors.php","Board of Supervisors"],
    
    "Greensville County Planning Commission":[greensville_county,"https://www.greensvillecountyva.gov/boards___commissions/board_of_supervisors/agendas___minutes/planning_commission.php","Planning Commission"],

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

    #UPDATE website is updated, need new code
    #"Clifton Forge":[clifton_forge,"https://www.cliftonforgeva.gov/council/council-agenda-and-minutes/"],

    "Covington":[covington,"https://covington.va.us/agendas-minutes/"],

    "City of Franklin":[city_of_franklin,"https://www.franklinva.com/government/city-council-agendas/"],

    "City of Galax":[galax,"https://galaxva.com/2024-city-council-agendas/"],

    "City of Lexington Planning Commission":[lexington_pc,"https://www.lexingtonva.gov/government/boards-and-commissions/planning-commission"],

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