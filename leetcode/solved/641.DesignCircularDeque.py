from collections import deque

class MyCircularDeque:

    def __init__(self, k: int):
        self.cheat = deque()
        self.maxsize = k

    def insertFront(self, value: int) -> bool:
        if len(self.cheat) < self.maxsize:
            self.cheat.appendleft(value)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if len(self.cheat) < self.maxsize:
            self.cheat.append(value)
            return True
        return False

    def deleteFront(self) -> bool:
        if self.cheat:
            self.cheat.popleft()
            return True
        return False

    def deleteLast(self) -> bool:
        if self.cheat:
            self.cheat.pop()
            return True
        return False

    def getFront(self) -> int:
        if self.cheat:
            return self.cheat[0]
        return -1

    def getRear(self) -> int:
        if self.cheat:
            return self.cheat[-1]
        return -1

    def isEmpty(self) -> bool:
        return len(self.cheat) == 0

    def isFull(self) -> bool:
        return len(self.cheat) == self.maxsize

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
