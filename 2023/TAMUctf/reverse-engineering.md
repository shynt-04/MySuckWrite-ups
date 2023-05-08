# Nothing

`This program seems to be taunting me, I'm sure there's something here...`

We are given a stripped file.

Disassembling with Ghidra, we discover that `FUN_00101179` is the main function:

```cpp
void FUN_00101179(void)

{
  puts("not here");
  FUN_00101155(0xffffffffffd011ab);
  return;
}
```

Looking at the Assembly instructions, we can see that some instructions is hidden by `??` after `RET` instruction at `001011aa`.

After changing instruction at this address to `NOP`, the decompile code for main function has changed:

```cpp
undefined8 FUN_00101179(int param_1,long param_2)

{
  int iVar1;
  undefined8 uVar2;
  ulong uVar3;
  char cStack77;
  undefined uStack76;
  undefined uStack75;
  undefined uStack74;
  undefined uStack73;
  undefined8 uStack72;
  undefined8 uStack64;
  undefined8 uStack56;
  undefined8 uStack48;
  undefined uStack40;
  undefined8 local_18;
  ulong uStack16;
  
  puts("not here");
  local_18 = FUN_00101155(0xffffffffffd011ab);
  if (param_1 == 2) {
    uStack72 = 0x626e7e6966656867;
    uStack64 = 0x6068527964735671;
    uStack56 = 0x48737d604c767f65;
    uStack48 = 0x62737c6e7c756b68;
    uStack40 = 0;
    cStack77 = 'g';
    uStack76 = 0x6f;
    uStack75 = 0x6f;
    uStack74 = 100;
    uStack73 = 0;
    uStack16 = 0;
    while( true ) {
      uVar3 = func_0x00101040(*(undefined8 *)(param_2 + 8));
      if (uVar3 <= uStack16) break;
      *(byte *)(uStack16 + *(long *)(param_2 + 8)) =
           *(byte *)(uStack16 + *(long *)(param_2 + 8)) ^ (byte)uStack16;
      uStack16 = uStack16 + 1;
    }
    iVar1 = func_0x00101050(*(undefined8 *)(param_2 + 8),&uStack72);
    if (iVar1 == 0) {
      puts(&cStack77);
    }
    uVar2 = 0;
  }
  else {
    uVar2 = 0xffffffff;
  }
  return uVar2;
}
```

Here, `param_1` is `argc` and `param_2` is `argv`. We have to run the exefile with an input that will be checked with value stored at `uStack72`.

However, the input is modified by xor(ing) its characters with those char's index. Mean:

```cpp
input[i] = input[i] ^ i;
```

So if we know the value store at `uStack72`, we can recover the input we need.

We use `gdb` to check its value. First we `break __libc_start_main` and hit `run` to find main address.

``` as
main=0x555555555179
```

After debugging, we find the value store at `uStack72` is `ghefi~nbqVsdyRh`e\177vL`}sHhku|n|sb`

Recover the flag:

```python
enc_flag = "ghefi~nbqVsdyRh`e\177vL`}sHhku|n|sb"
flag = ""

def xor(text, num):
    return chr(ord(text) ^ num)

for i in range(len(enc_flag)):
    flag += xor(enc_flag[i], i)

print(flag)
```

Flag: `gigem{hey_you_found_the_program}`

Resource: [Finding main() in Stripped Binary](https://link-url-here.org)

# Nothing 2

`Another funny obfuscation technique.`

Another stripped file. Just like `Nothing` chall, we find the `actual main` function is `_INIT_1`

After patching instruction `RET` to `NOP`, we discover check code snippet

```cpp
    if (expected_length == input_length) {
      for (uStack16 = 0; uStack16 < input_length; uStack16 = uStack16 + 1) {
        lVar1 = func_0x00101050("abcdefghijklmnopqrstuvwxyz1234567890{}_",
                                (int)*(char *)(uStack16 + *(long *)(param_2 + 8)));
        uStack48 = lVar1 - 0x102020U;
        if (0x26 < lVar1 - 0x102020U) {
          return;
        }
        if (*(char *)(lVar1 + 0x40) != acStack88[uStack16]) {
          return;
        }
      }
      cStack102 = 'c';
      uStack101 = 0x6f;
      uStack100 = 0x72;
      uStack99 = 0x72;
      uStack98 = 0x65;
      uStack97 = 99;
      uStack96 = 0x74;
      uStack95 = 0x20;
      uStack94 = 0x66;
      uStack93 = 0x6c;
      uStack92 = 0x61;
      uStack91 = 0x67;
      uStack90 = 0x21;
      uStack89 = 0;
      puts(&cStack102);
    }
```

It's easy to see that the input was encoded by using `substitution` technique.

Debug with `gdb`, we found expected value, origin alphabet and sub alphabet.

```python
enc_flag = "oao9{5in17smtisnm6bmt1bprznmrb{ye12"
first_board =  "4piq9zovafg8{1hkcm7std03xle}ry6w_ujn52b"
second_board = "abcdefghijklmnopqrstuvwxyz1234567890{}_"

flag = ""

for c in enc_flag:
    pos = first_board.index(c)
    flag += second_board[pos]

print(flag)
```

Flag: gigem{c0nstruct0r5_run_b3f0r3_m41n}

# Nope

`This program is pretty outta line, I can't seem to find the flag.`

Oh, this chall. I think the encode function is just like `Nothing` chall but NOT.

We know that the function is still single bytes xor and the input length is `23` so we can try to brute-force inputs (gigem{xxxxxxxxxxxxxxxxxxxxxxx})

Then by brute-forcing inputs and debugging with `gdb` (about 50 tries), i got the flag.

Flag: `gigem{fUnky_1nlin3_4sm}`

P/s: solutions using gdb-python would be updated :<