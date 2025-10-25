import requests
from bs4 import BeautifulSoup

def scrape(link):
    people = [];

    response = requests.get(link)
    soup = BeautifulSoup(response.content, 'html.parser');

    content_div = soup.find_all('tr')

    for tr in content_div:
        text = tr.find_all('td')

        person_name = text[0].get_text(strip=True)
        description = text[1].get_text(strip=True)

        person = {"name": person_name, "description": description, "department": "biomedical engineering"}
        people.append(person)

    return people;

    

print(scrape('https://www.cmu.edu/bme/Research/research_faculty_listing.html#bio'))