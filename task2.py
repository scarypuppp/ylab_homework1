def int32_to_ip(int32):

    ip = []
    bn = bin(int32)[2:]
    bn = '0'*(32 - len(bn)) + bn
    for i in range(4):
        to_dec = int(bn[i*8:8*i+8], 2)
        ip.append(str(to_dec))

    return '.'.join(ip)


assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"
