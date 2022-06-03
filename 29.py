    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        t = 0 
        while key >= 10:        #預設一個變數存放key切割相加後的總合
            t += key % 10       #如果key非個位數，一直執行，直至key剩個位數
            key = key // 10     #利用取餘數的方式將個位數取出並加入t
        t += key                #利用整數除法將個位數脫去
        return t                #將最後剩餘的個位數加入t 
            
    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
        tmp = self.data[addr]    #先命令一個節點給要處理的addr
        while tmp.next:          #有相同key的資料，建立鏈結串列
            tmp = tmp.next
        tmp.next = Node(key)     #將key放在鏈結串列的尾端
    
    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None
        lens = len(self.data)            #標記self.data最後有值的位置
        i = 0                            
        surf = False                     #先預設不存在
        while i < lens:                  #利用迴圈從第0項開始找到最後的位置
            if self.data[i] != None:     #若此位置有值
                tmp = self.data[i]       #命令一個新節點給這個值
                while tmp:
                    if tmp.val == key:   #若此值存在  
                        surf = True      #將原先預設值改掉
                    if tmp.next:         #若有碰撞鏈結串列
                        tmp = tmp.next   #繼續處理鏈結串列的下一筆資料  
                    else:
                        tmp = None       #清空該節點
            if surf:                     #找到的話
                break
            i += 1                       #繼續找下一個

        if surf:
            return i                      #若存在則回傳其值             
        else:
            return None                   #若不存在則回傳None 