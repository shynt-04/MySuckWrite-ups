arr = [130, 37, 70, 115, 64, 106, 143, 34, 54, 134, 96, 98, 125, 98, 138, 104, 25, 3, 66, 78, 24, 69, 91, 80, 87, 67, 95, 8, 25, 22, 115]
n = len(arr)
for i in range(0, n // 2):
    if i % 2 != 0: 
        arr[i] = arr[i] - 30
    else:
        x = arr[i]
        arr[i] = arr[n - i - 1] + 10
        arr[n - i - 1] = x - 20

for i in range(0, n):
    if i % 2 == 0:
        arr[i] = arr[i] ^ 0x13
    else:
        arr[i] = arr[i] ^ 0x37

print("".join(chr(x) for x in arr))

# n00bz{r3v_1s_s0_e4zy_r1ght??!!}