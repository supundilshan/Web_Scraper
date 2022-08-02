import requests
from bs4 import BeautifulSoup

# URL = 'https://ikman.lk/en/ads/colombo/land'
URL = 'https://ikman.lk/en/ads/piliyandala/land?sort=date&order=desc&buy_now=0&urgent=0&page=2'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find("ul", class_='list--3NxGO')
# print(results.prettify())

# Ghet all the links
links = []
for link in results.find_all('a', href=True, class_='card-link--3ssYv gtm-ad-item'):
    full_path = "https://ikman.lk/" + link['href']
    links.append(full_path)
    print(full_path)

# write to CSV
head = ['address']
import csv
wtr = csv.writer(open('out.csv', 'w'), delimiter=',', lineterminator='\n')
wtr.writerow(head)
for x in links:
    wtr.writerow([x])

# job_elems = results.find_all('div', class_='content--3JNQz')
# # print(job_elems)
#
# print("---------------------------------------------------------------")

# for job_elem in job_elems:
    # print("++++++++++++++")
    # print(job_elem, end='\n'*2)

# for job_elem in job_elems:
#     # Each job_elem is a new BeautifulSoup object.
#     # You can use the same methods on it as you did before.
#     title_elem = job_elem.find('h2', class_='heading--2eONR heading-2--1OnX8 title--3yncE block--3v-Ow')
#     price_elem = job_elem.find('div', class_='price--3SnqI color--t0tGX')
#
#     # print(title_elem)
#     # print(price_elem)
#
#     try:
#         print(title_elem.text)
#         print(price_elem.text)
#     except:
#         print()
#
#     print()



# heading--2eONR heading-2--1OnX8 title--3yncE block--3v-Ow
# content--3JNQz