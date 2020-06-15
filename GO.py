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
print(Fore.GREEN + '[1] - START ROOT [2] - NO START ROOT')

os.chdir('Z')

while True:

    root = int(input('\033[35m[-->]\033[39m'))
    oss = str(input('\033[32m[1]-android\n[2]-linux\n[-->]\033[39m'))
    if oss == ('1'):
        if root == (1):
            try:

                os.system('clear')
                os.system('root su')
                os.system('python3 GO.py')
            except:
                print('-.-')
        elif root == (2):
            os.system('clear')
            os.system('python3 GO.py')
    elif oss == ('2')
        if root == (1):
            try:

                os.system('clear')
                os.system('su')
                os.system('python3 GO.py')
            except:
                print('-.-')
        elif root == (2):
            os.system('clear')
            os.system('python3 GO.py')