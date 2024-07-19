from typing import List
import unittest
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        return res




# unittest for Best Time to Buy and Sell Stock
class TestMaxProfit(unittest.TestCase):
    def test_maxProfit(self):
        self.assertEqual(Solution().maxProfit([7,1,5,3,6,4]), 5)
        self.assertEqual(Solution().maxgitProfit([7,6,4,3,1]), 0)


if __name__ == "__main__":
    # execute unit test
    unittest.main()