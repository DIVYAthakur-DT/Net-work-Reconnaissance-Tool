import nmap
import pyfiglet
from termcolor import colored
import datetime


banner = pyfiglet.figlet_format("PORT SCANNER")
print(colored(banner, "cyan"))

print(colored("Advanced Nmap Automation Tool", "green"))
print("<---------------------------------------------------->")


scanner = nmap.PortScanner()


ip_addr = input(colored("Enter the IP address you want to scan: ", "yellow"))
print(colored(f"Target IP: {ip_addr}", "magenta"))


print(colored(f"Scan started at: {datetime.datetime.now()}", "blue"))


print("""
Select Scan Type

1. SYN Scan
2. TCP Connect Scan
3. UDP Scan
4. Ping Scan
5. Service Version Detection
6. OS Detection
7. Aggressive Scan
8. XMAS Scan
9. Comprehensive Scan
""")

choice = input(colored("Enter your choice: ", "yellow"))


if choice == '1':
    print(colored("Running SYN Scan...", "green"))
    scanner.scan(ip_addr, '1-1024', '-sS')

elif choice == '2':
    print(colored("Running TCP Connect Scan...", "green"))
    scanner.scan(ip_addr, '1-1024', '-sT')

elif choice == '3':
    print(colored("Running UDP Scan...", "green"))
    scanner.scan(ip_addr, '1-1024', '-sU')

elif choice == '4':
    print(colored("Running Ping Scan...", "green"))
    scanner.scan(ip_addr, arguments='-sn')

elif choice == '5':
    print(colored("Running Service Version Detection...", "green"))
    scanner.scan(ip_addr, '1-1024', '-sV')

elif choice == '6':
    print(colored("Running OS Detection...", "green"))
    scanner.scan(ip_addr, arguments='-O')

elif choice == '7':
    print(colored("Running Aggressive Scan...", "green"))
    scanner.scan(ip_addr, arguments='-A')

elif choice == '8':
    print(colored("Running XMAS Scan...", "green"))
    scanner.scan(ip_addr, '1-1024', '-sX')

elif choice == '9':
    print(colored("Running Comprehensive Scan...", "green"))
    scanner.scan(ip_addr, '1-1024', '-sS -sV -sC -O -A')

else:
    print(colored("Invalid option selected", "red"))
    exit()


print("\nScan Information:", scanner.scaninfo())


for host in scanner.all_hosts():

    print(colored(f"\nHost: {host}", "cyan"))
    print("State:", scanner[host].state())

    for proto in scanner[host].all_protocols():

        print(colored(f"\nProtocol: {proto}", "yellow"))

        ports = scanner[host][proto].keys()

        for port in sorted(ports):

            state = scanner[host][proto][port]['state']
            service = scanner[host][proto][port]['name']

            print(f"Port {port} | State: {state} | Service: {service}")

print(colored("\nScan Completed.", "green"))