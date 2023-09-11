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

Back to leeked instructions, we can see the repeated check by `LSEEK` after `INPUT`:

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

