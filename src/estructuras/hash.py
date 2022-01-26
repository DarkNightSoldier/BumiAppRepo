from listas_enlazadas import ListaEnlazadaDoble

class HashNode:
    def __init__(self, key: any, value: any, hashCode: int) -> None:
        self.key = key
        self.value = value
        self.next: HashNode = None
        self.hashCode = hashCode

class Map:
    def __init__(self):
        self.bucketArray = ListaEnlazadaDoble()
        self.numBuckets = 10
        self.size = 0
        for i in range(0, self.numBuckets):
            self.bucketArray.empujar_adelante(None)

    def size(self) -> int:
        return self.size

    def isEmpty(self) -> bool:
        return self.size() == 0

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
        bucketIndex = self.__getBucketIndex(k)
        hashCode = self.__hashCode(key)
        
        # Get head of chain
        head: HashNode = self.bucketArray.buscar_nodo(bucketIndex)
        
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
            self.bucketArray.buscar_nodo(bucketIndex).dato = head.next
        return head.value
    
    def get(self, key: any) -> any:
        bucketIndex = self.__getBucketIndex(key)
        hashCode = self.__hashCode(key)
        head: HashNode = self.bucketArray.buscar_nodo(bucketIndex)
        
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
        head: HashNode = self.bucketArray.buscar_nodo(bucketIndex)
        
        # Check if key is already present
        while head != None:
            if head.key == key and head.hashCode == hashCode:
                head.value = value
                return
            head = head.next

        # Inset key in chain
        self.size += 1
        head = self.bucketArray.buscar_nodo(bucketIndex)
        newNode: HashNode = HashNode(key, value, hashCode)
        newNode.next = head
        self.bucketArray.buscar_nodo(bucketIndex).dato = newNode

        # If load factor goes beyond threshold, then 
        # double hash table size.
        if ((1.0 * self.size) / self.numBuckets >= 0.7):
            temp: ListaEnlazadaDoble = self.bucketArray
            self.bucketArray = ListaEnlazadaDoble()
            self.numBuckets = 2 * self.numBuckets
            self.size = 0
            for i in range(self.numBuckets):
                self.bucketArray.empujar_adelante(None)
            for headNode in self.bucketArray.nodos():
                while headNode != None:
                    self.add(headNode.key, headNode.value)
                    headNode = headNode.next


if __name__ == "__main__":
    dicc: Map = Map()
    dicc.add("this",  1)
    dicc.add("code", 2)
    dicc.add("this", 4)
    dicc.add("hi", 5)
    print(dicc.size())
    print(dicc.remove("this"))
    print(dicc.remove("this"))
    print(dicc.size())
    print(dicc.isEmpty())