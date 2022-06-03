    def hash(self, key):
        # 使用「摺疊法」(以1為長;度)把輸入的 key 轉換成相對應的數字
        # return 型態為整數 int
        sum = 0
        for pos in range (len(self)):
            sum = sum + ord(self[pos])

        return sum%key

    def collision(self, addr, key):
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
        hashvalue = self.hashfunction(key,len(self.slots))
        self.slots = addr
        
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
         
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  
             
            else:
                 
                nextslot = self.rehash(hashvalue,len(self.slots))
                 
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot,len(self.slots))
                 
                if self.slots[nextslot] == None:
                    self.slots[nextslot]=key
                    self.data[nextslot]=data
              
                else:
                    self.data[nextslot] = data    

    def hashfunction(self,key,size):
        return key%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    def search(self, key):
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None 
        address = self.hash(key)
        if self.isExist(key):
            while self.data[address] != key:
                address = (address + 1) % self.M
            return address
        else:
            return None

    def v(self):
        print(self.data)