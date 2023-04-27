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

# Thanks for all the fish

`Welcome, human, to the 42nd centennial dolphin acrobatics show! Better get to it. These dolphins aren't going to train themselves...`

After running the exe file, a whale art and messages `...The dolphins don't appreciate your threats of violence.` appear then quit execution immediately without requiring a password or an input

Checking the ghidra, we know that the binary get input from a text file name `proc/getppid()/comm`

```cpp
  snprintf(local_58,0x14,"/proc/%d/comm",(ulong)uVar1);
  __stream = fopen(local_58,"r");
  fgets(local_38,0x20,__stream);
```

We can get the `getppid()` value using c++ and locate the input file

Diving into the decompile code, we discover that the input should be `tidbits` to go though three `if` conditions

```cpp
  iVar2 = strncmp("fish",local_38,4);
  if (iVar2 == 0) {
    puts("\nThe dolphins aren\'t in the mood for fish right now.");
  }
  else {
    iVar2 = strncmp("bash",local_38,4);
    if (iVar2 == 0) {
      puts("\nThe dolphins don\'t appreciate your threats of violence.");
    }
    else {
      iVar2 = strncmp("tidbits",local_38,7);
      if (iVar2 == 0) {
        puts("\nUpon seeing the tidbits, the dolphins begin their performance.");
        puts(
            "\nAs you give them the signal, you are amazed by the dolphins\' uncanny ability to\ nperform a double-backwards-somersault through a hoop whilst whistling \"The Star\nS pangled Banner.\"  You can\'t help but wonder if there\'s some hidden meaning behind \ntheir actions."
            );
        iVar2 = tricks();
        if (iVar2 == 0) {
          FUN_00121960();
        }
      }
      else {
        puts("\nThe dolphins are hungry...");
      }
    }
  }
```

So, first thing we do is change the input file using bash script
```bash
echo "tidbits" > input_file
# input_file = "/proc/getppid()/comm"
```

Then, we notice that it's not over yet, we still have to bypass the `tricks()` function.

Here is the `tricks()`:
```cpp
  __stream = popen("/bin/grep tidbits /proc/*/comm","r");
  if (__stream == (FILE *)0x0) {
    puts("ERROR: This challenge depends on grep.");
                    /* WARNING: Subroutine does not return */
    exit(1);
  }
  putchar(10);
  for (local_434 = 0;
      (pcVar1 = fgets(local_418,0x400,__stream), pcVar1 != (char *)0x0 && (local_434 < 6));
      local_434 = local_434 + 1) {
    printf("Performed trick %c...\n",(ulong)(local_434 + 0x41));
  }
  if (local_434 < 6) {
    if (4 < local_434) {
      uVar2 = 0;
      goto LAB_0014fa83;
    }
    puts("\nYou ran out of treats.  The dolphins are no longer following your lead.");
  }
  else {
    puts("\nYou overfed the dolphins and they decided to take a nap.");
  }
  uVar2 = 1;
```

It requires 5 lines of input to get the flag, however, the `proc/getppid()/comm` stores 15 characters and just one lines only

And when the competion's running, we did't know how to bypass it. Then, thanks to `Gift1a` hints using file patching in Discord, we solve that by patching binary with Ghidra

After changing `0x001338a1` instruction to `NOP` then export the exe file and run the file again, we got the flag

Flag: `shctf{0k_but_h4v3_y0u_s33n_th3_m1c3}`