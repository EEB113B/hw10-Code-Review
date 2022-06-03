    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        address = 0
        while key > 0:                   #利用迴圈計算出key每一位數相加的值
            address = address + key%10   #將key的值%10 抓出key的個位數 加入address內
            key = key//10                #將key整除10 替除掉先前抓出的個位數
        return address                   #回傳address
    
    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
        tmp = self.data[addr]            #將該位址第一筆資料當作head 並取名tmp
        nodex = Node(key)                #碰撞的值先使用Node處理資料
        while tmp.next != None:          #若tmp的下一筆資料不是None，代表該位址已經有兩筆以上的資料，利用迴圈找到該位址最後一筆資料
            tmp = tmp.next
        nodex.next = tmp.next            #使用鏈結串列插入資料的方式將新的碰撞資料加入該鏈結串列
        tmp.next = nodex
        
    
    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None
        address = self.hash(key)                      #先將search的key轉成address
        if self.data[address] == None:                #若在該陣列中search轉換的位址沒有東西，回傳None
            return None
        elif self.data[address].val == key :          #若在該陣列中search轉換的位址之值剛好等於search的key，回傳該位址
            return address
        else:
            tmp = self.data[address]                  #若非以上兩種情況，只有一種可能：其資料在碰撞處理中被放置在該位址的鏈結串列
            while tmp.val != key:                     #使用迴圈多次比較search資料是否在該位址的鏈結串列中
                if tmp.next == None:                  #若比到鏈結串列的尾巴都還沒有，回傳None
                    return None                  

                elif tmp.next.val == key:             #若tmp的next之值是search的key，回傳該位址
                    return address

                tmp = tmp.next                        #將tmp改成鏈結串列中下一筆資料
                if tmp.val == None:                   #若沒有下一筆資料，則回傳None
                    return None