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

My first time ever solving a VM chall xD

Decompile the `vm` file with Ghidra. Looking at the main function:

```c
void main(int param_1,undefined8 *param_2)

{
  int __fd;
  int iVar1;
  ssize_t sVar2;
  void *pvVar3;
  void *pvVar4;
  void *pvVar5;
  long in_FS_OFFSET;
  undefined4 local_14;
  undefined8 local_10;
  
  local_10 = *(undefined8 *)(in_FS_OFFSET + 0x28);
  local_14 = 0;
  if (param_1 < 2) {
    printf("Usage %s <program>\n",*param_2);
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  __fd = open((char *)param_2[1],0);
  if (__fd < 0) {
    printf("Could not open %s\n",param_2[1]);
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  sVar2 = read(__fd,&local_14,4);
  if (sVar2 < 4) {
    puts("Failed to read header");
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  iVar1 = strcmp((char *)&local_14,"SMOL");
  if (iVar1 != 0) {
    puts("Not a SMOL program");
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  pvVar3 = malloc(4);
  if (pvVar3 == (void *)0x0) {
    puts("malloc fail");
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  pvVar4 = malloc(0x20);
  if (pvVar4 == (void *)0x0) {
    puts("malloc fail");
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  pvVar5 = malloc(0x1000);
  *(void **)((long)pvVar4 + 0x18) = pvVar5;
  if (pvVar4 == (void *)0x0) {
    puts("malloc fail");
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  do {
    decode_instruction(__fd,pvVar3);
    execute_instruction(__fd,pvVar3,pvVar4);
    clear_ins();
  } while( true );
}
```

The `execute_instruction` function:

```c
void execute_instruction(int param_1,byte *param_2,long rbp)

{
  undefined8 *r0;
  undefined8 *r1;
  
  r0 = (undefined8 *)(rbp + (ulong)param_2[1] * 4);
  r1 = (undefined8 *)(rbp + (ulong)param_2[2] * 4);
  switch(*param_2) {
  case 0:
    *(uint *)r0 = *(uint *)r1;
    break;
  case 1:
    *(uint *)r0 = *(uint *)r0 + (uint)param_2[3] + *(uint *)r1;
    break;
  case 2:
    *(uint *)r0 = *(uint *)r0 + (uint)param_2[3] + *(uint *)r1;
    break;
  case 3:
    printf("%u\n",(ulong)*(uint *)r0);
    break;
  case 4:
    *(uint *)r0 = (uint)param_2[3];
    break;
  case 5:
    *(long *)(rbp + 0x18) = *(long *)(rbp + 0x18) + 8;
    **(undefined8 **)(rbp + 0x18) = *r1;
    break;
  case 6:
    *r0 = **(undefined8 **)(rbp + 0x18);
    *(long *)(rbp + 0x18) = *(long *)(rbp + 0x18) + -8;
    break;
  case 7:
    *(uint *)(rbp + 0x10) = *(uint *)r0 - *(uint *)r1;
    break;
  case 8:
    if (*(int *)(rbp + 0x10) == 0) {
      lseek(param_1,(long)(short)((ushort)param_2[3] + (ushort)param_2[2] * 0x100),1);
    }
    break;
  case 9:
    write(1,*(void **)(rbp + 0x18),(ulong)param_2[3]);
    break;
  case 10:
    *(uint *)r0 = *(uint *)r0 * *(uint *)r1;
    *(uint *)r0 = *(uint *)r0 + (uint)param_2[3];
    break;
  case 0xb:
    *(uint *)r0 = *(uint *)r0 + (uint)param_2[3];
    break;
  case 0xc:
                    /* WARNING: Subroutine does not return */
    exit(0);
  case 0xd:
    __isoc99_scanf(&DAT_00102008,r0);
    break;
  default:
    printf("[x] %x %x %x %x\n",(ulong)*param_2,(ulong)param_2[1],(ulong)param_2[2],(ulong)param_ 2[3]
          );
    puts("Error executing instruction!");
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  return;
}
```

The execution for each instrucion is very clear, so I write a scipt to leak password_check instruction:

```python
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
```

You can view the instruction in `leak.txt` and you may notice that after each `LSEEK` instruction, it will be an `EXIT`. Check the execution of `LSEEK` in Ghidra

```c
  case 8:
    if (*(int *)(rbp + 0x10) == 0) {
      lseek(param_1,(long)(short)((ushort)param_2[3] + (ushort)param_2[2] * 0x100),1);
    }
    break;
```

Search the `lseek` function in google:

