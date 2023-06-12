# Mypin

## Description

`I made a safe with a pin of only two digits.`

## Solution

Use `jd-gui` to decompile jar file and we get the .class source.

Examine secret.class and we know that the input is sent to `process` function 8 times before going to `getdata` function so we have to press 0/1 exactly 8 times to get the output

Bruteforcing 256 cases and we get the correct input 01011010 (which is 90 in decimal)

Flag: `n00bz{y0uuu_n33d_t0_bRutefoRc3_1s_e4zyY_}`

## Useful source

[Java decompiler](http://java-decompiler.github.io/)