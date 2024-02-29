from scapy.all import sniff, IP, TCP


def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto

        print(
            f"Source IP: {src_ip}, Destination IP: {dst_ip}, Protocol: {proto}")

        if proto == 6 and TCP in packet:  # TCP
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            # Use 'original' instead of 'payload'
            payload_data = packet[TCP].original.hex()

            print(f"Source Port: {src_port}, Destination Port: {dst_port}")
            print("Payload Data (hex):", payload_data)


# Start sniffing packets
sniff(prn=packet_callback, store=0)
