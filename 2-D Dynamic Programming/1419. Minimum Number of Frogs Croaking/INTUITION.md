# Intuition

叫聲僅有五個狀態在轉移: c -> r -> o -> a -> k

五個狀態進行狀態轉移:
當 c -> r: c -= 1 and r += 1
當 r -> o: r -= 1 and o += 1
當 o -> a: o -= 1 and a += 1
當 a -> k: a -= 1 and k += 1
當 k 叫完: a -= 1

每個階段殘留的叫聲總和，就代表該階段需要至少這麼多隻青蛙
iterate i over croakOfFrogs:
    answer = max(answer, c + r + o + a)
