
class Solution:
    def maximizeXorAndXor(self, nums):
        """
        Advanced solution with detailed explanations
        """
        n = len(nums)
        
        # INSIGHT 1: Precompute total XOR of all elements
        # This allows us to quickly compute XOR of unselected elements
        totalXor = 0
        for val in nums:
            totalXor ^= val
        

        def get_linear_basis(arr):
            """
            TECHNIQUE 1: Linear Basis Construction
            
            This is a greedy approach to build linear basis:
            - For each number, try to reduce it using existing basis elements
            - The reduction finds the "canonical form" under the current basis
            - Only add non-zero canonical forms to maintain linear independence
            """
            basis = []
            
            for num in arr:                
                # Try to reduce num using each basis element
                for b in basis:
                    # KEY: Always choose the smaller value between num and num^b
                    # This maintains a "reduced" form and ensures termination
                    num = min(num, num ^ b)                
                if num:  # If we can't reduce to 0, it's linearly independent
                    basis.append(num)
            
            return basis

        def get_max_xor(basis):
            """
            TECHNIQUE 2: Maximum XOR from Linear Basis
            
            Greedy approach: for each basis element, decide whether to include it
            by checking if it increases the current XOR value
            """
            max_xor = 0
            
            for b in basis:
                # Include basis element b if it increases the XOR
                max_xor = max(max_xor, max_xor ^ b)
            
            return max_xor

        maxVal = 0
        
        # STRATEGY: Try all possible ways to select elements for the AND operation (set B)
        for mask in range(1, 1 << n):  # Skip empty set
            
            # STEP 1: Compute AND of selected elements and XOR of selected elements
            selected_AND = -1  # Initialize to handle empty case
            selected_XOR = 0
            unselected = []

            for i in range(n):
                if (mask >> i) & 1:  # Element i is selected for AND operation
                    selected_XOR ^= nums[i]
                    if selected_AND == -1:
                        selected_AND = nums[i]
                    else:
                        selected_AND &= nums[i]
                else:  # Element i goes to unselected pool
                    unselected.append(nums[i])

            
            # STEP 2: INSIGHT - Use XOR properties for unselected elements
            # Since totalXor = selected_XOR ⊕ unselected_XOR
            # We have: unselected_XOR = totalXor ⊕ selected_XOR
            unselected_XOR = totalXor ^ selected_XOR
            
            # STEP 3: MATHEMATICAL INSIGHT - Optimal partitioning of unselected elements
            """
            We want to partition unselected elements into sets A and C to maximize:
            XOR(A) + XOR(C)
            
            If unselected_XOR = XOR(all unselected), and we partition into A and C:
            XOR(A) ⊕ XOR(C) = unselected_XOR
            
            Let x = XOR(A), then XOR(C) = unselected_XOR ⊕ x
            We want to maximize: x + (unselected_XOR ⊕ x)
            
            KEY INSIGHT: This is maximized when we can make both x and (unselected_XOR ⊕ x)
            as large as possible. The optimal strategy involves finding the maximum XOR
            subset that can be formed from a "reduced" version of the unselected elements.
            """
            
            # STEP 4: Bit manipulation trick for reduction
            inverted_mask = ~unselected_XOR
            
            # Reduce each unselected element by masking with inverted_mask
            # This effectively "removes" the bits that are set in unselected_XOR
            reduced = [(x & inverted_mask) for x in unselected]
            
            # STEP 5: Find maximum XOR from reduced elements using linear basis
            basis = get_linear_basis(reduced)
            max_xor = get_max_xor(basis)
            
            # STEP 6: MATHEMATICAL FORMULA
            """
            The final formula: selected_AND + unselected_XOR + 2 * max_xor
            
            Why 2 * max_xor?
            - max_xor represents the maximum XOR we can achieve from the reduced elements
            - Due to the reduction and XOR properties, this translates to an improvement
            of 2 * max_xor in the final sum XOR(A) + XOR(C)
            - The factor of 2 comes from the mathematical relationship between
            the original partition problem and the reduced problem

            The Mathematical Insight
            The key insight is analyzing the function f(x) = x + (unselected_XOR ⊕ x) bit by bit:
            Bit-Level Analysis
            For any bit position i, let's see what happens:

            If unselected_XOR[i] = 1:

            If x[i] = 0: contribution = 0 + 1 = 1
            If x[i] = 1: contribution = 1 + 0 = 1
            Result: Always contributes 1 (cannot be improved)


            If unselected_XOR[i] = 0:

            If x[i] = 0: contribution = 0 + 0 = 0
            If x[i] = 1: contribution = 1 + 1 = 2
            Result: Can contribute 0 or 2 (improvable!)



            The Strategy

            Fixed bits: Where unselected_XOR[i] = 1, we always get contribution 1
            Improvable bits: Where unselected_XOR[i] = 0, we want to set x[i] = 1 to get contribution 2 instead of 0

            Why the Bit Mask
            pythoninverted_mask = ~unselected_XOR
            reduced = [(x & inverted_mask) for x in unselected]

            inverted_mask identifies exactly the "improvable" bit positions (where unselected_XOR = 0)
            reduced elements contain only the bits that can actually improve our score
            We find the maximum XOR possible using only these improvable bits

            The Formula Breakdown
            Total = selected_AND + [base_contribution] + [improvement]
            Where:

            selected_AND: Contribution from set B (given)
            base_contribution = unselected_XOR: The fixed contribution we always get

            This equals the sum of all "fixed" bit positions (each contributes 1)


            improvement = 2 * max_xor: The extra score from optimizing improvable bits

            max_xor = maximum XOR achievable using only improvable bits
            Factor of 2 because each improvable bit contributes 2 instead of 0



            Why Factor 2?
            Each bit position where we can improve contributes:

            Without optimization: 0 (both x[i] and (unselected_XOR ⊕ x)[i] are 0)
            With optimization: 2 (both x[i] and (unselected_XOR ⊕ x)[i] are 1)
            Net improvement per bit: 2 - 0 = 2

            So if we can achieve XOR value max_xor using the improvable bits, our total improvement is 2 * max_xor.
            """
            current_val = selected_AND + unselected_XOR + 2 * max_xor
            
            maxVal = max(maxVal, current_val)

        return maxVal
