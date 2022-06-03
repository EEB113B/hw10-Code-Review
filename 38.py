    def hash(self, key):
        # 使用「摺疊法」(以1為長度)把輸入的 key 轉換成相對應的數字
        lst = []                         # 創個lst來儲存每個位數的數字
        while key >= 10:                 # 用迴圈來抓每個位數的數字
            lst.append(key % 10)
            key = key // 10 
        lst.append(key)
        n = len(lst)
        addr = 0
        for i in range(n):              # 加起來就是addr
            addr += lst[i]
        return addr

    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        emp = self.data[addr]          # 用emp記錄當下的節點
        while True:                
            if emp.next == None:       # 如果emp的下個節點為空 
                emp.next = Node(key)   # 把新的節點接在尾端
                break
            else:                      # 如果emp不為空
                emp = emp.next         # 將emp下移一位

    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None 
        keyAddr = self.hash(key)       # 用hash算要找的key的addr   
        emp = self.data[keyAddr]       # 用emp紀錄對應的addr
        while True:
            if emp == None:            # 如果emp為空, 回傳None
                return None            
            elif emp.val == key:       # 如果就是要找的值，回傳addr
                return keyAddr
            else:                      # 如果不為空，但值也不是我們要找的的話，將emp下移一位
                emp = emp.next