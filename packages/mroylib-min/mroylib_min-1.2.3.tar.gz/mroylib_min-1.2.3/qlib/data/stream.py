from zlib import decompress, compress
from base64 import b64encode, b64decode

def check_bal(c):
    if c is str:
        cc = ord(c)
    else:
        cc = c
    bc = bin(cc).split("b")[1]
    b1 = bc.count("1")
    b0 = bc.count("0")
    return abs(b1 - b0)


def lfsr(k, stream):
    last = 0x0
    init_str = b'this is a init xinsd stirng used to general'
    k_l = len(k)
    il = len(init_str)
    for i,v in enumerate(stream):
        c_b = k[i % k_l] 
        if check_bal(c_b) < 2:
            last =  c_b ^ last ^  init_str[i % il]
            yield last ^ v
        else:
            last =  c_b ^ init_str[i % il]
            yield last ^ v

def passpack(passwd, payload):
    if isinstance(payload, str):
        payload = payload.encode('utf8')
    if not isinstance(payload, bytes):
        raise Exception("not suport type , only str or bytes")

    return b64encode(compress( bytes(lfsr(passwd, payload))))

def passunpack(passwd, pack_payload):
    return bytes(lfsr(passwd, decompress(b64decode(pack_payload) ) ))
