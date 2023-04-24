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

Flag: shctf{gam3_0v3r_m@n_game_0ver}

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

Checking decompile code in ghidra, we discover that in function `adjust_economy`, with option `inflate_currency`, if two conditions `currency = 0` and `galactic_currency = usd` hold, `collapse_economy`, function where print the flag, will be triggered

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