import csv

CONTACT_IDENTIFIER = "Project Contact:"
DESCRIPTION_IDENTIFIER = "Project Description:"
PREREQ_IDENTIFIER = "Prerequisite Knowledge:"
RELEVANT_IDENTIFIER = "Link(s) to Relevant Papers:"
URLS_IDENTIFIER = "Project URLs:"

# Goal: parse json
with open('scrapers/research_opportunities/example_json/Simple Undergrad.csv', mode ='r') as file:
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
        print(project_contact)
        print(project_desc)
