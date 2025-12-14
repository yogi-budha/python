

# def closestTerm(lsit1,arr):
#         smallest_d ={}
#         for i in list1:
#             x = (i[0] - arr[0])**2
#             y = (i[1] - arr[1])**2

#             d = (x+y)*0.5
#             smallest_d[d] = (i[0],i[1])

#         return smallest_d

# list1 = [(1,1),(2,2),(3,3),(4,4)]
# arr = (0,0)
# smallest_d = closestTerm(list1,arr)

# print("Nearest to "+str(arr) + " is " + str(smallest_d[min(smallest_d.keys())]))


def closestTErm (list1,arr):
    distance = float("inf")
    nearest = None
    for x,y in list1:
        d = ((x-arr[0])**2 + (y-arr[1])**2)
        if d<distance:
            distance = d
            nearest = (x,y)

    return nearest


list1 = [(1,1),(2,2),(3,3),(4,4)]
arr = (0,0)
nearest = closestTErm(list1,arr)

print("Nearest to "+str(arr) + " is " + str(nearest))