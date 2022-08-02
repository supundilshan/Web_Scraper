from array import *
import requests
import csv
from bs4 import BeautifulSoup
import single_page

def page_Browser(page_URL,max_no):

    land_data = [["Title","Discreption","price"]]

    # URL = 'https://ikman.lk/en/ad/iddmk-hlaavt-for-sale-puttalam-65'
    for page_index in range(1, max_no+1):

        print()
        print("------------------------------------------------------------")
        print()
        print("Working  on Page ", page_index)

        URL = page_URL + str(page_index)
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')

        results = soup.find("ul", class_='list--3NxGO')
        # print(results.prettify())

        # Ghet all the links

        for link in results.find_all('a', href=True, class_='card-link--3ssYv gtm-ad-item'):
            full_path = "https://ikman.lk/" + link['href']
            print(full_path)

            land_data.append(single_page.singlepage(full_path))
            # single_page.singlepage(full_path)

    return land_data


if __name__ == '__main__':

    max_no = 5

    page_URL = 'https://ikman.lk/en/ads/boralesgamuwa/land?sort=date&order=desc&buy_now=0&urgent=0&page='

    land = page_Browser(page_URL, max_no)

    with open('boralesgamuwa.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write multiple rows
        writer.writerows(land)

        print("written in to csv")

    # land.append(singlepage(page_URL))
    # singlepage(page_URL)
    #
    # print("Land details")
    # print(land)
    # for x in land:
    #     for y in x:
    #         print(y, end=" ")
    #     print()
    # wtr = csv.writer(open('out.csv', 'w'), delimiter=',', lineterminator='\n')
    # for x in land:
    #     wtr.writerow(x)


