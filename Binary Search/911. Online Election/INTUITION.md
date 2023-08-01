# Intuition

*constraints: times is sorted in a strictly increasing order*

there may be a tie and we want previous vote among tied candidates to choose winner

- how to find winner? => hashmap and a current max votes variable
- if there is a tie, leading goes to most recent vote, i.e. current persons[i]

we can also store every winner at each vote in stack, and we can know the previous winner before current round from stack[-1].
- if current persons[i] doesn't has max votes, the winner doesn't change

we can store winner at each vote moment, then we can use binary search by time in `int q(int t)` to find the winner at that moment.