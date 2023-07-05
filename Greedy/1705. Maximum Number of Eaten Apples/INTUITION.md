# Intuition

think **Greedy** first.

for apples[i], it'll be outdated at i+days[i], then we should eat those which are about to be outdated first.

if we use a min heap, stores element as [outdated_day, numApples],
    => first, we should dump all the outdated apples
    => second, eat one apple => eaten += 1

after iteration, no more growing apples, therefore, we only can eat remaining apples
**keep eating until all the apples are rotten**, then return `eaten` as answer