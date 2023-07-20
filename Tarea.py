class Stack:
  def __init__(self):
   self.items = []
  def isEmpty(self):
   return self.items == []
  def push(self, item):
   self.items.append(item)
  def pop(self):
   return self.items.pop()
  def top(self):
   return self.items[len(self.items)-1]
  def size(self):
   return len(self.items)


bones = [3, 8, 10, 15, 2, 1] 

def my_stack_function(bones):
  s = Stack()
 
  for i in range(len(bones) - 1):
    for i in range(len(bones) - 1):
     if bones[i] > bones[i + 1]:
        aux = bones[i]
        bones[i] = bones[i + 1]
        bones[i + 1] = aux
  
  
  for i in bones:
      s.push(i)
  print(s.items)  
my_stack_function(bones)