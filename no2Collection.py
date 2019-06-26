import time
import requests
import configparser

compr = "0S"
config = configparser.RawConfigParser()
config.read('config.cfg')
token = config.get('authentication', 'token')
url = config.get('urls', 'no2collections')


response = requests.request("GET", url,
                            headers={'accessToken': token},
                            )
if(response.text[10] == compr[0]):
    print(response.json())
else:
    print("Error in the  Email: " + email + " or password ")
