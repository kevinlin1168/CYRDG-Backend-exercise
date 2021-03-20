import pycountry
import requests
import sys
import outputResult as output
from bs4 import BeautifulSoup

def get_country_code(name):
    for co in list(pycountry.countries):
        if name in co.name:
            return co.alpha_2
    return None

def country(countryCode = None):
    r = requests.get(f'https://www.alexa.com/topsites/countries/{countryCode}')
    siteList = []

    if r.status_code == requests.codes.ok:
        # 以 BeautifulSoup 解析 HTML 程式碼
        soup = BeautifulSoup(r.text, 'html.parser')
    #     print(soup)
        sites = soup.find_all(class_='td DescriptionCell')
        for s in sites:
            siteList.append(s.find('a').text)
            
    output.outputResult(siteList[:20])

if __name__ == '__main__':
    argvNumbers = len(sys.argv)
    try:
        if(argvNumbers > 2):
            raise Exception("Sorry, too many parameter")
        if (argvNumbers == 2):
            country(get_country_code(sys.argv[1]))
        if (argvNumbers == 1):
            raise Exception("Sorry, too less parameter")
    except:
        print("An exception occurred")
    