#!/usr/bin/env python3
import requests

#Функция - обработчик для проверки соединения.
def check_connection(url="https://ipinfo.io", timeout=3):
    try:
        requests.head(url, timeout=timeout)
        return True
    except requests.RequestException:
        return False

def get_ip_info(ip_address):
    if not check_connection():
        print("anonim-channel@Root:~$ ОШИБКА, СОЕДИНЕНИЕ НЕСТАБИЛЬНО!")
        return

    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Город: {data.get('city')}")
        print(f"Координаты: {data.get('loc')}")
        print(f"Провайдер: {data.get('org')}")
        print(f"Регион: {data.get('region')}")
        print(f"Часовой пояс: {data.get('timezone')}")
        print(f"Телефон: {data.get('phone')}")
    else:
        print("anonim-channel@Root:~$ ОШИБКА!!! СЕРВЕР НЕДОСТУПЕН ИЛИ НЕПРАВИЛЬНОЕ ЗНАЧЕНИЕ!")

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
        print("-" * 80)
        continue
    elif choice == "нет" or choice == "no":    
        print("anonim-channel@Root:~$ КАНАЛ СВЯЗИ ЗАКРЫТ ОПЕРАЦИЯ ЗАВЕРШЕНА!!!")
        break
    else:
        print("НЕИЗВЕСТНОЕ ЗНАЧЕНИЕ. РАБОТА ЗАВЕРШЕНА!!!")
        break

