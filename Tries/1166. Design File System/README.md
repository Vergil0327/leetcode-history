1166. Design File System

*[SUBSCRIBE TO UNLOCK](https://leetcode.com/problems/design-file-system/)*

You are asked to design a file system that allows you to create new paths and associate them with different values.

The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters. For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string "" and "/" are not.

Implement the FileSystem class:

bool createPath(string path, int value) Creates a new path and associates a value to it if possible and returns true. Returns false if the path already exists or its parent path doesn't exist.
int get(string path) Returns the value associated with path or returns -1 if the path doesn't exist.
Example 1:

Input: 
["FileSystem","createPath","get"]
[[],["/a",1],["/a"]]
Output: 
[null,true,1]
Explanation: 
FileSystem fileSystem = new FileSystem();

fileSystem.createPath("/a", 1); // return true
fileSystem.get("/a"); // return 1
Example 2:

Input: 
["FileSystem","createPath","createPath","get","createPath","get"]
[[],["/leet",1],["/leet/code",2],["/leet/code"],["/c/d",1],["/c"]]
Output: 
[null,true,true,2,false,-1]
Explanation: 
FileSystem fileSystem = new FileSystem();

fileSystem.createPath("/leet", 1); // return true
fileSystem.createPath("/leet/code", 2); // return true
fileSystem.get("/leet/code"); // return 2
fileSystem.createPath("/c/d", 1); // return false because the parent path "/c" doesn't exist.
fileSystem.get("/c"); // return -1 because this path doesn't exist. 
Constraints:

The number of calls to the two functions is less than or equal to 104 in total.
2 <= path.length <= 100
1 <= value <= 10^9

<details>
<summary>solutions</summary>

[here](https://www.cnblogs.com/Dylan-Java-NYC/p/16632244.html)
[here](https://cloud.tencent.com/developer/article/1787780)

```java
class FileSystem {
    Map<String, Integer> map;

    public FileSystem() {
        map = new HashMap<>();
        map.put("", -1);
    }

    public boolean createPath(String path, int value) {
        int ind = path.lastIndexOf("/");
        if(ind == -1){
            return false;
        }

        String parent = path.substring(0, ind);
        if(!map.containsKey(parent)){
            return false;
        }

        return map.putIfAbsent(path, value) == null;
    }

    public int get(String path) {
        return map.getOrDefault(path, -1);
    }
}

/**
 * Your FileSystem object will be instantiated and called as such:
 * FileSystem obj = new FileSystem();
 * boolean param_1 = obj.createPath(path,value);
 * int param_2 = obj.get(path);
 */

 class FileSystem {
    TrieNode root;

    public FileSystem() {
        root = new TrieNode();
    }

    public boolean createPath(String path, int value) {
        TrieNode cur = root;
        String [] arr = path.split("/");
        for(int i = 1; i < arr.length; i++){
            if(!cur.nexts.containsKey(arr[i])){
                if(i == arr.length - 1){
                    cur.nexts.put(arr[i], new TrieNode());
                }else{
                    return false;
                }
            }

            cur = cur.nexts.get(arr[i]);
        }

        if(cur.val != null){
            return false;
        }

        cur.val = value;
        return true;
    }

    public int get(String path) {
        TrieNode cur = root;
        String [] arr = path.split("/");
        for(int i = 1; i < arr.length; i++){
            if(!cur.nexts.containsKey(arr[i])){
                return -1;
            }

            cur = cur.nexts.get(arr[i]);
        }

        return cur.val == null ? -1 : cur.val;
    }
}

class TrieNode{
    Map<String, TrieNode> nexts;
    Integer val;

    public TrieNode(){
        nexts = new HashMap<>();
    }
}

/**
 * Your FileSystem object will be instantiated and called as such:
 * FileSystem obj = new FileSystem();
 * boolean param_1 = obj.createPath(path,value);
 * int param_2 = obj.get(path);
 */

 class FileSystem {
	unordered_map<string,int> m;
public:
    FileSystem() {
    	m["/"] = 0;
    }
    
    bool createPath(string path, int value) {
    	if(m.count(path+"/")) return false;
    	string tmp = path;
    	while(tmp.back() != '/') 
    		tmp.pop_back();//去除最后一层路径
    	if(!m.count(tmp)) return false;//前置路径不存在
    	m[path+"/"] = value;
    	return true;
    }
    
    int get(string path) {
    	if(m.count(path+'/'))
    		return m[path+'/'];
    	return -1;
    }
};
```

```go
type TrieNode struct{
  next map[rune]*TrieNode
  eow bool // end of word
}

type FileSystem struct {
  root *TrieNode
}

func NewFileSystem() FileSystem{
  return FileSystem{root: &TrieNode{next: make(map[rune]*TrieNode)}}
}

func (fs *FileSystem) CreatePath(path string, value int) bool {

}

func (fs *FileSystem) get(path string) int {

}
```
</details>