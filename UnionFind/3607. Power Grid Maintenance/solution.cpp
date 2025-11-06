#include <vector>
#include <map>
#include <set>
#include <numeric>  // For iota
#include <algorithm> // For swap

using namespace std;

class Solution
{
    struct DSU
    {
        vector<int> p, r;

        DSU(int n) : p(n, -1), r(n, 0)
        {
            iota(p.begin(), p.end(), 0);
        }
        int find(int x)
        {
            return p[x] == x ? x : p[x] = find(p[x]);
        }
        bool unite(int a, int b)
        {
            a = find(a);
            b = find(b);
            if (a == b)
                return false;
            if (r[a] < r[b])
                swap(a, b);
            p[b] = a;
            if (r[a] == r[b])
                ++r[a];
            return true;
        }
    };

public:
    vector<int> processQueries(int c, vector<vector<int>> &connections, vector<vector<int>> &queries)
    {
        DSU dsu(c + 1);
        for (const auto &conn : connections)
        {
            dsu.unite(conn[0], conn[1]);
        }

        map<int, set<int>> online;
        for (int i = 1; i <= c; i++)
        {
            int p = dsu.find(i);
            online[p].insert(i);
        }

        vector<int> res;
        for (const auto &query : queries)
        {
            int type = query[0], target = query[1];
            int p = dsu.find(target);

            if (type == 1)
            {
                if (online[p].count(target))
                {
                    res.push_back(target);
                }
                else
                {
                    auto iter = online[p].begin();
                    if (iter == online[p].end())
                    {
                        res.push_back(-1);
                    }
                    else
                    {
                        int smallest = *iter;
                        res.push_back(smallest);
                    }
                }
            }
            else
            {
                online[p].erase(target);
            }
        }
        return res;
    }
};