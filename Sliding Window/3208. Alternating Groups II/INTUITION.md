# Intuition

直覺想到的是維護一個k-size sliding window, 並紀錄他們的alternating color的數目

[X O X]     => size=3, alternating=2
[X O X ...] => size=n => alternating必須為k-1