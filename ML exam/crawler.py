import requests
from bs4 import BeautifulSoup
from xlwt import *
Workbook= Workbook(encoding='utf-8')
table=Workbook.add_sheet('data')
table.write(0,0,'Number')
table.write(0,1,'Title')
table.write(0,2,'Company')
table.write(0,3,'Location')
line=1
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
print(results.prettify())
num=0
job_elements = results.find_all("div", class_="card-content")
for job_element in job_elements:
    print(job_element, end="\n"*2)
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    num+=1
    print()
table.write(line,0,num)
table.write(line,1,title_element.text.strip())
table.write(line,2,company_element.text.strip())
table.write(line,3,location_element.text.strip())

#print(page.text)