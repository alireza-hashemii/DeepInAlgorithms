class Deque:
    def __init__(self):
        self.front = []
        self.back = []

    def add_front(self, element):
        self.front.append(element)

    def remove_front(self):
        if not self.front:
            raise IndexError("Deque is empty")
        return self.front.pop(0)

    def add_back(self, element):
        self.back.append(element)

    def remove_back(self):
        if not self.back:
            raise IndexError("Deque is empty")
        return self.back.pop()

    def peek_front(self):
        if not self.front:
            raise IndexError("Deque is empty")
        return self.front[0]

    def peek_back(self):
        if not self.back:
            raise IndexError("Deque is empty")
        return self.back[-1]