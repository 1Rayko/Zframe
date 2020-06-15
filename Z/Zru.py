
import requests 
import datetime
import sys
import time
import argparse
import os 
import colorama 
import csv  
import json 
import vk
import random
from colorama import init
from colorama import Fore, Back, Style
init(autoreset=True)
import itertools
import threading
import time
import base64
import urllib.request
from bs4 import BeautifulSoup
import socket


os.system('clear')
done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    

t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(0.8)
done = True
os.system ('clear')
print(Fore.GREEN +
""" ____  ____
/_  / / __/______ ___ _  ___
 / /_/ _// __/ _ `/  ' \/ -_)
/___/_/ /_/  \_,_/_/_/_/\__/
                            """)
print(Fore.BLUE +Back.WHITE + 'Автор : sudoreboot2020, Помощник : alonesain')
print(Fore.RED + 'Выбери опцию :')
print(Fore.YELLOW+"""-----#Деанон#-----
[1] - Saycheese
[2] - Seeker
[3] - sayhello 
[4] - sherlock 
[5] - Deanons
[6] - define
-----#Утилиты для ВК#-----
[7] - VTOOL
[8] - VKBRUTE
[9] - VK DNK 
[10] - kingfish
[11] - kingfish2.0
[12] - kingdish3.0
-----#Прочее#-----
[13]- smsham 
[14] - spymer
[15] - Recreator Phishing
[16] - DDOS
[17] - http tunnels
[18] - ADB-Toolkit
[19] - RedHawk
[20] - Tools
[21] - Banner
[22] - ADB-Termux Installer
[23] - b0mb3r
[24] - Tool-X""")

os.chdir('utils')

