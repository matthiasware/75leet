class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = 10e5
        max_sell = 0
        profit = 0
        for idx, item in enumerate(prices):
            if item < min_buy:
                min_buy = item
                max_sell = 0
            elif item - min_buy > profit:
                profit = item - min_buy
        return profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 10e5
        P = 0
        for R in prices:
            if R < L:
                L = R
            else:
                p_new = R - L
                if p_new > P:
                    P = p_new
        return P