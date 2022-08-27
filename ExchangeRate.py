import requests 

def CurrencyData(cur1,cur2):
    url = f"https://v6.exchangerate-api.com/v6/32a648b10e07cb72da082329/pair/{cur1}/{cur2}"
    response = requests.get(url)
    data = response.json()
    return round(data["conversion_rate"], 2)
