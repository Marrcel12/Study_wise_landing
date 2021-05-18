from googleapiclient.discovery import build
from google.oauth2 import service_account
import json
SERVICE_ACCOUNT_FILE = 'google-credentials.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
def get_data():
    creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    my_sp_id = '1_W2HWCEw5qcW8e6XDMHNB5KznoIBfMx7CYWMm1rA1Bg'
    my_range = 'Arkusz1!a1:g31'
    with build('sheets', 'v4', credentials=creds) as service:
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=my_sp_id,
                                        range=my_range).execute()
        values = result.get('values', [])

    return result["values"][1:]

def get_search_tags(data):
    school_level_topics={}
    for i in data:    
        list_levels=i[3].split(",")
        for level in list_levels: 
            if level not in school_level_topics:
                school_level_topics[level]=[]
            list_topics=i[4].split(",")
            for topic in list_topics:
                if topic not in school_level_topics[level]:
                    school_level_topics[level].append(topic)
    search_tags=[]
    for i in school_level_topics:
        for topic in school_level_topics[i]:
            search_tags.append(i+" - "+topic)
    return(search_tags)
    
def prepere_data(data):
    prepered_data=[]
    for i in data:
        levels=i[3].split(",")
        topics=i[4].split(",")
        tags=[]
        for level in levels:
            for topic in topics:
                tags.append(level+" - "+topic)
        prepered_data.append({
        "login":i[0],
        "ig_profile":i[1],"ig_photo":i[2],
        "school_levels":levels,
        "topics":topics,
        "tags":tags
        })
    return prepered_data
def get_data_query(data,tags):
    query_result=[]
    for tag in tags:
        for profile in data:
            if tag in profile["tags"]:
                if profile not in query_result:
                    query_result.append(profile)

    return query_result