while True:
    num =str(input("\033[35m\033[5m[*]"))
    if num == ('1') :
        print (Fore.GREEN + 'Запуск Saycheese')
        os.system('clear')
        os.chdir('saycheese-master')
        os.system('bash saycheese.sh')
    elif num == ('2'):
        print (Fore.GREEN + 'Запуск Seeker')
        os.system('clear')
        os.chdir('seeker-master')
        os.system('python3 seeker.py -t manual')
    elif num == ('3'):
        print (Fore.GREEN + 'Запуск sayhello')
        os.system('clear')
        os.chdir('sayhello-master')
        os.system('bash sayhello.sh')
    elif num == ('4'):
        print (Fore.GREEN + 'Запуск sherlock')
        os.system('clear')
        os.chdir('sherlock-master')
        os.system('python3 sherl.py')
    elif num == ('5'):
        print(Fore.GREEN+"Запуск deanons")
        os.chdir('deanons-master')
        os.system('clear')
        os.system('python3 dean.py')
    elif num == ('6'):
        print(Fore.FREEN+'Запуск Defnie')
        os.chdir('define-master')
        os.system('clear')
        os.system('php define.php')

    elif num == ('7'):
        print(Fore.GREEN + 'Запуск VTOOL')
        os.system('clear')
        os.chdir('vtool-master')
        os.system('python3 vtool.py')
    elif num == ('8') :
        print(Fore.GREEN + 'Запуск VKBRUTE')
        os.system('clear')
        os.chdir('vtool-master')
        os.system('python3 brute.py')
    elif num == ('9'):
        print(Fore.YELLOW+'Запуск VKtoPasswd')
        os.chdir('VkToPassword-master')
        os.system('clear')
        os.system('python3 vtp.py')
    elif num == ('10'):
        print(Fore.GREEN+'Запуск kingfish')
        os.system('clear')
        os.chdir('kingfish-master')
        os.system('python3 fsh.py')
    elif num == ('11'):
        print(Fore.GREEN+'Запуск kingfish2.0')
        os.system('clear')
        os.chdir('kingfish2-master')
        os.system('python3 fsh.py')
    elif num == ('12') :
        print (Fore.GREEN + 'Запуск kingfish3.0')
        os.system ('clear')
        os.chdir ('kingfish3.0')
        os.system ('python fsh.py')
    elif num == ('13'):
        print (Fore.GREEN + 'Starting smsham')
        os.system('clear')
        os.chdir('smsham-master')
        os.system('python3 smsham.py')

    elif num == ('14'):
        print(Fore.GREEN+'Запуск spymmer')
        os.system('clear')
        os.chdir('spymer-master')
        os.system('python3 spammer.py')
    elif num == ('15') :
        print (Fore.GREEN + 'Запуск Recreator Phishing')
        os.system ('clear')
        os.chdir ('Recreator-Phishing-master')
        os.system ('python3 recreator-phishing.py')

    elif num == ('16'):
        print(Fore.GREEN + 'Запуск DDOS')
        os.system('clear')
        os.chdir('DDos')
        print (Fore.LIGHTBLUE_EX+"""Выбери порт [1]-80 или [2]-443""")
        pod = int(input(''))
        if pod == (1) or pod == (80):
            os.system('python3 80port.py')
        elif pod == (2) or pod == (443):
            os.system('python3 443port.py')
        else:
            print(Fore.RED+'ОШИБКА')
    elif num == ('17'):
        print (Back.WHITE +Fore.BLUE  + '1 - ngrok или 2 - localhost.run')
        while True:
            num = str(input("\033[35m\033[5m[*]"))
            if num == ('1'):
                print(Fore.LIGHTBLUE_EX+'Какая ОС?')
                print(Fore.LIGHTRED_EX+"""[1]-android \n[2]-Linux""")
                osy = int(input("\033[35m\033[5m[*]"))
                print (Fore.LIGHTBLUE_EX  + 'Порт:')
                port = str(input("\033[35m\033[5m[*]"))
                if osy == (1):
                    os.system('./ngroka http '+port)
                elif osy == (2):
                    os.system('./ngrok http '+port)
            elif num == ('2'):
                print (Fore.LIGHTBLUE_EX  + 'Порт:')
                port = str(input("\033[35m\033[5m[*]"))
                os.system('ssh -R 80:localhost:'+port+' ssh.localhost.run')
            else :
                print(Fore.RED +'ОШИБКА')
    
    elif num == ('18') :
        print (Fore.GREEN + 'Starting ADB-Toolkit')
        os.system('clear')
        os.chdir('ADB-Toolkit')
        print(Fore.GREEN + '[1] - Установить [2] - Запустить ADB-Toolkit')
        adbtool = int(input(''))
        if adbtool == (1):
            os.system('bash install.sh')
        elif adbtool == (2):
            os.system('bash ADB-Toolkit.sh')

    elif num == ('19') :
        print (Fore.GREEN + 'Запуск RedHawk')
        os.system ('clear')
        os.chdir ('RED_HAWK')
        os.system ('php rhawk.php')
    elif num == ('20') :
        print (Fore.GREEN + 'Запуск Tools')
        os.system ('clear')
        os.chdir ('toolss')
        os.system ('python toolss.py')
    elif num == ('21') :
        print (Fore.GREEN + 'Запуск Banner')
        os.system ('clear')
        os.chdir ('Banner')
        os.system ('bash requirements.sh && bash typoban.sh')
    elif num == ('22') :
        os.system('clear')
        print(Fore.GREEN + ' installer / uninstaller ADB-Termux')
        os.chdir('Termux-ADB')
        print(Fore.GREEN + '[1] - Скачать или [2] - Удалить')
        adbinstall = int(input('[-->]'))
        if adbinstall == (1):
            os.system('bash InstallTools.sh')
        elif adbinstall == (2):
            os.system('bash RemoveTools.sh')
        
    elif num == ('23') :
        print(Fore.GREEN + 'Starting b0mb3r')
        os.system('clear')
        os.chdir('b0mb3r')
        print(Fore.GREEN + '[1] - Установить b0mb3r [2] - Запустить b0mb3r')
        b0mb3r = int(input('[-->]'))
        if b0mb3r == (1):
            os.system('bash requirements.txt && python setup.py')
            os.system('clear')
            os.system('b0mb3r')
        elif b0mb3r == (2):
            os.system('clear')
            os.system('b0mb3r')
    elif num == ('24') :
        print(Fore.GREEN + 'Запуск Tool-X')
        os.system('clear')
        os.chdir('Tool-X')
        print(Fore.GREEN + '[1] - Установить [2] - Запустить')
        starttoolx = int(input('[-->]'))
        if starttoolx == (1):
            os.system('chmod +x install && python install.py')
            os.system('clear')
        elif starttoolx == (2):
            os.system('clear')
            os.system('python Tool-X.py')
        

        

        

        

