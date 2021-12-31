def class_checker(first_octet):
    if 0 <= int(first_octet) <= 127:
        IP_class = "A"
    elif 128 <= int(first_octet) <= 191:
        IP_class = "B"
    elif 192 <= int(first_octet) <= 223:
        IP_class = "C"
    elif 224 <= int(first_octet) <= 239:
        IP_class = "D"
    elif 240 <= int(first_octet) <= 255:
        IP_class = "E"
    else:
        IP_class = "Not Found"
    return IP_class

def network_and_host_checker(IP_s):
    IP_class = class_checker(IP_s[0])
    IP_d = []
    if IP_class == "A":
        IP_d.append([IP_s[0]])
        IP_d.append([IP_s[1], IP_s[2], IP_s[3]])
    elif IP_class == "B":
        IP_d.append([IP_s[0], IP_s[1]])
        IP_d.append([IP_s[2], IP_s[3]])
    elif IP_class == "C":
        IP_d.append([IP_s[0], IP_s[1], IP_s[2]])
        IP_d.append([IP_s[3]])
    else:
        print("Other classes can't be used here.")
    return IP_d

def network_IP(IP_s):
    netNhost = network_and_host_checker(IP_s)
    if len(netNhost[1]) == 1:
        netNhost[1][0] = 0
        data = f"{netNhost[0][0]}.{netNhost[0][1]}.{netNhost[0][2]}.{netNhost[1][0]}"
    elif len(netNhost[1]) == 2:
        netNhost[1][0] = 0
        netNhost[1][1] = 0
        data = f"{netNhost[0][0]}.{netNhost[0][1]}.{netNhost[1][0]}.{netNhost[1][1]}"
    elif len(netNhost[1]) == 3:
        netNhost[1][0] = 0
        netNhost[1][1] = 0
        netNhost[1][2] = 0
        data = f"{netNhost[0][0]}.{netNhost[1][0]}.{netNhost[1][1]}.{netNhost[1][2]}"
    return data

def broadcast_IP(IP_s):
    netNhost = network_and_host_checker(IP_s)
    if len(netNhost[1]) == 1:
        netNhost[1][0] = 255
        data = f"{netNhost[0][0]}.{netNhost[0][1]}.{netNhost[0][2]}.{netNhost[1][0]}"
    elif len(netNhost[1]) == 2:
        netNhost[1][0] = 255
        netNhost[1][1] = 255
        data = f"{netNhost[0][0]}.{netNhost[0][1]}.{netNhost[1][0]}.{netNhost[1][1]}"
    elif len(netNhost[1]) == 3:
        netNhost[1][0] = 255
        netNhost[1][1] = 255
        netNhost[1][2] = 255
        data = f"{netNhost[0][0]}.{netNhost[1][0]}.{netNhost[1][1]}.{netNhost[1][2]}"
    return data

def numberOfNetworks(IP_s):
    IP_class = class_checker(IP_s[0])
    if IP_class == "A":
        data = (2 ** 7) - 2
    elif IP_class == "B":
        data = 2 ** 14
    elif IP_class == "C":
        data = 2 ** 21

    return data

def numberOfHosts(IP_s):
    IP_class = class_checker(IP_s[0])
    if IP_class == "A":
        data = (2 ** 24) - 2
    elif IP_class == "B":
        data = (2 ** 16) - 2
    elif IP_class == "C":
        data = (2 ** 8) - 2

    return data

