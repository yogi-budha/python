list1 = ['CampusX is a channel', 'for data-science', 'aspirants.']

def split(arr):
   list2=[]
   for i in arr:
      list2.extend(i.split(" "))
   return list2


a = split(list1)
print(a)