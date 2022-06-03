    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        sum = 0       #設定sum=0
        while key !=0:        
            sep_key = key % 10  #將key的值從個位數開始取出後放入sep_key
            sum += sep_key      #將sep_key加進sum中
            key //= 10          #將已取出的位數刪掉,進到下一位數
        return sum              #回傳轉換後的數字
    
    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
        start = self.data[addr]
        while start != None:  
            if start.next == None:      #找到鏈結串列尾端
                start.next = Node(key)  #把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
                break                             #結束迴圈
            start = start.next#依序向後找   
        
    
    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None
        addr = self.hash(key)            #找到key如果存在應該儲存在的位址
        start = self.data[addr]          #複製一個self.data[addr]的指標到start
        if start == None:                #如果start是空的就直接回傳None
            return None
        else:
            if start.val == key:         #如果start的值=key就回傳addr  
                    return addr
            else:
                dup = None               #預設回傳為None
                while start.next != None:#依序向後找
                    start = start.next
                    if start.val == key: #如果鏈結串列中有key
                        dup = addr       #將預設的dup改為addr
                        break            #結束迴圈
                return dup               #回傳dup