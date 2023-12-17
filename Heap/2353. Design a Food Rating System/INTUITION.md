# Intuition 1

replace sorted set with max heap

# Intuition 2

All the strings in foods are distinct. => foods[i] as key for mapping

=> food2cuisine[foods[i]] = cuisines[i]
=> food2rating[foods[i]] = ratings[i]

then we can call changeRating in O(1) to set new rating for any food

as for highestRated, 
we need a sorted data structure to check highest rating in target cuisine
=> we can add (-rating, food) to SortedSet and classify every SortedSet by cuisine
=> defaultdict(SortedSet): {cuisine: SortedSet}

then, each time we call changeRating, we maintain SortedSet by:

1. remove old rating in sorted set
    - we can know old rating by food2rating[food], therefore, key of food with old rating is `key = (-food2rating[food], food)`
    - just call SortedSet.remove(key)


2. add new rating to sorted set
    - new_key = (-newRating, food)
    - SortedSet.add(new_key)

then we can find highest rating in O(1) from SortedSet by: `weight, food = next(iter(SortedSet))`