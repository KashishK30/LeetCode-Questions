class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        current = numBottles 
        count = numBottles
        while current >= numExchange:
            new_bottles = current // numExchange
            count += new_bottles
            current = new_bottles + (current % numExchange)
        return count