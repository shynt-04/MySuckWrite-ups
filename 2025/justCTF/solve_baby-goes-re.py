binary_path = 'baby-goes-re'
file_offset = 0xCB6D5              

with open(binary_path, 'rb') as f:
    f.seek(file_offset)
    data = f.read(0x52AE4)

result_flag = []
flag_len = 0x35
v5 = 0
v4 = 0

for _ in range(flag_len):
    # 0x1337 = 4919
    index = v5 + v4 + 4919
    print(chr(data[index]), end='')
    # 0x1338 = 4920
    # 0x33 = 51
    next_v4 = v5 + v4 + 4920
    next_v5 = v5 + 51
    
    v4 = next_v4
    v5 = next_v5