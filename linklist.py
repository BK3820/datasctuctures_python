class Node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("list is empty")
            return

        itr = self.head
        list = ''

        while itr:
            list+=str(itr.data) + '-->'
            itr = itr.next
        print(list)

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)

    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_len(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count


if __name__ == '__main__':
    l1 = Linkedlist()
    l1.insert_at_begining(5)
    l1.insert_at_begining(54)
    l1.insert_at_end(33)
    l1.print()
    l1.insert_values("a b c d e".split(" "))
    l1.print()
    print(l1.get_len())
