#!/usr/bin/python


import sys
import socket
import threading
import time

global target

try:
    # target host name or ip address
    if len(sys.argv[1]) > 1:
        target = sys.argv[1]

except IndexError:
    print("  ")
    print(f'+------------------------------------------------+')
    print(f"|          Error!! No Target Specified           |")
    print(f'+------------------------------------------------+')
    print(f'| Syntax: (python port_scanner.py target_ip/dns) |')
    print(f'+------------------------------------------------+')
    quit()


def scan_port_1():
    port1 = [21, 22, 23, 25, 53, 80, 443, 110, 143, 161, 445, 3389, 137, 138, 631, 1700, 5060, 6881, 6889, 7042,]
    for port in port1:
        try:
            # Create socket object
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # set timeout
            sock.settimeout(1)

            # connect to target to detect port, send SYN packet
            result = sock.connect_ex((target, port))

            if result == 0:
                service = socket.getservbyport(port, 'tcp')
                state = 'Open'
                print(f'  {port}       {state}      {service}')

            sock.close()
        except socket.gaierror:
            pass
        except OSError:
            print(f'  {port}      Open      Unknown')


def scan_port_2():
    port2 = [3306, 5432, 1433, 27017, 8080, 8443, 8000, 9000, 7777, 27015, 25565, 27005, 27016, 1935, 5000, 5000]
    for port in port2:
        try:
            # Create socket object
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # set timeout
            sock.settimeout(1)

            # connect to target to detect port, send SYN packet
            result = sock.connect_ex((target, port))

            if result == 0:
                service = socket.getservbyport(port, 'tcp')
                state = 'Open'
                print(f'  {port}       {state}      {service}')

            sock.close()
        except socket.gaierror:
            pass
        except OSError:
            print(f'  {port}      Open      Unknown')


def scan_port_3():
    port3 = [857, 2121, 4444, 8888]
    for port in port3:
        try:
            # Create socket object
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # set timeout
            sock.settimeout(1)

            # connect to target to detect port, send SYN packet
            result = sock.connect_ex((target, port))

            if result == 0:
                service = socket.getservbyport(port, 'tcp')
                state = 'Open'
                print(f'  {port}       {state}      {service}')

            sock.close()
        except socket.gaierror:
            pass
        except OSError:
            print(f'  {port}      Open      Unknown')


def thread_scan():
    # create and start threads
    threads = []
    # for i in range(6):
    for i in range(3):
        if i == 0:
            thread = threading.Thread(target=scan_port_1)
        elif i == 1:
            thread = threading.Thread(target=scan_port_2)
        else:
            thread = threading.Thread(target=scan_port_3)

        threads.append(thread)
        thread.start()

    # wait for all threads to finish
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    try:
        # resolve dns
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        ip = socket.gethostbyname(target)

        print(f'\nScanning [{ip}] for open ports[+]...\n')

        print(f'+------------------------------+')
        print(f'| Port     State     Service   |')
        print(f'+------------------------------+')

        start = time.perf_counter()
        thread_scan()
        finish = time.perf_counter()

        print(f'+------------------------------+')
        print(f'\n Finished in {round(finish - start, 2)} second(s)')
        print(f'+------------------------------+')

    except socket.gaierror:
        print('\n [Error!] unable to resolve hostname, Check network Connection\n')

    except EnvironmentError:
        print(' Error Please check Network Connection')

    except KeyboardInterrupt:
        print(' Aborting... (Ctrl+c)')
        quit()
