import csv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

CONTACT_IDENTIFIER = "Project Contact:"
DESCRIPTION_IDENTIFIER = "Project Description:"
PREREQ_IDENTIFIER = "Prerequisite Knowledge:"
RELEVANT_IDENTIFIER = "Link(s) to Relevant Papers:"
URLS_IDENTIFIER = "Project URLs:"

uri = "mongodb+srv://MongoAccess:<mongodbpw>@cluster0.a6odq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'), tlsAllowInvalidCertificates=True)
db = client["CMUResearchDatabase"]
col = db["ResearchOpportunities"]

# Data (to be uploaded)
scs_data = []

# Goal: parse json

<<<<<<< HEAD
with open('example_json/Undergraduate Research Opportunities.csv', mode ='r') as file:
=======
with open('scrapers/research_opportunities/example_json/Simple Undergrad.csv', mode ='r') as file:
>>>>>>> 32aa157a9189c954b51069d4e63ff5ab743373a2
    csvFile = csv.DictReader(file)
    for line in csvFile:
        info = line[""]
        project_contact_i = info.index(CONTACT_IDENTIFIER)
        project_desc_i = info.index(DESCRIPTION_IDENTIFIER)
        project_prereq_i = info.index(PREREQ_IDENTIFIER)
        relevant_i = info.index(RELEVANT_IDENTIFIER)
        project_URL_i = info.index(URLS_IDENTIFIER)

        project_contact = info[project_contact_i + len(CONTACT_IDENTIFIER) : project_desc_i].strip()
        project_desc = info[project_desc_i + len(DESCRIPTION_IDENTIFIER) : project_prereq_i].strip()
        project_prereq = info[project_prereq_i + len(PREREQ_IDENTIFIER) : relevant_i].strip()       
        project_relevant = info[relevant_i + len(RELEVANT_IDENTIFIER) : project_URL_i].strip()
        project_URLs = info[project_URL_i + len(URLS_IDENTIFIER) : len(info)-1].strip()

        project_date_added = line["Date Added"]
        project_title = line["Project Title"]
        project_department = line["Department"]
        project_time_commitment = line["Time Commitment (Hours/Week)"]
        
        temp_dict = {
	    "Project Title": project_title,
            "Contact": project_contact,
            "Description": project_desc,
            "Prereqs": project_prereq,
            "Time Commitment": project_time_commitment,
            "Date Published": project_date_added,
            "Relevant Links": project_relevant + project_URLs,
            "Department": project_department
        }
        scs_data.append(temp_dict)

return_val = col.insert_many(scs_data)
print(return_val)
