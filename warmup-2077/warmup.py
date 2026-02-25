key = [0xDE, 0xAD, 0xBE, 0xEF]
b64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def b64decode(s):
    table = {c:i for i,c in enumerate(b64)}
    out = bytearray()
    i = 0
    while i < len(s):
        n = (table[s[i]] << 18) | (table[s[i+1]] << 12) | (table[s[i+2]] << 6) | table[s[i+3]]
        out.append((n >> 16) & 0xff)
        out.append((n >> 8) & 0xff)
        out.append(n & 0xff)
        i += 4
    return bytes(out)

def decode(s):
    raw = b64decode(s)
    return bytes(raw[i] ^ key[i & 3] for i in range(len(raw)))

print(decode("uszIhrray5W2yMyK75+N"))
print(decode("qsXXnLfe3527zNKDp97KnbHD2Z+/3s2Ysd/ag7HB0YOxwdGD"))