```
lseek() repositions the file offset of the open file description associated with the file descriptor fd to the argument offset according to the directive whence as follows:

SEEK_SET
    The file offset is set to offset bytes.

SEEK_CUR
    The file offset is set to its current location plus offset bytes.

SEEK_END
    The file offset is set to the size of the file plus offset bytes.
```

The option we used here is SEEK_CUR which will skip the next `offset` bytes. So, it is clear that `LSEEK` is just `if..else`

```pseudo
if [rbp+16] = 0:
    ok skip next (param_2[3] + param_2[2] * 0x100) bytes and go to next step
else: // no skip
    wrong
    exit
```

Additionally, `**[rbp+24]` will stored our input so that's why i use offset_24 for this pointer

Back to leeked instructions, we can see the repeated check by `LSEEK` after each `INPUT`:

```python
ADD *[rbp+24] += 8 THEN MOV **[rbp+24] = [rbp+12] = 1885566054
MOV *[rbp+0] = **[rbp+24] THEN SUB *[rbp+24] -= 8
*[rbp+0] = 1885566054
MOV *[rbp+4] = **[rbp+24] THEN SUB *[rbp+24] -= 8
*[rbp+4] = 671588
SUB *[rbp+16] = *[rbp+0] - [rbp+4] = 1884894466
LSEEK 4 bytes
EXIT
```

It is very tricky here, `1885566054` is the value we need. Convert it to hexadecimal then convert to ascii_string we get `pctf`, look good :D

Then I find all LSEEK instruction and look for the value that `MOV` to `**[rbp+24]`:

```python
[1885566054, 2071358815, 1915975269, 1920152425, 1850171185, 1935635570, 828599161, 2100310064]
```

Convert and get the flag:

> pctf{vm_r3vers3inG_1s_tr1cky}

## Reduced Reduced Instruction Set 2

> Expert - 29 solves

> p/s: read the easier one first


`vm2` is just like `vm` but extend 6 more types of instruction:

```c
  case 0xe:
    *r1 = *r1 ^ *r2;
    break;
  case 0xf:
    *r1 = (uint)*r1 >> (param_2[3] & 0x1f);
    break;
  case 0x10:
    iVar1 = getc(stdin);
    *r1 = iVar1;
    break;
  case 0x11:
    *r1 = *r1 << (param_2[3] & 0x1f);
    break;
  case 0x12:
    *r1 = *r1 - (uint)(byte)param_2[3];
    break;
  case 0x13:
    *r1 = (uint)*r1 % (uint)*r2;
    break;
```

So we just need to add those executions to `disass.py`:

```python
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
    rbp[offset1] = 32 # init input is "0" * 840
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
```

Now we get `leak.txt` but it has more than 120000 lines...

I'm about to quit and wait for WU but after looking through leak file, we can see the repeated pattern.

Ignore intructions before `GETC` because its work is just print `Can you ...` (the message appeared when you run)

`GETC` stand for `getchar()` in C. There are 840 `GETC` called so our input's length has to be 840 characters

Now let's look the first check after `GETC`. I have explained `LSEEK` above, those instructions from `LSEEK` to `EXIT` will be ignored because they just print `Wrong!` then exit program:

```c
MOV *[rbp+0] = **[rbp+24] THEN SUB *[rbp+24] -= 8
*[rbp+0] = 32
ADD *[rbp+24] += 8 THEN MOV **[rbp+24] = *[rbp+0] = 32
MOV *[rbp+8] = 0
*[rbp+8] = 0
ADD *[rbp+0] += *[rbp+8] + 0
*[rbp+0] = 32
MOV *[rbp+4] = 255
*[rbp+4] = 255
MODULO *[rbp+0] %= *[rbp+4]
*[rbp+0] = 32
MOV *[rbp+4] = 65
*[rbp+4] = 65
SUB *[rbp+16] = *[rbp+0] - *[rbp+4] = -33
LSEEK 288 bytes
```

Now the second one:

```c
MOV *[rbp+0] = **[rbp+24] THEN SUB *[rbp+24] -= 8
*[rbp+0] = 32
ADD *[rbp+24] += 8 THEN MOV **[rbp+24] = *[rbp+0] = 32
MOV *[rbp+4] = 65
*[rbp+4] = 65
XOR *[rbp + 0] = *[rbp + 0] ^ *[rbp + 4]
*[rbp+0] = 97
MOV *[rbp+8] = 1
*[rbp+8] = 1
ADD *[rbp+0] += *[rbp+8] + 0
*[rbp+0] = 98
MOV *[rbp+4] = 255
*[rbp+4] = 255
MODULO *[rbp+0] %= *[rbp+4]
*[rbp+0] = 98
MOV *[rbp+4] = 98
*[rbp+4] = 98
SUB *[rbp+16] = *[rbp+0] - *[rbp+4] = 0
LSEEK 288 bytes
```

