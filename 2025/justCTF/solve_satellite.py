import struct

def hex_to_bytes(hex_string):
    return bytes.fromhex(hex_string)

def tea_decrypt(v0, v1, key0, key1, key2, key3):
    sum_val = 0xC6EF3720
    delta = 0x61C88647
    while sum_val != 0:
        v1 = (v1 - (((v0 << 4) + key2) ^ (v0 + sum_val) ^ ((v0 >> 5) + key3))) & 0xFFFFFFFF
        v0 = (v0 - (((v1 << 4) + key0) ^ (v1 + sum_val) ^ ((v1 >> 5) + key1))) & 0xFFFFFFFF
        sum_val = (sum_val + delta) & 0xFFFFFFFF
    return v0, v1

def decrypt_data(hex_data):
    data_bytes = hex_to_bytes(hex_data)
    key0 = 0x12345678
    key1 = 0x9abcdef0
    key2 = 0x11111111
    key3 = 0x22222222
    decrypted_bytes = []
    for i in range(0, len(data_bytes), 8):
        if i + 7 < len(data_bytes):
            block = data_bytes[i:i+8]
            v0 = struct.unpack('<I', block[0:4])[0]
            v1 = struct.unpack('<I', block[4:8])[0]
            dec_v0, dec_v1 = tea_decrypt(v0, v1, key0, key1, key2, key3)
            dec_block = struct.pack('<II', dec_v0, dec_v1)
            decrypted_bytes.extend(dec_block)
            
    result_printable = ''.join(chr(b) for b in decrypted_bytes if 32 <= b <= 126)
    flag = ''.join(chr(b) for b in decrypted_bytes if b != 0)    
    return flag

hex_data = "5771D410CFFE844D24B50FCBBBDC1973A7A935E5C3468242950DFCCE94794B067F876A215D96EE09"
flag = decrypt_data(hex_data)
print(flag)    
