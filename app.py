import urllib.request
import re


def switch_phone(url, number):
    opener = urllib.request.FancyURLopener({})
    f = opener.open(url)
    content = f.read()
    try:
        content = content.decode('utf-8')
    except UnicodeDecodeError:
        content = content.decode('windows-1252')
    pattern2 = r'(\d{3}\d{6})'
    res = re.findall(pattern2, content)
    print(f"Найденые номера с сайта: {res}")
    for int in res:
        if int.count(number[6:]) > 0:
            print(f"Мы его не потеряли, вот он {int}")
    f.delete

number = '849513777'
url = "https://hands.ru/company/about/"


switch_phone(url, number)

url = "https://repetitors.info/"
number = '80050572'
switch_phone(url, number)
