# 🕵️ Network Packet Sniffer
Simple Python network packet sniffer using Scapy


> A lightweight Python packet sniffer for capturing, filtering, and analyzing network traffic in real-time. Perfect for learning networking, security labs, or troubleshooting.
## 🔹 Features
- Capture live network packets with Scapy.
- Filter traffic by **TCP**, **UDP**, or **all protocols**.
- Display **source & destination IPs** with protocol info.
- Show **first 50 bytes of payload** for analysis.
- Optionally save captures to **`.pcap` files** for Wireshark.
- Easy CLI interface for quick usage.


## 💻 Requirements
- Python **3.8+**
- Linux/macOS/Windows (raw socket permissions required)
- Python packages:
  - `scapy`
---

## ⚡ Installation

1. **Clone the repo**
   
git clone https://github.com/seema19551/network-packet-sniffer.git
cd network-packet-sniffer


# Install dependencies

pip install -r requirements.txt



*🎯 Example Output

[*] Starting sniffing on interface: eth0

[+] Source: 192.168.0.10 → Destination: 8.8.8.8 | Protocol: UDP
    Payload: b'E\x00\x00...'

[+] Source: 192.168.0.11 → Destination: 192.168.0.1 | Protocol: TCP
    Payload: b'GET / HTTP/1.1\r\nHost: 
