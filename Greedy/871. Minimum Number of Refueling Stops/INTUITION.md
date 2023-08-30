# Intuition

startFuel -> X X X X X X X X X X X

if refuel at i, we can reach `farthest position we can reached + stations[i][1]`

intuitively to come up with choosing available stations[i] which can make us reach farthest position first
=> greedy apporach

we can use max heap to pick best stations[i] amoung all the available stations where stations[i][0] <= the farthest position we can reach

1. keep record our farthest reached position and see if we can reach target by refueling at available stations

2. store available stations in max heap and refuel at best choice first

3. keep refueling until we reach target

4. if we run out of stations before we reach target => return -1