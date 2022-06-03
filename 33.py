    def hash(self, key):
        s = 0                           #s的作用為，將加總值放到其中(也就是address)
        key = str(key)                  #將key轉string，這樣就能分割數字
        for i in key:
            i = int(i)                  #當抓到分割後的數字，就轉成int
            s+=i                        #並加到s中
        return s                        #回傳s(address)

    def collision(self, addr, key):
        check = self.data[addr]         #check為self.data[addr]
        while check != None:            #當check不等於None(代表有address重複了)
            if check.next == None:      #如果check.next是空的
                check.next = Node(key)  #就將address重複的key做成 Node 物件，並接到後面
                break                   
            check = check.next          #如果check.next不是空的，就一直往後跑，直到抓到空的

    def search(self, key):
        addr = self.hash(key)           #將要搜尋的數字的address抓出來
        check = self.data[addr]         #check為self.data[addr]
        if check == None:               #如果要搜尋的數字的address，鏈結裡是空的話
            return None                 #回傳None(代表不存在)
        elif check.val == key:          #而如果要搜尋的數字的address，鏈結裡首項的值跟key相等的話
            return addr                 #回傳要搜尋的數字的address
        else:                               #其他(代表要搜尋的數字的address，鏈結裡首項的值跟key不相等)
            while check.val != key :        
                if check.next == None:      #如果鏈結後面沒有連接其他的Node
                    return None             #回傳None(代表不存在)
                elif check.next.val == key: #如果鏈結下一個Node的值等於key的話
                    return addr             #回傳要搜尋的數字的address
                check = check.next          #繼續往後找(直到鏈結的尾端)