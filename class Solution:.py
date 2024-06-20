class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')
        
        for num in nums:
            if num <= first:
                first = num  # Find the smallest possible value for the first element
            elif num <= second:
                second = num  # Find the smallest possible value for the second element, which is greater than the first
            else:
                # If we find a third element that is greater than both `first` and `second`, we have our triplet
                return True
        
        return False
