    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        total = 0
        while key > 0:                 #使用取餘數的方法抓出整數中每個位數
            a = key % 10 
            total = total + a          #用total計算每個位數的總和
            key = key // 10
        return total
    
    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
        cur = self.data[addr]     #定義節點的頭
        while cur.next != None:   # 在當前節點的next指標不為None時執行迴圈 (若當前節點的next指標是None，則代表已走訪到此鏈結串列的最後一個節點)
            cur = cur.next        #往下一個節點找
        cur.next = Node(key) # 把原本指向None的最後一個節點的next指標，改指向新的節點物件，並給予欲加入的Node
    
    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None
        cur = self.data[self.hash(key)]     #定義節點的頭
        
        while cur != None:                  #data中有值
            if cur.val == key:              #若該 key 存在 於此雜湊表中，則 return 地址位置
                return self.hash(key)
            cur = cur.next
        return None                         #若該 key 不存在 於此雜湊表中，則 return None