dist1={1:10, 2:20}
dist2={3:30, 4:40}
dist3={5:50,6:60}

def dict(*kwargs):
   result = {}
   for i in kwargs:
      print(i)
      result.update(i)
   print(result)

dict(dist1,dist2,dist3)