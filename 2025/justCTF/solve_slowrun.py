from Crypto.Util.number import long_to_bytes

F_cache = [-1] * 100000  
G_cache = [-1] * 100000  
def G(n):
    if G_cache[n] != -1:
        return G_cache[n]

    if n <= 1:
        return 1
    result = F(n - 1) + 3 * F(n - 2) - 5 * F(n - 3) + 3 * (n**4)
    
    G_cache[n] = result
    return result

def F(n):
    if F_cache[n] != -1:
        return F_cache[n]

    if n == 0:
        return 2
    if n == 1:
        return 1
    if n < 0:
        return 1
    term_1 = 73 * (n**5)
    term_2 = 8 * (n**3)
    term_3 = n - 4 
    term_4 = G(n - 1)
    
    result = term_1 + term_2 + term_3 + term_4
    
    F_cache[n] = result
    return result

if __name__ == "__main__":
    for input_value in range(100,100000):
        final_result = F(input_value)
        secret = (final_result \
        + 12871709638832864416674237492708808074465131233250468097567609804146306910998417223517320307084142930385333755674444057095681119233485961920941215894136808839080569675919567597231) \
        % 12871709638832864416674237492708808074465131233250468097567609804146306910998417223517320307084142930385333755674444057095681119233485961920941215894136808839080569675919567597231 \
        + 805129649450289111374098215345043938348341847793365469885914570440914675704049341968773123354333661444680237475120349087680072042981825910641377252873686258216120616639500404381

        if secret < 0:
            continue
        flag = (long_to_bytes(secret).decode(errors="ignore"))
        if "just" in flag:
            print(flag)
            break

# justCTF{1n_0rd3r_70_und3r574nd_r3cur510n_y0u_h4v3_t0_und3r574nd_r3cur510n}