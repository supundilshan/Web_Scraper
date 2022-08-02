from array import *
import requests
from bs4 import BeautifulSoup

def singlepage(page_URL):

    # URL = 'https://ikman.lk/en/ad/iddmk-hlaavt-for-sale-puttalam-65'
    URL = page_URL
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find("div", class_='ad-meta--17Bqm justify-content-flex-start--1Xozy align-items-normal--vaTgD flex-wrap-wrap--2PCx8 flex-direction-row--27fh1 flex--3fKk1')
    # print(results.prettify())

    job_elems = results.find_all('div', class_='full-width--XovDn justify-content-flex-start--1Xozy align-items-normal--vaTgD flex-wrap-nowrap--3IpfJ flex-direction-row--27fh1 flex--3fKk1')
    # print(job_elems)

    # for job_elem in job_elems:
    # print("++++++++++++++")
    # print(job_elem, end='\n'*2)

    output = []
    # output = array('u', [])
    # i = 0
    for job_elem in job_elems:

        title = ''
        description = ''

        title_elem = job_elem.find('div', class_='word-break--2nyVq label--3oVZK')
        description_elem = job_elem.find('div', class_='word-break--2nyVq value--1lKHt')
        # print(title_elem)
        # print(description_elem)

        try:
            title = title_elem.text
            description = description_elem.text
            print(title, ' : ', description)
            # print(description)
        except:
            print()

        # output[i] = title
        # i = i + 1
        # output[i] = description
        # i = i+1
        # output.append(title)
        # output.append(description)
        # print(output)

    # print(output)
    # return output


# if __name__ == '__main__':
#
#     land = []
#     page_URL = 'https://ikman.lk/en/ad/superb-land-close-to-malambe-town-for-sale-colombo-2'
#
#     land.append(singlepage(page_URL))
#     singlepage(page_URL)
#
#     print("Land details")
#     print(land)
