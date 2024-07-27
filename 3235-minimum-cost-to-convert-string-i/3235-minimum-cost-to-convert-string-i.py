class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        if len(source) != len(target):
            return -1
        
        # Step 1: Build the graph
        graph = defaultdict(list)
        for o, c, z in zip(original, changed, cost):
            graph[o].append((c, z))
        
        # Step 2: Use Dijkstra's algorithm to find shortest path costs for each character transformation
        def dijkstra(start):
            pq = [(0, start)]
            distances = {char: float('inf') for char in "abcdefghijklmnopqrstuvwxyz"}
            distances[start] = 0
            
            while pq:
                current_cost, current_char = heapq.heappop(pq)
                
                if current_cost > distances[current_char]:
                    continue
                
                for neighbor, weight in graph[current_char]:
                    new_cost = current_cost + weight
                    if new_cost < distances[neighbor]:
                        distances[neighbor] = new_cost
                        heapq.heappush(pq, (new_cost, neighbor))
            
            return distances
        
        # Step 3: Precompute the minimum transformation costs for all characters
        min_costs = {}
        for char in "abcdefghijklmnopqrstuvwxyz":
            min_costs[char] = dijkstra(char)
        
        # Step 4: Calculate the total minimum cost to transform source to target
        total_cost = 0
        for s_char, t_char in zip(source, target):
            if s_char == t_char:
                continue
            if min_costs[s_char][t_char] == float('inf'):
                return -1
            total_cost += min_costs[s_char][t_char]
        
        return total_cost