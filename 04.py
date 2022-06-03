    def hash(self, key):
        total = 0
        tmp = key
        while tmp > 0:
            n = tmp %10
            total += n
            tmp //= 10
        return total   
    def collision(self, addr, key):
        loca = self.data[addr]
        new_Node = Node(key)
        if loca.next == None:
            loca.next = new_Node
        elif loca.next.next == None:
            loca.next.next = new_Node
        elif loca.next.next.next == None:
            loca.next.next.next = new_Node
        # 使用「鏈結法」處理碰撞，在碰撞的 addr 內的 Node 物件當成鏈結串列的 head
        # 把欲插入的 key 做成 Node 物件並連接在鏈結串列的尾端
        # hint : addr 為 self.data 中的 index
    
    def search(self, key):
        add = self.hash(key)
        if self.data[add] == None:
            return 
        else:
            tmp = self.data[add]
            tmp_list = []
            while tmp:
                tmp_list.append(tmp.val)
                tmp = tmp.next
            if key in tmp_list:
                return add
        # 若輸入的 key 存在，則 return 他的地址 (在self.data中的index)
        # 若不存在則 return None