And the third one:

```c
MOV *[rbp+0] = **[rbp+24] THEN SUB *[rbp+24] -= 8
*[rbp+0] = 32
ADD *[rbp+24] += 8 THEN MOV **[rbp+24] = *[rbp+0] = 32
MOV *[rbp+4] = 98
*[rbp+4] = 98
XOR *[rbp + 0] = *[rbp + 0] ^ *[rbp + 4]
*[rbp+0] = 66
MOV *[rbp+8] = 2
*[rbp+8] = 2
ADD *[rbp+0] += *[rbp+8] + 0
*[rbp+0] = 68
MOV *[rbp+4] = 255
*[rbp+4] = 255
MODULO *[rbp+0] %= *[rbp+4]
*[rbp+0] = 68
MOV *[rbp+4] = 35
*[rbp+4] = 35
SUB *[rbp+16] = *[rbp+0] - *[rbp+4] = 33
LSEEK 288 bytes
```

You see the pattern? Here is how it works:

```python
(rbp[0] ^ 0 + 0) % 255 = 65
(rbp[1] ^ 65 + 1) % 255 = 98
(rbp[2] ^ 98 + 2) % 255 = 35
...
```

Is it clear? Our input will be encrypted by simple algorithm: `input[i] = (input[i] ^ data[i - 1] + i) % 255` (if `i = 0` then xor it with `0` instead)

However, after scrolling and looking at the transition, the actual algorithm is `input[i] = (input[i] ^ data[i - 1] + i % 255) % 255`

Now, our work is write a script to leak `data`, notice that after `MODULO`, the next `MOV` will give us `data` we need. So, we just need add a boolean `have_important_data` to print only the `data`

```python
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
have_important_data = 0
while(ptr < len(f)):
    offset1 = f[ptr+1]*4
    offset2 = f[ptr+2]*4
    # print(f"{f[ptr]} {f[ptr+1]} {f[ptr+2]} {chr(f[ptr+3])}")
    if f[ptr] == 0x0:
        rbp[offset1] = rbp[offset2]
    if f[ptr] == 0x1 or f[ptr] == 0x2:
        rbp[offset1] += rbp[offset2] + f[ptr+3]
    # if f[ptr] == 0x3:
        # print(f"PRINT [rbp+{offset1}]")
    if f[ptr] == 0x4:
        rbp[offset1] = f[ptr+3]
        if have_important_data == 1:
            have_important_data = 0
            print(f[ptr+3])
    if f[ptr] == 0x5:
        offset_24 += 8
        rbp_24[offset_24] = rbp[offset2]
    if f[ptr] == 0x6:
        rbp[offset1] = rbp_24[offset_24]
        offset_24 -= 8
    if f[ptr] == 0x7:
        rbp_16 = rbp[offset1] - rbp[offset2]
    if f[ptr] == 0xa:
        rbp[offset1] *= rbp[offset2]
        rbp[offset1] += f[ptr+3]
    if f[ptr] == 0xb:
        rbp[offset1] += f[ptr+3]
    if f[ptr] == 0xe:
        rbp[offset1] ^= rbp[offset2]
    if f[ptr] == 0xf:
        rbp[offset1] >>= (f[ptr+3] & 0x1f)
    if f[ptr] == 0x10:
        rbp[offset1] = 65
        l += 1
    if f[ptr] == 0x11:
        rbp[offset1] <<= (f[ptr+3] & 0x1f)
    if f[ptr] == 0x12:
        rbp[offset1] -= f[ptr+3]
    if f[ptr] == 0x13:
        rbp[offset1] %= rbp[offset2]
        have_important_data = 1
    ptr += 4
```
After optaining `data`, the last thing we need to do is reversed the algorithm which is very easy:

