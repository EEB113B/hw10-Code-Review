    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        x = [int(a) for a in str(key)]
        sum_x = sum(x)
        return sum_x
    
    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
        posi = self.data[addr]
        while posi.next != None:
            posi = posi.next
        posi.next = Node(key)
        

    def search(self, key):
        addr = self.hash(key)
        a = self.data[addr]
        while a != None:
            if a.val == key:
                return addr
            a = a.next
        return None    
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None