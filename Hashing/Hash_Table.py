class MyHash:
    def __init__(self, b):
        self.BUCKET = b
        self.table = [[] for x in range(b)]

    def insert(self, x):
        i = x % self.BUCKET
        self.table[i].append(x)

    def delete(self, x):
        i = x % self.BUCKET
        self.table[i].remove(x)

    def search(self, x):
        i = x % self.BUCKET
        return x in self.table[i]


table = MyHash(7)
table.insert(23)
table.insert(42)
table.insert(70)
table.insert(12)
print(table.search(23))     # True
table.delete(70)
print(table.search(70))     # False
