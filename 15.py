    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        rkey = 0 #設一個return key
        for i in str(key): #將key轉為字串跑for迴圈
            rkey += int(i) #轉回整數計算
        return rkey
    
    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
        tmp = self.data[addr] #執行鏈結串列
        while tmp.next != None: #尋找最後一個
            tmp = tmp.next #檢查下一個
        tmp.next = Node(key) #將最後一個指向新的Node
    
    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None
        address = self.hash(key) #建立一個address放入位置
        tmp = self.data[address] #執行鏈結串列
        while tmp:
            if tmp.val == key: #當值符合需求時return其位置
                return address
            tmp = tmp.next #檢查下一個
        return None #否則return None