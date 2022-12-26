# Concise Solution
class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = path.split("/")

        stack = []
        for d in directories:
            if not d: continue
            if d == ".": continue
            if d == "..":
                if stack: stack.pop()
                continue
            stack.append(d)

        path = ""
        while stack:
            path = "/" + stack.pop() + path

        return path if path else "/"

# Stack first try
class Solution:
    def simplifyPath(self, path: str) -> str:
        n = len(path)
        paths = []
        for i in range(n):
            if i > 0 and path[i] == "/" and path[i-1] == "/": continue
            paths.append(path[i])
        
        if paths[-1] == "/":
            paths.pop()

        res = []
        paths = "".join(paths).split("/")
        for directory in paths:
            if not directory: continue
            if directory == ".": continue
            if directory == "..":
                if res: res.pop()
                continue
            res.append(directory)

        p = "/"
        for directory in res:
            p += directory + "/"
        return p[:-1] if len(p) > 1 else p