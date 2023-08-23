# Intuition

apparently, we should use rolling hash, but how?

```
val(s[0]) * p0 + val(s[1]) * p1 + ... + val(s[k-1]) * pk-1
                 val(s[1]) * p0 + ... + val(s[k-1]) * pk-2 + val(s[k]) * pk-1
```

In Rabin-Karp algorithm (rolling hash), the hash function is
`hash(s, p, m) = (val(s[0]) * p^(k-1) + val(s[1]) * p^(k-2) + ... + val(s[k-1]) * p^0) mod m.`

if we start from left to right, we need to:
    1. -= val(s[0])
    2. //= p1
    3. += val(s[k]) * pk-1

since division can't work correctly with modulo, therefore, we should rolling hash backwards

we want:
    `res1 = val(s[1]) * p0 + ... + val(s[k-1]) * pk-2 + val(s[k]) * pk-1`
to become:
    `res2 = val(s[0]) * p0 + val(s[1]) * p1 + ... + val(s[k-1]) * pk-1`

we should:
1. -= val(s[k]) * pk-1
2. res1 *= p1
3. += val(s[0])
4. res2 = (res2+m)%m since we have substraction, avoid negative value
5. and we can preprocess val(s[i]) and p0 ~ pk-1