# Intuition

標記當前是否是block comment的狀態

是 -> 找尋`"*/"`
否 -> 查看是否是line comment (`"//"`是否存在)

如果兩種comment都不存在, 持續將字符存入`buffer`並append到最終答案裡