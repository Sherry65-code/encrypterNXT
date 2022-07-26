from os import system,name
if name == "nt":
    system("cls")
else:
    system("clear")
from time import sleep
print("Welcome to Invento Encryptor NXT")
sleep(1)
print("This program will install required dependencies")
sleep(1)
distroname = input("What is your os name or branch (d for debain based, a for arch based and w for windows) :")
if (distroname == "d"):
    print("Installing dependencies...")
    system("sudo apt update &> /dev/null")
    system("sudo apt install python3-tk python3-pip --assume-yes &> /dev/null")
    system("sudo pip3 install pyperclip &> /dev/null")
elif (distroname == "a"):
    print("Installing Dependencies...")
    system("sudo pacman -Sy python-pip tk --noconfirm &> /dev/null")
    system("sudo pip3 install pyperclip &> /dev/null")
elif (distroname == "w"):
    print("Installing Dependencies...")
    system("pip install pyperclip")
else:
    print("Wrong keyword. Rerun to try again.")
print("Done")