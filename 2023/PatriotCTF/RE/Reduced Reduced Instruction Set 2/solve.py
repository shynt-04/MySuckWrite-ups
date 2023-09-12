data = [65,98,35,69,36,92,67,56,32,76,47,106,14,120,24,67,115,35,97,37,94,147,15,120,47,113,57,52,113,31,93,61,124,58,107,45,131,201,224,231,172,238,200,203,218,213,40,55,115,76,91,174,18,175,252,209,221,55,142,35,143,37,126,75,167,200,205,239,206,3,168,34,77,135,241,221,254,231,208,76,188,8,185,31,147,38,157,80,123,115,91,214,2,199,13,202,31,148,23,225,246,60,185,63,194,76,141,87,227,5,219,46,126,126,137,88,156,102,121,129,110,199,33,202,43,136,100,138,122,143,50,200,38,199,41,204,62,167,87,196,56,220,65,240,38,217,77,210,64,197,72,184,112,183,50,225,33,223,86,215,95,207,93,219,77,9,207,46,3,204,80,206,155,168,55,242,60,253,75,31,201,92,240,136,180,123,211,92,228,75,253,72,252,87,250,88,61,36,20,44,13,50,11,246,108,207,190,153,194,125,240,108,33,26,82,9,58,243,122,250,107,252,120,233,170,165,174,114,234,104,243,187,180,194,142,211,170,204,152,208,149,167,193,166,123,254,146,218,175,200,166,191,216,246,147,234,203,172,143,231,135,249,148,249,148,190,216,195,187,236,219,205,181,223,205,189,178,242,158,12,135,252,169,165,204,193,198,7,152,26,140,10,163,240,198,208,204,23,158,30,150,39,54,114,75,96,115,70,95,101,68,93,120,87,94,172,201,205,225,211,53,146,46,147,68,122,93,128,245,32,162,24,185,32,79,126,175,22,198,244,213,76,150,87,151,76,147,16,220,25,152,12,129,4,163,231,245,1,219,32,173,247,1,208,94,154,111,143,85,166,57,208,42,128,90,155,53,238,62,154,93,251,12,227,24,246,22,186,54,218,71,172,77,170,91,8,215,138,58,235,23,6,185,95,197,124,170,93,13,199,47,227,36,162,111,170,128,139,136,145,87,228,63,199,83,220,93,228,46,188,141,156,154,178,116,9,248,68,223,111,211,91,55,49,14,42,25,57,13,227,135,181,163,147,123,214,111,212,124,41,14,73,57,33,33,211,143,187,158,149,189,168,155,200,133,206,137,136,203,133,217,142,207,161,183,191,185,198,141,206,153,233,181,174,206,158,220,173,202,177,242,164,206,246,122,68,50,62,13,98,5,91,62,17,105,59,96,70,50,12,130,2,122,86,23,142,0,131,249,175,241,161,193,172,220,210,13,118,59,121,58,115,54,101,34,37,106,40,126,61,128,28,102,58,117,130,18,97,60,138,49,140,24,177,199,223,241,11,168,2,157,45,146,34,150,65,113,89,189,34,148,44,140,55,159,70,126,100,85,196,1,181,32,167,219,2,192,252,230,220,87,141,73,135,78,205,2,200,31,206,16,199,78,136,87,224,254,2,211,97,127,130,84,174,51,186,84,161,76,227,98,132,114,205,37,200,42,196,33,197,36,135,117,161,92,187,36,206,121,168,78,181,98,150,117,161,98,169,30,242,42,230,46,232,53,176,112,182,101,172,106,185,56,187,113,190,120,178,128,74,205,79,216,88,235,54,4,28,27,238,60,5,219,119,202,120,215,97,200,95,239,74,238,144,181,144,117,198,117,215,192,109,204,138,197,110,235,107,212,140,187,166,157,208,199,165,162,161,176,160,162,174,109,225,104,42,46,36,48,42,41,52,47,248,119,253,114,243,206,222,155,229,115,71,33,58,58,12,254,164,199,158,187,235,129,230,132,236,140,3,107,81,57,88,49,99,17,111,92,67,63,47,108,22,134,9,129,253,169,243,175,169,227,223,201,215,209,210,220,223,214,27,157,35,119,58,67,86,91,167,243,2,161,254,195,236,192,224,197,227,185,20,170,25,171,5,98,79,121,91,105,95,121,81,105,99,81,134,50,102]

cnt = 0
last = 0
flag = ""
for x in data:
    y = x
    cur = (x - cnt) ^ last
    while cur > 255 or cur < 0:
        x += 255
        cur = (x - cnt) ^ last
    flag += chr(cur)
    last = y
    cnt += 1
    cnt %= 255

print(flag)