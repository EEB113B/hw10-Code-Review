    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        tmp_key = key       #設一個變數將key丟給它
        total = 0           #設return值為total
        while tmp_key >= 10:    #當tmp_key不小於10時，就一位一位的取出數字
            total += tmp_key % 10       #將每位數字相加存到total
            tmp_key = tmp_key // 10
        total += tmp_key        #將最後剩餘小於10的數加到total
        return total
    
    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
        self.tmp = [None]       
        self.tmp[0] = Node(key)     #重新設一個尾端節點
        self.rear = self.tmp[0]     #將新節點命名設為rear，為Node物件
        self.head = self.data[addr] #再設一個head物件，為address第一個index
        while self.head.next != None:   #一直跑到最後一個數，若跑到了就將它的下一個數設為新節點rear
            self.head = self.head.next
        self.head.next = self.rear

    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None
        for i in keys:  
            if i == key:    #判斷key裡面的數是否存在在keys裡
                address = self.hash(key)    #將算出的數用address接收
                return address