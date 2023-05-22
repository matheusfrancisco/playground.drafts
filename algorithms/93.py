import itertools

s = "25525511135"

def is_valid(ip):
    for chunk_ip in ip:
        if int(chunk_ip) <= 255 and not (chunk_ip[0] == "0" and chunk_ip != "0"):
            pass
        else:
            return False
    return True

        
def solve(s):
    out = []
    for i, j, l in itertools.combinations(range(1, len(s)), 3):
        possible_ip = [s[:i], s[i:j], s[j:l], s[l:]]
        if is_valid(possible_ip):
            out.append(".".join(possible_ip))
    return out

print(solve(s))



        
