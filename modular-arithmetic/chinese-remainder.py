def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def mod_inverse(a, m):
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError(f"The modular inverse of {a} modulo {m} does not exist.")
    return x % m

def chinese_remainder_theorem(congruences):
    M = 1
    for _, mi in congruences:
        M *= mi

    result = 0
    for ai, mi in congruences:
        Mi = M // mi
        yi = mod_inverse(Mi, mi)
        result += ai * Mi * yi

    return result % M

congruences = [(2, 5), (3, 11),(5,17)] 
a = chinese_remainder_theorem(congruences)
print("x ≡ a (mod M) ->", a)
