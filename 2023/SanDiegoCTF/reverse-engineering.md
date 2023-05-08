# Open Sesame

`
Enter the magic words to get the flag!
`

Chall gives us a `.pyc` file. Using some tools below to decompile this `.pyc` file.

[use command](https://bolexzy.hashnode.dev/decompiling-a-compiled-python-pyc-file-crackme4)

[pycdc tools](https://github.com/zrax/pycdc)

Each tool decompile to different code snippet but after gathering code's logic, we get the original `.py` file

```python
# Source Generated with Decompyle++
# File: sesame.pyc (Python 3.8)

MOD = 131
FLAG_LEN = 36
DOOR_SHAPE = [94, 68, 98, 110, 45, 81, 6, 76, 119, 53, 16, 19, 122, 91, 51, 44, 13, 35, 2, 124, 83, 101, 75, 122, 75, 124, 37, 8, 127, 0, 22, 130, 11, 42, 114, 19]

def gencave(flaglen):
    cave = []
    ps = []
    i = 1
    cave.append([])
    while len(cave) <= flaglen:
        i += 1
        skip = False
        for p in ps:
            if i % p == 0:
                skip = True
                continue
        if skip == True:
            continue
        ps.append(i)
        if len(cave[-1]) >= flaglen:
            cave.append([])
        cave[-1].append(i % MOD)
    cave = cave[:-1]
    return cave


def door(cave = None, word = None):
    if not word.isascii() or len(word) != FLAG_LEN:
        return False
    code = list(word.encode())
    m = magic(cave, code)
    return m == DOOR_SHAPE

def magic(a, b):
    return [sum((a[i][j] * b[j] for j in range(FLAG_LEN))) % MOD for i in range(FLAG_LEN)]

if __name__ == '__main__':
    cave = gencave(FLAG_LEN)            
    magic_words = input('Enter the magic words (the flag) to get the treasure (points): ')
    print('You got the flag! Get the treasure by submitting it.' if door(cave, magic_words) else 'This is not the flag :(')
```

Looking at `magic()` function and `door()` function, we know that:

$DOORSHAPE_i$ = $\sum_{j=0}^{FLAGLEN} cave_{i, j} * word_{j}$

We know $DOORSHAPE$ and $cave$ so we can use Gaussian (or brute force like my sol below) to solve set of modular equations with modulo `131` and recover the $word$

And this is the solution code:

```python
# Source Generated with Decompyle++
# File: sesame.pyc (Python 3.8)
from math import gcd

MOD = 131
FLAG_LEN = 36
DOOR_SHAPE = [94, 68, 98, 110, 45, 81, 6, 76, 119, 53, 16, 19, 122, 91, 51, 44, 13, 35, 2, 124, 83, 101, 75, 122, 75, 124, 37, 8, 127, 0, 22, 130, 11, 42, 114, 19]

def gencave(flaglen):
    cave = []
    ps = []
    i = 1
    cave.append([])
    while len(cave) <= flaglen:
        i += 1
        skip = False
        for p in ps:
            if i % p == 0:
                skip = True
                continue
        if skip == True:
            continue
        ps.append(i)
        if len(cave[-1]) >= flaglen:
            cave.append([])
        cave[-1].append(i % MOD)
    cave = cave[:-1]
    return cave

def lcm(a, b):
    return a * (b // gcd(a, b))

if __name__ == '__main__':
    cave = gencave(FLAG_LEN)

    solved = []
    for i in range(FLAG_LEN):
        solved.append(0)

    # Make cave become trigular matrix

    for i in range(FLAG_LEN):
        cave[i].append(DOOR_SHAPE[i])

    for i in range(FLAG_LEN):
        for j in range(i + 1, FLAG_LEN):
            if(cave[j][i] == 0): 
                continue
            bound = lcm(cave[i][i], cave[j][i])
            base1 = bound // cave[j][i]
            base2 = bound // cave[i][i]
            for k in range(i, FLAG_LEN + 1):
                cave[j][k] *= base1
                cave[j][k] -= base2 * cave[i][k]

    for i in range(FLAG_LEN):
        for j in range(FLAG_LEN + 1):
            if cave[i][j] >= 0:
                cave[i][j] %= MOD
            else: 
                cave[i][j] = MOD - (abs(cave[i][j]) % MOD)
    
    # Brute force solve from word[35] to word[0] 

    for i in range(FLAG_LEN - 1, -1, -1):
        total_solved = 0
        for j in range(i, FLAG_LEN):
            total_solved += solved[j] * cave[i][j] % MOD
        for x in range(131):
            if((cave[i][i] * x + total_solved) % MOD == cave[i][-1]):
                solved[i] = x

    print("".join(chr(x) for x in solved)) 
```

Flag: `sdctf{0p3n_s3sAm3_bUt_1n_l337Sp3aK!}`