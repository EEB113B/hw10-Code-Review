    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        a=len(keys)
        sum=0
        for j in range(a):
            sum+=(key.data%10)
            key.data=(key.data/10)
        return sum

    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
        a=len(keys)
        node.first=key[0]
        for k in range (a+1):
            while node.next!=0:
                node=node.next
            node.next=key[k+1]     
    
    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None
        a=len(keys)
        for j in range(a):
            if keys[j]==key:
                return key[j]