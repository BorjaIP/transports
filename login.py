import requests
import getpass
import configparser

#  The authentication system returns one token for 15 minutes

compr = "0S"

config = configparser.RawConfigParser()
config.read('config.cfg')

# Load config from config.cfg
email = config.get('authentication', 'email')
passwd = config.get('authentication', 'passwd')
url = config.get('urls', 'login')

# Input configuration from console
#  email = input("email: ")
#  try:
#  passwd = getpass.getpass()
#  except Exception as error:
#  print('ERROR', error)

headers = {
    'email': email,
    'password': passwd
}

print("Waiting connection...")
response = requests.request("GET", url, headers=headers)

if(response.text[10] == compr[0]):
    print("Correct connection")

    token = response.json()['data'][0]['accessToken']
    config.set('authentication', 'token', token)
    with open('config.cfg', 'w') as configfile:
        config.write(configfile)

else:
    print("Error in the  email: " + email + " or password ")
