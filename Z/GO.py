import os
import colorama
from colorama import Fore , Back , Style
from colorama import init
init()
os.system('clear')
print(Fore.GREEN +
""" ____  ____                  
/_  / / __/______ ___ _  ___ 
 / /_/ _// __/ _ `/  ' \/ -_)
/___/_/ /_/  \_,_/_/_/_/\__/ 
                            """)
print(Fore.GREEN+'Enter Lang :')
print("\033[31m[\033[33m1\033[31m] - RUS/РУС")
print("\033[31m[\033[33m2\033[31m] - ENG/АНГ")
os.chdir('Z')
while True:
    lag = input("\033[35m\033[5m[*]")
    if lag == ('1'):
        os.system('clear')
        os.system('python3 Zru.py')
    elif lag == ('2'):
        os.system('clear')
        os.system('python3 Zen.py')
    else :
        print("\33[31mRETURN")
