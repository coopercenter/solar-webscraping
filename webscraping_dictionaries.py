"Dictionaries for the localities that use the same type of document organization service"

"AgendaCenter localities" #REVIEW FOR INTEGRATION WITH THE LISTS
agendacenter_dictionary = {
    "Botetourt":{
        #new and horrible pop-up window that blocks my scraper (07/08: Seems to be gone now)
        'name':'Botetourt County',
        'url':"https://www.botetourtva.gov/AgendaCenter/Search/?term=&CIDs=3,8,6,&startDate=&endDate=&dateRange=&dateSelector=",
        "meeting_rows":"tr[class*=catAgendaRow",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Campbell":{ #went to a webpage rather than a pdf
        'name':"Campbell County",
        'url':"https://www.co.campbell.va.us/AgendaCenter/Search/?term=&CIDs=5,12,6,&startDate=&endDate=&dateRange",
        "meeting_rows":"tr[class*=catAgendaRow",
        'agenda_type':'webpage',
        'agenda_content':"div[id*='divInner'"},

    "Caroline":{
        'name':"Caroline County",
        'url':"https://co.caroline.va.us/AgendaCenter/Search/?term=&CIDs=2,3,4,&startDate=&endDate=&dateRange=&dateSelector=",
        "meeting_rows":"tr[class*=catAgendaRow",
        'agenda_type':'webpage',
        'agenda_content':"div[id*='divInner'"},

    "Charles City":{
        'name':'Charles City County',
        'url':'https://www.charlescityva.us/AgendaCenter/Search/?term=&CIDs=6,2,8,&startDate=&endDate=&dateRange=&dateSelector=',
        "meeting_rows":"tr[class*=catAgendaRow",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'
    },

    "Cumberland":{
        'name':"Cumberland County",
        'url':"https://www.cumberlandcounty.virginia.gov/AgendaCenter/Search/?term=&CIDs=2,4,3,&startDate=&endDate=&dateRange=&dateSelector=",
        "meeting_rows":"tr[class*=catAgendaRow",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Dinwiddie":{
        'name':"Dinwiddie County",
        'url':"https://www.dinwiddieva.us/AgendaCenter/Search/?term=&CIDs=2,3,4,1,&startDate=&endDate=&dateRange=&dateSelector=",
        "meeting_rows":"tr[class*=catAgendaRow",
        'agenda_type':'webpage',
        'agenda_content':"div[id*='divInner'"},
    
    'Essex PC':{
        'url':"https://www.essexva.gov/AgendaCenter/Search/?term=&CIDs=3,7,&startDate=&endDate=&dateRange=&dateSelector=",
        'name':'Essex County Planning Commission',
        'meeting_rows':"tr[class*=catAgendaRow",
        "agenda_type":"pdf",
        'agenda_content':"div[class*=textLayer"
    },

    "Franklin":{
        'name':"Franklin County",
        'url':"https://www.franklincountyva.gov/AgendaCenter/Search/?term=&CIDs=7,3,4,&startDate=&endDate=&dateRange=&dateSelector=",
        "meeting_rows":"tr[class*=catAgendaRow",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Halifax":{
        'name':"Halifax County",
        'url':"https://www.halifaxcountyva.gov/AgendaCenter/Search/?term=&CIDs=2,3,4,&startDate=&endDate=&dateRange=&dateSelector=",
        "meeting_rows":"tr[class*=catAgendaRow",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Henry":{
        'name':"Henry County",
        'url':"https://www.henrycountyva.gov/AgendaCenter/Search/?term=&CIDs=3,9,8,&startDate=&endDate=&dateRange=&dateSelector=",
        "meeting_rows":"tr[class*=catAgendaRow",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "King George":{
        'name':"King George County",
        'url':"https://www.kinggeorgecountyva.gov/AgendaCenter/Search/?term=&CIDs=2,3,5,&startDate=&endDate=&dateRange=&dateSe",
        "meeting_rows":"tr[class*=catAgendaRow",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Madison":{
        'name':"Madison County",
        'url':"https://www.madisonco.virginia.gov/AgendaCenter/Search/?term=&CIDs=3,5,6,11,&startDate=&endDate=&dateRange=&dateSelector=",
        "meeting_rows":"tr[class*=catAgendaRow",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'}, 

    "Mecklenburg":{
        'name':"Mecklenburg County",
        'url':"https://www.mecklenburgva.com/AgendaCenter",
        "meeting_rows":"tr[class*=catAgendaRow",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Middlesex":{
        'name':"Middlesex County",
        'url':"https://www.co.middlesex.va.us/AgendaCenter",
        "meeting_rows":"tr[class*=catAgendaRow",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Page":{
        'name':"Page County",
        'url':"https://www.pagecounty.virginia.gov/AgendaCenter/Search/?term=&CIDs=2,7,9,5,&startDate=&endDate=&dateRange=&dateSelector=",
        "meeting_rows":"tr[class*=catAgendaRow",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

   "Patrick":{
       'name':"Patrick County",
       'url':"https://www.co.patrick.va.us/AgendaCenter/Search/?term=&CIDs=3,4,&startDate=&endDate=&dateRange=&dateSelector=",
       "meeting_rows":"tr[class*=catAgendaRow",
       'agenda_type':'pdf',
       'agenda_content':'div[class*=textLayer'},
    
    "Powhatan":{
        'name':"Powhatan County",
        'url':"https://www.powhatanva.gov/AgendaCenter/Search/?term=&CIDs=2,10,7,&startDate=&endDate=&dateRange=&dateSelector=",
        "meeting_rows":"tr[class*=catAgendaRow",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

   "Rockbridge":{
       'name':"Rockbridge County",
       'url':"https://va-rockbridgecounty.civicplus.com/AgendaCenter/Search/?term=&CIDs=25,3,26,6,23,&startDate=&endDate=&dateRange=&dateSelector=",
       "meeting_rows":"tr[class*=catAgendaRow",
       'agenda_type':'pdf',
       'agenda_content':'div[class*=textLayer'},

    "Rockingham":{
        'name':"Rockingham County",
        'url':"https://www.rockinghamcountyva.gov/AgendaCenter",
        "meeting_rows":"tr[class*=catAgendaRow",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Russell":{
        'name':"Russell County",
        'url':"https://va-russellcounty.civicplus.com/AgendaCenter/Search/?term=&CIDs=5,3,&startDate=&endDate=&dateRange=&dateSelector=",
        "meeting_rows":"tr[class*=catAgendaRow",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Shenandoah":{
        'name':"Shenandoah County",
        'url':"https://shenandoahcountyva.us/AgendaCenter/Search/?term=&CIDs=15,4,11,12,3,&startDate=&endDate=&dateRange=&dateSelector=",
        "meeting_rows":"tr[class*=catAgendaRow",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Wise":{
        'name':"Wise County",
        'url':"https://www.wisecounty.org/AgendaCenter/Search/?term=&CIDs=3,6,4,&startDate=&endDate=&dateRange=&dateSelector=",
        "meeting_rows":"tr[class*=catAgendaRow",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "York":{
        'name':"York County",
        'url':"https://www.yorkcounty.gov/AgendaCenter/Search/?term=&CIDs=4,3,&startDate=&endDate=&dateRange=&dateSelector=",
        "meeting_rows":"tr[class*=catAgendaRow",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Bedford":{
        'name':"Town of Bedford",
        'url':"https://www.bedfordva.gov/AgendaCenter/Search/?term=&CIDs=3,2,&startDate=&endDate=&dateRange=&dateSelector=",
        "meeting_rows":"tr[class*=catAgendaRow",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Colonial Heights BZA PC":{
        'name':"City of Colonial Heights",
        'url':"https://www.colonialheightsva.gov/AgendaCenter/Search/?term=&CIDs=4,6,&startDate=&endDate=&dateRange=&dateSelector=",
        "meeting_rows":"tr[class*=catAgendaRow",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Colonial Heights CC":{
        'name':"City of Colonial Heights",
        'url':"https://www.colonialheightsva.gov/AgendaCenter/Search/?term=&CIDs=1,&startDate=&endDate=&dateRange=&dateSelector=",
        "meeting_rows":"tr[class*=catAgendaRow",
        'agenda_type':'webpage',
        'agenda_content':"div[id*='divInner'"},

    "Emporia":{
        'name':"City of Emporia",
        'url':"https://www.ci.emporia.va.us/AgendaCenter/Search/?term=&CIDs=2,6,8,&startDate=&endDate=&dateRange=&dateSelector=",
        "meeting_rows":"tr[class*=catAgendaRow",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Fredericksburg":{
        'name':"City of Fredericksburg",
        'url':"https://www.fredericksburgva.gov/AgendaCenter/Search/?term=&CIDs=6,1,15,9,&startDate=&endDate=&dateRange=&dateSelector=",
        "meeting_rows":"tr[class*=catAgendaRow",
        'agenda_type':'webpage',
        'agenda_content':"div[id*='divInner'"},

    "Hampton":{
        'name':"Hampton City",
        'url':"https://www.hampton.gov/AgendaCenter/Search/?term=&CIDs=2,1,6,7,&startDate=&endDate=&dateRange=&dateSelector=",
        "meeting_rows":"tr[class*=catAgendaRow",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Hopewell":{
        'name':"City of Hopewell",
        'url':"https://hopewellva.gov/AgendaCenter/Search/?term=&CIDs=2,5,&startDate=&endDate=&dateRange=&dateSelector=",
        "meeting_rows":"tr[class*=catAgendaRow",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Norfolk CC":{
        'name':"City of Norfolk",
        'url':"https://www.norfolk.gov/AgendaCenter/Search/?term=&CIDs=25,13,&startDate=&endDate=&dateRange=&dateSelector=",
        "meeting_rows":"tr[class*=catAgendaRow",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Petersburg":{
        'name':"City of Petersburg",
        'url':"http://www.petersburg-va.org/AgendaCenter/Search/?term=&CIDs=9,1,3,&startDate=&endDate=&dateRange=&dateSelector=",
        "meeting_rows":"tr[class*=catAgendaRow",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Portsmouth":{
        'name':"City of Portsmouth",
        'url':"https://www.portsmouthva.gov/AgendaCenter/Search/?term=&CIDs=11,7,4,&startDate=&endDate=&dateRange=&dateSelector=",
        "meeting_rows":"tr[class*=catAgendaRow",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Radford":{
        'name':"City of Radford",
        'url':"https://www.radfordva.gov/AgendaCenter/Search/?term=&CIDs=2,4,&startDate=&endDate=&dateRange=&dateSelector=",
        "meeting_rows":"tr[class*=catAgendaRow",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Suffolk":{
        'name':"City of Suffolk",
        'url':"https://www.suffolkva.us/AgendaCenter/Search/?term=&CIDs=20,21,11,4,12,3,&startDate=&endDate=&dateRange=&dateSelector=",
        "meeting_rows":"tr[class*=catAgendaRow",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Waynesboro BZA PC":{
        'name':"City of Waynesboro",
        'url':"https://www.waynesboro.va.us/AgendaCenter/Search/?term=&CIDs=5,4,&startDate=&endDate=&dateRange=&dateSelector=",
        "meeting_rows":"tr[class*=catAgendaRow",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Waynesboro CC":{
        'name':"City of Waynesboro",
        'url':"https://www.waynesboro.va.us/AgendaCenter/Search/?term=&CIDs=1,&startDate=&endDate=&dateRange=&dateSelector=",
        "meeting_rows":"tr[class*=catAgendaRow",
        'agenda_type':'webpage',
        'agenda_content':"div[id*='divInner'"}
    }

agendacenter2_dictionary = {
    "Poquoson":{
       'name':"City of Poquoson",
       'url':"https://www.ci.poquoson.va.us/AgendaCenter",
       "meeting_rows":"tr[class*=catAgendaRow",
       'agenda_type':'pdf',
       'agenda_content':'div[class*=textLayer'},

    "Grayson":{
        'name':'Grayson County Planning Commission',
        'url':"https://www.graysoncountyva.gov/AgendaCenter/Search/?term=&CIDs=3,&startDate=&endDate=&dateRange=&dateSelector=",
        "meeting_rows":"tr[class*=catAgendaRow",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

    "Grayson BOS":{
        'name':'Grayson County Board of Supervisors',
        'url':"https://www.graysoncountyva.gov/AgendaCenter/Search/?term=&CIDs=5,2,&startDate=&endDate=&dateRange=&dateSelector=",
        "meeting_rows":"tr[class*=catAgendaRow",
        'agenda_type':'pdf',
        'agenda_content':'div[class*=textLayer'},

}

"""BoardDocs localities"""
boarddocs_dictionary = {
    'Accomack':{
        'url':"https://go.boarddocs.com/va/coa/Board.nsf/Public",
        'name':"Accomack County",
        'featured':True,
        'second_page':False},

    "Culpeper":{
        'url':"https://go.boarddocs.com/va/ccva/Board.nsf/Public",
        'name':"Culpeper County",
        'featured':True,
        'second_page':False},

    "Essex":{ #no Featured tab, code closes year I want to scrape instead
        'url':"https://go.boarddocs.com/va/essexco/Board.nsf/Public",
        'name':"Essex County",
        'featured':False,
        'second_page':False},

    "Northumberland":{
        'url':"https://go.boarddocs.com/va/nuc/Board.nsf/vpublic?open",
        'name':"Northumberland County",
        'featured':True,
        'second_page':False},

    "Prince George":{
        'url':"https://go.boarddocs.com/va/princegeorge/Board.nsf/Public",
        'name':"Prince George County",
        'featured':True,
        'second_page':False},

    "Pulaski":{ #no Featured tab, code closes year I want instead
        'url':"https://go.boarddocs.com/va/copva/Board.nsf/Public#",
        'name':"Pulaski County",
        'featured':False,
        'second_page':True},

    "Rappahannock":{
        'url':"https://go.boarddocs.com/va/corva/Board.nsf/Public",
        'name':"Rappahannock County",
        'featured':True,
        'second_page':True},

    "Rockbridge":{
        'url':"https://go.boarddocs.com/va/rcva/Board.nsf/Public",
        'name':"Rockbridge County Board of Supervisors",
        'featured':False,
        'second_page':False},
}

"""Calendar View localities"""
calendar_view_dictionary = {
    "Nelson":{
        "url":"https://www.nelsoncounty-va.gov/events/month/",
        "name":"Nelson County",
        "agenda_type":"webpage",
        "meetings_tag":"a[class*='event-title-link'",
        "agenda_tag": None,
        "content_tag":"div[class*='fusion-text'"
    },

    "Sussex":{
        "url":"https://sussexcountyva.gov/events/month/",
        "name":"Sussex County",
        "agenda_type":"pdf",
        "meetings_tag": "a[class*='event-title-link'",
        "agenda_tag":"a[href*='.pdf'",
        "content_tag":"div[class*=textLayer"
    }
}

"CivicClerk localities"
civicclerk_dictionary = {
#"Amelia":{
    #'url':"https://ameliacova.portal.civicclerk.com/?category_id=26,28", #move BOS to PHP table, new code for PC
    #'name':"Amelia County",
    #'agenda_type':'pdf',
    #'agenda_content':'div[class*=textLayer'},

"Amherst":{
    'url':"https://amherstcova.portal.civicclerk.com/?category_id=27,29,33,32",
    'name':"Amherst County",
    "meeting_rows":"li[class*='MuiListItem-container'",
    'agenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'},

"Appomattox":{
    'url':"https://appomattoxcova.portal.civicclerk.com/",
    'name':"Appomattox County",
    "meeting_rows":"li[class*='MuiListItem-container'",
    'agenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'},

"Augusta":{
    'url':"https://augustacova.portal.civicclerk.com/",
    'name':"Augusta County",
    "meeting_rows":"li[class*='MuiListItem-container'",
    'agenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'},

#More updates at the AgendaCenter site, table this entry until there is a complete switch
"Charles City":{
    'url':"https://charlescitycova.portal.civicclerk.com/",
    'name':"Charles City County",
    "meeting_rows":"li[class*='MuiListItem-container'",
    "meeting_type":"pdf",
    "agenda_content":'div[class*=textLayer'},

"Charlottesville":{
    'url':"https://charlottesvilleva.portal.civicclerk.com/",
    'name':"City of Charlottesville",
    "meeting_rows":"li[class*='MuiListItem-container'",
    'agenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'},

"Chesterfield":{
    'url':"https://chesterfieldcova.portal.civicclerk.com/",
    'name':"Chesterfield County",
    "meeting_rows":"li[class*='MuiListItem-container'",
    'agenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'},

"Danville":{
    'url':"https://danvilleva.portal.civicclerk.com/",
    'name':"City of Danville",
    "meeting_rows":"li[class*='MuiListItem-container'",
    'agenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'},

"Greene":{
    'url':"https://greenecova.portal.civicclerk.com/", #historical archives at https://gcva.granicus.com/ViewPublisher.php?view_id=1
    'name':"Greene County",
    "meeting_rows":"li[class*='MuiListItem-container'",
    'agenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'},

"Hanover":{
    'url':"https://hanovercova.portal.civicclerk.com/?category_id=26,27",
    'name':"Hanover County",
    "meeting_rows":"li[class*='MuiListItem-container'",
    'agenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'},

"Isle of Wight":{
    "url":"https://isleofwightcova.portal.civicclerk.com/",
    "name":"Isle of Wight County",
    "meeting_rows":"li[class*='MuiListItem-container'",
    'agenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'

},

"James City":{
    'url':"https://jamescitycova.portal.civicclerk.com/",
    'name':"James City County",
    "meeting_rows":"li[class*='MuiListItem-container'",
    'agenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'},

"King William":{
    'url':"https://kingwilliamcova.portal.civicclerk.com/",
    'name':"King William County",
    "meeting_rows":"li[class*='MuiListItem-container'",
    'agenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'},

"Louisa":{
    'url':"https://louisacova.portal.civicclerk.com/",
    'name':"Louisa County",
    "meeting_rows":"li[class*='MuiListItem-container'",
    'agenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'},

"Lynchburg":{
    'url':"https://lynchburgva.portal.civicclerk.com/",
    'name':"City of Lynchburg",
    "meeting_rows":"li[class*='MuiListItem-container'",
    'agenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'},

"Martinsville":{
    "url":"https://martinsvilleva.portal.civicclerk.com/",
    "name":"City of Martinsville",
    "meeting_rows":"li[class*='MuiListItem-container'",
    'agenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'
},

"Mathews":{
    'url':"https://mathewscova.portal.civicclerk.com/",
    'name':"Mathews County",
    "meeting_rows":"li[class*='MuiListItem-container'",
    'agenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'},

"Orange":{
    'url':"https://orangecova.portal.civicclerk.com/",
    'name':"Orange County",
    "meeting_rows":"li[class*='MuiListItem-container'",
    'agenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'},

"Petersburg CC":{
    'url':"https://petersburgva.portal.civicclerk.com/",
    'name':"City of Petersburg",
    "meeting_rows":"li[class*='MuiListItem-container'",
    'agenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'},

"Pittsylvania":{
        "url":"https://pittsylvaniacova.portal.civicclerk.com/",
        "name":"Pittsylvania County",
        "meeting_rows":"li[class*='MuiListItem-container'",
        "agenda_type":"pdf",
        "agenda_content":"div[class*=textLayer"
    },

"Roanoke":{
    'url':"https://roanokeva.portal.civicclerk.com/",
    'name':"City of Roanoke",
    "meeting_rows":"li[class*='MuiListItem-container'",
    'agenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'},

'Salem':{
    'url':'https://salemva.portal.civicclerk.com/',
    'name':'City of Salem',
    "meeting_rows":"li[class*='MuiListItem-container'",
    'agenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'},

"Scott":{
    'url':"https://scottcova.portal.civicclerk.com/",
    'name':"Scott County",
    "meeting_rows":"li[class*='MuiListItem-container'",
    'agenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'},

"Spotsylvania":{
    'url':"https://spotsylvaniacova.portal.civicclerk.com/",
    'name':"Spotsylvania County",
    "meeting_rows":"li[class*='MuiListItem-container'",
    'agenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'},

"Stafford":{
    'url':"https://staffordcova.portal.civicclerk.com/?category_id=26,31",
    'name':"Stafford County",
    "meeting_rows":"li[class*='MuiListItem-container'",
    'agenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'},

"Surry":{
    'url':"https://surrycova.portal.civicclerk.com/",
    'name':"Surry County",
    "meeting_rows":"li[class*='MuiListItem-container'",
    'aagenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'},

"Warren":{
    'url':"https://warrencountyva.portal.civicclerk.com/?category_id=26,27",
    'name':"Warren County",
    "meeting_rows":"li[class*='MuiListItem-container'",
    'agenda_type':'pdf',
    'agenda_content':'div[class*=textLayer'},

"Westmoreland":{
    "url":"https://westmorelandcova.portal.civicclerk.com/",
    "name":"Westmoreland County",
    "meeting_rows":"li[class*='MuiListItem-container'",
    "agenda_type":"pdf",
    'agenda_content':'div[class*=textLayer'
}
}

"""CivicWeb localities"""
civicweb_dictionary = {
"Lancaster":{
    'url':"https://lancova.civicweb.net/Portal/MeetingTypeList.aspx",
    'name':"Lancaster County",
    'meetings_tag':"a[class*='list-link'",
    "content_tag":"html"},

"Lexington":{
    'url':"https://lexingtonva.civicweb.net/Portal/MeetingTypeList.aspx",
    'name':"City of Lexington",
    'meetings_tag':"a[class*='list-link'",
    "content_tag":"html"},

"Montgomery":{
    "url":"https://montva.community.highbond.com/Portal/MeetingTypeList.aspx",
    "name":"Montgomery County",
    "meetings_tag":"a[class*='list-link'",
    "content_tag":"html"
},

"Northampton":{
    "url":"https://co-northampton-va.community.highbond.com/Portal/MeetingTypeList.aspx",
    "name":"Northampton County",
    "meetings_tag":"a[class*='list-link'",
    "content_tag":"html"

},

"Newport News":{
    'url':"https://nngov.civicweb.net/Portal/MeetingTypeList.aspx",
    'name':"City of Newport News",
    'meetings_tag':"a[class*='list-link'",
    "content_tag":"html"},

'Williamsburg':{
    'url':'https://williamsburg.civicweb.net/Portal/Default.aspx',
    'name':'City of Williamsburg',
    'meetings_tag':"a[class*='list-link'",
    "content_tag":"html"
},

"Winchester":{
    'url':"https://winchesterva.civicweb.net/Portal/MeetingTypeList.aspx",
    'name':"City of Winchester",
    'meetings_tag':"a[class*='list-link'",
    "content_tag":"html"}
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

"Folding Year dictionaries" #broad term covering the different websites where the landing page for meeting documents is an accordion-folding folder style organized by year
folding_year_dictionary = {
    "Clifton Forge":{
        "url":"https://cliftonforgeva.gov/council/council-agenda-and-minutes/",
        "name":"Town of Clifton Forge",
        "archive_type":"closed",
        "years_tag":"h3[class*='de-accordion-trigger-heading'",
        "agenda_subfolder":False,
        "agenda_folder_tag":None,
        "month_subfolder":False,
        "months_tag":None,
        "meetings_tag":"a[href*='.pdf'",
        "content_tag":"div[class*=textLayer"},

    "Franklin City":{ #documents are downloads, adjust folding year code and dictionaries accordingly
        "url":"https://www.franklinva.gov/government/agendas_minutes.php",
        "name":"City of Franklin",
        "archive_type":"closed",
        "years_tag":"h3[class*='docs-toggle'",
        "agenda_subfolder":False,
        "agenda_folder_tag":None,
        "month_subfolder":True,
        "months_tag":"div[class*='inner-cat cat'",
        "meetings_tag":"a[href*='.pdf",
        "content_tag":"div[class*=textLayer"
    },

    "Greensville BOS":{
        "name":"Greensville County Board of Supervisors",
        "url":"https://www.greensvillecountyva.gov/boards___commissions/board_of_supervisors/agendas___minutes/board_of_supervisors.php",
        "archive_type":"closed",
        "years_tag":"h3[class*='docs-toggle'",
        "agenda_subfolder":True,
        "agenda_folder_tag":"h4[class*='docs-toggle'",
        "month_subfolder":False,
        "months_tag":None,
        "meetings_tag":"a[href*='.pdf'",
        "content_tag":"div[class*=textLayer"},
    
    "Greensville PC":{
        "name":"Greensville County Planning Commission",
        "url":"https://www.greensvillecountyva.gov/boards___commissions/board_of_supervisors/agendas___minutes/planning_commission.php",
        "archive_type":"closed",
        "years_tag":"h3[class*='docs-toggle'",
        "agenda_subfolder":True,
        "agenda_folder_tag":"h4[class*='docs-toggle'",
        "month_subfolder":False,
        "months_tag":None,
        "meetings_tag":"a[href*='.pdf'",
        "content_tag":"div[class*=textLayer"},

    "Prince Edward PC":{ #basically folding year, but test method
        "url":"https://www.co.prince-edward.va.us/Departments/Community-Development/Planning-Zoning/Planning-Commission-Meetings",
        "name":"Prince Edward County Planning Commission",
        "archive_type":"closed",
        "years_tag":"div[class*='accordion-item-header",
        "agenda_subfolder":False,
        "agenda_folder_tag":None,
        "month_subfolder":False,
        "months_tag":None,
        "meetings_tag":"a[href*='.pdf'",
        "content_tag":"div[class*=textLayer"
    },

    "Prince Edward BOS":{ #basically folding year
        "url":"https://www.co.prince-edward.va.us/Government/Board-of-Supervisors/Board-Meeting-Agendas-and-Meeting-Minutes",
        "name":"Prince Edward County Board of Supervisors",
        "archive_type":"closed",
        "years_tag":"div[class*='accordion-item-header",
        "agenda_subfolder":False,
        "agenda_folder_tag":None,
        "month_subfolder":False,
        "months_tag":None,
        "meetings_tag":"a[href*='.pdf'",
        "content_tag":"div[class*=textLayer"
    },

    
}

"""Folding Year Alternative Format"""
folding_year_v2_dictionary = {
    "Bland":{
        "url":"https://www.blandcountyva.gov/government/board_of_supervisors/agendas_and_minutes.php",
        "name":"Bland County",
        'archive_type':"closed",
        "years_tag":"h3[class*='docs-toggle'",
        "row_tag":"tr",
        "document_tag":"a[href*='.pdf'",
        "content_tag":"div[class*=textLayer"
    },

    "Virginia Beach PC":{
        "name":"Virginia Beach Planning Commission",
        "url":"https://planning.virginiabeach.gov/boards-commissions/planning-commission",
        "archive_type":"closed",
        "years_tag":"li[class*='accordion__item'",
        "row_tag":"li",
        "document_tag":"a[href*='-Agenda-",
        "content_tag":"div[class*=textLayer"
        },

     "Manassas Park PC":{
        "name":"Manassas Park Planning Commission",
        "url":"https://www.manassasparkva.gov/government/governing_body/meetings_agendas___minutes/planning_commission_meeting_agendas.php",
        "archive_type":"closed",
        "years_tag":"div[class*='agenda_heading'",
        "row_tag":"tr",
        "document_tag":"a[href*='Agenda'",
        "content_tag":"div[class*=textLayer"},

    "Manassas Park GB":{
        "name":"Manassas Park Governing Body",
        "url":"https://www.manassasparkva.gov/government/governing_body/meetings_agendas___minutes/index.php",
        "archive_type":"closed",
        "years_tag":"div[class*='agenda_heading'",
        "row_tag":"tr",
        "document_tag":"a[href*='Agenda'",
        "content_tag":"div[class*=textLayer"},

    "Nottoway BOS":{
        "name":"Nottoway County Board of Supervisors",
        "url":"https://nottoway.org/administration/boards___commissions/board_of_supervisors_(bos)/board_agendas_minutes.php",
        "archive_type":"closed",
        "years_tag":"h3[class*='agenda-toggle'",
        "row_tag":"tr",
        "document_tag":"a[href*='.pdf'",
        "content_tag":"div[class*=textLayer"},

    "Nottoway PC":{
        "name":"Nottoway County Planning Commission",
        "url":"https://nottoway.org/administration/boards___commissions/agenda_packets_minutes.php",
        "archive_type":"closed",
        "years_tag":"h3[class*='agenda-toggle'",
        "row_tag":"tr",
        "document_tag":"a[href*=.pdf",
        "content_tag":"div[class*=textLayer"},
}

"Granicus localities" #REVIEW FOR INTEGRATION WITH THE SPLIT LISTS
granicus_dictionary = {
"Fauquier":{
    'url':"https://fauquier-va.granicus.com/ViewPublisher.php?view_id=3",
    'name':"Fauquier County",
    "archive_type":"closed",
    "archive_tag":"div[class*='CollapsiblePanelClosed'",
    "meeting_rows":"tr",
    "agenda_type":"pdf",
    "agendas_tag":"a[href*='AgendaViewer.php'",
    "content_tag":"div[class*=textLayer"},

"Frederick":{
    'url':"https://fcva.granicus.com/ViewPublisher.php?view_id=1",
    'name':"Frederick County",
    "archive_type":"closed",
    "archive_tag":"div[class*='CollapsiblePanelClosed'",
    "meeting_rows":"tr",
    "agenda_type":"pdf",
    "agendas_tag":"a[href*='AgendaViewer.php'",
    "content_tag":"div[class*=textLayer"},

"Henrico PC/BZA":{
        "url":"https://henricocountyva.new.swagit.com/views/166/",
        "name":"Henrico County Planning Commission/Board of Zoning Appeals",
        "archive_type":"open",
        "archive_tag":None,
        "meeting_rows":"tr",
        "agenda_type":"pdf",
        "agendas_tag":"a[href*='/agenda'",
        "content_tag":"div[class*=textLayer"
    },

"Prince William BOS":{
    'url':"https://pwcgov.granicus.com/ViewPublisher.php?view_id=23",
    'name':"Prince William County Board of Supervisors",
    "archive_type":"open",
    "archive_tag":None,
    "meeting_rows":"tr",
    "agenda_type":"pdf",
    "agendas_tag":"a[href*='AgendaViewer.php'",
    "content_tag":"div[class*=textLayer"},

"Prince William PC":{
    'url':"https://pwcgov.granicus.com/ViewPublisher.php?view_id=12",
    'name':' Prince William County Planning Commission',
    "archive_type":"open",
    "archive_tag":None,
    "meeting_rows":"tr",
    "agenda_type":"pdf",
    "agendas_tag":"a[href*='AgendaViewer.php'",
    "content_tag":"div[class*=textLayer"},

"Washington":{
    'url':"https://www.washcova.com/PUBLIC-MEETINGS/",
    'name':"Washington County",
    "archive_type":"closed",
    "archive_tag":"div[class*='CollapsiblePanelClosed'",
    "meeting_rows":"tr[class*=listingRow",
    "agenda_type":"pdf",
    "agendas_tag":"a[href*='AgendaViewer.php'",
    "content_tag":"div[class*=textLayer"},

"Alexandria":{
    'url':"https://alexandria.granicus.com/ViewPublisher.php?view_id=57",
    'name':"City of Alexandria",
    "archive_type":"open",
    "archive_tag":None,
    "meeting_rows":"tr",
    "agenda_type":"pdf",
    "agendas_tag":"a[href*='AgendaViewer.php'",
    "content_tag":"div[class*=textLayer"},

"Bristol":{
    'url':"https://bristolva.granicus.com/ViewPublisher.php?view_id=1",
    'name':"City of Bristol",
    "archive_type":"closed",
    "archive_tag":"div[class*='CollapsiblePanelClosed'",
    "meeting_rows":"tr",
    "agenda_type":"pdf",
    "agendas_tag":"a[href*='AgendaViewer.php'",
    "content_tag":"div[class*=textLayer"},

"Chesapeake CC":{
    'url':"https://chesapeake.granicus.com/ViewPublisher.php?view_id=29",
    'name':"City of Chesapeake",
    "archive_type":"open",
    "archive_tag":None,
    "meeting_rows":"tr",
    "agenda_type":"pdf",
    "agendas_tag":"a[href*='AgendaViewer.php'",
    "content_tag":"div[class*=textLayer"},

"Chesapeake PC":{
    'url':"https://chesapeake.granicus.com/ViewPublisher.php?view_id=35",
    'name':"City of Chesapeake",
    "archive_type":"none",
    "archive_tag":None,
    "meeting_rows":"tr",
    "agenda_type":"pdf",
    "agendas_tag":"a[href*='AgendaViewer.php'",
    "content_tag":"div[class*=textLayer"},

"Fairfax":{
    'url':"https://fairfax.granicus.com/ViewPublisher.php?view_id=11",
    'name':"City of Fairfax",
    "archive_type":"open",
    "archive_tag":None,
    "meeting_rows":"tr",
    "agenda_type":"webpage",
    "agendas_tag":"a[href*='AgendaViewer.php'",
    "content_tag":"body"},

"Falls Church":{
    'url':"https://fallschurch-va.granicus.com/ViewPublisher.php?view_id=2",
    'name':"City of Falls Church",
    "archive_type":"closed",
    "archive_tag":"h3[class*='ui-accordion-header'",
    "meeting_rows":"tr",
    "agenda_type":"webpage",
    "agendas_tag":"a[href*='AgendaViewer.php'",
    "content_tag":"tr"},

"Manassas":{
    'url':"https://manassascity.granicus.com/ViewPublisher.php?view_id=1",
    'name':"Manassas City",
    "archive_type":"open",
    "archive_tag":None,
    "meeting_rows":"tr",
    "agenda_type":"pdf",
    "agendas_tag":"a[href*='AgendaViewer.php'",
    "content_tag":"div[class*=textLayer"},

"New Kent BOS":{
    'url':"https://newkentcounty.granicus.com/ViewPublisher.php?view_id=1", 
    'name':"New Kent County Board of Supervisors",
    "archive_type":"open",
    "archive_tag":None,
    "meeting_rows":"tr[class*=listingRow",
    "agenda_type":"pdf",
    "agendas_tag":"a[href*='AgendaViewer.php'",
    "content_tag":"div[class*=textLayer"
    }
}

"""Granicus version 2 localities""" #REVIEW FOR INTEGRATION WITH THE SPLIT LISTS
granicus_2_dictionary = {
"Goochland":{
    'url':"https://goochlandcountyva.iqm2.com/Citizens/Default.aspx",
    'name':"Goochland County",
    "agenda_type":"webpage",
    "content_tag":"tr"},

"Norfolk Planning Commission":{
    'url':"https://norfolkcityva.iqm2.com/Citizens/Board/1018-Planning-Commission",
    'name':"City of Norfolk Planning Commission",
    "agenda_type":"webpage",
    "content_tag":"tr"},

"Roanoke":{
    'url':'https://roanokecountyva.iqm2.com/Citizens/default.aspx', #current agenda link posted here https://www.roanokecountyva.gov/287/Agendas-Minutes
    'name':"Roanoke County",
    "agenda_type":"pdf",
    "content_tag":"div[class*=textLayer"}
}

"LaserFiche localities"
laserfiche_dictionary = {
    "Loudoun BOS":{
        'url':"https://www.loudoun.gov/3426/Board-of-Supervisors-Meetings-Packets",
        'name':"Loudoun County Board of Supervisors"}
}

"Legistar localities" #REVIEW FOR INTEGRATION WITH THE SPLIT LISTS
legistar_dictionary = {
    "Albemarle":{
        'url':"https://albemarle.legistar.com/Calendar.aspx",
        'name':"Albemarle County",
        "ccontent_tag":'tr[id*=ctl00'},

    "Hampton CC":{
        'url':"https://hampton.legistar.com/Calendar.aspx",
        'name':"Hampton City",
        "content_tag":'tr[id*=ctl00'}, 

    "City of Harrisonburg":{
        'url':"https://harrisonburg-va.legistar.com/Calendar.aspx",
        'name':"City of Harrisonburg",
        "content_tag":'tr[id*=ctl00'},

    'City of Richmond':{'url':'https://richmondva.legistar.com/Calendar.aspx',
                        'name':'City of Richmond',
                        "content_tag":'tr[id*=ctl00'}
}

"Links by Year localities" #not a precise document sharing system, but localities with similar enough page structure that the same broad steps can apply to multiple websites, the common theme being starting with an agendas homepage where you first navigate to the page for the current year then check individual agendas. Each locality dictionary contains the CSS tags unique to each website to navigate to the equivalent content.
links_by_year_dictionary = {
    'Clarke BOS':{
        'url':'https://www.clarkecounty.gov/government/boards-commissions/board-of-supervisors/bos-agendas/-folder-1017',
        'name':'Clarke County Board of Supervisors',
        "year_list_tag":"a[href*='agendas'",
        "agenda_link_tag":"a[target*='_blank'",
        "agenda_type":"pdf",
        'agenda_content_tag':"div[class*=textLayer"
    },

    'Clarke PC':{
        'url':"https://www.clarkecounty.gov/government/boards-commissions/planning-commission/pc-agendas/-folder-1031",
        'name':'Clarke County Planning Commission',
        "year_list_tag":"a[href*='agendas'",
        "agenda_link_tag":"a[target*='_blank'",
        "agenda_type":"pdf",
        'agenda_content_tag':"div[class*=textLayer"
    },

    #add Hurt, they've had solar in the past https://www.townofhurtva.gov/node/471/agenda

     'New Kent PC':{
        "url":"https://www.newkent-va.us/843/Meeting-Agendas",
        'name':'New Kent County Planning Commission',
        "year_list_tag":"a[href*='Archive'",
        "agenda_link_tag":"a[href*='Archive'",
        "agenda_type":"pdf",
        "agenda_content_tag":"div[class*=textLayer"
    },

    'Southampton BOS':{
        'url':"https://www.southamptoncounty.org/departments/board_of_supervisors/bos_meeting_agendas.php",
        'name':'Southampton County Board of Supervisors',
        "year_list_tag":"a[href*='agendas'",
        "agenda_link_tag":"a[target*='_self'",
        "agenda_type":"webpage",
        'agenda_content_tag':"div[id*='post'"
    },

    'Southampton PC':{
        'url':"https://www.southamptoncounty.org/departments/planning/archived_planning_agendas.php",
        'name':'Southampton County Planning Commission',
        "year_list_tag":"a[target*='_self'",
        "agenda_link_tag":"a[target*='_self'",
        "agenda_type":"webpage",
        'agenda_content_tag':"div[id*='post'"
    }
}

"""MeetingsTable localities""" #REVIEW FOR INTEGRATION WITH THE SPLIT LISTS
meetingstable_dictionary = {
#Chatham https://www.chatham-va.gov/meetings?page=0

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
#novusagenda_dictionary = {}

"""OnBase localities""" #REVIEW FOR INTEGRATION WITH THE SPLIT LISTS
onbase_dictionary = {
    "Arlington County Board":{
        'url':"https://meetings.arlingtonva.us/CountyBoard",
        'name':"Arlington County Board"},
    
    "Arlington County PC":{
        'url':"https://meetings.arlingtonva.us/Planning",
        'name':"Arlington County Planning Commission"}
}

"php table localities" #REVIEW FOR INTEGRATION WITH THE SPLIT LISTS
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

     #add town of Gordonsville https://www.townofgordonsville.org/government/mayor_and_town_council/agendas_and_minutes.php   
     #gordonsville PC https://www.townofgordonsville.org/government/boards_&_commissions/planning_commission/planning_commission_agendas_&_minutes.php

    #add Town of Louisa https://louisatown.org/government/meeting-minutes-agenda/ and the option to handle document downloads to code + dictionary

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

"PrimeGov localities" #REVIEW FOR INTEGRATION WITH THE SPLIT LISTS
primegov_dictionary = {
    "Bedford":{
        'url':"https://bedfordcounty.primegov.com/public/portal",
        'name':"Bedford County"}
}

"The Lists" #Localities whose files are just in a list of hyperlinked titles
the_lists_dictionary = {
    "Alleghany BOS":{
        "url":"https://www.co.alleghany.va.us/board-of-supervisors/agendas/",
        "name":"Alleghany County Board of Supervisors",
        "meetings_tag":"a[class*='attachment-link'",
        "content_tag":"div[class*=textLayer"
    },

    "Amelia PC":{
        "url":"https://www.ameliacova.com/departments/boards_and_commissions/planning_commission.php#outer-116sub-117",
        "name":"Amelia County Planning Commission",
        "meetings_tag":'a[href*="Packet.pdf"', # TODO WHY IS IT DOUBLE QUOTE
        'content_tag':'div[class*=textLayer'
    },

    "Brunswick":{
        "url":"https://www.brunswickco.com/government/board_of_supervisors/agendas___minutes",
        "name":"Brunswick County",
        "meetings_tag":'a[href*=".pdf"', # TODO WHY IS IT DOUBLE QUOTE
        'content_tag':"div[class*=textLayer"
    },

    "Buena Vista City Council":{
        "url":"https://www.buenavistava.org/city-services/government/city-council/council-agenda-minutes/",
        "name":"Buena Vista City Council",
        "meetings_tag":"a[href*=sharepoint",
        "content_tag":"div[class*='pageText'"},


     "Covington":{
        "url":"https://covington.va.us/about-covington/agenda-and-minutes.html",
        "meetings_tag":"a[href*='agenda'",
        "content_tag":"div[class*=textLayer",
        "name":"City of Covington"},

    "Craig":{
        "url":"https://craigcountyva.gov/government/board-of-supervisors/",
        "name":'Craig County Board of Supervisors',
        "meetings_tag":"a[href*='.pdf'",
        "content_tag":"div[class*=textLayer"
        },

    "Galax":{
        "name":"City of Galax",
        "url":"https://galaxva.com/2025-city-council-agendas/", #still on 2025, no 2026 agendas or minutes yet posted
        "meetings_tag":"a[class*='pb_button'",
        "content_tag":"div[class*=textLayer"},

    "Lexington":{
        "name":"City of Lexington Planning Commission",
        "url":"https://www.lexingtonva.gov/government/boards-and-commissions/planning-commission",
        "meetings_tag":"a[class*='content_link'",
        "content_tag":"div[class*=textLayer"},

    "Norton":{
        "name":"City of Norton City Council",
        "url":"https://www.nortonva.gov/Archive.aspx?AMID=37",
        "meetings_tag":"a[href*=Archive",
        "content_tag":"div[class*=textLayer"},

    "Richmond":{
        "url":"https://co.richmond.va.us/board-of-supervisors-agenda-packets",
        "meetings_tag":"a[href*='.pdf'",
        "content_tag":"div[class*=textLayer",
        "name":"Richmond County"},
    
     "Lee":{
        "url":"https://www.leecova.com/meeting-minutes",
        "name":"Lee County",
        "meetings_tag":"a[href*='.pdf'",
        "content_tag":"div[class*=textLayer"
    },

}

"The Split Lists" #localities where it's a list or table, but the agenda link is separated from the date-containing title

the_split_lists_dictionary = {

    "Henrico BOS":{ #gets a 403 forbidden error when run on VPN
        "url":"https://henrico.us/supervisors/supervisors-agenda-o-gram/",
        "name":"Henrico County Board of Supervisors",
        "meeting_rows":"tr",
        "agenda_tag":"a[href*='.pdf'",
        "content_tag":"div[class*=textLayer"
    },

    "King and Queen BOS":{
        "name":"King and Queen County Board of Supervisors",
        "url":"https://kingandqueenco.net/board-of-supervisors-meetings/",
        "meeting_rows":"tr",
        "agenda_tag":"a[href*='.pdf'",
        "content_tag":"div[class*=textLayer"}, 

    "King and Queen PC":{
        "name":"King and Queen County Planning Commission",
        "url":"https://kingandqueenco.net/planning-commission-meetings/",
        "meeting_rows":"tr",
        "agenda_tag":"a[href*='.pdf'",
        "content_tag":"div[class*=textLayer"},

    "Staunton PC":{
        "name":"Staunton Planning Commission",
        "url":"https://www.ci.staunton.va.us/government/city-council-/board-commissions/agendas-minutes-for-boards-commissions/-selmt-1078",
        "meeting_rows":"tr",
        "agenda_tag":"a[href*='MeetingAgenda/ShowPrimaryDocument'",
        "content_tag":"div[class*=textLayer"},

    "Staunton CC":{
        "name":"Staunton City Council",
        "url":"https://www.ci.staunton.va.us/agendas-minutes",
        "meeting_rows":"tr",
        "agenda_tag":"a[href*='MeetingAgenda/ShowPrimaryDocument'",
        "content_tag":"div[class*=textLayer"},

    "Tazewell BOS":{
        "name":"Tazewell County Board of Supervisors",
        "url":"https://tazewellcountyva.org/government/boards-and-commissions/board-of-supervisors/",
        "meeting_rows":"li",
        "agenda_tag":"a[href*='Packet.pdf'",
        "content_tag":"div[class*=textLayer"},

    "Tazewell PC":{
        "name":"Tazewell County Planning Commission",
        "url":"https://tazewellcountyva.org/government/boards-and-commissions/planning-commission/",
        "meeting_rows":"li",
        "agenda_tag":"a[href*='-Agenda.pdf'",
        "content_tag":"div[class*=textLayer"}

    
     #'Floyd':{ #unworkable right now with the new website coding, but theoretically a list
    #    'url':"https://www.floydcova.gov/agendas-minutes",
    #    'name':'Floyd County'
    #},
}

"Dictionaries for localities that need individual code"
locality_dictionary_single_use = {
    "Albemarle PC":{
        "url":"https://www.albemarle.org/government/community-development/boards-and-commissions/planning-commission/-toggle-all-3491",
        "name":"Albemarle County Planning Commission",
        "rows_tag":"tr",
        'meetings_tag':"a[href*=Calendar",
        "documents_tag":"a[href*=showpublisheddocument",
        "content_tag":"div[class*=textLayer"
    },

    "Buchanan":{
        "url":"https://buchanancountyvirginia.gov/board-of-supervisors/",
        "name":"Buchanan County",
        "pdfs_tag":"a[href*='.pdf",
        "content_tag":"div[class*=textLayer"
    },

    "Fairfax BOS":{
        "url":"https://www.fairfaxcounty.gov/boardofsupervisors/",
        "name":"Fairfax County Board of Supervisors",
        "meetings_tag":"a[href*='boardofsupervisors'",
        "agendas_tag":"a[href*='.pdf'",
        "content_tag":"div[class*=textLayer"
    },

    "Fairfax PC":{
        "url":"https://www.fairfaxcounty.gov/planningcommission/meetingcalendar",
        "name":"Fairfax County Planning Commission",
        "years_tag":"table[align*=center",
        "months_tag":"td[align*=center",
        "agendas_tag":"a[href*='.pdf'",
        "content_tag":"div[class*=textLayer"
    },

    "Giles":{
        "url":"https://virginiasmtnplayground.com/bos/",
        "name":"Giles County Board of Supervisors",
        "buttons_tag":'div[class*="vc_btn3-container"', # TODO WHY IS IT DOUBLE QUOTE
        "agendas_tag":"a",
        "content_tag":"div[class*=textLayer"
    },

    #Gretna minutes https://townofgretna.org/government/council-minutes

    "Highland BOS":{
        "url":"https://www.highlandcova.org/node/666/agenda", #document download
        "name":"Highland County Board of Supervisors",
        "folders_tag":"a[href*=agenda",
        "meetings_tag":"div[class*='views-row'",
        "agendas_tag":"a[href*='agenda.'",
        "content_tag":"div[class*=textLayer"
    },

    "Loudoun":{
        "url":"https://lfportal.loudoun.gov/LFPortalInternet/Browse.aspx?startid=305808&row=1&dbid=0",
        "links_tag":"a",
        "years_tag":"td",
        "folders_tag":"tr",
        "current_year_tag":"a",
        "meetings_tag":"a",
        "agendas_tag":"a[href*='Agenda.pdf'",
        "name":"Loudoun County Planning Commission"
    },

    "Virginia Beach CC":{
        "name":"Virginia Beach City Council",
        "url":"https://clerk.virginiabeach.gov/city-council",
        "agendas_tag":"a[href*='Brief-Agenda'",
        "content_tag":"div[class*=textLayer"},

    "Wythe":{
        "url":"http://www.wytheco.org/index.php/resources/public-notices",
        "notice_tags":'a[href*="public-notices"', # TODO WHY IS IT DOUBLE QUOTE
        "name":"Wythe County Public Notices"
    }

    #"Wythe County Board of Supervisors":[wythe_county,"http://www.wytheco.org/index.php/resources/meeting-minutes/packages/bos-packages"],

    #"Wythe County Planning Commission":[wythe_county,"http://www.wytheco.org/index.php/resources/meeting-minutes/packages/planning-commission"],

}

locality_dictionary_multi_use = {

    "Bath BOS":{
        "name":"Bath County Board of Supervisors",
        "url":"https://www.bathcountyva.gov/public_information/minutes_audios/board_of_supervisors",
        "archive_page_tag":'a[class*="pageButton number"', # TODO WHY IS IT DOUBLE QUOTE
        "years_tag":"div[class*='item docTitle'", # TODO IS THIS QUOTE GOOD
        "minutes_page_tag":'a[class*="pageButton number"', # TODO WHY IS IT DOUBLE QUOTE
        "minutes_tag":"a[class*='docItemTitle'", # TODO IS THIS QUOTE GOOD
        "content_tag":"div[class*=textLayer"
    },

    "Bath PC":{
        "name":"Bath County Planning Commission",
        "url":"https://www.bathcountyva.gov/public_information/minutes_audios/planning_commission",
        "archive_page_tag":'a[class*="pageButton number"', # TODO WHY IS IT DOUBLE QUOTE
        "years_tag":"div[class*='item docTitle'", # TODO IS THIS QUOTE GOOD
        "minutes_page_tag":'a[class*="pageButton number"', # TODO WHY IS IT DOUBLE QUOTE
        "minutes_tag":"a[class*='docItemTitle'", # TODO IS THIS QUOTE GOOD
        "content_tag":"div[class*=textLayer"
    },

    "Bath BZA":{
        "name":"Bath County Board of Zoning Appeals",
        "url":"https://www.bathcountyva.gov/public_information/minutes_audios/board_of_zoning_appeals",
        "archive_page_tag":'a[class*="pageButton number"', # TODO WHY IS IT DOUBLE QUOTE
        "years_tag":"div[class*='item docTitle'", # TODO IS THIS QUOTE GOOD
        "minutes_page_tag":'a[class*="pageButton number"', # TODO WHY IS IT DOUBLE QUOTE
        "minutes_tag":"a[class*='docItemTitle'", # TODO IS THIS QUOTE GOOD
        "content_tag":"div[class*=textLayer"
    },
}
