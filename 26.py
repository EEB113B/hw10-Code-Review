    def hash(self, key):
        #把每個位數取出來加總
        b = key//100000
        c = key//10000 - b*10
        d = key//1000 - b*100 - c*10
        e = key//100 - b*1000 - c*100 - d*10
        f = key//10 - b*10000 - c*1000 - d*100 - e*10
        g = key - b*100000 - c*10000 - d*1000 - e*100 - f*10
        return b+c+d+e+f+g
            
    def collision(self, addr, key):
        now = self.data[addr]
        if now != None:    #判斷是否發生碰撞
            #新增數字
            while now.next:
                now = now.next
            now.next = Node(key)
        
        else:   #未發生碰撞則新增進去
            self.data[addr] = Node(key)
            self.val = key
    
    def search(self, key):
        #把搜尋的數字放入hash
        address = self.hash(key)
        now = self.data[address]
        #判斷搜尋的值是否已存在
        while now:
            #已存在且key也相等就回傳address
            if now.val == key:
                return address
            #繼續看下一個
            now = now.next