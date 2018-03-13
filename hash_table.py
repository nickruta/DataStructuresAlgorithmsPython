""" Using the PEP 8 Style Guide for Python Code:
https://www.python.org/dev/peps/pep-0008/ and python linters """


class HashTable:
    """One of the great benefits of a dictionary is the fact that given a key,
    we can look up the as- sociated data value very quickly. In order to
    provide this fast look up capability, we need an implementation that
    supports an efficient search. We could use a list with sequential or binary
    search but it would be even better to use a hash table as described below
    since looking up an item in a hash table can approach 𝑂(1) performance.


    Big-O Complexity:
        We stated earlier that in the best case hashing would provide a 𝑂(1),
        constant time search technique. However, due to collisions, the number
        of comparisons is typically not so simple. Even though a complete
        analysis of hashing is beyond the scope of this text, we can state
        some well-known results that approximate the number of comparisons
        necessary to search for an item.

        The most important piece of information we need to analyze the use of a
        hash table is the load factor, 𝜆. Conceptually, if 𝜆 is small, then
        there is a lower chance of collisions, meaning that items are more
        likely to be in the slots where they belong. If 𝜆 is large, meaning
        that the table is filling up, then there are more and more collisions.
        This means that collision resolution is more difficult, requiring more
        comparisons to find an empty slot. With chaining, increased collisions
        means an increased number of items on each chain.

        As before, we will have a result for both a successful and an
        unsuccessful search. For a suc- cessful search using open addressing
        with linear probing, the average number of comparisons is approximately
        1/2(1 + 1/1-𝜆) and an unsuccessful search gives 1/2(1+(1/1-𝜆)squared)
        If we are using chaining, the average number of comparisons
        is 1 + 𝜆/2 for the successful case, and simply 𝜆 comparisons if the
        search is unsuccessful.

    """
    def __init__(self):
        """ Create a new, empty map with 11 slots."""
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        """ Add a new key-value pair to the map.

        Note:
            If the key is already in the map then replace the old value with
            the new value.

        Args:
            key (int) : the key value
            data (type unknown) : the data to be stored at that key value
        """
        hash_value = self.hash_function(key, len(self.slots))
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data  # replace
            else:
                next_slot = self.rehash(hash_value, len(self.slots))
                while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, len(self.slots))
                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data  # replace

    def hash_function(self, key, size):
        """ implements the simple remainder method. The collision resolution
        tech-nique is linear probing with a “plus 1” rehash function. The put
        function assumes that there will eventually be an empty slot unless the
        key is already present in the self.slots. It computes the original
        hash value and if that slot is not empty, iterates the rehash function
        until an empty slot occurs. If a nonempty slot already contains the
        key, the old data value is replaced with the new data value.

        Args:
            key (int) : the key value
            size (int) : the number of slots in the hash table

        Returns:
            hash_code (int) : the hash value used for storage in a certain slot
        """
        return key % size

    def rehash(self, old_hash, size):
        """ used to locate the next possible position.

        Args:
            old_hash (int) : the slot that has a conflict
            size (int) : the number of slots in the hash table

        Returns:
            hash_code (int) : the hash value used for storage in a certain slot
        """
        return (old_hash + 1) % size

    def get(self, key):
        """ begins by computing the initial hash value. If the value
        is not in the initial slot, rehash is used to locate the next possible
        position.

        Args:
            key (int) : the key for the item to be search for

        Returns:
            data (type unknown) : the data found, otherwise None
        """
        start_slot = self.hash_function(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = start_slot
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


h = HashTable()
h[54] = "cat"
h[26] = "dog"
h[93] = "lion"
h[17] = "tiger"
h[77] = "bird"
h[31] = "cow"
h[44] = "goat"
h[55] = "pig"
h[20] = "chicken"
print(h.slots)
print(h.data)
