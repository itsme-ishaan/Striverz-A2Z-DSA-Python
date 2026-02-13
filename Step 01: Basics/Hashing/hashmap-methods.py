class MyHashMap:
    
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]
    
    def hash_function(self, key):
        return key % self.size
    
    def put(self, key, value):
        index = self.hash_function(key)
        
        # Check if key already exists
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        
        # If key not found, insert new pair
        self.table[index].append((key, value))
    
    def get(self, key):
        index = self.hash_function(key)
        
        for k, v in self.table[index]:
            if k == key:
                return v
        
        return -1   # Key not found
    
    def remove(self, key):
        index = self.hash_function(key)
        
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index].pop(i)
                retur
