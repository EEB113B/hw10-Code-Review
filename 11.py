    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        addr=0                      #設地址位置為0
        while key>0:                #當key大於0
            rem=key%10              #key除以10的餘數
            addr+=rem               #地址位置加餘數
            key=key//10             #key除以10
        return addr                 #回傳相加後的地址位置
    
    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
        tmp=self.data[addr]         #碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        while tmp.next!=None:       #找出鏈結串列的尾端，當tmp的下一個不是空的
            tmp=tmp.next            #下一個tmp
        tmp.next=Node(key)          #建新的 Node 存放在此單向鏈結串列的尾端(tmp的下一個)

    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None
        addr=self.hash(key)         #找出他的地址
        tmp=self.data[addr]         #addr 內的 Node 物件當成鏈結串列的 head
        while tmp:                  #當tmp不是None
            if tmp.val==key:        #如果tmp的值等於key
                return addr         #回傳他的地址
            if tmp.val==None:       #如果tmp的值等於None
                return None         #回傳None
            tmp=tmp.next            #下一個tmp