```python
data = [65,98,35,69,36,92,67,56,32,76,47,106,14,120,24,67,115,35,97,37,94,147,15,120,47,113,57,52,113,31,93,61,124,58,107,45,131,201,224,231,172,238,200,203,218,213,40,55,115,76,91,174,18,175,252,209,221,55,142,35,143,37,126,75,167,200,205,239,206,3,168,34,77,135,241,221,254,231,208,76,188,8,185,31,147,38,157,80,123,115,91,214,2,199,13,202,31,148,23,225,246,60,185,63,194,76,141,87,227,5,219,46,126,126,137,88,156,102,121,129,110,199,33,202,43,136,100,138,122,143,50,200,38,199,41,204,62,167,87,196,56,220,65,240,38,217,77,210,64,197,72,184,112,183,50,225,33,223,86,215,95,207,93,219,77,9,207,46,3,204,80,206,155,168,55,242,60,253,75,31,201,92,240,136,180,123,211,92,228,75,253,72,252,87,250,88,61,36,20,44,13,50,11,246,108,207,190,153,194,125,240,108,33,26,82,9,58,243,122,250,107,252,120,233,170,165,174,114,234,104,243,187,180,194,142,211,170,204,152,208,149,167,193,166,123,254,146,218,175,200,166,191,216,246,147,234,203,172,143,231,135,249,148,249,148,190,216,195,187,236,219,205,181,223,205,189,178,242,158,12,135,252,169,165,204,193,198,7,152,26,140,10,163,240,198,208,204,23,158,30,150,39,54,114,75,96,115,70,95,101,68,93,120,87,94,172,201,205,225,211,53,146,46,147,68,122,93,128,245,32,162,24,185,32,79,126,175,22,198,244,213,76,150,87,151,76,147,16,220,25,152,12,129,4,163,231,245,1,219,32,173,247,1,208,94,154,111,143,85,166,57,208,42,128,90,155,53,238,62,154,93,251,12,227,24,246,22,186,54,218,71,172,77,170,91,8,215,138,58,235,23,6,185,95,197,124,170,93,13,199,47,227,36,162,111,170,128,139,136,145,87,228,63,199,83,220,93,228,46,188,141,156,154,178,116,9,248,68,223,111,211,91,55,49,14,42,25,57,13,227,135,181,163,147,123,214,111,212,124,41,14,73,57,33,33,211,143,187,158,149,189,168,155,200,133,206,137,136,203,133,217,142,207,161,183,191,185,198,141,206,153,233,181,174,206,158,220,173,202,177,242,164,206,246,122,68,50,62,13,98,5,91,62,17,105,59,96,70,50,12,130,2,122,86,23,142,0,131,249,175,241,161,193,172,220,210,13,118,59,121,58,115,54,101,34,37,106,40,126,61,128,28,102,58,117,130,18,97,60,138,49,140,24,177,199,223,241,11,168,2,157,45,146,34,150,65,113,89,189,34,148,44,140,55,159,70,126,100,85,196,1,181,32,167,219,2,192,252,230,220,87,141,73,135,78,205,2,200,31,206,16,199,78,136,87,224,254,2,211,97,127,130,84,174,51,186,84,161,76,227,98,132,114,205,37,200,42,196,33,197,36,135,117,161,92,187,36,206,121,168,78,181,98,150,117,161,98,169,30,242,42,230,46,232,53,176,112,182,101,172,106,185,56,187,113,190,120,178,128,74,205,79,216,88,235,54,4,28,27,238,60,5,219,119,202,120,215,97,200,95,239,74,238,144,181,144,117,198,117,215,192,109,204,138,197,110,235,107,212,140,187,166,157,208,199,165,162,161,176,160,162,174,109,225,104,42,46,36,48,42,41,52,47,248,119,253,114,243,206,222,155,229,115,71,33,58,58,12,254,164,199,158,187,235,129,230,132,236,140,3,107,81,57,88,49,99,17,111,92,67,63,47,108,22,134,9,129,253,169,243,175,169,227,223,201,215,209,210,220,223,214,27,157,35,119,58,67,86,91,167,243,2,161,254,195,236,192,224,197,227,185,20,170,25,171,5,98,79,121,91,105,95,121,81,105,99,81,134,50,102]

cnt = 0
last = 0
flag = ""
for x in data:
    y = x
    cur = (x - cnt) ^ last
    while cur > 255 or cur < 0:
        x += 255
        cur = (x - cnt) ^ last
    flag += chr(cur)
    last = y
    cnt += 1
    cnt %= 255

print(flag)
```
And we get the output:

```
A Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code,
or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type
of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number
of positions down the alphabet. For example, with a left shift of 3, D would be rplaced by A, E would
become B, and so on. The method is named aftr Julius Caesar, who used it in his private correspondence.
pctf{vM_r3v3rs1ng_g0t_a_l1ttl3_harder}
The Vigenere cipher is a method of encryptng alphabetic text where each letter of the plaintext
is encoded with a different Caesar cipher, whose increment is determined by the corresponding
letter of another text, the key.
The Vigenere cipher is therefore a special case of a polyalphabetic substitution.
```

> pctf{vM_r3v3rs1ng_g0t_a_l1ttl3_harder}