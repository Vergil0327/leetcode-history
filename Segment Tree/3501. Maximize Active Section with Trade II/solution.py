from math import inf
class Solution:
    def maxActiveSectionsAfterTrade(self, s, queries):
        n = len(s)
        
        segments = []
        start = 0
        for i in range(n):
            if i == n - 1 or s[i] != s[i + 1]:
                segments.append((start, i - start + 1))
                start = i + 1
        m = len(segments)
        
        max_power = ceil(log2(n))

        # segment tree for "0" segments - range max query
        rmq = [[-inf] * m for _ in range(max_power)]
        for i in range(m):
            if s[segments[i][0]] == '0' and i + 2 < m: # 由於segments必定0,1交錯, i + 2 < m 這條件確保了後面還接續跟著1-segments, 0-segments
                # 紀錄0-segments[i]跟0-segments[i+2]可以透過trade segments[i+1]來翻轉成"1"
                rmq[0][i] = segments[i][1] + segments[i + 2][1]
        
        # build segment tree
        for power in range(1, max_power):
            range_len = 1 << power
            for i in range(m - range_len + 1):
                rmq[power][i] = max(rmq[power - 1][i],
                                    rmq[power - 1][i + (range_len >> 1)])
        
        def get_max_in_range(l, r):
            if l > r: return -inf

            p = (r - l + 1).bit_length() - 1
            return max(rmq[p][l], rmq[p][r - (1 << p) + 1])
        
        active_count = s.count('1')
        result = []
        for left, right in queries:
            left_index = bisect_right(segments, left, key=lambda x:x[0]) - 1
            right_index = bisect_right(segments, right, key=lambda x:x[0]) - 1
            
            if right_index - left_index + 1 <= 2: # can't trade and flip
                result.append(active_count)
                continue
            
            def get_segment_size(i):
                if i == left_index:
                    return segments[left_index][1] - (left - segments[left_index][0])
                if i == right_index:
                    return right - segments[right_index][0] + 1
                return segments[i][1]
            
            def calculate_new_sections(i):
                if i < 0 or i + 2 >= m or s[segments[i][0]] == '1':
                    return -inf
                return get_segment_size(i) + get_segment_size(i + 2)
            
            # 排除有可能不是完整的left_index跟right_index segments
            # 用segment tree查看[left_index+1, right_index-3]這段範圍的max flipped active counts
            best_increase = max(get_max_in_range(left_index + 1, right_index - 3), 0)

            # 兩端點的0-segments單獨處理, 查看如果我們選擇翻轉最左或最右端點的0-segments, (left_index, left_index+1, left_index+2) or (right_index-2, right_index-1, right_index)
            # 所得到的active counts
            best_increase = max(best_increase, calculate_new_sections(left_index))
            best_increase = max(best_increase, calculate_new_sections(right_index - 2))
            
            result.append(active_count + best_increase)
        
        return result
