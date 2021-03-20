import requests
import sys
import outputResult as output
from bs4 import BeautifulSoup

def top(number = None):
    r = requests.get('https://www.alexa.com/topsites/')
    siteList = []

    if r.status_code == requests.codes.ok:
        # 以 BeautifulSoup 解析 HTML 程式碼
        soup = BeautifulSoup(r.text, 'html.parser')
    #     print(soup)
        sites = soup.find_all(class_='td DescriptionCell')
        for s in sites:
            siteList.append(s.find('a').text)
    if(number):
        number = int(number)
        if(number < len(siteList)):
            output.outputResult(siteList[:number])
            # return siteList[:number]
        else:
            print("range error")
            return None
    else:
        output.outputResult(siteList[:number])
        # return siteList

if __name__ == '__main__':
    argvNumbers = len(sys.argv)
    try:
        if(argvNumbers > 2):
            raise Exception("Sorry, too many parameter")
        if (argvNumbers == 2):
            top(sys.argv[1])
        if (argvNumbers == 1):
            top()
    except:
        print("An exception occurred")
    