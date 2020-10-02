'''In this all we have to do is that 
1.if track_min is empty simply push the item
2.if it is not empty then push those item by comparing the push item  
with the last element in track_min and append the lower one in trak_min 
and 
2.In pop method pop the element from both of the list  
'''
class Stack:
    def __init__(self):
        self.items = []
        self.track_min = []

    def push(self,item):
        self.items.append(item)
        if self.track_min == []:
            self.track_min.append(item)
        else:
            if item < self.track_min[-1]:
                self.track_min.append(item)
            else:
                self.track_min.append(self.track_min[-1])
    
    def pop(self):
        if self.items != []:
            self.items.pop()
        if self.track_min !=[]:
            self.track_min.pop()
        


    def top(self):
        if self.items != []:
            return self.items[-1]

    def is_empty(self):
        if self.items == []:
            return True
        return False
    
    def getMin(self):
        return self.track_min[-1]

minStack = Stack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin()) # return -3
minStack.pop()
print(minStack.top())    # return 0
print(minStack.getMin()) # return -2