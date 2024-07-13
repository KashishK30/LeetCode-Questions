class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = list(zip(positions, healths, directions))
        robots.sort()

        stack = []

        for pos, health, dirn in robots:
            if dirn == 'R':
                stack.append((pos, health, dirn))
            else:
                while stack and stack[-1][2] == 'R':
                    rgt_pos, rgt_health, rgt_dirn = stack.pop()
                    if rgt_health < health:
                        health -= 1
                    elif rgt_health > health:
                        if rgt_health - 1 > 0:
                            stack.append((rgt_pos, rgt_health - 1, rgt_dirn))
                        health = 0
                        break
                    else:
                        health = 0
                        break
                if health > 0:
                    stack.append((pos, health, dirn))
        
        pos_to_index = {pos: i for i, pos in enumerate(positions)}

        survivors = [0] * len(positions)

        for pos, health, dirn in stack:
            index = pos_to_index[pos]
            survivors[index] = health

        return [h for h in survivors if h > 0]