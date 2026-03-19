# Network Reconnaissance Tool

A Python-based network scanning tool that automates various **Nmap scans** for network reconnaissance and security analysis.
This project demonstrates fundamental cybersecurity concepts such as port scanning, service detection, OS fingerprinting, and vulnerability discovery.

---

## Features

* Multiple scan types using Nmap:

  * SYN Scan
  * UDP Scan
  * Comprehensive Scan
  * OS Detection
  * Version Detection
  * Aggressive Scan
* Automated scanning using Python
* Interactive CLI interface
* Displays open ports and protocols
* Banner output using `pyfiglet`
* Colored terminal output using `termcolor`

---

## Technologies Used

* Python
* Nmap
* python-nmap
* pyfiglet
* termcolor

---

## Installation

### 1. Install Nmap

#### Kali Linux

```bash
sudo apt install nmap
```

#### Windows

Download from: https://nmap.org/download.html

---

### 2. Clone the Repository

```bash
git clone https://github.com/DIVYAthakur-DT/network-reconnaissance-tool.git
cd network-reconnaissance-tool
```

---

### 3. Create Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate   # Linux/Kali
venv\Scripts\activate      # Windows
```

---

### 4. Install Requirements

```bash
pip install -r requirements.txt
```

---

## Usage

Run the tool:

```bash
python Networkscanner.py
```

Enter the target IP address and select the scan type:

```text
1. SYN ACK Scan
2. UDP Scan
3. Comprehensive Scan
```

---

## Example Output

```
Welcome, this is a simple Nmap automation tool
---------------------------------------------

Enter IP: 192.168.1.1
Selected: Comprehensive Scan

Open ports: [22, 80, 443]
Protocol: TCP
State: up
```

---

## Scan Types Explained

| Scan Type          | Description                                       |
| ------------------ | ------------------------------------------------- |
| SYN Scan           | Fast and stealthy scan to detect open ports       |
| UDP Scan           | Detects UDP services                              |
| Comprehensive Scan | Includes version detection, scripts, OS detection |
| OS Detection       | Identifies operating system                       |
| Version Detection  | Detects service versions                          |
| Aggressive Scan    | Combines multiple scan techniques                 |

---

## Project Structure

```
network-reconnaissance-tool
│
├── Networkscanner.py
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

## Security Concepts Demonstrated

* Network Reconnaissance
* Port Scanning Techniques
* Service Enumeration
* OS Fingerprinting
* Ethical Hacking Basics

---

## Disclaimer

This tool is developed for **educational purposes only**.
Do not use it on networks without proper authorization.

---

## Author

DIVYA

GitHub: https://github.com/DIVYAthakur-DT
