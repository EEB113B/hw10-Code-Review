    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        return key % self.M  #以長度為1的方式分割
    
    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
        address = self.hash(key)
        if self.data[address] == None:
            self.data[address] = key
        else:
            while self.data[address] != None:
                address = (address + 1) % self.M
            self.data[address] = key

    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None
        address = self.hash(key)
        if self.isExist(key):
            while self.data[address] != key: #輸入的 key 存在
                address = (address + 1) % self.M
            return address
        else:
            return None