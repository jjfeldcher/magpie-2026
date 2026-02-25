def checksum(p):
    u = ((p[1] << 30) | (p[3] << 28) | (p[0] << 26) | (p[2] << 24)) & 0xffffffff
    for i in range(4):
        u ^= ((p[i] * 0xC1BE2077) | 0xC0) & 0xffffffff
        shift = p[i & 1] & 0x1f
        divisor = (0xFFF1 << shift) & 0xffffffff
        m = (0x7fffffff % divisor) + i
        u = (u * m) & 0xffffffff
    return u

target = 0x6748e3e8
moves = ['U','D','L','R']

for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                p = [a,b,c,d]
                if checksum(p) == target:
                    print(moves[a] + moves[b] + moves[c] + moves[d])
                    raise SystemExit