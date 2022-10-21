class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit=0
        m=prices[0]
        for price in prices:
            m= min(m, price)
            if price>m:
                profit=max(profit, price-m)
        return profit