# EZrev

## Description 

`Rev is EZ!`

## Solution

Use java decompile (link below) to get .class source

Looking at `main` function

``` java
final String s = array[0];
if (s.length() != 31) {
    System.out.println("L");
    return;
}
final int[] array2 = s.chars().toArray();
for (int i = 0; i < array2.length; ++i) {
    if (i % 2 == 0) {
        array2[i] = (char)(array2[i] ^ 0x13);
    }
    else {
        array2[i] = (char)(array2[i] ^ 0x37);
    }
}
for (int j = 0; j < array2.length / 2; ++j) {
    if (j % 2 == 0) {
        final int n = array2[j] - 10;
        array2[j] = (char)(array2[array2.length - 1 - j] + 20);
        array2[array2.length - 1 - j] = (char)n;
    }
    else {
        array2[j] = (char)(array2[j] + 30);
    }
}
if (Arrays.equals(array2, new int[] { 130, 37, 70, 115, 64, 106, 143, 34, 54, 134, 96, 98, 125, 98, 138, 104, 25, 3, 66, 78, 24, 69, 91, 80, 87, 67, 95, 8, 25, 22, 115 })) {
    System.out.println("W");
}
```

Initial array is processed through 2 steps

Step 1: 
- Value at even index `XOR` with `0x13` 
- Value at odd index `XOR` with `0x37`

Step 2:
- Add 30 to value at odd index
- Subtract 10 to value at even index (which is in the first half of the array) and add 20 to value at its opposite index (opposite index of `i` is `n - i - 1`) then swap them.

We have the final array so it's easy to reverse. (`EZrev.py`)

Flag: `n00bz{r3v_1s_s0_e4zy_r1ght??!!}`

## Source

[Java decompiler online](http://www.javadecompilers.com/)

[XOR properties](https://www.educative.io/answers/what-is-the-xor-bitwise-operator)

