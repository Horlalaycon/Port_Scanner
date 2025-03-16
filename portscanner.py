import socket
import threading
import time
from colorama import init, Fore, Back, Style
import argparse
import re

# initialize colorama
init()

# domain name option processing
def convert_domain_name(domain):
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(1)
		ip = socket.gethostbyname(domain)
		pattern= r"(\d+\.\d+\.\d+\.\d+)"
		match = re.search(pattern, ip)
		match_result = match.group(1)
		return match_result

	except socket.gaierror as e:
		print(Fore.RED + f" Error: Incorrect domain name, ({e})")
		quit()

# CLI options
parser = argparse.ArgumentParser(prog="portscanner.py", description="A Program used to detect open ports on networks", epilog="Example: (portscanner.py -ip 1.2.3.4) / (portscanner.py -d hey.com)", formatter_class=argparse.RawTextHelpFormatter)

# One of the two options must be selected
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-ip", "--ip_addr", help="Specify Target's IP address to geolocate", )
group.add_argument("-d", "--domain", help="Specify Target's Domain name to geolocate")
args = parser.parse_args()

if args.domain:
	target = convert_domain_name(args.domain)

else:
	# check if ip address is correct
	target_pattern = r"(\d+\.\d+\.\d+\.\d+)"
	target_match = re.search(target_pattern, args.ip_addr)
	if target_match:
		target_match_result = target_match.group(1)
		target = target_match_result
	else:
		print(Fore.RED + f" Error: Invalid IP address")
		quit()


def scan_instance1():
	ports = [21, 22, 23, 25, 53, 80, 443, 110, 143, 161, 445, 3389, 137, 138, 631, 1700, 5060, 6881, 6889, 7042]
	for port in ports:
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			# set timeout
			sock.settimeout(2)
			result = sock.connect_ex((target, port))

			# if port is open
			if result == 0:
				state = "Open"
				service = socket.getservbyport(port)
				# output
				print(Style.DIM + f"\r         {port}     {state}      {service}")
			sock.close()

		except OSError:
			print(Style.DIM + f"\r         {port}      Open       Unknown")



def scan_instance2():
	ports = [3306, 5432, 1433, 27017, 8080, 8443, 8000, 9000, 7777, 27015, 25565, 27005, 27016, 1935, 5000, 5000]
	for port in ports:
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			# set timeout
			sock.settimeout(2)
			result = sock.connect_ex((target, port))

			# if port is open
			if result == 0:
				state = "Open"
				service = socket.getservbyport(port)
				# output
				print(Style.DIM + f"\r         {port}     {state}      {service}")
			sock.close()

		except OSError:
			print(Style.DIM + f"\r         {port}      Open       Unknown")



def scan_instance3():
	ports = [857, 2121, 4444, 8888]
	for port in ports:
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			# set timeout
			sock.settimeout(2)
			result = sock.connect_ex((target, port))

			# if port is open
			if result == 0:
				state = "Open"
				service = socket.getservbyport(port)
				# output
				print(Style.DIM + f"\r         {port}     {state}      {service}")
			sock.close()

		except OSError:
			print(Style.DIM + f"\r         {port}      Open       Unknown")


def thread_scan():
	threads = []

	for i in range(3):
		if i == 0:
			thread = threading.Thread(target=scan_instance1)
		elif i == 1:
			thread = threading.Thread(target=scan_instance2)
		else:
			thread = threading.Thread(target=scan_instance3)

		threads.append(thread)
		thread.start()
		# wait for all threads to finish
		for thread in threads:
			thread.join()

def main():
	# banner
	print(Back.WHITE + Fore.BLACK + Style.BRIGHT + "            Network Port Scanner            " + Style.RESET_ALL)
	print(Back.WHITE + Fore.BLACK + Style.BRIGHT + "       By: Sys Br3ach3r                     " + Style.RESET_ALL)

	print(f'\n [+] Scanning [{Fore.LIGHTGREEN_EX + target + Style.BRIGHT + Style.RESET_ALL}] ports...')
	print(Style.BRIGHT + Fore.CYAN + f"        Ports   State   Services" + Style.RESET_ALL)

	start = time.perf_counter()
	thread_scan()
	finish = time.perf_counter()

	print(Back.WHITE + Fore.BLACK + Style.BRIGHT + f"   Finished in: {round(finish - start, 2)} seconds        " + Style.RESET_ALL)


if __name__ == "__main__":
	try:
		main()

	except KeyboardInterrupt:
		print(f"Aborting (Ctrl + C)")
		quit()