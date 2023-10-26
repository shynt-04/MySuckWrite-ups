import string
import gdb

gdb.execute("file ./brute")
gdb.Breakpoint("*0x565559a7")

flag = "picoCTF{"
alphabet = string.printable

while '}' not in flag:
    for c in alphabet:
        open('input.txt', 'w').write(flag + c)
        gdb.execute("run < input.txt")
        msg = gdb.execute("x/x $ebp-0x14", to_string=True)
        msg = msg[20:]
        cnt = int(msg, 16)
        if(cnt > len(flag)):
            flag += c
            print(flag)

print(flag)