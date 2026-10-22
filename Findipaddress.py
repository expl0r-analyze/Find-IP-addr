import requests

def get_ip_info(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    if response.status_code == 200
        data = response.json()
        if data[status] == "success":
            print(f"Страна {data.get('country')}")
            print(f"Город: {data.get('city')}")
            print(f"координаты: {data.get('loc')}")
        else:
            print("ERROR!", data["message"]

ip = (input("Введите желаемый айпи: ")) #<<<< ВВЕДИТЕ ЖЕЛАЕМЫЙ АЙПИ
    
get_ip_info(ip)
