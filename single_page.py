from array import *
import requests
from bs4 import BeautifulSoup

def singlepage(page_URL):

    output = []

    # URL = 'https://ikman.lk/en/ad/iddmk-hlaavt-for-sale-puttalam-65'
    URL = page_URL
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    # -----------------------------  Find land Price ---------------------------
    price_box = soup.find("div", class_='ui-price-tag')
    price = price_box.text
    # print(price)

    # -----------------------------  Find land Details --------------------------
    detail_box = soup.find("div", class_='item-properties')
    # print(results.prettify())

    details_elems = detail_box.find_all('dl')
    # print(job_elems)

    for elems in details_elems:

        title_elem = elems.find('dt')
        description_elem = elems.find('dd')
        # print(title_elem)
        # print(description_elem)

        try:
            title = title_elem.text
            output.append(title)
            description = description_elem.text
            output.append(description)
            # print(title, ' : ', description)
        except:
            print()
    # -----------------------------  Find land Details --------------------------

    output.append(price)
    # print("in single page")
    # print(output)

    return output


if __name__ == '__main__':

    land = []
    page_URL = 'https://ikman.lk//en/ad/pilliyndl-ngryen-hond-iddmk-for-sale-colombo'

    land.append(singlepage(page_URL))
    # singlepage(page_URL)

    # print("Land details")
    print(land)
