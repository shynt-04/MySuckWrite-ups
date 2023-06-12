#include <bits/stdc++.h>

using namespace std;

int a[105];

int main() {
  for(int i = 0; i < 256; ++ i) {
    if((i >> 4) == 6) a[1] = a[2] = i;
  }
  a[5] = 123;
  a[29] = 125;
  a[4] = a[27] = a[28] = 122;
  a[26] = 90;
  for(int i = 0; i < 256; ++ i) {
    for(int j = 0; j < 256; ++ j) {
      if((i | j) == 122 && (i & j) == 66) {
        if((302 + 10890 - i) % (i + 1) == 0) {
          a[6] = i;
          a[3] = j;
          a[7] = (302 + 10890 - a[6]) / (a[6] + 1);
          a[8] = 302 - a[6] - a[7];
          a[9] = a[8] + 5;
          a[10] = a[9] + 27;
          a[11] = 32 ^ a[10];
          a[12] = 180 - a[11];
          a[13] = 185 - a[12];
          a[15] = a[12];
          a[17] = a[13];
          a[16] = 217 - a[17];
          a[14] = a[16];
          a[18] = 90;
          a[19] = a[18];
          a[21] = 95;
          a[24] = 180 - a[6];
          a[23] = ~(-33 - a[24]);
          a[25] = a[9];
          a[20] = 127 ^ a[19] ^ a[21];
          a[22] = a[20];
          int check = 1;
          for(int i = 1; i <= 29; ++ i) {
            if(a[i] <= 0) check = 0;
          }
          if(check) {
            cout << 'n';
            for(int i = 1; i <= 29; ++ i) {
              cout << (char) a[i];
            }
            cout << "\n";
          }
        }
      }
    }
  }
}

// flag: n00bz{ZzZ_zZZ_zZz_ZZz_zzZ_Zzz}