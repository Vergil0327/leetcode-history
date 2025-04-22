# Intuition

這題數據規模很小, 遍歷每個strs[i]的可能subseq.然後再跟其他strs[j]比對亦可過關

但其實我們無須遍歷每個strs[i]的可能subseq, 將它自身作為subseq.去檢視
如果strs[i]不是任何人的subseq, 那它自身長度就是possible answer

將自身做完subseq.是因為, 假設他有更短的subseq不是任何人的subseq.
那們它自身也必定不是任何人的subseq.