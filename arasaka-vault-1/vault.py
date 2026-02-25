alphabet = "!+-jtN]#QTV9n6fX7;sdO{bF?_xZlpGuz(CiMLg$qA}H*kvP0m5.h[@BwUIocJ%3"
encoded = "ZbN$l]LL7[;]GBM0p{JMn]wBF@kTndNu7.t0phUu?.t0{@Uux.Nndj{uGd+[QFh&"

rev = {}
for i in range(len(alphabet)):
    rev[alphabet[i]] = i

out = bytearray()

i = 0
while i < len(encoded):
    block = encoded[i:i+4]
    vals = []
    pad = 0
    for c in block:
        if c in rev:
            vals.append(rev[c])
        else:
            vals.append(0)
            pad += 1
    triple = (vals[0] << 18) | (vals[1] << 12) | (vals[2] << 6) | vals[3]
    out.append((triple >> 16) & 0xff)
    if pad < 2:
        out.append((triple >> 8) & 0xff)
    if pad < 1:
        out.append(triple & 0xff)
    i += 4

print(out.decode())