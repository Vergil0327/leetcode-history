# https://wangwilly.github.io/willywangkaa/2018/03/19/Algorithm-Z-%E6%BC%94%E7%AE%97%E6%B3%95/
def z_function(s):
    n = len(s)
    z = [0] * n

    L = R = 0
    for i in range(1, n):
        if i > R:
            L = R = i
            while R < n and s[R-L] == s[R]:
                R += 1
            z[i] = R-L
            R -= 1
        else:
            k = i-L
            if z[k] < R-i+1:
                z[i] = z[k]
            else:
                L = i
                while R < n and s[R-L] == s[R]:
                    R += 1
                z[i] = R-L
                R -= 1
    return z


def search(text, pattern):
    # Create concatenated string "P$T"
    concat = pattern + "$" + text
    l = len(concat)
 
    # Construct Z array
    z = z_function(concat)
 
    #  now looping through Z array for matching condition
    for i in range(len(pattern)+1, len(z)):
        if z[i] == len(pattern):
            print("found pattern at index:", i-len(pattern)-1)

if __name__ == '__main__':
    text = "GEEKS FOR GEEKS"
    pattern = "GEEK"
    search(text, pattern)