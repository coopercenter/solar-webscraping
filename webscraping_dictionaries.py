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

agenda_content_tags = { #table this idea for now, it's making things unnecessarily complicated, attach the actual tags to the locality dictionaries
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
        #new and horrible pop-up window that blocks my scraper!
        'name':'Botetourt County',
        'url':"https://www.botetourtva.gov/AgendaCenter/Search/?term=&CIDs=3,8,6,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Campbell":{
        'name':"Campbell County",
        'url':"https://www.co.campbell.va.us/AgendaCenter/Search/?term=&CIDs=5,12,6,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'webpage',
        'agenda_content':"div[id*='divInner'"},

    "Caroline":{
        'name':"Caroline County",
        'url':"https://co.caroline.va.us/AgendaCenter/Search/?term=&CIDs=2,3,4,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'webpage',
        'agenda_content':"div[id*='divInner'"},

    "Cumberland":{
        'name':"Cumberland County",
        'url':"https://www.cumberlandcounty.virginia.gov/AgendaCenter/Search/?term=&CIDs=2,4,3,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Dinwiddie":{
        'name':"Dinwiddie County",
        'url':"https://www.dinwiddieva.us/AgendaCenter/Search/?term=&CIDs=2,3,4,1,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'webpage',
        'agenda_content':"div[id*='divInner'"},

    "Franklin":{
        'name':"Franklin County",
        'url':"https://www.franklincountyva.gov/AgendaCenter/Search/?term=&CIDs=7,3,13,4,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Grayson":{
        'name':'Grayson County Board of Supervisors',
        'url':"https://www.graysoncountyva.gov/AgendaCenter/Search/?term=&CIDs=5,2,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Halifax":{
        'name':"Halifax County",
        'url':"https://www.halifaxcountyva.gov/AgendaCenter/Search/?term=&CIDs=2,3,4,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Henry":{
        'name':"Henry County",
        'url':"https://www.henrycountyva.gov/AgendaCenter/Search/?term=&CIDs=3,9,7,8,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "King George":{
        'name':"King George County",
        'url':"https://www.kinggeorgecountyva.gov/AgendaCenter/Search/?term=&CIDs=2,3,5,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Madison":{
        'name':"Madison County",
        'url':"https://www.madisonco.virginia.gov/AgendaCenter/Search/?term=&CIDs=3,5,7,6,11,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'}, 

    "Mecklenburg":{
        'name':"Mecklenburg County",
        'url':"https://www.mecklenburgva.com/AgendaCenter/Search/?term=&CIDs=2,5,8,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Middlesex":{
        'name':"Middlesex County",
        'url':"https://www.co.middlesex.va.us/AgendaCenter/Search/?term=&CIDs=4,8,2,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Page":{
        'name':"Page County",
        'url':"https://www.pagecounty.virginia.gov/AgendaCenter/Search/?term=&CIDs=2,7,5,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

   "Patrick":{
       'name':"Patrick County",
       'url':"https://www.co.patrick.va.us/AgendaCenter/Search/?term=&CIDs=3,4,&startDate=&endDate=&dateRange=&dateSelector=",
       'agenda_type':'pdf',
       'agenda_content':'div[class*=textLayer'},
    
    "Powhatan":{
        'name':"Powhatan County",
        'url':"https://www.powhatanva.gov/AgendaCenter/Search/?term=&CIDs=2,10,7,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

   "Rockbridge":{
       'name':"Rockbridge County",
       'url':"https://va-rockbridgecounty.civicplus.com/AgendaCenter/Search/?term=&CIDs=25,3,6,5,23,&startDate=&endDate=&dateRange=&dateSelector=",
       'agenda_type':'pdf',
       'agenda_content':'div[class*=textLayer'},

    "Rockingham":{
        'name':"Rockingham County",
        'url':"https://www.rockinghamcountyva.gov/AgendaCenter",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Russell":{
        'name':"Russell County",
        'url':"https://va-russellcounty.civicplus.com/AgendaCenter/Search/?term=&CIDs=5,4,3,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Shenandoah":{
        'name':"Shenandoah County",
        'url':"https://shenandoahcountyva.us/AgendaCenter/Search/?term=&CIDs=4,11,3,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Wise":{
        'name':"Wise County",
        'url':"https://www.wisecounty.org/AgendaCenter/Search/?term=&CIDs=3,6,4,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "York":{
        'name':"York County",
        'url':"https://www.yorkcounty.gov/AgendaCenter/Search/?term=&CIDs=4,3,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Bedford":{
        'name':"Town of Bedford",
        'url':"https://www.bedfordva.gov/AgendaCenter/Search/?term=&CIDs=3,2,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Charles City":{
        'name':'Charles City County',
        'url':'https://www.charlescityva.us/AgendaCenter/Search/?term=&CIDs=6,2,8,&startDate=&endDate=&dateRange=&dateSelector=',
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'
    },

    "Colonial Heights BZA PC":{
        'name':"City of Colonial Heights",
        'url':"https://www.colonialheightsva.gov/AgendaCenter/Search/?term=&CIDs=4,6,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Colonial Heights CC":{
        'name':"City of Colonial Heights",
        'url':"https://www.colonialheightsva.gov/AgendaCenter/Search/?term=&CIDs=1,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'webpage',
        'agenda_content':"div[id*='divInner'"},

    "Emporia":{
        'name':"City of Emporia",
        'url':"https://www.ci.emporia.va.us/AgendaCenter/Search/?term=&CIDs=2,6,8,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Fredericksburg":{
        'name':"City of Fredericksburg",
        'url':"https://www.fredericksburgva.gov/AgendaCenter/Search/?term=&CIDs=6,1,9,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'webpage',
        'agenda_content':"div[id*='divInner'"},

    "Hampton":{
        'name':"Hampton City",
        'url':"https://www.hampton.gov/AgendaCenter/Search/?term=&CIDs=2,6,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Hopewell":{
        'name':"City of Hopewell",
        'url':"https://hopewellva.gov/AgendaCenter",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Martinsville":{
        'name':"City of Martinsville",
        'url':"https://www.martinsville-va.gov/AgendaCenter/Search/?term=&CIDs=2,6,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Norfolk CC":{
        'name':"City of Norfolk",
        'url':"https://www.norfolk.gov/AgendaCenter/Search/?term=&CIDs=25,13,14,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Petersburg":{
        'name':"City of Petersburg",
        'url':"http://www.petersburg-va.org/AgendaCenter/Search/?term=&CIDs=9,1,3,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Portsmouth":{
        'name':"City of Portsmouth",
        'url':"https://www.portsmouthva.gov/AgendaCenter/Search/?term=&CIDs=11,7,4,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Radford":{
        'name':"City of Radford",
        'url':"https://www.radfordva.gov/AgendaCenter/Search/?term=&CIDs=2,4,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Suffolk":{
        'name':"City of Suffolk",
        'url':"https://www.suffolkva.us/AgendaCenter/Search/?term=&CIDs=20,21,11,4,12,3,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Waynesboro BZA PC":{
        'name':"City of Waynesboro",
        'url':"https://www.waynesboro.va.us/AgendaCenter/Search/?term=&CIDs=7,4,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Waynesboro CC":{
        'name':"City of Waynesboro",
        'url':"https://www.waynesboro.va.us/AgendaCenter/Search/?term=&CIDs=1,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'webpage',
        'agenda_content':"div[id*='divInner'"}
    }

agendacenter2_dictionary = {
    "Poquoson":{
       'name':"City of Poquoson",
       'url':"https://www.ci.poquoson.va.us/AgendaCenter/Search/?term=&CIDs=2,3,&startDate=&endDate=&dateRange=&dateSelector=",
       'agenda_type':'pdf',
       'agenda_content':'div[class*=textLayer'},

    "Grayson":{
        'name':'Grayson County Planning Commission',
        'url':"https://www.graysoncountyva.gov/AgendaCenter/Search/?term=&CIDs=3,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Grayson BOS":{
        'name':'Grayson County Board of Supervisors',
        'url':"https://www.graysoncountyva.gov/AgendaCenter/Search/?term=&CIDs=5,2,&startDate=&endDate=&dateRange=&dateSelector=",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

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

"CivicClerk localities" #no need to check for 05/27 dates in these localities since current code checks all visible meetings
civicclerk_dictionary = {
#"Amelia":{
    #'url':"https://ameliacova.portal.civicclerk.com/?category_id=26,28", #move BOS to PHP table, new code for PC
    #'name':"Amelia County",
    #'agenda_type':'pdf',
    #'agenda_content':'div[class*=textLayer'},

"Amherst":{
    'url':"https://amherstcova.portal.civicclerk.com/?category_id=27,29,33,32",
    'name':"Amherst County",
    'agenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'},

"Appomattox":{
    'url':"https://appomattoxcova.portal.civicclerk.com/",
    'name':"Appomattox County",
    'agenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'},

"Augusta":{
    'url':"https://augustacova.portal.civicclerk.com/",
    'name':"Augusta County",
    'agenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'},

#More updates at the AgendaCenter site, table this entry until there is a complete switch
#"Charles City":{
    #'url':"https://charlescitycova.portal.civicclerk.com/?category_id=26,27,29",
    #'name':"Charles City County"},

"Charlottesville":{
    'url':"https://charlottesvilleva.portal.civicclerk.com/",
    'name':"City of Charlottesville",
    'agenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'},

"Chesterfield":{
    'url':"https://chesterfieldcova.portal.civicclerk.com/",
    'name':"Chesterfield County",
    'agenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'},

"Danville":{
    'url':"https://danvilleva.portal.civicclerk.com/",
    'name':"City of Danville",
    'agenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'},

"Greene":{
    'url':"https://greenecova.portal.civicclerk.com/", #historical archives at https://gcva.granicus.com/ViewPublisher.php?view_id=1
    'name':"Greene County",
    'agenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'},

"Hanover":{
    'url':"https://hanovercova.portal.civicclerk.com/?category_id=26,27",
    'name':"Hanover County",
    'agenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'},

"James City":{
    'url':"https://jamescitycova.portal.civicclerk.com/",
    'name':"James City County",
    'agenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'},

"King William":{
    'url':"https://kingwilliamcova.portal.civicclerk.com/",
    'name':"King William County",
    'agenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'},

"Louisa":{
    'url':"https://louisacova.portal.civicclerk.com/",
    'name':"Louisa County",
    'agenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'},

"Lynchburg":{
    'url':"https://lynchburgva.portal.civicclerk.com/",
    'name':"City of Lynchburg",
    'agenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'},

"Mathews":{
    'url':"https://mathewscova.portal.civicclerk.com/",
    'name':"Mathews County",
    'agenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'},

"Orange":{
    'url':"https://orangecova.portal.civicclerk.com/",
    'name':"Orange County",
    'agenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'},

"Petersburg CC":{
    'url':"https://petersburgva.portal.civicclerk.com/",
    'name':"City of Petersburg",
    'agenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'},

"Roanoke":{
    'url':"https://roanokeva.portal.civicclerk.com/",
    'name':"City of Roanoke",
    'agenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'},

'Salem':{
    'url':'https://salemva.portal.civicclerk.com/',
    'name':'City of Salem',
    'agenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'},

"Scott":{
    'url':"https://scottcova.portal.civicclerk.com/",
    'name':"Scott County",
    'agenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'},

"Spotsylvania":{
    'url':"https://spotsylvaniacova.portal.civicclerk.com/",
    'name':"Spotsylvania County",
    'agenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'},

"Stafford":{
    'url':"https://staffordcova.portal.civicclerk.com/?category_id=26,31",
    'name':"Stafford County",
    'agenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'},

"Surry":{
    'url':"https://surrycova.portal.civicclerk.com/",
    'name':"Surry County",
    'aagenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'},

"Warren":{
    'url':"https://warrencountyva.portal.civicclerk.com/?category_id=26,27",
    'name':"Warren County",
    'agenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'}
}

"""CivicWeb localities"""
civicweb_dictionary = {
"Lancaster":{
    'url':"https://lancova.civicweb.net/Portal/MeetingTypeList.aspx",
    'name':"Lancaster County",
    'meetings_tag':"a[class*='list-link'"},

"Lexington":{
    'url':"https://lexingtonva.civicweb.net/Portal/MeetingTypeList.aspx",
    'name':"City of Lexington",
    'meetings_tag':"a[class*='list-link'"},

"Newport News":{
    'url':"https://nngov.civicweb.net/Portal/MeetingTypeList.aspx",
    'name':"City of Newport News",
    'meetings_tag':"a[class*='list-link'"},

'Williamsburg':{
    'url':'https://williamsburg.civicweb.net/Portal/Default.aspx',
    'name':'City of Williamsburg',
    'meetings_tag':"a[class*='list-link'"
},

"Winchester":{
    'url':"https://winchesterva.civicweb.net/Portal/MeetingTypeList.aspx",
    'name':"City of Winchester",
    'meetings_tag':"a[class*='list-link'"}
}

"""Document Center localities"""
document_center_dictionary = {
    "Dickenson":{
        'url':"https://www.dickensonva.org/DocumentCenter/Index/39", #new link, confirm it works
        'name':"Dickenson County",
        "content_tag":"div[class*=textLayer"}
}

"EScribe localities"
escribe_dictionary = {
    "Gloucester":{
        'url':"https://pub-gloucesterva.escribemeetings.com/?FillWidth=1",
        'name':"Gloucester County"}
}

"Granicus localities"
granicus_dictionary = {
"Fauquier":{
    'url':"https://fauquier-va.granicus.com/ViewPublisher.php?view_id=3",
    'name':"Fauquier County"},

"Frederick":{
    'url':"https://fcva.granicus.com/ViewPublisher.php?view_id=1",
    'name':"Frederick County"},

"Prince William BOS":{
    'url':"https://pwcgov.granicus.com/ViewPublisher.php?view_id=23",
    'name':"Prince William County Board of Supervisors"},

"Prince William PC":{
    'url':"https://pwcgov.granicus.com/ViewPublisher.php?view_id=12",
    'name':' Prince William County Planning Commission'},

"Alexandria":{
    'url':"https://alexandria.granicus.com/ViewPublisher.php?view_id=57", #format is weird, revisit this
    'name':"City of Alexandria"},

"Bristol":{
    'url':"https://bristolva.granicus.com/ViewPublisher.php?view_id=1",
    'name':"City of Bristol"},

"Chesapeake CC":{
    'url':"https://chesapeake.granicus.com/ViewPublisher.php?view_id=29",
    'name':"City of Chesapeake"},

"Chesapeake PC":{
    'url':"https://chesapeake.granicus.com/ViewPublisher.php?view_id=35",
    'name':"City of Chesapeake"},

"Fairfax":{
    'url':"https://fairfax.granicus.com/ViewPublisher.php?view_id=11", #NOT A PDF no PDF option for agendas
    'name':"City of Fairfax"},

"Falls Church":{
    'url':"https://fallschurch-va.granicus.com/ViewPublisher.php?view_id=2", #also not a PDF, no PDF option for agenda
    'name':"City of Falls Church"},

"Manassas":{
    'url':"https://manassascity.granicus.com/ViewPublisher.php?view_id=1",
    'name':"Manassas City"}
}

"""Granicus version 2 localities"""
granicus_2_dictionary = {
"Goochland":{
    'url':"https://goochlandcountyva.iqm2.com/Citizens/Default.aspx",
    'name':"Goochland County"},

"Norfolk Planning Commission":{
    'url':"https://norfolkcityva.iqm2.com/Citizens/Board/1018-Planning-Commission",
    'name':"City of Norfolk Planning Commission"}, #this is a download now

"Roanoke":{
    'url':'https://roanokecountyva.iqm2.com/Citizens/default.aspx',
    'name':"Roanoke County"},

"Washington":{
    'url':"https://washingtoncountyva.iqm2.com/citizens/default.aspx?frame=no",
    'name':"Washington County"}
}

"LaserFiche localities"
laserfiche_dictionary = {
    "Loudoun BOS":{
        'url':"https://www.loudoun.gov/3426/Board-of-Supervisors-Meetings-Packets",
        'name':"Loudoun County Board of Supervisors"}
}

"Legistar localities"
legistar_dictionary = {
    "Albemarle":{
        'url':"https://albemarle.legistar.com/Calendar.aspx",
        'name':"Albemarle County"},

    "Hampton CC":{
        'url':"https://hampton.legistar.com/Calendar.aspx",
        'name':"Hampton City"}, 

    "City of Harrisonburg":{
        'url':"https://harrisonburg-va.legistar.com/Calendar.aspx",
        'name':"City of Harrisonburg"},

    'City of Richmond':{'url':'https://richmondva.legistar.com/Calendar.aspx',
                        'name':'City of Richmond'}
}

"Links by Year localities" #not a precise document sharing system, but localities with similar enough page structure that the same broad steps can apply to multiple websites, the common theme being starting with an agendas homepage where you first navigate to the page for the current year then check individual agendas. Each locality dictionary contains the CSS tags unique to each website to navigate to the equivalent content.
links_by_year_dictionary = {
    'Clarke BOS':{
        'url':'https://www.clarkecounty.gov/government/boards-commissions/board-of-supervisors/bos-agendas/-folder-1017',
        'name':'Clarke County Board of Supervisors',
        "agenda_link_tag":"a[target*='_blank'",
        'agenda_content_tag':"div[class*=textLayer"
    },

    'Clarke PC':{
        'url':"https://www.clarkecounty.gov/government/boards-commissions/planning-commission/pc-agendas/-folder-1031",
        'name':'Clarke County Planning Commission',
        "agenda_link_tag":"a[target*='_blank'",
        'agenda_content_tag':"div[class*=textLayer"
    },

     'New Kent PC':{
        "url":"https://www.newkent-va.us/843/Meeting-Agendas",
        'name':'New Kent County Planning Commission',
        "agenda_link_tag":"a[href*='Archive'",
        "agenda_content_tag":"div[class*=textLayer"
    },

    'Southampton BOS':{
        'url':"https://www.southamptoncounty.org/departments/board_of_supervisors/bos_meeting_agendas.php",
        'name':'Southampton County Board of Supervisors',
        "agenda_link_tag":"a[target*='_blank'",
        'agenda_content_tag':"section[class*='main-content-wrap'"
    },

    'Southampton PC':{
        'url':"https://www.southamptoncounty.org/departments/planning/archived_planning_agendas.php",
        'name':'Southampton County Planning Commission',
        "agenda_link_tag":"a[target*='_blank'",
        'agenda_content_tag':"section[class*='main-content-wrap'"
    }
}

"""MeetingsTable localities"""
meetingstable_dictionary = {
'Essex PC':{
        'url':"https://www.essex-virginia.org/meetings?date_filter%5Bvalue%5D%5Bmonth%5D=1&date_filter%5Bvalue%5D%5Bday%5D=1&date_filter%5Bvalue%5D%5Byear%5D=2023&date_filter_1%5Bvalue%5D%5Bmonth%5D=12&date_filter_1%5Bvalue%5D%5Bday%5D=31&date_filter_1%5Bvalue%5D%5Byear%5D=2023&field_microsite_tid=All&field_microsite_tid_1=28",
        'name':'Essex County Planning Commission',
        'meetings_tag':"div[class*='views-row'",
        'agenda_content_tag':"div[class*=textLayer"
    },

"Fluvanna PC":{
    'url':"https://www.fluvannacounty.org/meetings?field_microsite_tid_1=28",
    'name':"Fluvanna County Planning Commission",
    'meetings_tag':'tr',
    'agenda_content_tag':"div[class*=textLayer"},

"Fluvanna BOS":{
    'url':"https://www.fluvannacounty.org/meetings?field_microsite_tid_1=27",
    'name':"Fluvanna County Board of Supervisors",
    'meetings_tag':'tr',
    'agenda_content_tag':"div[class*=textLayer"},

"Northumberland PC":{
    'url':"https://www.co.northumberland.va.us/meetings?field_microsite_tid_1=28",
    'name':"Northumberland County",
    'meetings_tag':'tr',
    'agenda_content_tag':"div[class*=textLayer"}
}

"""NovusAGENDA localities"""
novusagenda_dictionary = {
"Isle of Wight PC":{
    'url':"https://isleofwight.novusagenda.com/agendapublic/meetingsgeneral.aspx?MeetingType=2",
    'name':"Isle of Wight County Planning Commission"},

"Isle of Wight BOS":{
    'url':"https://isleofwight.novusagenda.com/agendapublic/meetingsgeneral.aspx?MeetingType=1",
    'name':"Isle of Wight County Board of Supervisors"},

"New Kent BOS":{
    'url':"https://newkent.novusagenda.com/agendapublic/meetingsgeneral.aspx",
    'name':"New Kent County"}
}

"""OnBase localities"""
onbase_dictionary = {
    "Arlington County Board":{
        'url':"https://meetings.arlingtonva.us/CountyBoard",
        'name':"Arlington County Board"},
    
    "Arlington County PC":{
        'url':"https://meetings.arlingtonva.us/Planning",
        'name':"Arlington County Planning Commission"}
}

"php table localities"
php_table_dictionary = {
    'Amelia BOS':{
        'url':'https://www.ameliacova.com/departments/boards_and_commissions/agendas_and_minutes.php',
        'name':'Amelia County Board of Supervisors',
        'web_document':'Packet'},

    "Buckingham BOS":{
        'url':"https://www.buckinghamcountyva.org/administration/boards___commissions/board_of_supervisors/board_agenda_minutes_youtube.php",
        'name':"Buckingham County Board of Supervisors",
        'web_document':"Agenda"},

    "Buckingham PC":{
        'url':"https://www.buckinghamcountyva.org/administration/boards___commissions/planning_commission.php",
        'name':"Buckingham County Planning Commission",
        'web_document':'Agenda'},

    "Carroll County":{
        'url':"https://www.carrollcountyva.gov/government/board_of_supervisors/meeting_documentation.php",
        'name':"Carroll County Board of Supervisors",
        'web_document':'Agenda'}, #new link, confirm process still valid

    "Charlotte BOS":{
        'url':"https://www.charlottecountyva.gov/government/board_of_supervisors/agendas___minutes.php",
        'name':"Charlotte County Board of Supervisors",
        'web_document':'Agenda'},

    "Charlotte PC":{
        'url':"https://www.charlottecountyva.gov/departments/planning___zoning/agendas___minutes.php",
        'name':"Charlotte County Planning Commission",
        'web_document':'Agenda'}, 

    "Lunenburg BOS":{
        'url':"https://www.lunenburgva.gov/government/board_of_supervisors/agendas___minutes.php",
        'name':'Lunenburg County Board of Supervisors',
        'web_document':'Agenda'},

    'Lunenburg PC':{
        'url':"https://www.lunenburgva.gov/government/planning_commission/agendas___minutes.php",
        'name':'Lunenburg County Planning Commission',
        'web_document':'Agenda'
    },

    "Smyth BOS":{
        'url':"https://smythcounty.org/government/agendas___minutes_/board_of_supervisors_agendas___minutes.php",
        'name':"Smyth County Board of Supervisors",
        'web_document':'Agenda'},

    "Smyth PC":{
        'url':"https://smythcounty.org/government/agendas___minutes_/planning_commission_agendas___minutes.php",
        'name':"Smyth County Planning Commission",
        'web_document':'Agenda'},

    "South Boston CC":{
        "url":"https://www.southboston.com/departments/council/council_minutes_of_meetings.php",
        "name":"South Boston City Council",
        "web_document":"Agenda"}
}

"PrimeGov localities"
primegov_dictionary = {
    "Bedford":{
        'url':"https://bedfordcounty.primegov.com/public/portal",
        'name':"Bedford County"}
}

"Dictionaries for localities that need individual code"
locality_dictionary_single_use = {
    "Albemarle PC":{
        "url":"https://www.albemarle.org/government/community-development/boards-and-commissions/planning-commission/-toggle-next30days",
        "name":"Albemarle County Planning Commission",
        "content_tag":"div[class*=textLayer"
    },

    "Alleghany BOS":{
        "url":"https://www.co.alleghany.va.us/board-of-supervisors/agendas/",
        "name":"Alleghany County Board of Supervisors",
        "content_tag":"div[class*=textLayer"
    },

    "Amelia PC":{
        "url":"https://www.ameliacova.com/departments/boards_and_commissions/planning_commission.php#outer-116sub-117",
        "name":"Amelia County Planning Commission",
        'content_tag':'div[class*=textLayer'
    },

    "Bland":{
        "url":"https://www.blandcountyva.gov/page/agendas-and-minutes/",
        "name":"Bland County"
    },

    "Brunswick":{
        "url":"https://www.brunswickco.com/government/board_of_supervisors/agendas___minutes",
        "name":"Brunswick County",
        'content_tag':"div[class*=textLayer"
    },

    "Buchanan":{
        "url":"https://buchanancountyvirginia.gov/board-of-supervisors/",
        "name":"Buchanan County",
        "content_tag":"div[class*=textLayer"
    },

    "Buena Vista City Council":{
        "url":"https://www.buenavistava.org/city-services/government/city-council/council-agenda-minutes/",
        "name":"Buena Vista City Council"},

    "Clifton Forge":{
        "url":"https://cliftonforgeva.gov/council/council-agenda-and-minutes/",
        "name":"Town of Clifton Forge",
        "content_tag":"div[class*=textLayer"},

    "Covington":{
        "url":"https://covington.va.us/about-covington/agenda-and-minutes.html",
        "name":"Town of Covington"}, #new url, new site design, nothing useful posted yet

    "Craig":{
        "url":"https://craigcountyva.gov/government/board-of-supervisors/",
        "name":'Craig County Board of Supervisors'
    },

    "Fairfax BOS":{
        "url":"https://www.fairfaxcounty.gov/boardofsupervisors/",
        "name":"Fairfax County Board of Supervisors",
        "content_tag":"div[class*=textLayer"
    },

    "Fairfax PC":{
        "url":"https://www.fairfaxcounty.gov/planningcommission/meetingcalendar",
        "name":"Fairfax County Planning Commission",
        "content_tag":"div[class*=textLayer"
    },

    #'Floyd':{ #unworkable right now with the new website coding
    #    'url':"https://www.floydcova.gov/agendas-minutes",
    #    'name':'Floyd County'
    #},

    "Franklin":{
        "name":"City of Franklin",
        "url":"https://www.franklinva.com/government/city-council-agendas/",
        "content_tag":"div[class*=textLayer"},

    "Galax":{
        "name":"City of Galax",
        "url":"https://galaxva.com/2025-city-council-agendas/",
        "content_tag":"div[class*=textLayer"},

    #go back through functions for robust agenda content search method addition starting here
    "Giles":{
        "url":"https://virginiasmtnplayground.com/bos/",
        "name":"Giles County Board of Supervisors",
        "content_tag":"div[class*=textLayer"
    },

    "Henrico BOS":{
        "url":"https://henrico.us/supervisors/supervisors-agenda-o-gram/",
        "name":"Henrico County Board of Supervisors",
        "content_tag":"div[class*=textLayer"
    },

    "Henrico PC":{
        "url":"https://henrico.us/planning/meetings/",
        "name":"Henrico County Planning Commission",
        "content_tag":"div[class*=textLayer"
    },

    "Highland BOS":{
        "url":"https://www.highlandcova.org/node/666/agenda",
        "name":"Highland County Board of Supervisors",
        "content_tag":"div[class*=textLayer"
    },

    "Lee":{ #rewrite function!
        "url":"https://www.leecova.com/meeting-minutes",
        "name":"Lee County"
    },

    "Lexington":{
        "name":"City of Lexington Planning Commission",
        "url":"https://www.lexingtonva.gov/government/boards-and-commissions/planning-commission",
        "content_tag":"div[class*=textLayer"},

    "Loudoun":{
        "url":"https://lfportal.loudoun.gov/LFPortalInternet/Browse.aspx?startid=305808&row=1&dbid=0",
        "name":"Loudoun County Planning Commission"
    },

    "Nelson":{
        "url":"https://www.nelsoncounty-va.gov/events/list/",
        "name":"Nelson County"
    },

    "Norton":{
        "name":"City of Norton City Council",
        "url":"https://www.nortonva.gov/Archive.aspx?AMID=37",
        "content_tag":"div[class*=textLayer"},

    "Pittsylvania":{
        "url":"https://www.pittsylvaniacountyva.gov/government/agenda-center/-toggle-all",
        "name":"Pittsylvania County",
        "content_tag":"div[class*=textLayer"
    },

    "Prince Edward PC":{
        "url":"https://www.co.prince-edward.va.us/departments/planning-zoning/planning-commission-meetings",
        "name":"Prince Edward County Planning Commission",
        "content_tag":"div[class*=textLayer"
    },

    "Prince Edward BOS":{
        "url":"https://www.co.prince-edward.va.us/government/board-of-supervisors/board-meeting-agendas-and-meeting-minutes/-toggle-all",
        "name":"Prince Edward County Board of Supervisors",
        "content_tag":"div[class*=textLayer"
    },

    "Richmond":{
        "url":"https://co.richmond.va.us/board-of-supervisors-agenda-packets",
        "name":"Richmond County"
    },

    "Sussex":{
        "url":"https://www.sussexcountyva.gov/page/agendas-and-minutes/",
        "name":"Sussex County",
        "content_tag":"div[class*=textLayer"
    },

    "Virginia Beach CC":{
        "name":"Virginia Beach City Council",
        "url":"https://clerk.virginiabeach.gov/city-council",
        "content_tag":"div[class*=textLayer"},

    "Virginia Beach PC":{
        "name":"Virginia Beach Planning Commission",
        "url":"https://planning.virginiabeach.gov/boards-commissions/planning-commission",
        "content_tag":"div[class*=textLayer"},

    "Wythe":{
        "url":"http://www.wytheco.org/index.php/resources/public-notices",
        "name":"Wythe County Public Notices"
    },

    #"Wythe County Board of Supervisors":[wythe_county,"http://www.wytheco.org/index.php/resources/meeting-minutes/packages/bos-packages"],

    #"Wythe County Planning Commission":[wythe_county,"http://www.wytheco.org/index.php/resources/meeting-minutes/packages/planning-commission"],

}

locality_dictionary_multi_use = {

    "Bath BOS":{
        "name":"Bath County Board of Supervisors",
        "url":"https://www.bathcountyva.gov/public_information/minutes_audios/board_of_supervisors",
        "content_tag":"div[class*=textLayer"
    },

    "Bath PC":{
        "name":"Bath County Planning Commission",
        "url":"https://www.bathcountyva.gov/public_information/minutes_audios/planning_commission",
        "content_tag":"div[class*=textLayer"
    },

    "Bath BZA":{
        "name":"Bath County Board of Zoning Appeals",
        "url":"https://www.bathcountyva.gov/public_information/minutes_audios/board_of_zoning_appeals",
        "content_tag":"div[class*=textLayer"
    },

    "Greensville BOS":{
        "name":"Greensville County Board of Supervisors",
        "url":"https://www.greensvillecountyva.gov/boards___commissions/board_of_supervisors/agendas___minutes/board_of_supervisors.php",
        "content_tag":"div[class*=textLayer"}, #accordion thingy, similar to others
    
    "Greensville PC":{
        "name":"Greensville County Planning Commission",
        "url":"https://www.greensvillecountyva.gov/boards___commissions/board_of_supervisors/agendas___minutes/planning_commission.php",
        "content_tag":"div[class*=textLayer"},

    "King and Queen BOS":{
        "name":"King and Queen County Board of Supervisors",
        "url":"https://kingandqueenco.net/board-of-supervisors-meetings/",
        "content_tag":"div[class*=textLayer"}, #have seen similar county website structure

    "King and Queen PC":{
        "name":"King and Queen County Planning Commission",
        "url":"https://kingandqueenco.net/planning-commission-meetings/",
        "content_tag":"div[class*=textLayer"},

    "Manassas Park PC":{
        "name":"Manassas Park Planning Commission",
        "url":"https://www.manassasparkva.gov/government/governing_body/meetings_agendas___minutes/planning_commission_meeting_agendas.php",
        "content_tag":"div[class*=textLayer"},

    "Manassas Park GB":{
        "name":"Manassas Park Governing Body",
        "url":"https://www.manassasparkva.gov/government/governing_body/meetings_agendas___minutes/index.php",
        "content_tag":"div[class*=textLayer"}, #revise method

    "Nottoway BOS":{
        "name":"Nottoway County Board of Supervisors",
        "url":"https://nottoway.org/administration/boards___commissions/board_of_supervisors_(bos)/board_agendas_minutes.php",
        "content_tag":"div[class*=textLayer"},

    "Nottoway PC":{
        "name":"Nottoway County Planning Commission",
        "url":"https://nottoway.org/administration/boards___commissions/agenda_packets_minutes.php",
        "content_tag":"div[class*=textLayer"},

    "Staunton PC":{
        "name":"Staunton Planning Commission",
        "url":"https://www.ci.staunton.va.us/government/city-council-/board-commissions/agendas-minutes-for-boards-commissions/-selmt-1078",
        "content_tag":"div[class*=textLayer"},

    "Staunton CC":{
        "name":"Staunton City Council",
        "url":"https://www.ci.staunton.va.us/agendas-minutes",
        "content_tag":"div[class*=textLayer"},

    "Tazewell BOS":{
        "name":"Tazewell County Board of Supervisors",
        "url":"https://tazewellcountyva.org/government/boards-and-commissions/board-of-supervisors/",
        "content_tag":"div[class*=textLayer"},

    "Tazewell PC":{
        "name":"Tazewell County Planning Commission",
        "url":"https://tazewellcountyva.org/government/boards-and-commissions/planning-commission/",
        "content_tag":"div[class*=textLayer"},

    "Wesmoreland BOS":{
        "name":"Westmoreland County Board of Supervisors",
        "url":"https://www.westmoreland-county.org/bos",
        "content_tag":"div[class*=textLayer"},

    "Westmoreland PC":{
        "name":"Westmoreland County Planning Commission",
        "url":"https://www.westmoreland-county.org/pc",
        "content_tag":"div[class*=textLayer"}
}
