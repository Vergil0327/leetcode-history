# Intuition

直覺想到的是利用prefix跟suffix

> res[i] = prefix_product[i-1] * suffix_product[i+1]

這時觀察一下會發現這個表達式, 答案只跟前一個prefix_product跟後一個suffix product有關
所以可以只用O(1) space