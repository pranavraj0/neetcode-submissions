class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_rate = max(1, sum(piles) // h)
        max_rate = max(piles)

        best_rate = max_rate
        while min_rate <= max_rate:
            mid_rate = (min_rate + max_rate) // 2

            hours_mid_rate = 0
            for p in piles:
                hours_mid_rate += (p + mid_rate - 1) // mid_rate
            if hours_mid_rate <= h:
                # if mid rate allows all bananas to be eaten, can try reducing mid rate
                best_rate = mid_rate
                max_rate = mid_rate - 1
            else:
                # if mid rate doesn't allow banans to be eaten, have to increase rate
                min_rate = mid_rate + 1
        return best_rate
        