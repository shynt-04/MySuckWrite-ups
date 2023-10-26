arr = []

len_file = 264

with open("output.txt") as f:
    for i in range(len_file):
        arr.append(int(f.readline()))

def random_gen():
    list1 = []
    for i in range(1, len_file + 1):
        y = (((i * 327) % 681) + 344) % 313
        list1.append(y)
    return list1

bm = "10 " * 30
bm = bm.split(" ")
blocks = []

def backtrack(raw, expect_bm, seed):
    i = len(raw) - 1
    y = (i * seed) % 30
    n = bm[y]
    while (n != "10"):
        y = (y + 1) % 30
        n = bm[y]
    save = bm[y]
    if raw[i] == "1":
        n = "11"
    else:
        n = "00"
    if n != expect_bm[y]:
        return
    if len(raw) == 30:
        # print("raw: ", raw)
        blocks.append(raw)
        return
    bm[y] = n
    backtrack(raw + "0", expect_bm, seed)
    backtrack(raw + "1", expect_bm, seed)
    bm[y] = save

result = 0
seeds = []
for i in range(1, len_file + 1):
    seeds.append(i * 127 % 500)

randoms = random_gen()

for i in range(len_file):
    fun = arr[i] ^ randoms[i]
    if i > 0:
        fun ^= arr[i - 1]
    # print("fun: ", i, fun)
    bin_fun = bin(fun)[2:]
    # print("bin fun: ", bin_fun)
    expect_bm = []
    for j in range(0, len(bin_fun), 2):
        expect_bm.append(bin_fun[j:j+2])
    # print(expect_bm)
    backtrack("0", expect_bm, seeds[i])
    backtrack("1", expect_bm, seeds[i])

out = []
for j in range(len(blocks)):
    for i in range(0, len(blocks[j]), 6):
        if j == 0:
            out.append([])
        out[i // 6].append(blocks[j][i:i+6])

for c in out:
    map0 = ""
    map1 = ""
    flag = ""
    for s in c:
        if map1 == "":
            map1 = s
        else:
            if map0 == "":
                map0 = s
        if s == map0:
            flag += "1"
        else:
            flag += "0"
    print(flag)
# print(arr)
# print(randoms)
# print(seeds)