import time
import requests
import configparser

compr = "0S"
config = configparser.RawConfigParser()
config.read('config.cfg')
token = config.get('authentication', 'token')

# Example: casa :5324 - uni: 4281
#  numStop = input("Numero de la parada: ")

numStop = '4281'

t_end = time.time() + 60 * 1

while time.time() < t_end:
    url = config.get('urls', 'stops')
    url = url + numStop + "/arrives/all/"

    data = {
        "statistics": "N",
        "cultureInfo": "EN",
        "Text_StopRequired_YN": "Y",
        "Text_EstimationsRequired_YN": "Y",
        "Text_IncidencesRequired_YN": "Y",
        "DateTime_Referenced_Incidencies_YYYYMMDD": "20180823"
    }
    response = requests.request(
        "POST",
        url,
        headers={'accessToken': token},
        json=data
    )

    if(response.text[10] == compr[0]):
        arrives = response.json()['data'][0]['Arrive']
        stops = response.json()['data'][1]['StopLines']
        name = stops['Data']['Description']
        line = stops['Data']['Label']

        print("\n\nNombre de la parada: " + name)
        print("Linea: " + line)

        for arrive in arrives:
            direction = arrive['destination']
            estimateArrive = arrive['estimateArrive'] % 3600/60
            print("\nDirección: " + direction)
            print("Tiempo de espera: " + str(round(estimateArrive)))

        time.sleep(10)

    else:
        print("Error in the  Email: " + email + " or password ")
