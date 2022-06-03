    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        # 計算位址，將每個位數相加
        addr = 0
        while key >= 10:
            a = key % 10
            key = key//10
            addr += a
        addr += key
        return addr

    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
        # 從首節點開始走訪
        cur = self.data[addr]
        while cur.next != None:
            cur = cur.next
        # 當節點指向None，新增節點Key
        cur.next = Node(key)
        
        
    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None
        # 找到要搜尋的key的位址
        addr = self.hash(key)
        # 從該節點開始走訪
        cur = self.data[addr]
        while cur != None:
            # 若該節點的值與key相同，回傳其位址
            if cur.val == key:
                return addr
            # 若不同繼續走訪
            else:
                cur = cur.next
        # 走訪結束皆無相同的值，回傳None
        return None