import sys
import re
import socket
import pyfiglet
from datetime import datetime
import colorama
from colorama import *
colorama.init()

print(Fore.LIGHTMAGENTA_EX + "-" * 70)
print(pyfiglet.figlet_format("PORT SCANNER"))
print("Time started: " + str(datetime.now()))
print("made by SSMV")
print("-" * 70)

regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
target = input(str("Enter target ip: "))
in_port = input("Enter port (optional): ")
in_range = input("Enter range (optional) [Syntax: n-m]: ")
if in_range:
    in_range = in_range.split("-")
    in_range[1] = str(int(in_range[1]) + 1)

def check():
    if re.search(regex, target):
        return "valid_ip"
    else:
        return "invalid_ip"

def default_func(rng1, rng2):
    try:
        for port in range(int(rng1), int(rng2)):
            print(Fore.LIGHTMAGENTA_EX + f"Checking port {port}...")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)
            check = s.connect_ex((target, port))
            if check == 0:
                print(Fore.LIGHTGREEN_EX + f"Port {port} is open.")
            s.close()

    except KeyboardInterrupt:
        print(Fore.YELLOW + "Keyboard interruption. \nExiting...")
        sys.exit()

    except socket.gaierror:
        print(Fore.YELLOW + "Host is not responding... \nExiting...")
        sys.exit()

    except socket.error:
        print("Socket Error Occurred. \nExiting...")
        sys.exit()

if check() == "valid_ip":
    if in_range and in_port:
        default_func(in_port, int(in_port) + 1)
        default_func(in_range[0], in_range[1])
    elif in_range:
        default_func(in_range[0], in_range[1])
    elif in_port:
        default_func(in_port, int(in_port) + 1)
    else: 
        default_func(1, 65535)
else:
    print(Fore.RED + "Invalid IP address. \nPlease retry.")    