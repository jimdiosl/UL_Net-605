import os
import sys
import time
from unittest import result
from urllib import response

# Define variable tiempo convertido en string para usar al nombrar el archivo de salida
timesrt = time.strftime("%Y%m%d-%H%M%S")
result = (f"result_{timesrt}.txt")

# Verifica el tipo de Sistema Operativo
OS_TYPE = os.name

#Define un contador modificador del tipo de sistema operativo
count = '-n' if OS_TYPE == 'nt' else '-c'

#Creamos función para leer lista de ips desde un archivo .txt
def create_ip_list():
    ip_list = []
    with open("ip_list.txt", "r") as file:
        for line in file:
            ip_list.append(line.strip())
    return ip_list

#Creamos funcion para realir ping a la lista de ips
def ping_device(ip_list):

    results_file = open (result, "w")
    for ip in ip_list:
        response = os.popen(f"ping {ip} {count} 1").read()
        if "recibidos = 1" and "aproximados" in response:
       #if "Received = 1" and "Approximate" in response: #Si el sistema esta en inglés
            print(f"UP {ip} Ping Exitoso")
            results_file.write(f"UP {ip} Ping Successful" + "\n" )
        else:
            print(f"DOWN {ip} Ping No Exitoso")
            results_file.write(f"Down {ip} Ping Unsuccessful" + "\n" )
    
    results_file.close()

if __name__ == "__main__":
    ping_device(create_ip_list())



