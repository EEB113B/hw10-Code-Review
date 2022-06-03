    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        total = 0 #預設總和為0
        while key > 0: #當key還有數值
            total += key % 10 #以1為長度 key除10取餘數會得到長度為1的值 再將這個值加給total
            key = key // 10 #key除10
        return total #回傳total給addr
    
    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
        tmp = self.data[addr] #發生碰撞鏈結addr的head指定為tmp
        while tmp.next: #找到addr鏈結的尾
            tmp = tmp.next
        tmp.next = Node(key) #將Node(key)指定為新的鏈結尾
        
    
    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None
        lens = len(self.data) #計算self.data list長度為多少
        find = None #預設未找到這個key
        i = 0
        while i < lens: #從self.data的index 0 到list尾
            if self.data[i] != None: #如果這個地址是有儲存資料才檢查是否有key
                tmp = self.data[i] #這個地址的鏈結head指定為tmp
                while tmp: 
                    if tmp.val == key: #如果tmp的val等於key 
                        find = i #將i(找到的地址)給find
                    if tmp.next: #如果下一個節點還有資料
                        tmp = tmp.next #將下一個節點指定為tmp
                    else:
                        tmp = None #若沒有就指定為None 那迴圈將不會繼續
            if find: #如果找到之後就直接break
                break
            i += 1 
        return find #回傳key的地址 若沒有就回傳None