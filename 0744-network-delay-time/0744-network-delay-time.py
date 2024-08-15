import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        pq = [(0, k)]

        dist = {node: float('inf') for node in range(1, n + 1)}
        dist[k] = 0

        while pq:
            time, node = heapq.heappop(pq)

            if time > dist[node]:
                continue
            
            for neighbor, t in graph[node]:
                d = t + time
                if d < dist[neighbor]:
                    dist[neighbor] = d
                    heapq.heappush(pq, (d, neighbor))

        max_time = max(dist.values())

        return max_time if max_time < float('inf') else -1