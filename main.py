from requests import get, post, Session
import json
from bs4 import BeautifulSoup
import json


def getStudentsNameInfo():
    final_data = list()
    try:
        base_url = 'https://sms24.me/en/countries/'
        response = get(base_url).text

        rows = BeautifulSoup(str(response), 'html.parser').find_all('a', href=True)[0:]

        # json_data = json.loads(response.text)
        for a in rows:
            print("Found the URL:", a['href'])

        

        # print(json.dumps(final_data))
    except Exception as ex:
        print('error: %s' % ex)


getStudentsNameInfo()
