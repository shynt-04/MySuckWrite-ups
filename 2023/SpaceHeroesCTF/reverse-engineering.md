# Acheron 
File requires `password`, after disassembling with ghidra we easily identify the `password` check code snippet
```cpp
if (local_28 == 'N') {
    if (local_27 == 'E') {
      if (local_26 == 'N') {
        if (local_25 == 'W') {
          if (local_24 == 'S') {
            if (local_23 == 'S') {
              if (local_22 == 'E') {
                if (local_21 == 'W') {
                  if (local_20 == 'S') {
                    if (local_1f == 'N') {
                      if (local_1e == 'E') {
                        if (local_1d == 'N') {
                          if (local_1c == 'S') {
                            if (local_1b == 'S') {
                              if (local_1a == 'W') {
                                if (local_19 == 'E') {
                                  if (local_18 == 'E') {
                                    if (local_17 == 'N') {
                                      if (local_16 == 'W') {
                                        if (local_15 == 'S') {
                                          if (local_14 == 'N') {
                                            if (local_13 == 'N') {
                                              if (local_12 == 'E') {
                                                if (local_11 == 'S') {
                                                  if (local_10 == 'S') {
                                                    success();
                                                  }
```
And we get the `password: NENWSSEWSNENSSWEENWSNNESS`

Flag: `shctf{gam3_0v3r_m@n_game_0ver}`

# Galatic Federation 
File requires `username/password`

Disassemble with ghidra and we find two lines that check the `uesr/pass`:
```cpp
bVar2 = std::operator==(local_78,"hktpu")
bVar2 = std::operator==(local_58,"8fs7}:f~Y;unS:yfqL;uZ")
```
We can guess this is `user/pass` but encoded with caesar cipher `shift = 4`

After decoding we get `admin`/`1_l0v3_wR4ngL3r_jE4nS` as `user/pass`

After entering the username and password, an option screen appears

Checking decompile code in ghidra, we discover that in function `adjust_economy/inflate_currency`, if two conditions `currency = 0` and `galactic_currency = usd` hold, function `collapse_economy` where print the flag, will be triggered

To set `galactic_currency = usd`, select the option `presidential_decree/change_galactic_currency`

To set `currency = 0`, enter `-100%` in the option `adjust_economy/inflate_currency`

And this is the final message:
```   
Meanwhile, somewhere on the Level 9 control room...
Morty: So w-what are you doing with Level 9 access anyways?
Rick: Destroying the guu-*belch*-Galactic Government.
Summer: Are you going to set all their nukes to target each other?
Morty: O-Or reprogram their military portals to disintegrate their entire spacefleet?
Rick: Good pitches kids, I'm almost proud. But watch closely as Grandpa topples an empire by changing a one...
*click*
...to a zero.
shctf{w4it_uH_wh0s_P4y1Ng_m3_2_y3L1_@_tH15_gUy?}
[*] Got EOF while reading in interactive
```

# Guardian of the Galaxy
Again, file requires a password and firstly we decompile it with Ghidra

After checking main function, we can see that the password is divided into 3 parts

```cpp
for (i = 0; i < 9; i = i + 1) {
    first_part[local_c] = input_pass[i];
    local_c = local_c + 1;
}
```

first_part encoded: `od_pbw1gu`

```cpp
for (i2 = 9; i2 < 18; i2 = i2 + 1) {
    second_part[local_28] = input_pass[i2];
    local_28 = local_28 + 1;
}
```

second_part encoded: `5F31735F6E30745F74`

```cpp
for (i3 = 18; i3 < 27; i3 = i3 + 1) {
    uVar4 = (ulong)input_pass[i3];
    third_part[local_30] = input_pass[i3];
    local_30 = local_30 + 1;
}
```
third_part encoded: `d/[h-i-py`

Parts 1 and 3 are encoded using the Caesar cipher with shift 4. Part 2 is encoded in hexadecimal.

Decoding reveals the password, which is also the flag:
 ```
 shctf{5ky
 _1s_n0t_t
 h3_l1m1t}
 ```

Flag: `shctf{5ky_1s_n0t_th3_l1m1t}`

# Batlle boats in space

The challenge asks us to find a `m x n` matrix consisting of only `B` and `~` characters

Checking 'battleship.c', we can see more than 1000 lines of code

We easily notice the map check code snippet but how to print the map with around 1000 lines of `if`

However, every `if` have the same format that compare `a[i][j] != c` so we can change `!=` to `=` and run the code again

Then we get a map:
```
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~BBBBB~~B~~~~~~B~~BBBBB~~BBBBBBB~BBBBBBB~~~~B~~BBBBB~~BBBBBBB~B~~~~~B~B~~~~B~~~~~~~~~BBBBBBB~B~~~~~~B~~~~B~~~BBBBBBB~~~~~~~~~~BBBBB~~B~~~~~~B~BBBBBBB~BBBBBB~~B
~B~~~~~B~B~~~~~~B~B~~~~~B~~~~B~~~~B~~~~~~~~~B~~B~~~~~B~~~~B~~~~BB~~~~B~B~~~B~~~~~~~~~~~~~B~~~~B~~~~~~B~~~B~B~~~~~B~~~~~~~~~~~~B~~~~~B~B~~~~~~B~~~~B~~~~B~~~~~B~~
~B~~~~~~~B~~~~~~B~B~~~~~~~~~~B~~~~BBBBB~~~~B~~~B~~~~~~~~~~B~~~~B~B~~~B~B~~B~~~~~~~~~~~~~~B~~~~B~~~~~~B~~~B~B~~~~~B~~~~~~~~~~~~B~~~~~~~B~~~~~~B~~~~B~~~~B~~~~~B~~
~~BBBBB~~BBBBBBBB~B~~~~~~~~~~B~~~~B~~~~~~~B~~~~~BBBBB~~~~~B~~~~B~~B~~B~BB~~~~~~~~~~~~~~~~B~~~~BBBBBBBB~~BBBBB~~~~B~~~~~~~~~~~~~BBBBB~~BBBBBBBB~~~~B~~~~BBBBBB~~~
~~~~~~~B~B~~~~~~B~B~~~~~~~~~~B~~~~B~~~~~~~~B~~~~~~~~~B~~~~B~~~~B~~~B~B~B~~B~~~~~~~~~~~~~~B~~~~B~~~~~~B~~B~~~B~~~~B~~~~~~~~~~~~~~~~~~B~B~~~~~~B~~~~B~~~~B~~~~~~~~
~B~~~~~B~B~~~~~~B~B~~~~~B~~~~B~~~~B~~~~~~~~~B~~B~~~~~B~~~~B~~~~B~~~~BB~B~~~B~~~~~~~~~~~~~B~~~~B~~~~~~B~~B~~~B~~~~B~~~~~~~~~~~~B~~~~~B~B~~~~~~B~~~~B~~~~B~~~~~~~~
~~BBBBB~~B~~~~~~B~~BBBBB~~~~~B~~~~B~~~~~~~~~~B~~BBBBB~~BBBBBBB~B~~~~~B~B~~~~B~BBBBBBB~~~~B~~~~B~~~~~~B~~B~~~B~~~~B~~~~BBBBBBB~~BBBBB~~B~~~~~~B~BBBBBBB~B~~~~~~~B
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```
Flag: `shctf{sink_that_ship}`

p/s: num_bullets is useless
