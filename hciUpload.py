from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json
import csv

with open('C:/Users/irisy/Desktop/scottylabs/private.json', mode ='r') as file:
    passwords = json.load(file)

    uri = f"mongodb+srv://MongoAccess:{passwords['password']}@cluster0.a6odq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")

        print(f'Available Databases: {client.list_database_names()}')

        research_db = client['CMUResearchDatabase']

        professor_col = research_db['ResearchOpportunities']
        
        data_to_insert = []
        with open('C:/Users/irisy/Desktop/15-112/hackathon/cmu-research-backend/scrapers/research_opportunities/cleaned_projects.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)  # automatically uses header row as keys
            for row in reader:
                data_to_insert.append(dict(row))

    # ---- Insert into Mongo ----
        if data_to_insert:
            result = professor_col.insert_many(data_to_insert)
            print(f"Inserted {len(result.inserted_ids)} documents into MongoDB.")

    except Exception as e:
        print(e)