    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        num = 0             #用來算地址的
        while(key != 0): 
            num += key % 10 #key取餘數加到num裡面
            key= key // 10  #key 除10取整數
        # print("num: " ,num)
        return num
    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
        tmp = self.data[addr]   #設一個指標指向第一個node
        while tmp !=None:       #如果此node的下一個有值就再往下跑，如果沒有就用key取代 node.next
            if tmp.next == None:    
                tmp.next = Node(key)
                break           #以免無限輪迴
            tmp = tmp.next
    
    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None
        lend = len(self.data)   #data長度
        for i in range(lend):   
            if self.data[i] !=None: #如果此地址有值
                tmp = self.data[i]  #看此值以及其串列是否有跟key相等
                while tmp != None:
                    if tmp.val == key:
                        return i    #相等就直接回傳
                    tmp = tmp.next
        return None     #都沒找到就回傳None