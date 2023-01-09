# Intuition

first byte define the next continuous data to be n-bytes data

therefore, let's count one bit in least 8 bit from left to right first

and we can know how many `1` bit we got

let's say we have `ones` 1 bit

- `ones` can't be **1** since 1-byte UTF-8 data is 0 1 bit. thus, if `ones=1` return **False**
- based on UTF-8 definition, `ones` can't greater than 4. thus, if `ones >= 5`, return **False**

now, valid `ones` can be:

**0**: when `ones=0`, it means this continuous data is 1-byte UTF-data and it is always correct

**2**, **3**, **4**: it means 2~4 bytes UTF-8, we need to check:
  1. if next `n-1` data start with `10` or not.
  2. if we have enough `n-1` bytes

after checking every thing done, we can return **True**
