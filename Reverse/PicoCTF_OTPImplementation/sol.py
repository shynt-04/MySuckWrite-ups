# import gdb

# gdb.execute("file ./otp")

# alphabet = "0123456789abcdef"
# tmp_key = "occdpnkibjefihcgjanhofnhkdfnabmofnopaghhgnjhbkalgpnpdjonblalfciifiimkaoenpealibelmkdpbdlcldicplephbo"

# gdb.Breakpoint("*0x5555554009bd")

# key = ""

# while(len(key) < 100):
#     for c in alphabet:
#         curKey = key + c
#         while(len(curKey) < 100):
#             curKey += "a"
#         gdb.execute("run " + curKey)
#         msg = gdb.execute("x/s $rdi", to_string=True)
#         msg = msg[17:len(msg) - 2]
#         cnt = 0
#         for (x, y) in zip(msg, tmp_key):
#             if x == y:
#                 cnt += 1
#             else:
#                 break

#         if cnt > len(key):
#             key += c
#             print(msg)
#             print(key)
        
key = "720867e7c4d89fd29be5bb459c1498d1b4888380fb675c3ddc7123af25ad5e30e9027373c1a6dec9b87c6114bc4a5e6cd45e"
enc_flag = open("flag.txt", "r").read()

print("".join(chr(int(key[i:i+2], 16) ^ int(enc_flag[i:i+2], 16)) for i in range(0, 100, 2)))
