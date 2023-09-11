import binascii  

f = open("./password_checker.smol", "rb").read()

rbp = []
for i in range(25):
    rbp.append(0)

rbp_24 = []
for i in range(1000):
    rbp_24.append(0)
offset_24 = 500
rbp_16 = 0

print(f[4])
ptr = 4
while(ptr < len(f)):
    offset1 = f[ptr+1]*4
    offset2 = f[ptr+2]*4
    # print(f"{f[ptr]} {f[ptr+1]} {f[ptr+2]} {chr(f[ptr+3])}")
    if f[ptr] == 0x0:
        print(f"MOV *[rbp+{offset1}] = *[rbp+{offset2}]")
        rbp[offset1] = rbp[offset2]
        print(f"*[rbp+{offset1}] = {rbp[offset1]}")
    if f[ptr] == 0x1 or f[ptr] == 0x2:
        print(f"ADD *[rbp+{offset1}] += *[rbp+{offset2}] + {f[ptr+3]}")
        rbp[offset1] += rbp[offset2] + f[ptr+3]
        print(f"*[rbp+{offset1}] = {rbp[offset1]}")
    if f[ptr] == 0x3:
        print(f"PRINT *[rbp+{offset1}]")
    if f[ptr] == 0x4:
        print(f"MOV *[rbp+{offset1}] = {f[ptr+3]}")
        rbp[offset1] = f[ptr+3]
        print(f"*[rbp+{offset1}] = {rbp[offset1]}")
    if f[ptr] == 0x5:
        print(f"ADD *[rbp+24] += 8 THEN MOV **[rbp+24] = [rbp+{offset2}] = {rbp[offset2]}")
        offset_24 += 8
        rbp_24[offset_24] = rbp[offset2]
    if f[ptr] == 0x6:
        print(f"MOV *[rbp+{offset1}] = **[rbp+24] THEN SUB *[rbp+24] -= 8")
        rbp[offset1] = rbp_24[offset_24]
        offset_24 -= 8
        print(f"*[rbp+{offset1}] = {rbp[offset1]}")
    if f[ptr] == 0x7:
        print(f"SUB *[rbp+16] = *[rbp+{offset1}] - [rbp+{offset2}] = {rbp[offset1] - rbp[offset2]}")
        rbp_16 = rbp[offset1] - rbp[offset2]
    if f[ptr] == 0x8:
        print(f"LSEEK {f[ptr+2] * 256 + f[ptr+3]} bytes")
        if rbp_16 == 0:
            ptr += f[ptr+2] * 256 + f[ptr+3]
            continue
    if f[ptr] == 0x9:
        print(f"WRITE {f[ptr+3]} bytes of **[rbp+24]")
        hex_string = hex(rbp_24[offset_24])[2:]
        print(hex_string)
    if f[ptr] == 0xa:
        print(f"MUL *[rbp+{offset1}] *= *[rbp+{offset2}] THEN ADD *[rbp+{offset1}] += {f[ptr+3]}")
        rbp[offset1] *= rbp[offset2]
        rbp[offset1] += f[ptr+3]
        print(f"*[rbp+{offset1}] = {rbp[offset1]}")
    if f[ptr] == 0xb:
        print(f"ADD *[rbp+{offset1}] += {f[ptr+3]}")
        rbp[offset1] += f[ptr+3]
        print(f"*[rbp+{offset1}] = {rbp[offset1]}")
    if f[ptr] == 0xc:
        print("EXIT")
        # break
    if f[ptr] == 0xd:
        print("INPUT")
    ptr += 4

    # pctf{vm_r3vers3inG_1s_tr1cky}
    # look for big value after each INPUT call then convert to hex_string then to ascii_string 
    # 1885566054 2071358815 1915975269 1920152425 1850171185 1935635570 828599161 2100310064