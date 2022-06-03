    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        addr=0                 ##設變數為零，用來加總
        for i in str(key):     ##先將輸入的key轉成字串，再利用for迴圈依序取出每個數字
            addr+=int(i)       ##將每個數字再由字元模式轉成數值，然後給前面設的變數addr做加總
        return addr            ##回傳地址

    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
        cur=self.data[addr]     ##令cur指向data中，位置為addr的節點
        while cur.next!=None:   ##利用while迴圈，讓cur指向最後一個節點
            cur=cur.next
        cur.next=Node(key)      ##讓cur.next指向新增加的節點

    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None
        addr=self.hash(key)     ##讓addr存取key若是存在，所會在的地址
        cur=self.data[addr]     ##令cur指向data中，位置為addr的節點
        while cur!=None:        ##利用while迴圈去確認key是否存在
            if cur.val==key:    ##如果cur所在節點的val相等於key
                return addr     ##直接回傳地址
            cur=cur.next        ##如果不等於，就跑下一個節點
        return None             ##回傳None