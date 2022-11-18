this is a follow-up of [264. Ugly Number II](../264.%20Ugly%20Number%20II/)

if we use same technique in 264., it'll be `O(N*K)` where N is n-th number and K is len(Primes)

it looks inefficient if we need to iterate through all the primes to find minimum ugly number and see if we need to update its pointer or not

what kind of data structure we can use to find minimum value quickly ?

I think priority queue (min heap) is a good choice here

thus, we can use priority queue (min heap) to find minimum ugly number quickly and update its pointer at the same time if we use 2-D array in priority queue