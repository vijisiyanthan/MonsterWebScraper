import requests
from sys import argv
from bs4 import BeautifulSoup

if __name__ == '__main__':
    city = argv[1]
    title = str(argv[2])
    print(title)
    URL = f'https://www.monster.ca/jobs/search/?q=Software-Developer&where={city}'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='ResultsContainer')

    job_elems = results.find_all('section', class_='card-content')
    python_jobs = results.find_all('h2',
                                   string=lambda text: title in text.lower())

    for job_elem in job_elems:
        title_elem = job_elem.find('h2', class_='title')
        company_elem = job_elem.find('div', class_='company')
        location_elem = job_elem.find('div', class_='location')
        if None in (title_elem, company_elem, location_elem):
            continue
        # print(title_elem.text.strip())
        # print(company_elem.text.strip())
        # print(location_elem.text.strip())
        # print()

    for job in python_jobs:
        link = job.find('a')['href']
        print(job.text.strip())
        print(f"Apply here:{link}\n")
