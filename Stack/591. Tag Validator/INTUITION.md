# Intuition

首先想到肯定會利用到`Stack`來比對前後tag是否matched

主要有兩種tag
1. `<![CDATA[`  CDATA_CONTENT   `]]>`
2. `<TAG_NAME>` TAG_CONTENT     `</TAG_NAME>`

由於CDATA中間不管什麼content都可以合法捕捉，所以先處理CDATA tag

再來再找出合法的`<TAG></TAG>`

由於Open Tag可能會跟Closed Tag混淆(因為開頭都是`<`)，但Closed Tag一定是`</`開頭，
因此我們先找尋Closed Tag

如果沒找到Closed Tag並且也過濾掉CDATA tag，那麼再找到的`<`開頭一定是Open Tag

確定好if-elif-else順序後:

1. 每當找到Closed Tag，找出TAG_NAME並且與Stack內的TAG_NAME相比對，看是否matched
2. 每當找到Open Tag，先檢查是否符合規則，如果是合法TAG_NAME就加入到stack裡
   1. 是否為alphanum
   2. 長度是否在[1,9]這區間
   3. 是否都大寫

**Edge Case**
整個string必須被一個Open-Closed Tag給捕捉，因此我們必須額外判斷找到的第一個open-closed tag是否捕捉整個string，並且TAG_NAME頭尾一致

# Complexity

- time complexity
$$O(N)$$

- space complexity
$$O(N)$$