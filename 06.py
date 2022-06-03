    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        hashCode = 0
        strkey = str(key)
        for i in strkey:
            hashCode += int(i)
            return hashCode

    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
            hashIndex = self.hash(key)
        val = None(key,addr)
        current = self.date[hashIndex].head
        while current.next:
            current = current.next
        current.next = val

    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None
        hashIndex = self.hash(key)
        slot = self.data[hashIndex]
        current = slot.head
        while current.next:
            if key in current.next.addr:
                return current.next.addr
            else:
                current = current.next
            return None