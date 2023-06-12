# Mypin

## Description

`I made a safe with a pin of only two digits.`

## Solution

Use `jd-gui` to decompile jar file and we get the .class source.

Examine secret.class and we know that the input is sent to `process` function 8 times before going to `getdata` function so we have to press 0/1 exactly 8 times to get the output

```java
public void process(char paramChar) {
    if (this.cnt > 9)
        return; 
    int i = this.mydata.length / 9;
    for (byte b = 1; b <= i; b++) {
        int j = 9 * b - this.cnt;
        int k = this.box[b - 1] + this.mydata[j];
        k += paramChar - 48;
        this.mydata[j] = k % 2;
        if (k >= 2) {
            this.box[b - 1] = 1;
        } else {
            this.box[b - 1] = 0;
        } 
    } 
    this.cnt++;
}
```

Bruteforcing 256 cases and we get the correct input 01011010 (which is 90 in decimal)

Flag: `n00bz{y0uuu_n33d_t0_bRutefoRc3_1s_e4zyY_}`

## Useful source

[Java decompiler](http://java-decompiler.github.io/)