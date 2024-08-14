class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in flights:
            graph[u].append((v, w))

        pq = [(0, src, 0)]

        min_cost = {}

        while pq:
            cost, city, stops = heapq.heappop(pq)

            if city == dst:
                return cost

            if stops <= k:
                for next_city, price in graph[city]:
                    next_cost = price + cost

                    if (next_city, stops + 1) not in min_cost or next_cost < min_cost[(next_city, stops + 1)]:
                        min_cost[(next_city, stops + 1)] = next_cost
                        heapq.heappush(pq, (next_cost, next_city, stops + 1))
        return -1