    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        new_key = 0                                 # 等等 key 經過摺疊法操作後放進 new_key
        while key > 0 :                             # 等會 key 會經過摺疊法處理，如果處理完的結果大於0，那就持續使用摺疊法
            new_key = new_key + key % 10            # 將 key 除以 10 取餘數後放到 new_key 裡
            key = key // 10                         # 將 key 除以 10 取整數部分
        return new_key                              # 最終回傳經過摺疊法操作後的 new_key
    
    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
        Node_Key = Node(key)                        # 建立節點
        tmp1 = self.data[addr]                      # 設一個暫存變數
        while tmp1 != None:                         # 當暫存變數不為 None，就一直執行
            if tmp1.next == None:                   # 如果暫存變數的下一個節點為 None
                break                               # 就離開迴圈
            tmp1 = tmp1.next                        # 不然就繼續尋找下一個節點，直到找到最後一個節點
        Node_Key.next = tmp1.next                   # 找到尾端節點後，將它放在 Node_Key 的下一個節點
        tmp1.next = Node_Key                        

    
    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None
        tmp2 = self.data[self.hash(key)]            # 設立一個暫存變數
        while tmp2 != None:                         # 當暫存變數不為 None，就一直執行
            if tmp2.val == key:                     # 尋找輸入的 key 是否存在
                return self.hash(key)               # 如果存在，就回傳其地址
            else:                                   # 否則
                tmp2 = tmp2.next                    # 繼續尋找下一個節點
        return None                                 # 如果真的找不到(不存在)，即回傳 None