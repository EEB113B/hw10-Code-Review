    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        total = 0
        while key > 0: #將數字的每一位數取出來並加在一起
            total = total + key % 10 # %符號為除法取餘數，舉例，123除10等於12餘3所以123 % 10 = 3 
            key = key // 10 # //符號為除法取整數，舉例，123除10等於12餘3所以123 // 10 = 12
        return total

    
    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
        tmp = self.data[addr] #先使用指標將self.data[j]傳給tmp
        while tmp.next != None: 
            tmp = tmp.next
        tmp.next = Node(key) #因為該addr已有Node物件，所以將新的數字連接在該addr時self.data[addr]的next

    
    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None
        check = None #預設check是None，for迴圈結束後如果check沒有變為其他值，代表沒有找到符合的資料
        for j in range(50):
            if self.data[j]: #如果self.data[j]不是None
                tmp = self.data[j] #先使用指標將self.data[j]傳給tmp
                while tmp != None: #當tmp不是None就一直執行
                    if tmp.val == key: #找到符合的資料
                        check =  j   #將index傳給check
                    tmp = tmp.next #將tmp.next傳給tmp，如果新的tmp也不為None，代表後面還有資料，就會繼續執行
                    
        return check