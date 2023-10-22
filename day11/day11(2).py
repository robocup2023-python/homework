import requests
ur1=""
api_key="{your's key}"

responce=requests.get(ur1.format(api_key))
if responce.status_code==200:
    data=responce.json()
    print(data)
else:
    print("Error")