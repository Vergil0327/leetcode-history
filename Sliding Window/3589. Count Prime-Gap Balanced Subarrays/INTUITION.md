# Intuition
            
首先可以用埃氏篩(sieve of Eratosthenes)找出is_primes[nums[i]]來表示nums[i]是否為質數
然後利用sliding window的方式，維持一個SortedList來存儲當前window內的質數, 並同時紀錄該window內的質數的index

如此一來, 對於當前的合法右質數端點indices[-1]來說, 我們可以求出合法的左端點個數為`indices[-2]-l+1`

# Optimized

利用deque取代SortedList來找出maximum和minimum, 這樣可以減少時間複雜度