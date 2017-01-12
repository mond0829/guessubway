#This grogram is based on South Korea system.
#So if you want to use in your country, change URL in line 8.


import requests
import json

b= input("Which station do you want to go? : ")
data = requests.get("http://swopenapi.seoul.go.kr/api/subway/sample/json/realtimeStationArrival/1/5/"+b+'/')

dict_data = json.loads(data.text)

for i in range (4) :
    print("")
    print(dict_data['realtimeArrivalList'][i]['trainLineNm'])
    print(dict_data['realtimeArrivalList'][i]['arvlMsg2'])
