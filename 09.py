    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        s = 0
        while key != 0:
            s = s + key % 10
            key = key // 10
        return s
    
    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
        n = self.data[addr]
        while n.next != None:
            n = n.next
        n.nxt = Node(key)

    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None
        a = self.hash(key)
        key_add = self.data[a]
        if key_add == None:
            return None
        while key_add != None:
            if key_add.val == key:
                return a
            key_add = key_add.next