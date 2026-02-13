class MyHashMap:
    
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]
         
        # Initially we create an array of empty buckets
        # Index:
        # 0  -> []
        # 1  -> []
        # 2  -> []
        # 3  -> []
        # 4  -> []
        # 5  -> []
        # 6  -> []
        # 7  -> []
        # 8  -> []
        # 9  -> []
    
    def hash_function(self, key):
        return key % self.size

        # We calculate index using modulo
        #
        # Example:
        # key = 15
        # size = 10
        #
        # 15 % 10 = 5
        #
        # So data will go to index 5
    
    def put(self, key, value):
        index = self.hash_function(key)

        # Suppose we do:
        # put(1,100)
        # 1 % 10 = 1
        # Table becomes:
        # 1 -> [(1,100)]
        
        # Now suppose we do:
        # put(11,999)
        # 11 % 10 = 1
        # Collision! Same bucket.
        # 1 -> [(1,100), (11,999)]
        
        
        # Now Check if key already exists
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return

          # Updating existing key
                # Before:
                # [(1,100)]
                # After put(1,500):
                # [(1,500)] 
        
        # Next : If key not found, insert new pair
        self.table[index].append((key, value))

        # After append example:
        # Index 1:
        # [(1,100), (11,999)]
    
    def get(self, key):
        index = self.hash_function(key)

        # Example:
        # get(11)
        # index = 1
        # Bucket:
        # [(1,100), (11,999)]
        # We search linearly inside bucket
        
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
