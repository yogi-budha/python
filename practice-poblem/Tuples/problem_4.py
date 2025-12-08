# Q4: Count no of tuples, list and set from a list
list1 = [{'hi', 'bye'},{'Geeks', 'forGeeks'},('a', 'b'),['hi', 'bye'],['a', 'b']]

tuple_count = 0
list_count =0
set_count = 0

for i in list1:
    if type(i) == tuple:
        tuple_count = tuple_count+1
    elif type(i) == list:
        list_count = list_count+1
    elif type(i) == set:
        set_count= set_count+1
    
print("tuple-",tuple_count)
print("list-",list_count)
print("set-",set_count)