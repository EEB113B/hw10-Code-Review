    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        tem = 0                                 #設立一變數
        addre = 0                               #設立地址
        while key >=10:                         #當key >=10 時
            tem = key % 10                      #將key除予10之後的餘數設為tem
            addre += tem                        #將地址加上tem
            key = key // 10                     #key除以10
        if key < 10:                            #當key不足10時
            addre += key                        #地址加上key
            return addre                        #return 地址
    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
        Node_key = Node(key)                #將key設為Node
        tmp = self.data[addr]               #將tmp設為地址第一個數(head)
        while tmp != None:                  #當tmp不為None時
            if tmp.next == None:            #如果tmp下一個數為None
                break                       #則跳出迴圈
            tmp = tmp.next                  #如果沒有則換成下一個數            
        tmp.next = Node_key                 #將最後一數的下一個數更改為key
    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None
        ind = self.hash(key)                #設一index為key的地址
        cur = (self.data[ind])              #將cur設為地址的第一數
        while cur != None:                  #當cur不為None時
            if cur.val == key:              #如果cur的值等於key的時候
                return ind                  #回傳key的地址
            else:                           
                cur = cur.next              #如果不等於時將cur改為下一個數
        return None                         #如果cur比較完都沒有的話回傳None