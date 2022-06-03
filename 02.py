    def hash(self, key):
        addr = 0 #初始化一個變數為0
        while key != 0: #這個迴圈是把key的每一位數加起來，形成addr
            n = key % 10
            key = key // 10
            addr += n
        return addr
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
    
    def collision(self, addr, key):
        tmp = self.data[addr]
        while tmp.next != None: #當tmp的下一個不是None(tmp不是尾巴)
            tmp = tmp.next #tmp往下一個移
        tmp.next = Node(key) #把key插在後面

        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
    
    def search(self, key):
        for address in range(50): #檢查data裡所有項
            tmp = self.data[address] 
            while tmp: #因為每一項有可能只是一個數字，或者一個鏈結串列
                if tmp.val == key: #如果存在
                    return address #回傳address
                tmp = tmp.next #否則往下檢查
        return None
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None