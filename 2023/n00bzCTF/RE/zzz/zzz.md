# zzz

## Description

`3z Author: NoobHacker`

## Solution

Use IDA Pro to decompile the given binary.

Examine `check_password` function

```cpp
int __fastcall check(char *a1)
{
  if ( *a1 >> 4 != 6 )
    bye();
  if ( a1[1] != a1[2] )
    bye();
  if ( ((unsigned __int8)a1[3] | (unsigned __int8)a1[6]) != 122
    || ((unsigned __int8)a1[3] & (unsigned __int8)a1[6]) != 66 )
  {
    bye();
  }
  if ( a1[4] != a1[28] )
    bye();
  if ( a1[5] * a1[29] != 15375 )
    bye();
  if ( a1[7] + a1[6] + a1[8] != 302 || a1[6] * a1[7] - a1[8] != 10890 )
    bye();
  if ( a1[9] - a1[8] != 5 || a1[10] - a1[9] != 27 || ((unsigned __int8)a1[11] ^ (unsigned __int8)a1[10]) != 32 )
    bye();
  if ( a1[12] != a1[15] || a1[12] + a1[11] != 180 || a1[13] + a1[12] != 185 )
    bye();
  if ( a1[14] + a1[13] - a1[16] != a1[13] )
    bye();
  if ( a1[16] + a1[17] != 217 || a1[17] != a1[13] )
    bye();
  if ( a1[16] + a1[14] != 2 * a1[14] )
    bye();
  if ( a1[18] != 90 || a1[18] != a1[19] || ((unsigned __int8)(a1[20] ^ a1[19]) ^ (unsigned __int8)a1[21]) != 127 )
    bye();
  if ( ((unsigned __int8)a1[22] ^ (unsigned __int8)(a1[21] ^ a1[20])) != a1[21] )
    bye();
  if ( a1[21] != 95 || a1[24] + a1[6] != 180 )
    bye();
  if ( ~a1[23] + a1[24] != -33 )
    bye();
  if ( a1[25] != a1[9] )
    bye();
  if ( a1[26] + a1[27] != 212 )
    bye();
  if ( a1[27] != a1[28] )
    bye();
  return puts("You got it!");
}
```

Just find a[1], a[2], ..., a[n] and transfer to ASCII to get the flag (zzz.cpp)

`Flag: n00bz{ZzZ_zZZ_zZz_ZZz_zzZ_Zzz}`