class MyHash:
    def __init__(self, c):
        self.capacity = c
        self.table = [-1] * c
        self.size = 0

    def hash(self, x):
        return x % self.capacity

    def search(self, x):
        h = self.hash(x)
        t = self.table
        i = h
        while t[i] != -1:
            if t[i] == x:
                return True
            i = (i + 1) % self.capacity
            if i == h:
                return False
        return False

    def insert(self, x):
        if self.size == self.capacity:
            return False
        if self.search(x):
            return False

        i = self.hash(x)
        t = self.table
        while t[i] not in (-1, -2):
            i = (i + 1) % self.capacity
        t[i] = x
        self.size = self.size + 1
        return True

    def remove(self, x):
        h = self.hash(x)
        t = self.table
        i = h
        while t[i] != -1:
            if t[i] == x:
                t[i] = -2
                return True
            i = (i+1)%self.capacity
            if i == h:
                return False
        return False


# Driver code

m = MyHash(7)
m.insert(23)
m.insert(45)
m.insert(67)
print(m.search(45))
print(m.remove((67)))