def subnet_mask(IP_s, subs):
    IP_class = class_checker(IP_s[0])
    for i in range(1,1000):
        if subs == 2 ** i:
            subnets = i
        elif subs >= 2 ** i and subs < 2 ** (i+1):
            subnets = i + 1
    netNhost = network_and_host_checker(IP_s)
    if len(netNhost[1]) == 1:
        netNhost[0][0] = "11111111"
        netNhost[0][1] = "11111111"
        netNhost[0][2] = "11111111"
        netNhost[1][0] = "00000000"
        IP = f"{netNhost[0][0]}.{netNhost[0][1]}.{netNhost[0][2]}.{netNhost[1][0]}"
    elif len(netNhost[1]) == 2:
        netNhost[0][0] = "11111111"
        netNhost[0][1] = "11111111"
        netNhost[1][0] = "00000000"
        netNhost[1][1] = "00000000"
        IP = f"{netNhost[0][0]}.{netNhost[0][1]}.{netNhost[1][0]}.{netNhost[1][1]}"
    elif len(netNhost[1]) == 3:
        netNhost[0][0] = "11111111"
        netNhost[1][0] = "00000000"
        netNhost[1][1] = "00000000"
        netNhost[1][2] = "00000000"
        IP = f"{netNhost[0][0]}.{netNhost[1][0]}.{netNhost[1][1]}.{netNhost[1][2]}"
    IP = IP.split(".")
    if len(netNhost[1]) == 1:
        IP[3] = ( subnets * "1" ) + IP[3][subnets:]
    elif len(netNhost[1]) == 2:
        if subnets <= 8:
            IP[2] = ( subnets * "1" ) + IP[2][subnets:]
        else:
            IP[2] = ( 8 * "1" ) + IP[2][subnets:]
            IP[3] = ( (subnets - 8) * "1" ) + IP[3][subnets:]
    elif len(netNhost[1]) == 3:
        if subnets <= 8:
            IP[2] = ( subnets * "1" ) + IP[2][subnets:]
        elif subnets <= 16:
            IP[2] = ( 8 * "1" ) + IP[2][subnets:]
            IP[3] = ( (subnets - 8) * "1" ) + IP[3][subnets:]
        elif subnets <= 24:
            IP[2] = ( 8 * "1" ) + IP[2][subnets:]
            IP[3] = ( 8 * "1" ) + IP[3][subnets:]
            IP[4] = ( (subnets - 16) * "1" ) + IP[4][subnets:]
    if IP_class == "A": 
        S_M = IP
        S_M[0] = 255
        S_M[1] = int(S_M[1], 2)
        S_M[2] = int(S_M[2], 2)
        S_M[3] = int(S_M[3], 2)
    elif IP_class == "B": 
        S_M = IP
        S_M[0] = 255
        S_M[1] = 255
        S_M[2] = int(S_M[2], 2)
        S_M[3] = int(S_M[3], 2)
    elif IP_class == "C": 
        S_M = IP
        S_M[0] = 255
        S_M[1] = 255
        S_M[2] = 255
        S_M[3] = int(S_M[3], 2)
    return S_M
        
