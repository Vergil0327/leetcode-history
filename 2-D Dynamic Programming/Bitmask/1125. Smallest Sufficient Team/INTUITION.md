# Intuition

目標是找出一個可滿足req_skills的people的最小subset

再來觀察一下邊界條件
- 1 <= req_skills.length <= 16
- 1 <= people.length <= 60

這時發現`req_skills.length`非常的小，最多就16種，所以我們可以用bitmask來表示當前的req_skills狀態

這樣狀態數為 2^16，再加上如果每次都要遍歷每個people來更新狀態的話，時間複雜度上限為 2^16 * 60，屬於可接受範圍，因此我們可以繼續考慮Dynamic Programming with Bitmask

那我們試著這樣定義DP:

`dp[skill_state]: the minimum possible size of sufficient team to satisfy skill_state`

ex. if skill_state = 1001 -> dp[skill_state] means the minimum size of sufficient team which satisfies {req_skills[0], req_skills[3]}

and we can also use bitmask to represent every people[i].

```py
skill2idx = {skill: i for i, skill in enumerate(req_skills)}
peopleSkills = []
for p in people:
    state = 0
    for skill in p:
        state |= (1<<skill2idx[skill])
    peopleSkills.append(state)
```

then, we can try to construct state transfer process.

**State Transfer**

first, we enumerate every possible state and update DP

it's easier to update future state `dp[next_state]` by using current `dp[current_state]`, since we can derive future state with current state plus any of people[i]

```py
for skill in peopleSkills:
    # if we choose people[i], next_state should be current state + peopleSkills[i]
    dp[next_state] = min(dp[next_state], dp[state]+1)
```

since we want to know all the people we selected, let's change implementation a little bit.
we use hashset to store selected people[i] for every state

```py
res = defaultdict(set)
for i, personSkills in enumerate(peopleSkills):
    if dp[state]+1 < dp[next_state]:
        dp[next_state] = dp[state]+1
        res[next_state] = res[state] | {i}
```

and our target is to satisfy `(1<<n)-1` state. thus `dp[(1<<n)-1]` should be minimum size of sufficient team and `res[(1<<n)-1]` should be a hashset which stores selected people

**base case**
dp[0] = 0, for 0 req_skills, the minimum people we need is 0

# Complexity

- time complexity
$$O(2^n * m)$$

- space complexity
$$O(2^n)$$