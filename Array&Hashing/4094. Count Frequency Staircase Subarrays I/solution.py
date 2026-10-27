class Solution:
    def countStaircase(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0

        # Precompute triangular lengths k * (k + 1) // 2 mapping to k
        triangular_to_k = {}
        k = 1
        while True:
            tri_len = k * (k + 1) // 2
            if tri_len > n:
                break
            triangular_to_k[tri_len] = k
            k += 1

        for i in range(n):
            freq = {}
            first_appear = []  # Tracks distinct elements in order of arrival

            for j in range(i, n):
                val = nums[j]
                if val not in freq:
                    freq[val] = 1
                    first_appear.append(val)
                else:
                    freq[val] += 1

                length = j - i + 1

                # A valid staircase can only occur at triangular lengths
                if length in triangular_to_k:
                    k_expected = triangular_to_k[length]

                    # Must have exactly k_expected distinct elements
                    if len(first_appear) == k_expected:
                        # Check if m-th element appears exactly m times
                        valid = True
                        for idx, elem in enumerate(first_appear):
                            expected_count = idx + 1
                            if freq[elem] != expected_count:
                                valid = False
                                break

                        if valid:
                            ans += 1

        return ans