def subnet_ip(IP_s, subs):
    IP = network_and_host_checker(IP_s)
    IP_class = class_checker(IP_s[0])

    if len(IP[1]) == 1:
        a = int(IP[1][0])
        bnr = bin(a).replace('0b','')
        x = bnr[::-1]
        while len(x) < 8:
            x += '0'
        bnr = x[::-1]
        IP[1][0] = bnr

        IP = f"{IP[0][0]}.{IP[0][1]}.{IP[0][2]}.{IP[1][0]}"
        IP = IP.split(".")

    elif len(IP[1]) == 2:
        a = int(IP[1][0])
        bnr = bin(a).replace('0b','')
        x = bnr[::-1]
        while len(x) < 8:
            x += '0'
        bnr = x[::-1]
        IP[1][0] = bnr

        a = int(IP[1][1])
        bnr = bin(a).replace('0b','')
        x = bnr[::-1]
        while len(x) < 8:
            x += '0'
        bnr = x[::-1]
        IP[1][1] = bnr

        IP = f"{IP[0][0]}.{IP[0][1]}.{IP[1][0]}.{IP[1][1]}"
        IP = IP.split(".")

    elif len(IP[1]) == 3:
        a = int(IP[1][0])
        bnr = bin(a).replace('0b','')
        x = bnr[::-1]
        while len(x) < 8:
            x += '0'
        bnr = x[::-1]
        IP[1][0] = bnr

        a = int(IP[1][1])
        bnr = bin(a).replace('0b','')
        x = bnr[::-1]
        while len(x) < 8:
            x += '0'
        bnr = x[::-1]
        IP[1][1] = bnr

        a = int(IP[1][2])
        bnr = bin(a).replace('0b','')
        x = bnr[::-1]
        while len(x) < 8:
            x += '0'
        bnr = x[::-1]
        IP[1][2] = bnr

        IP = f"{IP[0][0]}.{IP[1][0]}.{IP[1][1]}.{IP[1][2]}"
        IP = IP.split(".")
    S_M = subnet_mask(IP_s, subs)
    if IP_class == "A":
        a = S_M[1]
        bnr = bin(a).replace('0b','')
        x = bnr[::-1]
        while len(x) < 8:
            x += '0'
        bnr = x[::-1]
        S_M[1] = bnr

        a = S_M[2]
        bnr = bin(a).replace('0b','')
        x = bnr[::-1]
        while len(x) < 8:
            x += '0'
        bnr = x[::-1]
        S_M[2] = bnr

        a = S_M[3]
        bnr = bin(a).replace('0b','')
        x = bnr[::-1]
        while len(x) < 8:
            x += '0'
        bnr = x[::-1]
        S_M[3] = bnr
    elif IP_class == "B":
        a = S_M[2]
        bnr = bin(a).replace('0b','')
        x = bnr[::-1]
        while len(x) < 8:
            x += '0'
        bnr = x[::-1]
        S_M[2] = bnr

        a = S_M[3]
        bnr = bin(a).replace('0b','')
        x = bnr[::-1]
        while len(x) < 8:
            x += '0'
        bnr = x[::-1]
        S_M[3] = bnr

    elif IP_class == "C":
        a = S_M[3]
        bnr = bin(a).replace('0b','')
        x = bnr[::-1]
        while len(x) < 8:
            x += '0'
        bnr = x[::-1]
        S_M[3] = bnr

    netNhost = network_and_host_checker(IP_s)
    if len(netNhost[1]) == 1:
        a = int(netNhost[1][0])
        bnr = bin(a).replace('0b','')
        x = bnr[::-1]
        while len(x) < 8:
            x += '0'
        bnr = x[::-1]
        netNhost[1][0] = bnr
        IP = f"{netNhost[0][0]}.{netNhost[0][1]}.{netNhost[0][2]}.{netNhost[1][0]}"
    elif len(netNhost[1]) == 2:
        a = int(netNhost[1][0])
        bnr = bin(a).replace('0b','')
        x = bnr[::-1]
        while len(x) < 8:
            x += '0'
        bnr = x[::-1]
        netNhost[1][0] = bnr

        a = int(netNhost[1][1])
        bnr = bin(a).replace('0b','')
        x = bnr[::-1]
        while len(x) < 8:
            x += '0'
        bnr = x[::-1]
        netNhost[1][1] = bnr

        IP = f"{netNhost[0][0]}.{netNhost[0][1]}.{netNhost[1][0]}.{netNhost[1][1]}"
    elif len(netNhost[1]) == 3:
        a = int(netNhost[1][0])
        bnr = bin(a).replace('0b','')
        x = bnr[::-1]
        while len(x) < 8:
            x += '0'
        bnr = x[::-1]
        netNhost[1][0] = bnr

        a = int(netNhost[1][1])
        bnr = bin(a).replace('0b','')
        x = bnr[::-1]
        while len(x) < 8:
            x += '0'
        bnr = x[::-1]
        netNhost[1][1] = bnr

        a = int(netNhost[1][2])
        bnr = bin(a).replace('0b','')
        x = bnr[::-1]
        while len(x) < 8:
            x += '0'
        bnr = x[::-1]
        netNhost[1][2] = bnr
        
        IP = f"{netNhost[0][0]}.{netNhost[1][0]}.{netNhost[1][1]}.{netNhost[1][2]}"
    IP = IP.split(".")
    
    if IP_class == "A":
        d1 = []
        d2 = []
        d3 = []

        D1 = ""
        D2 = ""
        D3 = ""
        
        S_M_1 = [char for char in S_M[1]]
        S_M_2 = [char for char in S_M[2]]
        S_M_3 = [char for char in S_M[3]]

        IP_1 = [char for char in IP[1]]
        IP_2 = [char for char in IP[2]]
        IP_3 = [char for char in IP[3]]

        for i in range(8):
            d1.append(int(S_M_1[i]) * int(IP_1[i]))
            d2.append(int(S_M_2[i]) * int(IP_2[i]))
            d3.append(int(S_M_3[i]) * int(IP_3[i]))
        for i in range(8):
            D1 += str(d1[i])
            D2 += str(d2[i])
            D3 += str(d3[i])

        subnet_IP = f"{IP[0]}.{int(D1, 2)}.{int(D2, 2)}.{int(D3, 2)}"
    elif IP_class == "B":
        d1 = []
        d2 = []

        D1 = ""
        D2 = ""

        S_M_1 = [char for char in S_M[2]]
        S_M_2 = [char for char in S_M[3]]

        IP_1 = [char for char in IP[2]]
        IP_2 = [char for char in IP[3]]
        for i in range(8):
            d1.append(int(S_M_1[i]) * int(IP_1[i]))
            d2.append(int(S_M_2[i]) * int(IP_2[i]))
        for i in range(8):
            D1 += str(d1[i])
            D2 += str(d2[i])
        
        subnet_IP = f"{IP[0]}.{IP[1]}.{int(D1, 2)}.{int(D2, 2)}"
    elif IP_class == "C":
        d1 = []

        D1 = ""

        S_M_1 = [char for char in S_M[3]]

        IP_1 = [char for char in IP[3]]
        for i in range(8):
            d1.append(int(S_M_1[i]) * int(IP_1[i]))
        subnet_IP = f"{IP[0]}.{IP[1]}.{IP[2]}.{int(D1, 2)}"
    return subnet_IP