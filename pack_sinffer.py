from scapy.all import sniff, IP, TCP, UDP, Raw

def packet_callback(packet):
    if IP in packet:
        protocol = "Other"
        if TCP in packet:
            protocol = "TCP"
        elif UDP in packet:
            protocol = "UDP"

        print(f"\n[+] Source: {packet[IP].src} → Destination: {packet[IP].dst} | Protocol: {protocol}")
        
        # Print payload if available
        if Raw in packet:
            try:
                payload = packet[Raw].load
                print(f"    Payload: {payload[:50]}")  # Print first 50 bytes only
            except:
                print("    Payload: [Unable to decode]")

# Start sniffing packets (you can increase count or remove it for continuous sniffing)
sniff(prn=packet_callback, count=10)