class LRUCache:
    def __init__(self, capacity = 16):
        self.capacity = capacity
        self.values = {}
        self.ages = {}

    def put(self, key, value):
            
        if len(self.values) >= self.capacity:
            maxAgeKey = None
            for i in self.ages.keys():
                if maxAgeKey == None:
                    maxAgeKey = i
                if self.ages[i] > self.ages[maxAgeKey]:
                    maxAgeKey = i
            self.values.pop(maxAgeKey)
            self.ages.pop(maxAgeKey)

        self.values.update({key: value})
        self.ages.update({key: 0})

    def get(self, key):
        if key not in self.values.keys():
            return None

        self.ages[key] = 0
        for i in self.values.keys():
            if i != key:
                self.ages[i] += 1

        return self.values[key]

    
    def foo(self):
        print(self.values, self.ages)
        print(self.values.keys())
        print(len(self.values))

#tests
def test1():
    c = LRUCache(10)
    for i in "abcdefghij":
        c.put(i, None)
    for i in "bcdaaafg":
        c.get(i)
    c.put("k", None)
    return c.values.keys()
assert test1() == {'a', 'b', 'c', 'd', 'd', 'f', 'g', 'h', 'i', 'j', 'k'}

def test2():
    c = LRUCache()
    return c.get("a")
assert test2() is None
