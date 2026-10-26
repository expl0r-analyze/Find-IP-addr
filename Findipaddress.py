import requests

def get_ip_info(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Город: {data.get('city')}")
        print(f"координаты: {data.get('loc')}")
        print(f"Организация: {data.get('org')}")
        print(f"часовой пояс: {data.get('timezone')}")
    else:
        print("ERROR!")

ip = (input("Введите желаемый айпи: ")) #<<<< ВВЕДИТЕ ЖЕЛАЕМЫЙ АЙПИ
    
get_ip_info(ip)
