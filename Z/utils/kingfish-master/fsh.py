import os, sys
print("""
 _  ___             _____
| |/ (_)_ __   __ _|  ___|
| ' /| | '_ \ / _` | |_
| . \| | | | | (_| |  _|
|_|\_\_|_| |_|\__, |_|    
              |___/
""")
print("Starting...")
ports = input("[PORT]: ")
if ports == "":
    ports=8080
os.system("php -S localhost:"+str(ports))
