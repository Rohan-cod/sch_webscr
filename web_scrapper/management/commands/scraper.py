from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
import requests

from web_scrapper.models import Job_posting 



class Command(BaseCommand):
	help = "collect job postings from monster.com"
	def handle(self, *args, **options):
		URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=India'
		page = requests.get(URL)
		soup = BeautifulSoup(page.content, 'html.parser')
		results = soup.find(id='ResultsContainer')
		job_elems = results.find_all('section', class_='card-content')
		for job_elem in job_elems:
			title_elem = job_elem.find('h2', class_='title')
			url_elm = job_elem.find('a')
			company_elem = job_elem.find('div', class_='company')
			location_elem = job_elem.find('div', class_='location')
			if None in (title_elem, company_elem, location_elem):
				continue
			title=title_elem.text.strip()
			company=company_elem.text.strip()
			location=location_elem.text.strip()
			url=url_elm['href']
			print(title,company,location)
			try:
				Job_posting.objects.create(
						title=title,
						company=company,
						location=location,
						url=url
					)
			except:
				pass