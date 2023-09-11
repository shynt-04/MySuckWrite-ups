f = open("./password_checker2.smol", "rb").read()

rbp = []
for i in range(0x20):
    rbp.append(0)

rbp_24 = []
for i in range(0x4000):
    rbp_24.append(0)
offset_24 = 0
rbp_16 = 0

ptr = 4
l = 0
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
    # if f[ptr] == 0x3:
        # print(f"PRINT [rbp+{offset1}]")
    if f[ptr] == 0x4:
        print(f"MOV *[rbp+{offset1}] = {f[ptr+3]}")
        rbp[offset1] = f[ptr+3]
        print(f"*[rbp+{offset1}] = {rbp[offset1]}")
    if f[ptr] == 0x5:
        print(f"ADD *[rbp+24] += 8 THEN MOV **[rbp+24] = *[rbp+{offset2}] = {rbp[offset2]}")
        offset_24 += 8
        rbp_24[offset_24] = rbp[offset2]
    if f[ptr] == 0x6:
        print(f"MOV *[rbp+{offset1}] = **[rbp+24] THEN SUB *[rbp+24] -= 8")
        rbp[offset1] = rbp_24[offset_24]
        offset_24 -= 8
        print(f"*[rbp+{offset1}] = {rbp[offset1]}")
    if f[ptr] == 0x7:
        print(f"SUB *[rbp+16] = *[rbp+{offset1}] - *[rbp+{offset2}] = {rbp[offset1] - rbp[offset2]}")
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
    # if f[ptr] == 0xd:
        # print("INPUT")
    if f[ptr] == 0xe:
        print(f"XOR *[rbp + {offset1}] = *[rbp + {offset1}] ^ *[rbp + {offset2}]")
        rbp[offset1] ^= rbp[offset2]
        print(f"*[rbp+{offset1}] = {rbp[offset1]}")
    if f[ptr] == 0xf:
        print(f"SHIFT RIGHT *[rbp + {offset1}] = *[rbp + {offset1}] >> ({f[ptr+3] & 0x1f})")
        rbp[offset1] >>= (f[ptr+3] & 0x1f)
        print(f"*[rbp+{offset1}] = {rbp[offset1]}")
    if f[ptr] == 0x10:
        print("GETC")
        rbp[offset1] = 32
        l += 1
    if f[ptr] == 0x11:
        print(f"SHIFT LEFT *[rbp + {offset1}] = *[rbp + {offset1}] << ({f[ptr+3] & 0x1f})")
        rbp[offset1] <<= (f[ptr+3] & 0x1f)
        print(f"*[rbp+{offset1}] = {rbp[offset1]}")
    if f[ptr] == 0x12:
        print(f"SUB *[rbp+{offset1}] -= {f[ptr+3]}")
        rbp[offset1] -= f[ptr+3]
        print(f"*[rbp+{offset1}] = {rbp[offset1]}")
    if f[ptr] == 0x13:
        print(f"MODULO *[rbp+{offset1}] %= *[rbp+{offset2}]")
        rbp[offset1] %= rbp[offset2]
        print(f"*[rbp+{offset1}] = {rbp[offset1]}")
    ptr += 4

print(l)