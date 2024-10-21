# Intuition

逆向思考, 從`target`一路逆著操作回來即可

ex. abc

`abc -> abb -> aba -> ab -> aa -> a`

或者從`a`透過操作1 `append`跟操作2 `convert`正向操作直到形成`target`也行

time: O(n * (26*n))