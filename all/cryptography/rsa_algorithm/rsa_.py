# Encoding : encode divides the string s (plaintext)into blocks, each block includes 4 letters,
# and calls encode1 for encoding. Input for encode: String s (plaintext), encryption public
# key: n, e. Output: List L of Integers (ciphertext)
# Decoding: decode calls decode1 for decoding each block.
# Input of decode: List L of integers (ciphertext), and decryption key(private key): n, d
# Output : list PL ( the plaintext)
#
def encode1(s, n, e):
    s = str(s)
    r1 = sum(ord(s[i])*256 ^ i for i in range(len(s)))
    r2 = power_mod(r1, e, n)
    return r2


def decode1(m, n, d):
    n = power_mod(m, d, n)
    n = Integer(n)
    v = []
    while n != 0:
        v.append(chr(n % 256))
        n //= 256  # this replace n by floor (n/256)
    return ''.join(v)
# -------------------------------------------------


def encode(s, n, e):
    s = str(s)
    L = []
    PL = []
    m = len(s)/4-1
    for i in [0..m]:
        k = 4*i
        PL.append(s[k:k+4])
        if len(s) % 4 == 1:
            PL.append(s[len(s)-1])
        if len(s) % 4 == 2:
            PL.append(s[len(s)-2: len(s)])
        if len(s) % 4 == 3:
            PL.append(s[len(s)-3: len(s)])
    for i in range(0, len(PL)):
        r = encode1(PL[i], n, e)
        L.append(r)
    return L


def decode(L, n, d):
    PL = []
    for i in range(0, len(L)):
        r = decode1(L[i], n, d)
        PL.append(r)
    return ''.join(PL)


# ----------------------------------
p = next_prime(53265233378754387548735497985395693629760926702937609236720938134895928365982365982659125695691256958615154355874922)
q = next_prime(726932536754815815481451981265826576938769467403976409674096709760272026579267592567925629562956923652986523502393)
e = next_prime(97325279879698693289836598563986591659185691865915691865759265829862659238686875875365)
n = p * q
# -------------------> Publickey is (n,e)
pn = (p-1) * (q-1)
d = inverse_mod(e, pn)
# --------------------> Private (security) key is (n,d)
u ='Someday there will be a new world of shining hope for your family, your fatherland and your mankind'
c = encode(u, n, e)
print(c)
r = decode(c, n, d)
print(r)
