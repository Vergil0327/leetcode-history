# Intuition

**Hash By Person**
比較直覺的方式是，我們可以將每個人的company加入到Hashset裡，然後在O(N^2)遍歷比對看是不是其他人的subset

**Hash By Company**
但我們也可以反過來看說，每個company屬於哪些人，將這些人加入Hashset裡，然後遍歷比對當下的person[i]所擁有的company有沒有被其他人給擁有，如果都沒有，那就不是別人的subset

並且在數據規模小的時候，可以用bitmask替換hashset查看有無交集