import requests

def get_ip_info(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Город: {data.get('city')}")
        print(f"Координаты: {data.get('loc')}")
        print(f"Провайдер: {data.get('org')}")
        print(f"Регион: {data.get('region')}")
        print(f"часовой пояс: {data.get('timezone')}")
    else:
        print("anonim-channel@Root:~$ ОШИБКА!!! СЕРВЕР НЕДОСТУПЕН!")

preview = """


_____________________________________________________________________________________



@@@@@@  @@@@@@@@      @@@@@@@@    @@@@@@      @@@@@@    @@      @@  @@@@@@@@@@  
@@@@@@  @@@@@@@@      @@@@@@@@    @@@@@@      @@@@@@    @@      @@  @@@@@@@@@@  
  @@    @@      @@  @@          @@          @@      @@  @@      @@      @@      
  @@    @@      @@  @@          @@          @@      @@  @@      @@      @@      
  @@    @@@@@@@@      @@@@@@    @@          @@      @@  @@      @@      @@      
  @@    @@@@@@@@      @@@@@@    @@          @@      @@  @@      @@      @@      
  @@    @@                  @@  @@          @@      @@  @@      @@      @@      
  @@    @@                  @@  @@          @@      @@  @@      @@      @@      
@@@@@@  @@          @@@@@@@@      @@@@@@      @@@@@@      @@@@@@        @@      
@@@@@@  @@          @@@@@@@@      @@@@@@      @@@@@@      @@@@@@        @@      

_____________________________________________________________________________________




[+] ИНИЦИАЛИЗАЦИЯ ДАННЫХ...
[+] ПРОГРУЗКА ПАКЕТОВ...
[+] ОБРАБОТКА ДАННЫХ...
[+] ШИФРОВАНИЕ КАНАЛА СВЯЗИ...
[+] ИНИЦИАЛИЗАЦИЯ ЗАВЕРШЕНА...


"""
print(preview)

while True:
    ip = input("anonim-channel@Root:~$ ВВЕДИТЕ ЖЕЛАЕМЫЙ АЙПИ: ")
    get_ip_info(ip)

    choice = input("anonim-channel@Root:~$ ЖЕЛАЕТЕ ПРОДОЛЖИТЬ? (да/нет): ")
    if choice == "да" or choice == "yes":
        print("-" * 50)
        continue
    if choice == "нет" or choice == "no":    
        print("anonim-channel@Root:~$ КАНАЛ СВЯЗИ ЗАКРЫТ ОПЕРАЦИЯ ЗАВЕРШЕНА!!!")
        break
