import requests
from bs4 import BeautifulSoup

robotics_data = []

def scrape_robotics(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.content, 'html.parser');

    cards = soup.find_all(class_="info-card")

    for card in cards:
        link = card.find('a').get('href')
        name = card.find(class_="info-card__title").string
        scrape_project_page(link, name)

def scrape_project_page(link, name):
    print(link)
    project = {"Project Title": "", "Contact": "", "Description": "", "Prereqs": "", "Time Commitement": "", "Date Published": "", "Relevant Links": [], "College": ["School of Computer Science"], "Department": ["Robotics Institute"], "Position": "", "Paid/Unpaid": "", "Desired Skill Level": "", "Database": "https://www.ri.cmu.edu/research/projects/"};

    response = requests.get(link);
    soup = BeautifulSoup(response.content, 'html.parser');
    links = []

    project["Project Title"] = name;

    # change to be dictionary {name: andrewID}
    # project["Contact"] = soup.find(class_="contact") or ""
    
    desc = soup.find(class_='statement-inner')
    if (desc):
        project["Description"] = desc.get_text(separator='\n', strip=True)

    external = soup.find(class_ = "external_link")
    if (external):
        links.append(external.find("a").get("href"))
    links.append(link)
    project["Relevant Links"] = links
    print(project["Relevant Links"])


scrape_robotics('https://www.ri.cmu.edu/research/projects/')