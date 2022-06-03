    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        addr = 0
        for i in range(6):
            addr += key%10
            key = key//10
            if (key == 0):
                break

        return addr
    
    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
        ptr = self.data[addr]
        new_node = Node(key)
        while ptr.next != None:
            ptr = ptr.next
        ptr.next = new_node
    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None
        addr = self.hash(key)
        if self.data[addr] != None:
            ptr = self.data[addr]
            while ptr.val != key:
                ptr = ptr.next
                if ptr == None:
                    return None
            return addr
        else:
            return None