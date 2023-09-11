# Reverse Engineering (Solved 7/8)

## Python XOR 

> Beginner - 569 solves

```python
from string import punctuation

alphabet = list(punctuation)
data = "bHEC_T]PLKJ{MW{AdW]Y"
def main():
#   For loop goes here
    for key in alphabet:
        decrypted = ''.join([chr(ord(x) ^ ord(key)) for x in data])
        print(decrypted)
main()

```

> Flag{python_is_e@sy}

## Coffee Shop

> Easy - 504 solves

[Java Decompiler](http://www.javadecompilers.com)

```java
if (encodeToString.length() != 20) {
    failure();
}
else if (!encodeToString.endsWith("NoZXI=")) {
    failure();
}
else if (!encodeToString.startsWith("R2FsZU")) {
    failure();
}
else if (!encodeToString.substring(6, 14).equals("JvZXR0aW")) {
    failure();
}
else {
    success();
}
```

Decode base64: R2FsZUJvZXR0aWNoZXI=

> PCTF{GaleBoetticher}

## Patchwork

> Easy - 355 solves

There is a jump instruction before calling `give_flag()` so just patch it to NOP with Ghidra

Previous:

`        0010116a 74  0a           JZ         LAB_00101176`

Patched:

`        0010116a 66  90           NOP`

> PCTF{JuMp_uP_4nd_g3t_d0Wn}

## Suboptimal

> Medium - 170 solves

Simple reversing, here is my script:

```c++
#include<bits/stdc++.h>

using namespace std;

string enc = "xk|nF{quxzwkgzgwx|quitH";

int main() {
	for (int i = 0; i < 23; ++ i) {
		for (int c = 65; c <= 125; ++ c) {
			int x = c;
			if (x > 64 && x < 126) {
				x = (x + 65) % 122;
				if (x < 65) x += 61;
			}
			x = (x + 65) % 122;
			if (x < 65) x += 61;
			if (x == (int) enc[i]) {
				cout << (char) c;
			}
		}
	}
}
```

> pctf{simproc_r_optimal}

## Python Garbage Compiler

> Medium - 145 solves

Simple python reversing, notice that the seed in only 10 so we can brute force the flag:

```python
import string
from random import *

enc_flag = open("output.txt", "r").read()
alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + "}_{?"

h = 0
flag = ""
while h < len(enc_flag):
    try:
        flag += enc_flag[h + 1] + enc_flag[h] 
    except:
        flag += enc_flag[h]
    h += 2

enc_flag = flag[::-1]
seed(10)

for i in range(1000):
    ok = 1
    flag = ""
    for j in range(len(enc_flag)):
        flag += chr((randint(0, 5) + ord(enc_flag[j])) ^ j)
    for c in flag:
        if c not in alphabet:
            ok = 0
    flag = flag[::-1]
    if ok == 1:
        print(flag)
```

> PCTF{H0w_D1d_y0U_br34k_my_1337_c0de?}

## Reduced Reduced Instruction Set

> Hard - 47 solves



## Reduced Reduced Instruction Set 2

> Expert - 29 solves