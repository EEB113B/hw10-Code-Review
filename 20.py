    def hash(self, key):
        addr = 0
        while key>0:                  #用取10餘數的方法抓出每個位數
            addr = key%10 + addr
            key = key//10
        return addr             
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
    
    def collision(self, addr, key):
        current = self.data[addr]   #鏈結串列的head
        while current.next:         #跑到鏈結串列尾端
            current = current.next 
        current.next = Node(key)    #Node(key)連接
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
    
    def search(self, key):
        addr = self.hash(key)           #算出key理論上的位置 
        current = self.data[addr] 
        if current == None:             #如果理論位置為none 直接回傳
            return None
        while current:                  #理論位置存在數字，從頭走到尾
            if current.val == key:      #key確實存在理論位置
                return addr
                break
            current = current.next
        
        if current == None:           #走到底還是沒發現key
            return None


        
      
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None