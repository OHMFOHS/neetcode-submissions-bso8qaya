class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pos_speed = []
        for i in range(len(position)):
            pos_speed.append((position[i], speed[i]))
        pos_speed.sort(reverse = True)
        for p, s in pos_speed:
            time = (target - p) / s
            if stack and time <= stack[-1]:
                continue
            stack.append(time)
        return len(stack)

