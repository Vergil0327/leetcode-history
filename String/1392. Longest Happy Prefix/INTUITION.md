# Intuition

s = XXXXYYYY

XXXX == YYYY
YYYY
   XXXX
  XXXX
 XXXX
XXXX

for effecient comparison, try hash string before comparison

```
hash(X) = hash(Y)
hash(XX) = hash(YY)
hash(XXX) = hash(YYY)
hash(XXXX) = hash(YYYY)
hash(prefix) = hash(suffix)

hashedPrefix = ?
hashedSuffix = ?

rolling hash -> hashedPrefix[i] = hashedPrefix[i-1] + hash(s[i]) where i += 1 if i < n
             -> hashedSuffix[i] = hashedSuffix[i-1] + hash(s[j]) where j -= 1 if j >= 0
```

Hashed Prefix:

XXXX
i ->

key = ord(s[i])
hash = hash * P + key

add i+1
hash = hash * P + key

P we can choose a prime number to distribute each hashed key

thus, we can start with `hashedPrefix = hashedSuffix = 0`
and use two pointers to do rolling hash and keep comparing both.

Hashed Suffix:

XXXX
<- j

hashedSuffix = ord(s[j]) * pow(P, # of digits - 1) + hashedSuffix

if we have hash collision, once hashedPrefix == hashedSuffix, we should check if prefix == suffix.
then, we can safely update our res to current length
