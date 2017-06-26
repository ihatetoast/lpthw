from bs4 import BeautifulSoup

import urllib2

response = urllib2.urlopen("https://austin.craigslist.org/search/sof")
html = response.read()
soup = BeautifulSoup(html, "html.parser")
it_jobs = soup.find_all("a", class_="result-title" )
jobs = set(it_jobs)


for job in jobs:
	if "JavaScript" in job.string:
		print "This job has JavaScript: " + job.string