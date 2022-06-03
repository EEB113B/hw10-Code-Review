    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        # Generate hash from key.
        # Time O(N), Space O(1), where N is the length of key.
        hashed = 0
        for i in range(len(key)):
            hashed = (256 * hashed + ord(key[i])) % 101
        return hashed
    
    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index


        hashIndex = self.hash(key, self.size)
        node = Node(key, addr)
        if not self.values[hashIndex]:
            self.values[hashIndex] = LinkedList(node)
        else:
            current = self.values[hashIndex].head
            while current.next:
                current = current.next
            current.next = node
        self.values[hashIndex].count +=1
        self.length +=1

    
    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None

        hashIndex = self.hash(key, self.size)
        slot = self.values[hashIndex]
        current = slot.head
        if key in current.value:
            return current.value
        while current.next:
            if key in current.next.value:
                return current.next.value
            else:
                current = current.next
        return None