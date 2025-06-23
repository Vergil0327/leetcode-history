typedef long long ll;

class Solution {
public:
    ll genOddPalindrome(ll n) {
        int cur = n;
        ll rev = 0;
        int digits = 0;

        while (cur > 0) {
            rev = rev*10 + cur%10;
            cur /= 10;
            digits++;
        }

        return (n/10) * pow(10, digits) + rev;
    }

    ll genEvenPalindrome(ll n) {
        int cur = n;
        ll rev = 0;
        int digits = 0;

        while (cur > 0) {
            rev = rev*10 + cur%10;
            cur /= 10;
            digits++;
        }

        return n * pow(10, digits) + rev;
    }
    
    bool isKMirror(ll n, int k) {
        vector<int> arr;
        while (n > 0) {
            arr.push_back(n%k);
            n /= k;
        }

        int l = 0, r = arr.size() - 1;

        while (l < r) {
            if (arr[l] != arr[r]) return false;

            l++;
            r--;
        }

        return true;
    }
    long long kMirror(int k, int n) {
        int length = 1;
        ll res = 0;
        int count = 0;

        while (count < n) {
            int start = pow(10, length-1);
            int end = pow(10, length);

            for (int i=start; i<end; i++) {
                ll val = genOddPalindrome(i);
                if (isKMirror(val, k)) {
                    res += val;
                    count++;
                    if (count == n) {
                        return res;
                    }
                }
            }
            
            for (int i=start; i<end; i++) {
                ll val = genEvenPalindrome(i);
                if (isKMirror(val, k)) {
                    res += val;
                    count++;
                    if (count == n) {
                        return res;
                    }
                }
            }

            length++;
        }

        return res;
    }
};