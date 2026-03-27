import ipaddress

print("=== Simple IP Analyzer ===")

ip = input("Enter an IP address: ")

try:
    ip_obj = ipaddress.IPv4Address(ip)
    parts = ip.split('.')
    first = int(parts[0])
    second = int(parts[1])

    # Default values
    ip_class = ""
    subnet = ""
    ip_type = ""
    usable = ""

    # -------- Special Cases --------
    if ip == "0.0.0.0":
        ip_class = "Invalid"
        subnet = "N/A"
        ip_type = "Special"
        usable = "No"

    elif ip == "255.255.255.255":
        ip_class = "Broadcast"
        subnet = "N/A"
        ip_type = "Special"
        usable = "No"

    elif first == 127:
        ip_class = "Loopback"
        subnet = "255.0.0.0"
        ip_type = "Private"
        usable = "No"

    elif first == 169 and second == 254:
        ip_class = "APIPA"
        subnet = "255.255.0.0"
        ip_type = "Private"
        usable = "Limited"

    # -------- Normal IP --------
    else:
        # Class + subnet
        if first <= 126:
            ip_class = "Class A"
            subnet = "255.0.0.0"
        elif first <= 191:
            ip_class = "Class B"
            subnet = "255.255.0.0"
        elif first <= 223:
            ip_class = "Class C"
            subnet = "255.255.255.0"
        else:
            ip_class = "Class D/E"
            subnet = "N/A"

        # Private or Public
        if ip_obj.is_private:
            ip_type = "Private"
        else:
            ip_type = "Public"

        # Usable check
        if subnet != "N/A":
            net = ipaddress.IPv4Network(ip + "/" + subnet, strict=False)

            if ip_obj == net.network_address:
                usable = "No (Network)"
            elif ip_obj == net.broadcast_address:
                usable = "No (Broadcast)"
            else:
                usable = "Yes"
        else:
            usable = "No"

    # -------- Output --------
    print("\n--- Result ---")
    print("IP:", ip)
    print("Class:", ip_class)
    print("Subnet:", subnet)
    print("Type:", ip_type)
    print("Usable:", usable)

except:
    print("Invalid IP address")
