def Load():
    try:
        with open("ip.txt", 'r') as i:
            ip_list = {}
            for line in i:
                parts = line.strip().split('\t')
                if len(parts) == 1:
                    parts = line.strip().split(' ')
                if len(parts) == 1:
                    parts = line.strip().split(',')
                if len(parts) == 2:
                    ip, domain = parts
                    ip_list[ip] = domain
            return ip_list
    except FileNotFoundError:
        print("File doesnt exist")


def is_private():
    ip_list = Load()
    private_ip = {}
    for ip in ip_list:
        ip_pieces = ip.split('.')
        if ip_pieces[0] == '10' or (ip_pieces[0] == '172' and 16 <= int(ip_pieces[1]) <= 31) or (
                ip_pieces[0] == '192' and ip_pieces[1] == '168'):
            private_ip[ip] = True
        else:
            private_ip[ip] = False
    return private_ip


def is_valid():
    ip_list = Load()
    valid_ip = {}
    for ip in ip_list:
        ip_pieces = ip.split('.')
        for piece in ip_pieces:
            if 0 <= int(piece) <= 255 and len(ip_pieces) == 4:
                valid_ip[ip] = True
            else:
                valid_ip[ip] = False
                break
    return valid_ip


def private_valid():
    ip_list = Load()
    private_ips = is_private()
    valid_ips = is_valid()
    private_and_valid = {}
    for ip in private_ips:
        if private_ips[ip] == True and valid_ips[ip] == True:
            private_and_valid[ip] = ip_list[ip]
    print("\nPrivate and valid IPs:\n")
    for ip in private_and_valid:
        print(f"{ip} {private_and_valid[ip]}")
    print()
    print('*' * 80)


def public_valid():
    ip_list = Load()
    private_ips = is_private()
    valid_ips = is_valid()
    public_and_valid = {}
    for ip in private_ips:
        if private_ips[ip] == False and valid_ips[ip] == True:
            public_and_valid[ip] = ip_list[ip]
    print("\nPublic and valid IPs:\n")
    for ip in public_and_valid:
        print(f"{ip} {public_and_valid[ip]}")
    print()
    print('*' * 80)


def unique_domains():
    ip_list = Load()
    domains = set()
    for ip in ip_list:
        domain = ip_list[ip]
        domains.add(domain)
    print("\nUnique domains: \n")
    for domain in domains:
        print(domain)
    print()
    print('*' * 80)


def unique_ips():
    ip_list = is_valid()
    ips = set()
    for ip in ip_list:
        if ip_list[ip]:
            ips.add(ip)
    print("\nUnique IPs: \n")
    for ip in ips:
        print(ip)
    print()
    print('*' * 80)


private_valid()
public_valid()
unique_domains()
unique_ips()
