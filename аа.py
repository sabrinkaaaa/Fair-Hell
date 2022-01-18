import requests


API_KEY = "40d1649f-0493-4b70-98ba-98533de7710b"
address = "Хабаровск, Уфа, Нижний Новгород, Калининград".split(", ")

for adres in address:
    geocoder_request = f" http://qeocode-maps.yandex.ru/1.x/?apikey= {API_KEY}" \
                       f"&geocode={adres}&format=json"

    response = requests.get(geocoder_request)

if response.status_code == 200:
    json_request = response.json()
    with open("b.json", "wb") as steam:
        steam. write(response.content)
    toponym = json_request["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
    toponym_okrug = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"][1]["name"]
    print(toponym_address, "-", toponym_okrug)
else:
    print(response.status_code)