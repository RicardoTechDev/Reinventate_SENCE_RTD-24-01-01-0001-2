a = 5  # en binario es 0101
b = 3  # en binario es 0011

#Da 1 solo si ambos bits son 1.
print(a & b) # AND → 1

"""
    a = 0 1 0 1 --> 5
    b = 0 0 1 1 --> 3
        --------
    AND 0 0 0 1

0001 = 1
"""

#Da 1 si al menos uno es 1
print(a | b)   # OR  → 7