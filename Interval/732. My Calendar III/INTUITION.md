# Intuition

```
example 1.
    10         20
                            50      60
    10                 40
5   10
                  25            55
```

目的是要算最大重疊區間 => use sweep line to find overlap
=> think difference array
=> +1 at startTime, -1 at endTime
=> we can sweep timeline to find maximum overlap interval