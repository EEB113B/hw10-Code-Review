    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        
        address = 0
        
        while key > 0:                      #將key每一位數取出來並加起來
            address += key % 10
            key = key//10
        
        return address                      #return key各位數的總和(即為addr)
    
    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
        
        self.head = self.data[addr]         #將addr中的第一個Node設為head
        tmp  = self.head                    #將tmp的標籤設在head
        
        while tmp.next != None:             #當tmp的下一個是None時，tmp即為目前串列的尾端
            tmp = tmp.next
        
        tmp.next = Node(key)                #尾端的下一個位置串上新的碰撞節點
    
    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None
        
        addr = self.hash(key)               #先將key可能存在的addr找出來
        self.head = self.data[addr]
        tmp  = self.head
        
        while tmp != None:                  #將串列跑一次
            if tmp.val == key:              #當跑到某個節點的值為key時，return addr結束function
                return addr
            tmp = tmp.next
            
        if tmp == None:                     #當tmp == None，表示tmp跑完整個串列都沒有找到key，return None代表雜湊中沒有key這個值
            return None