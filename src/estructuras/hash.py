
from typing import List

class HashNode:
    def __init__(self, key: any, value: any, hashCode: int) -> None:
        self.key = key
        self.value = value
        self.next: HashNode = None
        self.hashCode = hashCode

class ArrayList:
    def __init__(self):
        self.data: List[HashNode] = []

    def add(self, value: HashNode):
        self.data.append(value)

    def get(self, index: int):
        return self.data[index]

    def set(self, index: int, value: HashNode):
        self.data[index] = value


class Map:
    def __init__(self):
        self.bucketArray = ArrayList()
        self.numBuckets = 10
        self.size = 0
        for i in range(0, self.numBuckets):
            self.bucketArray.add(None)

    def getSize(self) -> int:
        return self.size

    def isEmpty(self) -> bool:
        return self.getSize() == 0

    def hashFunction(self, value: any) -> int:
        return id(value)

    def __hashCode(self, key: any) -> int:
        return self.hashFunction(key)

    # This implements hash functions to find index for a key
    def __getBucketIndex(self, key: any) -> int:
        hashCode = self.__hashCode(key)
        index = hashCode % self.numBuckets
        # key.hashCode() could be negative.
        index = index * -1 if index < 0 else index
        return index

    # Method to remove a given key
    def remove(self, key: any) -> any:

        # Apply hash function to find index for given key
        bucketIndex = self.__getBucketIndex(key)
        hashCode = self.__hashCode(key)
        
        # Get head of chain
        head: HashNode = self.bucketArray.get(bucketIndex)
        
        # Search for kye in its chain
        prev: HashNode = None
        while head != None:
            # If key found
            if (head.key == key and head.hashCode == hashCode):
                break
            # Else keep moving in chain
            prev = head
            head = head.next
        if head == None:
            return None

        # Reduce size.
        self.size = self.size - 1

        # Remove key
        if prev != None:
            prev.next = head.next
        else: 
            self.bucketArray.set(bucketIndex, head.next)
        return head.value
    
    def get(self, key: any) -> any:
        bucketIndex = self.__getBucketIndex(key)
        hashCode = self.__hashCode(key)
        head: HashNode = self.bucketArray.get(bucketIndex)
        
        # Search key in chain.
        while head != None:
            if head.key == key and head.hashCode == hashCode:
                return head.value
            head = head.next
        # If key not found
        return None

    def add(self, key: any, value: any) -> None:
        bucketIndex = self.__getBucketIndex(key)
        hashCode = self.__hashCode(key)
        head: HashNode = self.bucketArray.get(bucketIndex)
        
        # Check if key is already present
        while head != None:
            if head.key == key and head.hashCode == hashCode:
                head.value = value
                return
            head = head.next

        # Inset key in chain
        self.size += 1
        head = self.bucketArray.get(bucketIndex)
        newNode: HashNode = HashNode(key, value, hashCode)
        newNode.next = head
        self.bucketArray.set(bucketIndex, newNode)

        # If load factor goes beyond threshold, then 
        # double hash table size.
        if ((1.0 * self.size) / self.numBuckets >= 0.7):
            temp: ArrayList = self.bucketArray
            self.bucketArray = ArrayList()
            self.numBuckets = 2 * self.numBuckets
            self.size = 0
            for i in range(self.numBuckets):
                self.bucketArray.add(None)
            for headNode in temp.data:
                while headNode != None:
                    self.add(headNode.key, headNode.value)
                    headNode = headNode.next


if __name__ == "__main__":
    dicc: Map = Map()
    dicc.add("this",  1)
    dicc.add("code", 2)
    dicc.add("this", 4)
    dicc.add("hi", 5)
    print(dicc.getSize())
    print(dicc.remove("this"))
    print(dicc.remove("this"))
    print(dicc.getSize())
    print(dicc.isEmpty())
    print(dicc.hashFunction(dicc))