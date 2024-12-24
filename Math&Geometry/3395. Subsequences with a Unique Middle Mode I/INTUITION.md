# Intuition

seq.size == 5 and seq[2] is majority

合法組合：
1. XXXXX
2. A XXXX
3. XXXX A
4. A XXX B
5. A XX B C 
6. A B XX C

這邊除了組合數, 還得利用排容原理在condition5跟condition6上
A B C 不可有任何一個數相同或三數都相同而產生double跟tripple倒是不再有unique mode

```py
def calc_2(elem, first_counter, second_counter, first_other_cnt, second_other_cnt):
    """
    Calculate the number of ways to choose two elements other than elem from the sequence
    """
    # count include
    result = first_other_cnt * comb_2(second_other_cnt)

    for k, v in first_counter.items():
        if k == elem: continue

        vv = second_counter[k]
        # count exclude triples -- [0 1] 1 [0 0]
        result -= v * comb_2(vv)
        # count exclude doubles -- [0 1] 1 [0 2] / [0 1] 1 [2 0]
        result -= v * vv * (second_other_cnt - vv)
    
    for k, v in second_counter.items():
        if k == elem: continue

        # count exclude doubles -- [0 1] 1 [2 2]
        result -= comb_2(v) * (first_other_cnt - first_counter[k])
    
    return result

# condition 5: [0 1] 1 [0 0] - 2 elements
left_cnt * calc_2(nums[i], left, right, left_other, right_other) % mod

# condition 6: [0 0] 1 [0 1] - 2 elements
right_cnt * calc_2(nums[i], right, left, right_other, left_other) % mod
```

