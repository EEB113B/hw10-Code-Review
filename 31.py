    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        total=0#初始位址
        while key>0:#做摺疊法
            total+=key%10
            key=key//10
        return total
    
    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
        tmp=self.data[addr]#暫存當前節點值
        while tmp.val!=None:
            if tmp.next==None:#如果下一個為None
                tmp.next=Node(key)#將當前節點next指向key
                break
            else:#非None
                tmp=tmp.next#暫存節點指向他的next
    
    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None
        index=self.hash(key)#儲存當前位址
        cur=self.data[index]#暫存當前節點值
        while cur !=None:
            if cur.val==key:#比對當前節點值是否為key
                return index#相同則return當前位址
            else:#不同則指向下一個繼續比對
                cur=cur.next
        return None#cur最後指向None則return None