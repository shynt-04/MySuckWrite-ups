# Crack & Crack

## Dictionary

[rockyou.txt](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwi52u_Bxcv_AhUsbmwGHWJpBZYQFnoECBMQAQ&url=https%3A%2F%2Fgithub.com%2Fbrannondorsey%2Fnaive-hashcat%2Freleases%2Fdownload%2Fdata%2Frockyou.txt&usg=AOvVaw3snAERl1mU6Ccr4WFEazBd&opi=89978449)

## ZIP Crack

[ZIP crack tutorial](https://github.com/jingleyang/security_ctf/blob/master/hacking-lab.com/5020%20Password%20protected%20ZIP%20Writeup.md)

`fcrackzip -b -D -p rockyou.txt -u ./flag.zip`

```bash

  PASSWORD FOUND!!!!: pw == 1337h4x0r
```

## PDF crack

[PDF crack tutorial](https://www.cybrary.it/blog/cracking-encrypted-pdf-password-using-dictionary-attack)

`pdfcrack -f flag.pdf -w rockyou.txt`

```bash
PDF version 1.5
Security Handler: Standard
V: 2
R: 3
P: -3904
Length: 128
Encrypted Metadata: True
FileID: 3ac35b37fdbe79c0efcd2074d254feec
U: 7046f3323934ab6c310e0f7edae1de0400000000000000000000000000000000
O: 9ccbdd5b3bcac3e7e2a53e3cf13b34b8008d6b9d8538b18583e6557227e73c9c
Average Speed: 36882.9 w/s. Current Word: '123yourmom'
Average Speed: 34596.3 w/s. Current Word: 'nutsoe'
Average Speed: 47485.1 w/s. Current Word: '1216xc05'
Average Speed: 37507.3 w/s. Current Word: 'tonysg2'
Average Speed: 34906.0 w/s. Current Word: 'shaung06'
Average Speed: 38656.3 w/s. Current Word: 'pogradec93'
found user-password: 'noobmaster'
```

Flag: `n00bz{CR4CK3D_4ND_CR4CK3D_1a4d2e5f}`