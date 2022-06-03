    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        total = 0 
        while key >= 10:   #判斷是否大於十
            total += key % 10  #total存放個位數
            key = key // 10  #key更新，少了個位數
        total += key
        return total
    
    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
        tmp = self.data[addr]
        while tmp.next:
            tmp = tmp.next   #新的Node存放在此單向鏈結串列的尾端
        tmp.next = Node(key) 

    
    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None
        lens = len(self.data)  #資料長度
        i = 0
        find = False
        while i < lens:   #判斷是否有東西
            if self.data[i] != None:
                tmp = self.data[i]
                while tmp:
                    if tmp.val == key:
                        find = True
                    if tmp.next:
                        tmp = tmp.next
                    else:
                        tmp = None
            if find:
                break
            i += 1

        if find:   # find=true
            return i     #存在 return 地址
        else:
            return None  #不存在 return None